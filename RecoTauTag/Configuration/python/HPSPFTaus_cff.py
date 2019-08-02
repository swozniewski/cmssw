import FWCore.ParameterSet.Config as cms
import copy
from Configuration.Eras.Modifier_phase2_common_cff import phase2_common

'''

Sequences for HPS taus

'''

## Discriminator sources
from RecoTauTag.RecoTau.PFRecoTauDiscriminationByIsolation_cfi                      import *
from RecoTauTag.RecoTau.PFRecoTauDiscriminationByLeadingTrackFinding_cfi            import *
from RecoTauTag.RecoTau.PFRecoTauDiscriminationAgainstElectron_cfi                  import *
from RecoTauTag.RecoTau.PFRecoTauDiscriminationAgainstElectronMVA6_cfi              import *
from RecoTauTag.RecoTau.PFRecoTauDiscriminationAgainstElectronDeadECAL_cfi          import *
from RecoTauTag.RecoTau.PFRecoTauDiscriminationAgainstMuon_cfi                      import *
from RecoTauTag.RecoTau.PFRecoTauDiscriminationAgainstMuon2_cfi                     import *
from RecoTauTag.RecoTau.PFRecoTauDiscriminationAgainstMuonMVA_cfi                   import *

from RecoTauTag.RecoTau.RecoTauDiscriminantCutMultiplexer_cfi import *
## Helper functions to change the source of the discriminants
from RecoTauTag.RecoTau.TauDiscriminatorTools import *
## PFjet input parameters
from RecoTauTag.RecoTau.PFRecoTauPFJetInputs_cfi import PFRecoTauPFJetInputs
## DeltaBeta correction factor
ak4dBetaCorrection = 0.20
## MVAs from SQLlite file/prep. DB
from RecoTauTag.Configuration.loadRecoTauTagMVAsFromPrepDB_cfi import *

## Selection of taus that pass the HPS selections: pt > 15, mass cuts, tauCone cut
from RecoTauTag.RecoTau.PFRecoTauDiscriminationByHPSSelection_cfi import hpsSelectionDiscriminator, decayMode_1Prong0Pi0, decayMode_1Prong1Pi0, decayMode_1Prong2Pi0, decayMode_2Prong0Pi0, decayMode_2Prong1Pi0, decayMode_3Prong0Pi0, decayMode_3Prong1Pi0

hpsPFTauDiscriminationByDecayModeFindingNewDMs = hpsSelectionDiscriminator.clone(
    PFTauProducer = cms.InputTag('hpsPFTauProducer'),
    #----------------------------------------------------------------------------
    # CV: disable 3Prong1Pi0 decay mode
    decayModes = cms.VPSet(
        decayMode_1Prong0Pi0,
        decayMode_1Prong1Pi0,
        decayMode_1Prong2Pi0,
        decayMode_2Prong0Pi0,
        decayMode_2Prong1Pi0,
        decayMode_3Prong0Pi0,
        decayMode_3Prong1Pi0,
    )
    #----------------------------------------------------------------------------
)
hpsPFTauDiscriminationByDecayModeFindingOldDMs = hpsSelectionDiscriminator.clone(
    PFTauProducer = cms.InputTag('hpsPFTauProducer'),
    decayModes = cms.VPSet(
        decayMode_1Prong0Pi0,
        decayMode_1Prong1Pi0,
        decayMode_1Prong2Pi0,
        decayMode_3Prong0Pi0
    ),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(True)
)
hpsPFTauDiscriminationByDecayModeFinding = hpsPFTauDiscriminationByDecayModeFindingOldDMs.clone() ## CV: kept for backwards compatibility

## Decay mode prediscriminant
requireDecayMode = cms.PSet(
    BooleanOperator = cms.string("and"),
    decayMode = cms.PSet(
        Producer = cms.InputTag('hpsPFTauDiscriminationByDecayModeFindingNewDMs'),
        cut = cms.double(0.5)
    )
)

## Cut based isolations dR=0.5
hpsPFTauBasicDiscriminators = pfRecoTauDiscriminationByIsolation.clone(
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = requireDecayMode.clone(),
    deltaBetaPUTrackPtCutOverride     = True, # Set the boolean = True to override.
    deltaBetaPUTrackPtCutOverride_val = 0.5,  # Set the value for new value.
    isoConeSizeForDeltaBeta = 0.8,
    deltaBetaFactor = "%0.4f"%(ak4dBetaCorrection),
    IDdefinitions = cms.VPSet(
        cms.PSet(
            IDname = cms.string("ChargedIsoPtSum"),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            storeRawSumPt = cms.bool(True)
            ),
        cms.PSet(
            IDname = cms.string("NeutralIsoPtSum"),
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            storeRawSumPt = cms.bool(True)
            ),
        cms.PSet(
            IDname = cms.string("NeutralIsoPtSumWeight"),
            ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
            storeRawSumPt = cms.bool(True),
            UseAllPFCandsForWeights = cms.bool(True)
            ),
        cms.PSet(
            IDname = cms.string("TauFootprintCorrection"),
            storeRawFootprintCorrection = cms.bool(True)
            ),
        cms.PSet(
            IDname = cms.string("PhotonPtSumOutsideSignalCone"),
            storeRawPhotonSumPt_outsideSignalCone = cms.bool(True)
            ),
        cms.PSet(
            IDname = cms.string("PUcorrPtSum"),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawPUsumPt = cms.bool(True)
            ),
        cms.PSet(
            IDname = cms.string("ByRawCombinedIsolationDBSumPtCorr3Hits"),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawSumPt = cms.bool(True)
            )
        ),
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            IDname = cms.string("ByLooseCombinedIsolationDBSumPtCorr3Hits"),
            maximumSumPtCut = cms.double(2.5),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
            maxAbsPhotonSumPt_outsideSignalCone = cms.double(1.e+9),
            maxRelPhotonSumPt_outsideSignalCone = cms.double(0.10)
            ),
        cms.PSet(
            IDname = cms.string("ByMediumCombinedIsolationDBSumPtCorr3Hits"),
            maximumSumPtCut = cms.double(1.5),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
            maxAbsPhotonSumPt_outsideSignalCone = cms.double(1.e+9),
            maxRelPhotonSumPt_outsideSignalCone = cms.double(0.10)
            ),
        cms.PSet(
            IDname = cms.string("ByTightCombinedIsolationDBSumPtCorr3Hits"),
            maximumSumPtCut = cms.double(0.8),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
            maxAbsPhotonSumPt_outsideSignalCone = cms.double(1.e+9),
            maxRelPhotonSumPt_outsideSignalCone = cms.double(0.10)
            ),
        cms.PSet(
            IDname = cms.string("ByLooseChargedIsolation"),
            maximumSumPtCut = cms.double(2.5),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True)
            ),
        cms.PSet(
            IDname = cms.string("ByPhotonPtSumOutsideSignalCone"),
            maximumSumPtCut = cms.double(-1.0),
            applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
            maxAbsPhotonSumPt_outsideSignalCone = cms.double(1.e+9),
            maxRelPhotonSumPt_outsideSignalCone = cms.double(0.10)
            )
        )
)
hpsPFTauBasicDiscriminators.qualityCuts.isolationQualityCuts.minTrackHits = cms.uint32(3)
hpsPFTauBasicDiscriminatorsTask = cms.Task(
    hpsPFTauBasicDiscriminators
)
hpsPFTauBasicDiscriminatorsSeq = cms.Sequence(
    hpsPFTauBasicDiscriminatorsTask
)

### dummy tasks to make these names available. To be removed!!!!!!!
hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits=hpsPFTauBasicDiscriminators.clone()
hpsPFTauChargedIsoPtSum=hpsPFTauBasicDiscriminators.clone()
hpsPFTauNeutralIsoPtSum=hpsPFTauBasicDiscriminators.clone()
hpsPFTauPUcorrPtSum=hpsPFTauBasicDiscriminators.clone()
hpsPFTauNeutralIsoPtSumWeight=hpsPFTauBasicDiscriminators.clone()
hpsPFTauFootprintCorrection=hpsPFTauBasicDiscriminators.clone()
hpsPFTauPhotonPtSumOutsideSignalCone=hpsPFTauBasicDiscriminators.clone()
hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits=hpsPFTauBasicDiscriminators.clone()
hpsPFTauDiscriminationByLoosePileupWeightedIsolation3Hits=hpsPFTauBasicDiscriminators.clone()
hpsPFTauDiscriminationByMediumPileupWeightedIsolation3Hits=hpsPFTauBasicDiscriminators.clone()
hpsPFTauDiscriminationByTightPileupWeightedIsolation3Hits=hpsPFTauBasicDiscriminators.clone()
hpsPFTauDiscriminationByRawPileupWeightedIsolation3Hits=hpsPFTauBasicDiscriminators.clone()
hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone=hpsPFTauBasicDiscriminators.clone()

## Cut based isolations dR=0.3
hpsPFTauBasicDiscriminatorsdR03 = hpsPFTauBasicDiscriminators.clone(
    deltaBetaFactor = cms.string('0.0720'), # 0.2*(0.3/0.5)^2
    customOuterCone = cms.double(0.3),
    IDdefinitions = cms.VPSet(
        cms.PSet(
            IDname = cms.string("ChargedIsoPtSumdR03"),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            storeRawSumPt = cms.bool(True)
            ),
        cms.PSet(
            IDname = cms.string("NeutralIsoPtSumdR03"),
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            storeRawSumPt = cms.bool(True)
            ),
        cms.PSet(
            IDname = cms.string("NeutralIsoPtSumWeightdR03"),
            ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
            storeRawSumPt = cms.bool(True),
            UseAllPFCandsForWeights = cms.bool(True)
            ),
        cms.PSet(
            IDname = cms.string("TauFootprintCorrectiondR03"),
            storeRawFootprintCorrection = cms.bool(True)
            ),
        cms.PSet(
            IDname = cms.string("PhotonPtSumOutsideSignalConedR03"),
            storeRawPhotonSumPt_outsideSignalCone = cms.bool(True)
            ),
        cms.PSet(
            IDname = cms.string("PUcorrPtSumdR03"),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawPUsumPt = cms.bool(True)
            )
        ),
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            IDname = cms.string("ByLooseCombinedIsolationDBSumPtCorr3HitsdR03"),
            maximumSumPtCut = cms.double(2.5),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
            maxAbsPhotonSumPt_outsideSignalCone = cms.double(1.e+9),
            maxRelPhotonSumPt_outsideSignalCone = cms.double(0.10)
            ),
        cms.PSet(
            IDname = cms.string("ByMediumCombinedIsolationDBSumPtCorr3HitsdR03"),
            maximumSumPtCut = cms.double(1.5),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
            maxAbsPhotonSumPt_outsideSignalCone = cms.double(1.e+9),
            maxRelPhotonSumPt_outsideSignalCone = cms.double(0.10)
            ),
        cms.PSet(
            IDname = cms.string("ByTightCombinedIsolationDBSumPtCorr3HitsdR03"),
            maximumSumPtCut = cms.double(0.8),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            applyPhotonPtSumOutsideSignalConeCut = cms.bool(True),
            maxAbsPhotonSumPt_outsideSignalCone = cms.double(1.e+9),
            maxRelPhotonSumPt_outsideSignalCone = cms.double(0.10)
            )
        )
)
hpsPFTauBasicDiscriminatorsdR03Task = cms.Task(
    hpsPFTauBasicDiscriminatorsdR03
)
hpsPFTauBasicDiscriminatorsdR03Seq = cms.Sequence(
    hpsPFTauBasicDiscriminatorsdR03Task
)

# define helper function to read indices of basic IDs
def getBasicTauDiscriminatorRawIndex(module, IDname):
    IDdefs = module.IDdefinitions.value()
    for i in range(len(module.IDdefinitions.value())):
        if IDname==IDdefs[i].IDname.value():
            return i
    print "Basic Tau Discriminator <{}> not found!".format(IDname)
    raise Exception


## ByLooseMuonRejection3
hpsPFTauDiscriminationByMuonRejection3 = pfRecoTauDiscriminationAgainstMuon2.clone(
    PFTauProducer = cms.InputTag('hpsPFTauProducer'),
    Prediscriminants = noPrediscriminants,
    wpDefinitions = cms.VPSet(
        cms.PSet(
            IDname = cms.string('ByLooseMuonRejection3'),
            discriminatorOption = cms.string('custom'),
            HoPMin = cms.double(0.2),
            maxNumberOfMatches = cms.int32(1),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(-1)
        ),
        cms.PSet(
            IDname = cms.string('ByTightMuonRejection3'),
            discriminatorOption = cms.string('custom'),
            HoPMin = cms.double(0.2),
            maxNumberOfMatches = cms.int32(1),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(0)
        )
    )
)


## ByLooseElectronRejection
hpsPFTauDiscriminationByLooseElectronRejection = pfRecoTauDiscriminationAgainstElectron.clone(
    PFTauProducer = cms.InputTag('hpsPFTauProducer'),
    Prediscriminants = noPrediscriminants,
    PFElectronMVA_maxValue = cms.double(0.6)
)
## ByMediumElectronRejection
hpsPFTauDiscriminationByMediumElectronRejection = pfRecoTauDiscriminationAgainstElectron.clone(
    PFTauProducer = cms.InputTag('hpsPFTauProducer'),
    Prediscriminants = noPrediscriminants,
    ApplyCut_EcalCrackCut = cms.bool(True)
)
## ByTightElectronRejection
hpsPFTauDiscriminationByTightElectronRejection = pfRecoTauDiscriminationAgainstElectron.clone(
    PFTauProducer = cms.InputTag('hpsPFTauProducer'),
    Prediscriminants = noPrediscriminants,
    ApplyCut_EcalCrackCut = cms.bool(True),
    ApplyCut_BremCombined = cms.bool(True)
)
## ByDeadECALElectronRejection 
hpsPFTauDiscriminationByDeadECALElectronRejection = pfRecoTauDiscriminationAgainstElectronDeadECAL.clone(
    PFTauProducer = cms.InputTag('hpsPFTauProducer'),
    Prediscriminants = requireDecayMode.clone()
)
## ByMVA6rawElectronRejection
hpsPFTauDiscriminationByMVA6rawElectronRejection = pfRecoTauDiscriminationAgainstElectronMVA6.clone(
    PFTauProducer = cms.InputTag('hpsPFTauProducer'),
    Prediscriminants = requireDecayMode.clone(),
    loadMVAfromDB = cms.bool(True),
    vetoEcalCracks = cms.bool(False),
    mvaName_NoEleMatch_woGwoGSF_BL = cms.string("RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL"),
    mvaName_NoEleMatch_wGwoGSF_BL = cms.string("RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL"),
    mvaName_woGwGSF_BL = cms.string("RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL"),
    mvaName_wGwGSF_BL = cms.string("RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL"),
    mvaName_NoEleMatch_woGwoGSF_EC = cms.string("RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC"),
    mvaName_NoEleMatch_wGwoGSF_EC = cms.string("RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC"),
    mvaName_woGwGSF_EC = cms.string("RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC"),
    mvaName_wGwGSF_EC = cms.string("RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC")
)
## ByMVA6ElectronRejection
hpsPFTauDiscriminationByMVA6ElectronRejection = recoTauDiscriminantCutMultiplexer.clone(
    PFTauProducer = cms.InputTag('hpsPFTauProducer'),
    Prediscriminants = requireDecayMode.clone(),
    toMultiplex = cms.InputTag('hpsPFTauDiscriminationByMVA6rawElectronRejection'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0), # minMVANoEleMatchWOgWOgsfBL
            cut = cms.string("RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL"),
            variable = cms.string("pt")
        ),
        cms.PSet(
            category = cms.uint32(2), # minMVANoEleMatchWgWOgsfBL
            cut = cms.string("RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL"),
            variable = cms.string("pt")
        ),
        cms.PSet(
            category = cms.uint32(5), # minMVAWOgWgsfBL
            cut = cms.string("RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL"),
            variable = cms.string("pt")
        ),
        cms.PSet(
            category = cms.uint32(7), # minMVAWgWgsfBL
            cut = cms.string("RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL"),
            variable = cms.string("pt")
        ),
        cms.PSet(
            category = cms.uint32(8), # minMVANoEleMatchWOgWOgsfEC
            cut = cms.string("RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC"),
            variable = cms.string("pt")
        ),
        cms.PSet(
            category = cms.uint32(10), # minMVANoEleMatchWgWOgsfEC
            cut = cms.string("RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC"),
            variable = cms.string("pt")
        ),
        cms.PSet(
            category = cms.uint32(13), # minMVAWOgWgsfEC
            cut = cms.string("RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC"),
            variable = cms.string("pt")
        ),
        cms.PSet(
            category = cms.uint32(15), # minMVAWgWgsfEC
            cut = cms.string("RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC"),
            variable = cms.string("pt")
        )
    ),
    workingPoints = cms.vstring(
        "_WPEff98",
        "_WPEff90",
        "_WPEff80",
        "_WPEff70",
        "_WPEff60"
    )
)

# Define the HPS selection discriminator used in cleaning
hpsSelectionDiscriminator.PFTauProducer = cms.InputTag("combinatoricRecoTaus")
#----------------------------------------------------------------------------
# CV: disable 3Prong1Pi0 decay mode
hpsSelectionDiscriminator.decayModes = cms.VPSet(
    decayMode_1Prong0Pi0,
    decayMode_1Prong1Pi0,
    decayMode_1Prong2Pi0,
    decayMode_2Prong0Pi0,
    decayMode_2Prong1Pi0,
    decayMode_3Prong0Pi0,
    decayMode_3Prong1Pi0,
)
#----------------------------------------------------------------------------

from RecoTauTag.RecoTau.RecoTauCleaner_cfi import RecoTauCleaner
hpsPFTauProducerSansRefs = RecoTauCleaner.clone(
    src = cms.InputTag("combinatoricRecoTaus")
)
hpsPFTauProducerSansRefs.cleaners[1].src = cms.InputTag("hpsSelectionDiscriminator")

from RecoTauTag.RecoTau.RecoTauPiZeroUnembedder_cfi import RecoTauPiZeroUnembedder
hpsPFTauProducer = RecoTauPiZeroUnembedder.clone(
    src = cms.InputTag("hpsPFTauProducerSansRefs")
)

from RecoTauTag.RecoTau.PFTauPrimaryVertexProducer_cfi      import *
from RecoTauTag.RecoTau.PFTauSecondaryVertexProducer_cfi    import *
from RecoTauTag.RecoTau.PFTauTransverseImpactParameters_cfi import *
hpsPFTauPrimaryVertexProducer = PFTauPrimaryVertexProducer.clone(
    PFTauTag = cms.InputTag("hpsPFTauProducer"),
    ElectronTag = cms.InputTag(""),
    MuonTag = cms.InputTag(""),
    PVTag = cms.InputTag("offlinePrimaryVertices"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    Algorithm = cms.int32(0),
    useBeamSpot = cms.bool(True),
    RemoveMuonTracks = cms.bool(False),
    RemoveElectronTracks = cms.bool(False),
    useSelectedTaus = cms.bool(False),
    discriminators = cms.VPSet(
        cms.PSet(
            discriminator = cms.InputTag('hpsPFTauDiscriminationByDecayModeFindingNewDMs'),
            selectionCut = cms.double(0.5)
        )
    ),
    cut = cms.string("pt > 18.0 & abs(eta) < 2.4")
)

hpsPFTauSecondaryVertexProducer = PFTauSecondaryVertexProducer.clone(
    PFTauTag = cms.InputTag("hpsPFTauProducer")
)
hpsPFTauTransverseImpactParameters = PFTauTransverseImpactParameters.clone(
    PFTauTag = cms.InputTag("hpsPFTauProducer"),
    PFTauPVATag = cms.InputTag("hpsPFTauPrimaryVertexProducer"),
    PFTauSVATag = cms.InputTag("hpsPFTauSecondaryVertexProducer"),
    useFullCalculation = cms.bool(True)
)
hpsPFTauVertexAndImpactParametersTask = cms.Task(
    hpsPFTauPrimaryVertexProducer,
    hpsPFTauSecondaryVertexProducer,
    hpsPFTauTransverseImpactParameters
)
hpsPFTauVertexAndImpactParametersSeq = cms.Sequence(
    hpsPFTauVertexAndImpactParametersTask
)

#Define new Run2 MVA isolations
from RecoTauTag.RecoTau.PFRecoTauDiscriminationByMVAIsolationRun2_cff import *
hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw = discriminationByIsolationMVArun2v1raw.clone(
    PFTauProducer = cms.InputTag('hpsPFTauProducer'),
    Prediscriminants = requireDecayMode.clone(),
    loadMVAfromDB = cms.bool(True),
    mvaName = cms.string("RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2"),
    mvaOpt = cms.string("DBoldDMwLTwGJ"),
    srcTauTransverseImpactParameters = cms.InputTag('hpsPFTauTransverseImpactParameters'),
    srcBasicTauDiscriminators = cms.InputTag('hpsPFTauBasicDiscriminators'),
    srcChargedIsoPtSumIndex = cms.int32(getBasicTauDiscriminatorRawIndex(hpsPFTauBasicDiscriminators, 'ChargedIsoPtSum')),
    srcNeutralIsoPtSumIndex = cms.int32(getBasicTauDiscriminatorRawIndex(hpsPFTauBasicDiscriminators, 'NeutralIsoPtSum')),
    srcPUcorrPtSumIndex = cms.int32(getBasicTauDiscriminatorRawIndex(hpsPFTauBasicDiscriminators, 'PUcorrPtSum')),
    srcPhotonPtSumOutsideSignalConeIndex = cms.int32(getBasicTauDiscriminatorRawIndex(hpsPFTauBasicDiscriminators, 'PhotonPtSumOutsideSignalCone')),
    srcFootprintCorrectionIndex = cms.int32(getBasicTauDiscriminatorRawIndex(hpsPFTauBasicDiscriminators, 'TauFootprintCorrection')),
    verbosity = cms.int32(0)
)

hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT = discriminationByIsolationMVArun2v1.clone(
    PFTauProducer = cms.InputTag('hpsPFTauProducer'),
    Prediscriminants = requireDecayMode.clone(),
    toMultiplex = cms.InputTag('hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw'),
    loadMVAfromDB = cms.bool(True),
    mvaOutput_normalization = cms.string("RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_mvaOutput_normalization"),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0),
            cut = cms.string("RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2"),
            variable = cms.string("pt")
        )
    ),
    workingPoints = cms.vstring(
        "_WPEff95",
        "_WPEff90",
        "_WPEff80",
        "_WPEff70",
        "_WPEff60",
        "_WPEff50",
        "_WPEff40"
    )
)
    
hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw = hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw.clone(
    mvaName = cms.string("RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2"),
    mvaOpt = cms.string("DBnewDMwLTwGJ"),
    verbosity = cms.int32(0)
)

hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT = hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT.clone(
    toMultiplex = cms.InputTag('hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw'),
    loadMVAfromDB = cms.bool(True),
    mvaOutput_normalization = cms.string("RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_mvaOutput_normalization"),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0),
            cut = cms.string("RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2"),
            variable = cms.string("pt")
        )
    ),
    workingPoints = cms.vstring(
        "_WPEff95",
        "_WPEff90",
        "_WPEff80",
        "_WPEff70",
        "_WPEff60",
        "_WPEff50",
        "_WPEff40"
    )
)

hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw = hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw.clone(
    mvaName = cms.string("RecoTauTag_tauIdMVAPWoldDMwLTv1"),
    mvaOpt = cms.string("PWoldDMwLT"),
    srcNeutralIsoPtSumIndex = cms.int32(getBasicTauDiscriminatorRawIndex(hpsPFTauBasicDiscriminators, 'NeutralIsoPtSumWeight')),
    verbosity = cms.int32(0)
)

hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLT = hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT.clone(
    toMultiplex = cms.InputTag('hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw'),
    loadMVAfromDB = cms.bool(True),
    mvaOutput_normalization = cms.string("RecoTauTag_tauIdMVAPWoldDMwLTv1_mvaOutput_normalization"),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0),
            cut = cms.string("RecoTauTag_tauIdMVAPWoldDMwLTv1"),
            variable = cms.string("pt")
        )
    ),
    workingPoints = cms.vstring(
        "_WPEff90",
        "_WPEff80",
        "_WPEff70",
        "_WPEff60",
        "_WPEff50",
        "_WPEff40"
    )
)

hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw = hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw.clone(
    mvaName = cms.string("RecoTauTag_tauIdMVAPWnewDMwLTv1"),
    mvaOpt = cms.string("PWnewDMwLT"),
    verbosity = cms.int32(0)
)

hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLT = hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLT.clone(
    toMultiplex = cms.InputTag('hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw'),
    loadMVAfromDB = cms.bool(True),
    mvaOutput_normalization = cms.string("RecoTauTag_tauIdMVAPWnewDMwLTv1_mvaOutput_normalization"),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0),
            cut = cms.string("RecoTauTag_tauIdMVAPWnewDMwLTv1"),
            variable = cms.string("pt")
        )
    ),
    workingPoints = cms.vstring(
        "_WPEff90",
        "_WPEff80",
        "_WPEff70",
        "_WPEff60",
        "_WPEff50",
        "_WPEff40"
    )
)

hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw = hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw.clone(
    mvaName = cms.string("RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2"),
    mvaOpt = cms.string("DBoldDMwLTwGJ"),
    srcBasicTauDiscriminators = cms.InputTag('hpsPFTauBasicDiscriminatorsdR03'),
    srcChargedIsoPtSumIndex = cms.int32(getBasicTauDiscriminatorRawIndex(hpsPFTauBasicDiscriminatorsdR03, 'ChargedIsoPtSumdR03')),
    srcNeutralIsoPtSumIndex = cms.int32(getBasicTauDiscriminatorRawIndex(hpsPFTauBasicDiscriminatorsdR03, 'NeutralIsoPtSumdR03')),
    srcPUcorrPtSumIndex = cms.int32(getBasicTauDiscriminatorRawIndex(hpsPFTauBasicDiscriminatorsdR03, 'PUcorrPtSumdR03')),
    srcPhotonPtSumOutsideSignalConeIndex = cms.int32(getBasicTauDiscriminatorRawIndex(hpsPFTauBasicDiscriminatorsdR03, 'PhotonPtSumOutsideSignalConedR03')),
    srcFootprintCorrectionIndex = cms.int32(getBasicTauDiscriminatorRawIndex(hpsPFTauBasicDiscriminatorsdR03, 'TauFootprintCorrectiondR03')),
    verbosity = cms.int32(0)
)
hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT = hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT.clone(
    PFTauProducer = cms.InputTag('hpsPFTauProducer'),
    Prediscriminants = requireDecayMode.clone(),
    toMultiplex = cms.InputTag('hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw'),
    loadMVAfromDB = cms.bool(True),
    mvaOutput_normalization = cms.string("RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_mvaOutput_normalization"),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0),
            cut = cms.string("RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2"),
            variable = cms.string("pt")
        )
    ),
    workingPoints = cms.vstring(
        "_WPEff95",
        "_WPEff90",
        "_WPEff80",
        "_WPEff70",
        "_WPEff60",
        "_WPEff50",
        "_WPEff40"
    )
)

hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw = hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw.clone(
    mvaName = cms.string("RecoTauTag_tauIdMVAPWdR03oldDMwLTv1"),
    mvaOpt = cms.string("PWoldDMwLT"),
    srcNeutralIsoPtSumIndex = cms.int32(getBasicTauDiscriminatorRawIndex(hpsPFTauBasicDiscriminators, 'NeutralIsoPtSumWeight')),
    verbosity = cms.int32(0)
)
hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLT = hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT.clone(
    toMultiplex = cms.InputTag('hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw'),
    loadMVAfromDB = cms.bool(True),
    mvaOutput_normalization = cms.string("RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_mvaOutput_normalization"),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0),
            cut = cms.string("RecoTauTag_tauIdMVAPWdR03oldDMwLTv1"),
            variable = cms.string("pt")
        )
    ),
    workingPoints = cms.vstring(
        "_WPEff90",
        "_WPEff80",
        "_WPEff70",
        "_WPEff60",
        "_WPEff50",
        "_WPEff40"
    )
)

hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTTask = cms.Task(
    hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw,
    hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT
    )

hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTTask = cms.Task(
    hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw,
    hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT
    )

hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTTask = cms.Task(
    hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw,
    hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLT
    )

hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTTask = cms.Task(
    hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw,
    hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLT
    )

hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTTask = cms.Task(
    hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw,
    hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT
    )

hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTTask = cms.Task(
    hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw,
    hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLT
    )

hpsPFTauMVAIsolation2Task = cms.Task(
    #hpsPFTauBasicDiscriminatorsTask, included separately in produceAndDiscriminateHPSPFTausTask
    hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTTask,
    hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTTask,
    hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTTask,    
    hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTTask,
    #hpsPFTauBasicDiscriminatorsdR03Task, included separately in produceAndDiscriminateHPSPFTausTask
    hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTTask,
    hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTTask
    )

hpsPFTauMVAIsolation2Seq = cms.Sequence(
    hpsPFTauMVAIsolation2Task
    )

produceHPSPFTausTask = cms.Task(
    hpsSelectionDiscriminator,
    #hpsTightIsolationCleaner,
    #hpsMediumIsolationCleaner,
    #hpsLooseIsolationCleaner,
    #hpsVLooseIsolationCleaner,
    hpsPFTauProducerSansRefs,
    hpsPFTauProducer
    )

produceHPSPFTaus = cms.Sequence(
    produceHPSPFTausTask
    )

produceAndDiscriminateHPSPFTausTask = cms.Task(
    produceHPSPFTausTask,
    hpsPFTauDiscriminationByDecayModeFindingNewDMs,
    hpsPFTauDiscriminationByDecayModeFindingOldDMs,
    hpsPFTauDiscriminationByDecayModeFinding, # CV: kept for backwards compatibility
    hpsPFTauBasicDiscriminatorsTask,
    hpsPFTauBasicDiscriminatorsdR03Task,
    hpsPFTauDiscriminationByLooseElectronRejection,
    hpsPFTauDiscriminationByMediumElectronRejection,
    hpsPFTauDiscriminationByTightElectronRejection,
    hpsPFTauDiscriminationByMVA6rawElectronRejection,
    hpsPFTauDiscriminationByMVA6ElectronRejection,
    hpsPFTauDiscriminationByDeadECALElectronRejection,
    hpsPFTauDiscriminationByMuonRejection3,
    hpsPFTauVertexAndImpactParametersTask,
    hpsPFTauMVAIsolation2Task
    )

produceAndDiscriminateHPSPFTaus = cms.Sequence(
    produceAndDiscriminateHPSPFTausTask
    )
