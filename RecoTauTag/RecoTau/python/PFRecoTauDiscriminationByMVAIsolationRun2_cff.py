import FWCore.ParameterSet.Config as cms

from RecoTauTag.RecoTau.RecoTauDiscriminantCutMultiplexer_cfi import *
from RecoTauTag.Configuration.HPSPFTaus_cff import *

discriminationByIsolationMVArun2v1raw = cms.EDProducer("PFRecoTauDiscriminationByMVAIsolationRun2",

    # tau collection to discriminate
    PFTauProducer = cms.InputTag('pfTauProducer'),

    # Require leading pion ensures that:
    #  1) these is at least one track above threshold (0.5 GeV) in the signal cone
    #  2) a track OR a pi-zero in the signal cone has pT > 5 GeV
    Prediscriminants = requireLeadTrack,
    loadMVAfromDB = cms.bool(True),
    inputFileName = cms.FileInPath("RecoTauTag/RecoTau/data/emptyMVAinputFile"), # the filename for MVA if it is not loaded from DB
    mvaName = cms.string("tauIdMVAnewDMwLT"),
    mvaOpt = cms.string("newDMwLT"),

    # NOTE: tau lifetime reconstruction sequence needs to be run before
    srcTauTransverseImpactParameters = cms.InputTag(''),
    
    srcBasicTauDiscriminators = cms.InputTag('hpsPFTauBasicDiscriminators'),

    verbosity = cms.int32(0)
)

discriminationByIsolationMVArun2v1 = recoTauDiscriminantCutMultiplexer.clone(
    PFTauProducer = cms.InputTag('pfTauProducer'),    
    Prediscriminants = requireLeadTrack,
    toMultiplex = cms.InputTag('discriminationByIsolationMVArun2v1raw'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0),
            cut = cms.string("newDMwLT"),
            variable = cms.string("pt"),
        )
    ),
    workingPoints = cms.vstring(
        "Eff80",
        "Eff70",
        "Eff60",
        "Eff50",
        "Eff40"
    )
)

mvaIsolation2TaskRun2 = cms.Task(
    hpsPFTauBasicDiscriminators
   , discriminationByIsolationMVArun2v1raw
   , discriminationByIsolationMVArun2v1
)
mvaIsolation2SeqRun2 = cms.Sequence(mvaIsolation2TaskRun2)
