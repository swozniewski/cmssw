import FWCore.ParameterSet.Config as cms

##################### Updated tau collection with MVA-based tau-Ids rerun #######
# Used only in some eras
from RecoTauTag.Configuration.loadRecoTauTagMVAsFromPrepDB_cfi import *
from RecoTauTag.RecoTau.PATTauDiscriminationByMVAIsolationRun2_cff import *
from Configuration.Eras.Modifier_run2_miniAOD_80XLegacy_cff import run2_miniAOD_80XLegacy
from Configuration.Eras.Modifier_run2_nanoAOD_94XMiniAODv1_cff import run2_nanoAOD_94XMiniAODv1

### MVAIso 2017v2
## DBoldDM
# Raw
patTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw = patDiscriminationByIsolationMVArun2v1raw.clone(
   PATTauProducer = cms.InputTag('slimmedTaus'),
   Prediscriminants = noPrediscriminants,
   loadMVAfromDB = cms.bool(True),
   mvaName = cms.string("RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2"), # name of the training you want to use
   mvaOpt = cms.string("DBoldDMwLTwGJ"), # option you want to use for your training (i.e., which variables are used to compute the BDT score)
   verbosity = cms.int32(0)
)
# WPs
patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT = patDiscriminationByIsolationMVArun2v1.clone(
   PATTauProducer = cms.InputTag('slimmedTaus'),
   Prediscriminants = noPrediscriminants,
   toMultiplex = cms.InputTag('patTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw'),
   loadMVAfromDB = cms.bool(True),
   mvaOutput_normalization = cms.string("RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_mvaOutput_normalization"), # normalization fo the training you want to use
   mapping = cms.VPSet(
      cms.PSet(
         category = cms.uint32(0),
         cut = cms.string("RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2"), # this is the name of the working point you want to use
         variable = cms.string("pt"),
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
# MVAIso DBoldDM Seqeunce
patTauDiscriminationByIsolationMVArun2v1DBoldDMwLTSeq = cms.Sequence(
    patTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw
    + patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT
)
## DBnewDM
# Raw
patTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw = patDiscriminationByIsolationMVArun2v1raw.clone(
   PATTauProducer = cms.InputTag('slimmedTaus'),
   Prediscriminants = noPrediscriminants,
   loadMVAfromDB = cms.bool(True),
   mvaName = cms.string("RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2"), # name of the training you want to use
   mvaOpt = cms.string("DBnewDMwLTwGJ"), # option you want to use for your training (i.e., which variables are used to compute the BDT score)
   verbosity = cms.int32(0)
)
# WPs
patTauDiscriminationByIsolationMVArun2v1DBnewDMwLT = patDiscriminationByIsolationMVArun2v1.clone(
   PATTauProducer = cms.InputTag('slimmedTaus'),
   Prediscriminants = noPrediscriminants,
   toMultiplex = cms.InputTag('patTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw'),
   loadMVAfromDB = cms.bool(True),
   mvaOutput_normalization = cms.string("RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_mvaOutput_normalization"), # normalization fo the training you want to use
   mapping = cms.VPSet(
      cms.PSet(
         category = cms.uint32(0),
         cut = cms.string("RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2"), # this is the name of the working point you want to use
         variable = cms.string("pt"),
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
# MVAIso DBnewDM Seqeunce
patTauDiscriminationByIsolationMVArun2v1DBnewDMwLTSeq = cms.Sequence(
    patTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw
    + patTauDiscriminationByIsolationMVArun2v1DBnewDMwLT
)
## DBoldDMdR0p3
# Raw
patTauDiscriminationByIsolationMVArun2v1DBoldDMdR0p3wLTraw = patDiscriminationByIsolationMVArun2v1raw.clone(
   PATTauProducer = cms.InputTag('slimmedTaus'),
   Prediscriminants = noPrediscriminants,
   loadMVAfromDB = cms.bool(True),
   mvaName = cms.string("RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2"), # name of the training you want to use
   mvaOpt = cms.string("DBoldDMwLTwGJ"), # option you want to use for your training (i.e., which variables are used to compute the BDT score)
   srcChargedIsoPtSum = cms.string('chargedIsoPtSumdR03'),
   srcFootprintCorrection = cms.string('footprintCorrectiondR03'),
   srcNeutralIsoPtSum = cms.string('neutralIsoPtSumdR03'),
   srcPUcorrPtSum = cms.string('puCorrPtSum'),
   srcPhotonPtSumOutsideSignalCone = cms.string('photonPtSumOutsideSignalConedR03'),
   verbosity = cms.int32(0)
)
# WPs
patTauDiscriminationByIsolationMVArun2v1DBoldDMdR0p3wLT = patDiscriminationByIsolationMVArun2v1.clone(
   PATTauProducer = cms.InputTag('slimmedTaus'),
   Prediscriminants = noPrediscriminants,
   toMultiplex = cms.InputTag('patTauDiscriminationByIsolationMVArun2v1DBoldDMdR0p3wLTraw'),
   loadMVAfromDB = cms.bool(True),
   mvaOutput_normalization = cms.string("RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_mvaOutput_normalization"), # normalization fo the training you want to use
   mapping = cms.VPSet(
      cms.PSet(
         category = cms.uint32(0),
         cut = cms.string("RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2"), # this is the name of the working point you want to use
         variable = cms.string("pt"),
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
# MVAIso DBoldDMdR0p3 Seqeunce
patTauDiscriminationByIsolationMVArun2v1DBoldDMdR0p3wLTSeq = cms.Sequence(
    patTauDiscriminationByIsolationMVArun2v1DBoldDMdR0p3wLTraw
    + patTauDiscriminationByIsolationMVArun2v1DBoldDMdR0p3wLT
)
### MVAIso 2017v1 for Nano on top of MiniAODv1
## DBoldDM
# Raw
patTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw2017v1 = patDiscriminationByIsolationMVArun2v1raw.clone(
   PATTauProducer = cms.InputTag('slimmedTaus'),
   Prediscriminants = noPrediscriminants,
   loadMVAfromDB = cms.bool(True),
   mvaName = cms.string("RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1"), # name of the training you want to use
   mvaOpt = cms.string("DBoldDMwLTwGJ"), # option you want to use for your training (i.e., which variables are used to compute the BDT score)
   verbosity = cms.int32(0)
)
# WPs
patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2017v1 = patDiscriminationByIsolationMVArun2v1.clone(
   PATTauProducer = cms.InputTag('slimmedTaus'),
   Prediscriminants = noPrediscriminants,
   toMultiplex = cms.InputTag('patTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw2017v1'),
   loadMVAfromDB = cms.bool(True),
   mvaOutput_normalization = cms.string("RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_mvaOutput_normalization"), # normalization fo the training you want to use
   mapping = cms.VPSet(
      cms.PSet(
         category = cms.uint32(0),
         cut = cms.string("RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1"), # this is the name of the working point you want to use
         variable = cms.string("pt"),
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
# MVAIso DBoldDM Seqeunce
patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2017v1Seq = cms.Sequence(
    patTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw2017v1
    + patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2017v1
)
### MVAIso 2015 for Nano on top of MiniAODv2
## DBoldDM
# Raw
patTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw2015 = patDiscriminationByIsolationMVArun2v1raw.clone(
   PATTauProducer = cms.InputTag('slimmedTaus'),
   Prediscriminants = noPrediscriminants,
   loadMVAfromDB = cms.bool(True),
   mvaName = cms.string("RecoTauTag_tauIdMVADBoldDMwLTv1"), # name of the training you want to use
   mvaOpt = cms.string("DBoldDMwLT"), # option you want to use for your training (i.e., which variables are used to compute the BDT score)
   verbosity = cms.int32(0)
)
# VLoose WP
patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2015 = patDiscriminationByIsolationMVArun2v1.clone(
   PATTauProducer = cms.InputTag('slimmedTaus'),
   Prediscriminants = noPrediscriminants,
   toMultiplex = cms.InputTag('patTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw2015'),
   loadMVAfromDB = cms.bool(True),
   mvaOutput_normalization = cms.string("RecoTauTag_tauIdMVADBoldDMwLTv1_mvaOutput_normalization"), # normalization fo the training you want to use
   mapping = cms.VPSet(
      cms.PSet(
         category = cms.uint32(0),
         cut = cms.string("RecoTauTag_tauIdMVADBoldDMwLTv1"), # this is the name of the working point you want to use
         variable = cms.string("pt"),
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
# MVAIso DBoldDM Seqeunce
patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2015Seq = cms.Sequence(
    patTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw2015
    + patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2015
)


### Define new anit-e discriminants (2018)
antiElectronDiscrMVA6_version = "MVA6v3_noeveto"
## Raw
from RecoTauTag.RecoTau.PATTauDiscriminationAgainstElectronMVA6_cfi import patTauDiscriminationAgainstElectronMVA6
from RecoTauTag.RecoTau.TauDiscriminatorTools import noPrediscriminants
patTauDiscriminationByElectronRejectionMVA62018Raw = patTauDiscriminationAgainstElectronMVA6.clone(
    Prediscriminants = noPrediscriminants, #already selected for MiniAOD
    vetoEcalCracks = False, #keep tau candidates in EB-EE cracks
    mvaName_NoEleMatch_wGwoGSF_BL = 'RecoTauTag_antiElectron'+antiElectronDiscrMVA6_version+'_gbr_NoEleMatch_wGwoGSF_BL',
    mvaName_NoEleMatch_wGwoGSF_EC = 'RecoTauTag_antiElectron'+antiElectronDiscrMVA6_version+'_gbr_NoEleMatch_wGwoGSF_EC',
    mvaName_NoEleMatch_woGwoGSF_BL = 'RecoTauTag_antiElectron'+antiElectronDiscrMVA6_version+'_gbr_NoEleMatch_woGwoGSF_BL',
    mvaName_NoEleMatch_woGwoGSF_EC = 'RecoTauTag_antiElectron'+antiElectronDiscrMVA6_version+'_gbr_NoEleMatch_woGwoGSF_EC',
    mvaName_wGwGSF_BL = 'RecoTauTag_antiElectron'+antiElectronDiscrMVA6_version+'_gbr_wGwGSF_BL',
    mvaName_wGwGSF_EC = 'RecoTauTag_antiElectron'+antiElectronDiscrMVA6_version+'_gbr_wGwGSF_EC',
    mvaName_woGwGSF_BL = 'RecoTauTag_antiElectron'+antiElectronDiscrMVA6_version+'_gbr_woGwGSF_BL',
    mvaName_woGwGSF_EC = 'RecoTauTag_antiElectron'+antiElectronDiscrMVA6_version+'_gbr_woGwGSF_EC'
)
## anti-e 2018 WPs
from RecoTauTag.RecoTau.PATTauDiscriminantCutMultiplexer_cfi import patTauDiscriminantCutMultiplexer
# VLoose
patTauDiscriminationByElectronRejectionMVA62018 = patTauDiscriminantCutMultiplexer.clone(
    PATTauProducer = patTauDiscriminationByElectronRejectionMVA62018Raw.PATTauProducer,
    Prediscriminants = patTauDiscriminationByElectronRejectionMVA62018Raw.Prediscriminants,
    toMultiplex = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018Raw"),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0),
            cut = cms.string('RecoTauTag_antiElectron'+antiElectronDiscrMVA6_version+'_gbr_NoEleMatch_woGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(2),
            cut = cms.string('RecoTauTag_antiElectron'+antiElectronDiscrMVA6_version+'_gbr_NoEleMatch_wGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(5),
            cut = cms.string('RecoTauTag_antiElectron'+antiElectronDiscrMVA6_version+'_gbr_woGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(7),
            cut = cms.string('RecoTauTag_antiElectron'+antiElectronDiscrMVA6_version+'_gbr_wGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(8),
            cut = cms.string('RecoTauTag_antiElectron'+antiElectronDiscrMVA6_version+'_gbr_NoEleMatch_woGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(10),
            cut = cms.string('RecoTauTag_antiElectron'+antiElectronDiscrMVA6_version+'_gbr_NoEleMatch_wGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(13),
            cut = cms.string('RecoTauTag_antiElectron'+antiElectronDiscrMVA6_version+'_gbr_woGwGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(15),
            cut = cms.string('RecoTauTag_antiElectron'+antiElectronDiscrMVA6_version+'_gbr_wGwGSF_EC'),
            variable = cms.string('pt')
        )
    ),
    workingPoints = cms.vstring(
      "_WPeff98",
      "_WPeff90",
      "_WPeff80",
      "_WPeff70",
      "_WPeff60"
    )
)
### Define v1 anit-e discriminants (2015)
antiElectronDiscrMVA6v1_version = "MVA6v1"
## Raw
patTauDiscriminationByElectronRejectionMVA62015Raw = patTauDiscriminationAgainstElectronMVA6.clone(
    Prediscriminants = noPrediscriminants, #already selected for MiniAOD
    vetoEcalCracks = True, #don't keep tau candidates in EB-EE cracks for v1
    mvaName_NoEleMatch_wGwoGSF_BL = 'RecoTauTag_antiElectron'+antiElectronDiscrMVA6v1_version+'_gbr_NoEleMatch_wGwoGSF_BL',
    mvaName_NoEleMatch_wGwoGSF_EC = 'RecoTauTag_antiElectron'+antiElectronDiscrMVA6v1_version+'_gbr_NoEleMatch_wGwoGSF_EC',
    mvaName_NoEleMatch_woGwoGSF_BL = 'RecoTauTag_antiElectron'+antiElectronDiscrMVA6v1_version+'_gbr_NoEleMatch_woGwoGSF_BL',
    mvaName_NoEleMatch_woGwoGSF_EC = 'RecoTauTag_antiElectron'+antiElectronDiscrMVA6v1_version+'_gbr_NoEleMatch_woGwoGSF_EC',
    mvaName_wGwGSF_BL = 'RecoTauTag_antiElectron'+antiElectronDiscrMVA6v1_version+'_gbr_wGwGSF_BL',
    mvaName_wGwGSF_EC = 'RecoTauTag_antiElectron'+antiElectronDiscrMVA6v1_version+'_gbr_wGwGSF_EC',
    mvaName_woGwGSF_BL = 'RecoTauTag_antiElectron'+antiElectronDiscrMVA6v1_version+'_gbr_woGwGSF_BL',
    mvaName_woGwGSF_EC = 'RecoTauTag_antiElectron'+antiElectronDiscrMVA6v1_version+'_gbr_woGwGSF_EC'
)
## anti-e v1 WPs
patTauDiscriminationByElectronRejectionMVA62015 = patTauDiscriminationByElectronRejectionMVA62018.clone(
    PATTauProducer = patTauDiscriminationByElectronRejectionMVA62015Raw.PATTauProducer,
    Prediscriminants = patTauDiscriminationByElectronRejectionMVA62015Raw.Prediscriminants,
    toMultiplex = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62015Raw"),
    workingPoints = cms.vstring(
      "_WPEff99",
      "_WPEff96",
      "_WPEff91",
      "_WPEff85",
      "_WPEff79"
    )
)
for m in patTauDiscriminationByElectronRejectionMVA62015.mapping:
    m.cut = m.cut.value().replace(antiElectronDiscrMVA6_version, antiElectronDiscrMVA6v1_version)
### Put all anti-e tau-IDs into a sequence
_patTauDiscriminationByElectronRejection2018Seq = cms.Sequence(
    patTauDiscriminationByElectronRejectionMVA62018Raw
    +patTauDiscriminationByElectronRejectionMVA62018
)
_patTauDiscriminationByElectronRejection2015Seq = cms.Sequence(
    patTauDiscriminationByElectronRejectionMVA62015Raw
    +patTauDiscriminationByElectronRejectionMVA62015
)
patTauDiscriminationByElectronRejectionSeq = _patTauDiscriminationByElectronRejection2015Seq.copy()
(~run2_miniAOD_80XLegacy).toReplaceWith(patTauDiscriminationByElectronRejectionSeq,
                      _patTauDiscriminationByElectronRejection2018Seq)


### put all new MVA tau-Id stuff to one Sequence
_patTauMVAIDsSeq2017v2 = cms.Sequence(
    patTauDiscriminationByIsolationMVArun2v1DBoldDMwLTSeq
    +patTauDiscriminationByIsolationMVArun2v1DBnewDMwLTSeq
    +patTauDiscriminationByIsolationMVArun2v1DBoldDMdR0p3wLTSeq
    +patTauDiscriminationByElectronRejectionSeq
)
patTauMVAIDsSeq = _patTauMVAIDsSeq2017v2.copy()
patTauMVAIDsSeq += patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2015Seq

_patTauMVAIDsSeqWith2017v1 = _patTauMVAIDsSeq2017v2.copy()
_patTauMVAIDsSeqWith2017v1 += patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2017v1Seq
for era in [run2_nanoAOD_94XMiniAODv1,]:
    era.toReplaceWith(patTauMVAIDsSeq,_patTauMVAIDsSeqWith2017v1)

# embed new MVA tau-Ids into new tau collection
def tauIDMVAinputs(module, wp):
    return cms.PSet(inputTag = cms.InputTag(module), workingPointIndex = cms.int32(-1 if wp=="raw" else -2 if wp=="category" else globals()[module].workingPoints.index(wp)))
slimmedTausUpdated = cms.EDProducer("PATTauIDEmbedder",
    src = cms.InputTag('slimmedTaus'),
    tauIDSources = cms.PSet() # PSet defined below in era dependent way
)
_tauIDSources2017v2 = cms.PSet(
        #oldDM
        byIsolationMVArun2v1DBoldDMwLTraw2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "raw"),
        byVVLooseIsolationMVArun2v1DBoldDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_WPEff95"),
        byVLooseIsolationMVArun2v1DBoldDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_WPEff90"),
        byLooseIsolationMVArun2v1DBoldDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_WPEff80"),
        byMediumIsolationMVArun2v1DBoldDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_WPEff70"),
        byTightIsolationMVArun2v1DBoldDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_WPEff60"),
        byVTightIsolationMVArun2v1DBoldDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_WPEff50"),
        byVVTightIsolationMVArun2v1DBoldDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_WPEff40"),
        #newDM
        byIsolationMVArun2v1DBnewDMwLTraw2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "raw"),
        byVVLooseIsolationMVArun2v1DBnewDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_WPEff95"),
        byVLooseIsolationMVArun2v1DBnewDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_WPEff90"),
        byLooseIsolationMVArun2v1DBnewDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_WPEff80"),
        byMediumIsolationMVArun2v1DBnewDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_WPEff70"),
        byTightIsolationMVArun2v1DBnewDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_WPEff60"),
        byVTightIsolationMVArun2v1DBnewDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_WPEff50"),
        byVVTightIsolationMVArun2v1DBnewDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_WPEff40"),
        #oldDMdR0p3
        byIsolationMVArun2v1DBdR03oldDMwLTraw2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMdR0p3wLT", "raw"),
        byVVLooseIsolationMVArun2v1DBdR03oldDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMdR0p3wLT", "_WPEff95"),
        byVLooseIsolationMVArun2v1DBdR03oldDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMdR0p3wLT", "_WPEff90"),
        byLooseIsolationMVArun2v1DBdR03oldDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMdR0p3wLT", "_WPEff80"),
        byMediumIsolationMVArun2v1DBdR03oldDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMdR0p3wLT", "_WPEff70"),
        byTightIsolationMVArun2v1DBdR03oldDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMdR0p3wLT", "_WPEff60"),
        byVTightIsolationMVArun2v1DBdR03oldDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMdR0p3wLT", "_WPEff50"),
        byVVTightIsolationMVArun2v1DBdR03oldDMwLT2017v2 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMdR0p3wLT", "_WPEff40")
)
_tauIDSources2017v1 = cms.PSet(
    byIsolationMVArun2v1DBoldDMwLTraw2017v1 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2017v1", "raw"),
    byVVLooseIsolationMVArun2v1DBoldDMwLT2017v1 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2017v1", "_WPEff95"),
    byVLooseIsolationMVArun2v1DBoldDMwLT2017v1 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2017v1", "_WPEff90"),
    byLooseIsolationMVArun2v1DBoldDMwLT2017v1 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2017v1", "_WPEff80"),
    byMediumIsolationMVArun2v1DBoldDMwLT2017v1 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2017v1", "_WPEff70"),
    byTightIsolationMVArun2v1DBoldDMwLT2017v1 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2017v1", "_WPEff60"),
    byVTightIsolationMVArun2v1DBoldDMwLT2017v1 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2017v1", "_WPEff50"),
    byVVTightIsolationMVArun2v1DBoldDMwLT2017v1 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2017v1", "_WPEff40")
)
_tauIDSourcesWith2017v1 = cms.PSet(
    _tauIDSources2017v2.clone(),
    _tauIDSources2017v1
)
_tauIDSources2015 = cms.PSet(
    byIsolationMVArun2v1DBoldDMwLTraw2015 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2015", "raw"),
    byVLooseIsolationMVArun2v1DBoldDMwLT2015 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2015", "_WPEff90"),
    byLooseIsolationMVArun2v1DBoldDMwLT2015 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2015", "_WPEff80"),
    byMediumIsolationMVArun2v1DBoldDMwLT2015 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2015", "_WPEff70"),
    byTightIsolationMVArun2v1DBoldDMwLT2015 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2015", "_WPEff60"),
    byVTightIsolationMVArun2v1DBoldDMwLT2015 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2015", "_WPEff50"),
    byVVTightIsolationMVArun2v1DBoldDMwLT2015 = tauIDMVAinputs("patTauDiscriminationByIsolationMVArun2v1DBoldDMwLT2015", "_WPEff40")
)
_tauIDSourcesWith2015 = cms.PSet(
    _tauIDSources2017v2.clone(),
    _tauIDSources2015
)
slimmedTausUpdated.tauIDSources=_tauIDSourcesWith2015

for era in [run2_nanoAOD_94XMiniAODv1,]:
    era.toModify(slimmedTausUpdated,
                 tauIDSources = _tauIDSourcesWith2017v1
    )

_antiETauIDSources2018 = cms.PSet(
    againstElectronMVA6Raw2018 = tauIDMVAinputs("patTauDiscriminationByElectronRejectionMVA62018", "raw"),
    againstElectronMVA6category2018 = tauIDMVAinputs("patTauDiscriminationByElectronRejectionMVA62018", "category"),
    againstElectronVLooseMVA62018 = tauIDMVAinputs("patTauDiscriminationByElectronRejectionMVA62018", "_WPeff98"),
    againstElectronLooseMVA62018 = tauIDMVAinputs("patTauDiscriminationByElectronRejectionMVA62018", "_WPeff90"),
    againstElectronMediumMVA62018 = tauIDMVAinputs("patTauDiscriminationByElectronRejectionMVA62018", "_WPeff80"),
    againstElectronTightMVA62018 = tauIDMVAinputs("patTauDiscriminationByElectronRejectionMVA62018", "_WPeff70"),
    againstElectronVTightMVA62018 = tauIDMVAinputs("patTauDiscriminationByElectronRejectionMVA62018", "_WPeff60")
)
_tauIDSourcesWithAntiE2018 = cms.PSet(
    slimmedTausUpdated.tauIDSources.clone(),
    _antiETauIDSources2018
)
_antiETauIDSources2015 = cms.PSet(
    againstElectronMVA6Raw2015 = tauIDMVAinputs("patTauDiscriminationByElectronRejectionMVA62015", "raw"),
    againstElectronMVA6category2015 = tauIDMVAinputs("patTauDiscriminationByElectronRejectionMVA62015", "category"),
    againstElectronVLooseMVA62015 = tauIDMVAinputs("patTauDiscriminationByElectronRejectionMVA62015", "_WPEff99"),
    againstElectronLooseMVA62015 = tauIDMVAinputs("patTauDiscriminationByElectronRejectionMVA62015", "_WPEff96"),
    againstElectronMediumMVA62015 = tauIDMVAinputs("patTauDiscriminationByElectronRejectionMVA62015", "_WPEff91"),
    againstElectronTightMVA62015 = tauIDMVAinputs("patTauDiscriminationByElectronRejectionMVA62015", "_WPEff85"),
    againstElectronVTightMVA62015 = tauIDMVAinputs("patTauDiscriminationByElectronRejectionMVA62015", "_WPEff79")
)
_tauIDSourcesWithAntiE2015 = cms.PSet(
    slimmedTausUpdated.tauIDSources.clone(),
    _antiETauIDSources2015
)
slimmedTausUpdated.tauIDSources=_tauIDSourcesWithAntiE2015
(~run2_miniAOD_80XLegacy).toModify(slimmedTausUpdated,
                 tauIDSources = _tauIDSourcesWithAntiE2018
    )


patTauMVAIDsSeq += slimmedTausUpdated

