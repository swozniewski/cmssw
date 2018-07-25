/*
 * RecoTauDiscriminantCutMultiplexer
 *
 * Authors: Evan K. Friis, UW; Sebastian Wozniewski, KIT
 *
 * Takes two PFTauDiscriminators.
 *
 * The "key" discriminantor is rounded to the nearest integer.
 *
 * A set of cuts for different keys on the "toMultiplex" discriminantor is
 * provided in the config file.
 *
 * Both the key and toMultiplex discriminators should map to the same PFTau
 * collection.
 *
 */
#include <boost/foreach.hpp>
#include "RecoTauTag/RecoTau/interface/TauDiscriminationProducerBase.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "CommonTools/Utils/interface/StringObjectFunction.h"
#include "DataFormats/TauReco/interface/PFTau.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"

#include "CondFormats/PhysicsToolsObjects/interface/PhysicsTGraphPayload.h"
#include "CondFormats/DataRecord/interface/PhysicsTGraphPayloadRcd.h"
#include "CondFormats/PhysicsToolsObjects/interface/PhysicsTFormulaPayload.h"
#include "CondFormats/DataRecord/interface/PhysicsTFormulaPayloadRcd.h"

#include "TMath.h"
#include "TGraph.h"
#include "TFormula.h"
#include "TFile.h"

class RecoTauDiscriminantCutMultiplexer : public PFTauDiscriminationProducerBaseNEW 
{
 public:
  explicit RecoTauDiscriminantCutMultiplexer(const edm::ParameterSet& pset);

  ~RecoTauDiscriminantCutMultiplexer() override;
  reco::PFSingleTauDiscriminatorContainer discriminate(const reco::PFTauRef&) const override;
  void beginEvent(const edm::Event& event, const edm::EventSetup& eventSetup) override;
  
 private:
  std::string moduleLabel_;

  bool loadMVAfromDB_;
  edm::FileInPath inputFileName_;

  struct DiscriminantCutEntry
  {
    DiscriminantCutEntry()
      : cutVariable_(),
	cutFunction_(),
	mode_(kUndefined)
    {}
    ~DiscriminantCutEntry()
    {
    }
    double cutValue_;
    std::string cutName_;
    std::unique_ptr<StringObjectFunction<reco::PFTau>> cutVariable_;
    std::unique_ptr<const TGraph> cutFunction_;
    enum { kUndefined, kFixedCut, kVariableCut };
    int mode_;
  };
  typedef std::map<int, std::vector<std::unique_ptr<DiscriminantCutEntry>>> DiscriminantCutMap;
  DiscriminantCutMap cuts_;

  std::string mvaOutputNormalizationName_;
  std::unique_ptr<const TFormula> mvaOutput_normalization_;

  bool isInitialized_;

  edm::InputTag toMultiplex_;
  edm::InputTag key_;
  edm::Handle<reco::PFTauDiscriminator> toMultiplexHandle_;
  edm::Handle<reco::PFTauDiscriminator> keyHandle_;
  edm::EDGetTokenT<reco::PFTauDiscriminator> toMultiplex_token;
  edm::EDGetTokenT<reco::PFTauDiscriminator> key_token;

  int verbosity_;
};

namespace
{
  std::unique_ptr<TFile> openInputFile(const edm::FileInPath& inputFileName) {
    if ( inputFileName.location() == edm::FileInPath::Unknown){  throw cms::Exception("RecoTauDiscriminantCutMultiplexer::loadObjectFromFile") 
      << " Failed to find File = " << inputFileName << " !!\n";
    }
    return std::unique_ptr<TFile>{ new TFile(inputFileName.fullPath().data()) };
  }

  template <typename T>
  std::unique_ptr<const T> loadObjectFromFile(TFile& inputFile, const std::string& objectName)
  {
    const T* object = dynamic_cast<T*>(inputFile.Get(objectName.data()));
    if ( !object )
      throw cms::Exception("RecoTauDiscriminantCutMultiplexer::loadObjectFromFile") 
        << " Failed to load Object = " << objectName.data() << " from file = " << inputFile.GetName() << " !!\n";
    //Need to use TObject::Clone since the type T might be a base class
    std::unique_ptr<const T> copy{ static_cast<T*>(object->Clone()) };

    return std::move(copy);
  }

  std::unique_ptr<const TGraph> loadTGraphFromDB(const edm::EventSetup& es, const std::string& graphName, const int& verbosity_ = 0)
  {
    if(verbosity_){
      std::cout << "<loadTGraphFromDB>:" << std::endl;
      std::cout << " graphName = " << graphName << std::endl;
    }
    edm::ESHandle<PhysicsTGraphPayload> graphPayload;
    es.get<PhysicsTGraphPayloadRcd>().get(graphName, graphPayload);
    return std::unique_ptr<const TGraph>{ new TGraph(*graphPayload.product()) };
  }  

  std::unique_ptr<TFormula> loadTFormulaFromDB(const edm::EventSetup& es, const std::string& formulaName, const TString& newName, const int& verbosity_ = 0)
  {
    if(verbosity_){
      std::cout << "<loadTFormulaFromDB>:" << std::endl;
      std::cout << " formulaName = " << formulaName << std::endl;
    }
    edm::ESHandle<PhysicsTFormulaPayload> formulaPayload;
    es.get<PhysicsTFormulaPayloadRcd>().get(formulaName, formulaPayload);

    if ( formulaPayload->formulas().size() == 1 && formulaPayload->limits().size() == 1 ) {
      return std::unique_ptr<TFormula> {new TFormula(newName, formulaPayload->formulas().at(0).data()) };
    } else {
      throw cms::Exception("RecoTauDiscriminantCutMultiplexer::loadTFormulaFromDB") 
	<< "Failed to load TFormula = " << formulaName << " from Database !!\n";
    }
    return std::unique_ptr<TFormula>{};
  }  
}

RecoTauDiscriminantCutMultiplexer::RecoTauDiscriminantCutMultiplexer(const edm::ParameterSet& cfg)
  : PFTauDiscriminationProducerBaseNEW(cfg),
    moduleLabel_(cfg.getParameter<std::string>("@module_label")),
    mvaOutput_normalization_(),
    isInitialized_(false)
{
  
  toMultiplex_ = cfg.getParameter<edm::InputTag>("toMultiplex");
  toMultiplex_token = consumes<reco::PFTauDiscriminator>(toMultiplex_);
  key_ = cfg.getParameter<edm::InputTag>("key");
  key_token = consumes<reco::PFTauDiscriminator>(key_);

  verbosity_ = ( cfg.exists("verbosity") ) ?
    cfg.getParameter<int>("verbosity") : 0;


  loadMVAfromDB_ = cfg.exists("loadMVAfromDB") ? cfg.getParameter<bool>("loadMVAfromDB") : false;
  if ( !loadMVAfromDB_ ) {
    if(cfg.exists("inputFileName")){
      inputFileName_ = cfg.getParameter<edm::FileInPath>("inputFileName");
    }else throw cms::Exception("MVA input not defined") << "Requested to load tau MVA input from ROOT file but no file provided in cfg file";
  }
  if(verbosity_)  std::cout << moduleLabel_ << " loadMVA = " << loadMVAfromDB_ << std::endl;
  if ( cfg.exists("mvaOutput_normalization") ) {
    mvaOutputNormalizationName_ = cfg.getParameter<std::string>("mvaOutput_normalization"); 
  }

  // Setup our cut map
  typedef std::vector<edm::ParameterSet> VPSet;
  typedef std::vector<std::string> VString;
  typedef std::vector<double> VDouble;
  //VPSet globalWorkingPoints = cfg.getParameter<VPSet>("workingPoints");
  VPSet mapping = cfg.getParameter<VPSet>("mapping");
  for ( VPSet::const_iterator mappingEntry = mapping.begin();
	mappingEntry != mapping.end(); ++mappingEntry ) {
    unsigned category = mappingEntry->getParameter<uint32_t>("category");
    std::vector<std::unique_ptr<DiscriminantCutEntry>> cutWPs;
    if ( mappingEntry->existsAs<std::string>("cut") ) {
      std::string categoryname = mappingEntry->getParameter<std::string>("cut");
      bool localWPs = false;
      bool WPsAsDouble = false;
      if ( mappingEntry->exists("workingPoints") ) {
          localWPs = true; //workingPoints = mappingEntry->getParameter<VPSet>("workingPoints");
          if ( mappingEntry->existsAs<VDouble>("workingPoints") ) {
              WPsAsDouble = true;
          } else if ( mappingEntry->existsAs<VString>("workingPoints") ) {
              WPsAsDouble = false;
          } else {
              throw cms::Exception("RecoTauDiscriminantCutMultiplexer") 
                  << " Configuration Parameter 'workingPoints' must be filled with cms.String or cms.Double!!\n";
          }
      } else if ( cfg.exists("workingPoints") ) {
          localWPs = false;
          if ( cfg.existsAs<VDouble>("workingPoints") ) {
              WPsAsDouble = true;
          } else if ( cfg.existsAs<VString>("workingPoints") ) {
              WPsAsDouble = false;
          } else {
              throw cms::Exception("RecoTauDiscriminantCutMultiplexer") 
                  << " Configuration Parameter 'workingPoints' must be filled with cms.String or cms.Double!!\n";
          }
      } else {
          throw cms::Exception("RecoTauDiscriminantCutMultiplexer") 
            << " Undefined Configuration Parameter 'workingPoints' !!\n";
      }
      if ( WPsAsDouble ){
        VDouble workingPoints;
        if ( localWPs ) workingPoints = mappingEntry->getParameter<VDouble>("workingPoints");
        else cfg.getParameter<VDouble>("workingPoints");
        for ( VDouble::const_iterator wp = workingPoints.begin();
            wp != workingPoints.end(); ++wp ) {
          std::unique_ptr<DiscriminantCutEntry> cut{new DiscriminantCutEntry()};
          cut->cutValue_ = *wp;
          cut->mode_ = DiscriminantCutEntry::kFixedCut;
          cutWPs.push_back(std::move(cut));
        }
      } else {
        VString workingPoints;
        if ( localWPs ) workingPoints = mappingEntry->getParameter<VString>("workingPoints");
        else cfg.getParameter<VString>("workingPoints");
        for ( VString::const_iterator wp = workingPoints.begin();
            wp != workingPoints.end(); ++wp ) {
          std::unique_ptr<DiscriminantCutEntry> cut{new DiscriminantCutEntry()};  
          cut->cutName_ = categoryname + *wp;
          std::string cutVariable_string = mappingEntry->getParameter<std::string>("variable");
          cut->cutVariable_.reset( new StringObjectFunction<reco::PFTau>(cutVariable_string) );
          cut->mode_ = DiscriminantCutEntry::kVariableCut;
          cutWPs.push_back(std::move(cut));
        }
      }
    } else {
      throw cms::Exception("RecoTauDiscriminantCutMultiplexer") 
        << " Undefined Configuration Parameter 'cut' !!\n";
    }
    cuts_[category] = std::move(cutWPs);
  }

  verbosity_ = ( cfg.exists("verbosity") ) ?
    cfg.getParameter<int>("verbosity") : 0;
  if(verbosity_) std::cout << "constructed " << moduleLabel_ << std::endl;
}

RecoTauDiscriminantCutMultiplexer::~RecoTauDiscriminantCutMultiplexer()
{
}

void RecoTauDiscriminantCutMultiplexer::beginEvent(const edm::Event& evt, const edm::EventSetup& es) 
{
  if(verbosity_) std::cout << " begin! " << moduleLabel_ << " " << isInitialized_ << std::endl;
  if ( !isInitialized_ ) {
    //Only open the file once and we can close it when this routine is done
    // since all objects gotten from the file will have been copied
    std::unique_ptr<TFile> inputFile;
    if ( mvaOutputNormalizationName_ != "" ) {
      if ( !loadMVAfromDB_ ) {
	inputFile = openInputFile(inputFileName_);
	mvaOutput_normalization_ = loadObjectFromFile<TFormula>(*inputFile, mvaOutputNormalizationName_);
      } else {
	auto temp = loadTFormulaFromDB(es, mvaOutputNormalizationName_, Form("%s_mvaOutput_normalization", moduleLabel_.data()), verbosity_);
	mvaOutput_normalization_ = std::move(temp);
      }
    }
    for ( DiscriminantCutMap::iterator cutWPs = cuts_.begin();
	  cutWPs != cuts_.end(); ++cutWPs ) {
      for ( std::vector<std::unique_ptr<DiscriminantCutEntry>>::iterator cut = cutWPs->second.begin();
          cut != cutWPs->second.end(); ++cut ) {
          if ( (*cut)->mode_ == DiscriminantCutEntry::kVariableCut ) {
	  if ( !loadMVAfromDB_ ) {
	    if(not inputFile) {
	      inputFile = openInputFile(inputFileName_);
	    }
	    if(verbosity_) std::cout << "Loading from file" << inputFileName_ << std::endl;
	    (*cut)->cutFunction_ = loadObjectFromFile<TGraph>(*inputFile, (*cut)->cutName_);
	  } else {
	    if(verbosity_) std::cout << "Loading from DB" << std::endl;
	    (*cut)->cutFunction_ = loadTGraphFromDB(es, (*cut)->cutName_, verbosity_);
          }
	}
      }
    }
    isInitialized_ = true;
  }

  evt.getByToken(toMultiplex_token, toMultiplexHandle_);
  evt.getByToken(key_token, keyHandle_);
}

reco::PFSingleTauDiscriminatorContainer
RecoTauDiscriminantCutMultiplexer::discriminate(const reco::PFTauRef& tau) const
{
  if ( verbosity_ ) {
    std::cout << "<RecoTauDiscriminantCutMultiplexer::discriminate>:" << std::endl;
    std::cout << " moduleLabel = " << moduleLabel_ << std::endl;
  }

  reco::PFSingleTauDiscriminatorContainer result;
  double disc_result = (*toMultiplexHandle_)[tau];
  if ( verbosity_ ) {
    std::cout << "disc_result = " <<  disc_result << std::endl;
  }
  result.rawValue = disc_result;
  if ( mvaOutput_normalization_ ) {
    disc_result = mvaOutput_normalization_->Eval(disc_result);
    //if ( disc_result > 1. ) disc_result = 1.;
    //if ( disc_result < 0. ) disc_result = 0.;
    if ( verbosity_ ) {
      std::cout << "disc_result (normalized) = " <<  disc_result << std::endl;
    }
  }
  double key_result = (*keyHandle_)[tau];
  DiscriminantCutMap::const_iterator cutWPsIter = cuts_.find(TMath::Nint(key_result));
  
  // Return null if it doesn't exist
  if ( cutWPsIter == cuts_.end() ) {
    result.rawValue = prediscriminantFailValue_;
    return result;
  }
  // See if the discriminator passes our cuts
  for ( std::vector<std::unique_ptr<DiscriminantCutEntry>>::const_iterator cutIter = cutWPsIter->second.begin();
          cutIter != cutWPsIter->second.end(); ++cutIter ) {
    bool passesCuts = false;
    if ( (*cutIter)->mode_ == DiscriminantCutEntry::kFixedCut ) {
      passesCuts = (disc_result > (*cutIter)->cutValue_);
      if ( verbosity_ ) {
        std::cout << "cutValue (fixed) = " << (*cutIter)->cutValue_ << " --> passesCuts = " << passesCuts << std::endl;
      }
    } else if ( (*cutIter)->mode_ == DiscriminantCutEntry::kVariableCut ) {
      double cutVariable = (*(*cutIter)->cutVariable_)(*tau);
      double xMin, xMax, dummy;
      (*cutIter)->cutFunction_->GetPoint(0, xMin, dummy);
      (*cutIter)->cutFunction_->GetPoint((*cutIter)->cutFunction_->GetN() - 1, xMax, dummy);
      const double epsilon = 1.e-3;
      if      ( cutVariable < (xMin + epsilon) ) cutVariable = xMin + epsilon;
      else if ( cutVariable > (xMax - epsilon) ) cutVariable = xMax - epsilon;
      double cutValue = (*cutIter)->cutFunction_->Eval(cutVariable);
      passesCuts = (disc_result > cutValue);
      if ( verbosity_ ) {
        std::cout << "cutValue (@" << cutVariable << ") = " << cutValue << " --> passesCuts = " << passesCuts << std::endl;
      }
    } else assert(0);
    result.workingPoints.push_back(passesCuts);
  }
  return result;
}

DEFINE_FWK_MODULE(RecoTauDiscriminantCutMultiplexer);
