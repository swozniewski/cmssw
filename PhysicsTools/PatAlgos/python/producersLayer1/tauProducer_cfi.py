import FWCore.ParameterSet.Config as cms

import RecoTauTag.Configuration.HPSPFTaus_cff as RecoModules #Working point indices are extracted from here

def tauIDinputs(module, wp=None):
    if wp:
        return cms.PSet( inputTag = cms.InputTag(module), workingPointIndex = cms.int32(-1 if wp=="raw" else getattr(RecoModules, module).workingPoints.index(wp)))
    else:
        return cms.PSet( inputTag = cms.InputTag(module), workingPointIndex = cms.int32(-2))

patTaus = cms.EDProducer("PATTauProducer",
    # input
    tauSource = cms.InputTag("hpsPFTauProducer"),
    tauTransverseImpactParameterSource = cms.InputTag("hpsPFTauTransverseImpactParameters"),

    # add user data
    userData = cms.PSet(
      # add custom classes here
      userClasses = cms.PSet(
        src = cms.VInputTag('')
      ),
      # add doubles here
      userFloats = cms.PSet(
        src = cms.VInputTag('')
      ),
      # add ints here
      userInts = cms.PSet(
        src = cms.VInputTag('')
      ),
      # add candidate ptrs here
      userCands = cms.PSet(
        src = cms.VInputTag('')
      ),
      # add "inline" functions here
      userFunctions = cms.vstring(),
      userFunctionLabels = cms.vstring()
    ),

    # jet energy corrections
    addTauJetCorrFactors = cms.bool(False),
    tauJetCorrFactorsSource = cms.VInputTag(cms.InputTag("patTauJetCorrFactors")),

    # embedding objects (for Calo- and PFTaus)
    embedLeadTrack = cms.bool(False), ## embed in AOD externally stored leading track
    embedSignalTracks = cms.bool(False), ## embed in AOD externally stored signal tracks
    embedIsolationTracks = cms.bool(False), ## embed in AOD externally stored isolation tracks
    # embedding objects (for PFTaus only)
    embedLeadPFCand = cms.bool(False), ## embed in AOD externally stored leading PFCandidate
    embedLeadPFChargedHadrCand = cms.bool(False), ## embed in AOD externally stored leading PFChargedHadron candidate
    embedLeadPFNeutralCand = cms.bool(False), ## embed in AOD externally stored leading PFNeutral Candidate
    embedSignalPFCands = cms.bool(False), ## embed in AOD externally stored signal PFCandidates
    embedSignalPFChargedHadrCands = cms.bool(False), ## embed in AOD externally stored signal PFChargedHadronCandidates
    embedSignalPFNeutralHadrCands = cms.bool(False), ## embed in AOD externally stored signal PFNeutralHadronCandidates
    embedSignalPFGammaCands = cms.bool(False), ## embed in AOD externally stored signal PFGammaCandidates
    embedIsolationPFCands = cms.bool(False), ## embed in AOD externally stored isolation PFCandidates
    embedIsolationPFChargedHadrCands = cms.bool(False), ## embed in AOD externally stored isolation PFChargedHadronCandidates
    embedIsolationPFNeutralHadrCands = cms.bool(False), ## embed in AOD externally stored isolation PFNeutralHadronCandidates
    embedIsolationPFGammaCands = cms.bool(False), ## embed in AOD externally stored isolation PFGammaCandidates

    # embed IsoDeposits
    isoDeposits = cms.PSet(),

    # user defined isolation variables the variables defined here will be accessible
    # via pat::Tau::userIsolation(IsolationKeys key) with the key as defined in
    # DataFormats/PatCandidates/interface/Isolation.h
    userIsolation = cms.PSet(),

    # tau ID (for efficiency studies)
    addTauID     = cms.bool(True),
    tauIDSources = cms.PSet(
        # configure many IDs as InputTag <someName> = <someTag>
        # you can comment out those you don't want to save some
        # disk space
        decayModeFinding = tauIDinputs("hpsPFTauDiscriminationByDecayModeFinding"),
        decayModeFindingNewDMs =tauIDinputs("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
        chargedIsoPtSum = tauIDinputs("hpsPFTauChargedIsoPtSum"),
        neutralIsoPtSum = tauIDinputs("hpsPFTauNeutralIsoPtSum"),
        puCorrPtSum = tauIDinputs("hpsPFTauPUcorrPtSum"),
        neutralIsoPtSumWeight = tauIDinputs("hpsPFTauNeutralIsoPtSumWeight"),                  
        footprintCorrection = tauIDinputs("hpsPFTauFootprintCorrection"),
        photonPtSumOutsideSignalCone = tauIDinputs("hpsPFTauPhotonPtSumOutsideSignalCone"),
        againstMuonLoose3 = tauIDinputs("hpsPFTauDiscriminationByLooseMuonRejection3"),
        againstMuonTight3 = tauIDinputs("hpsPFTauDiscriminationByTightMuonRejection3"),
        byLooseCombinedIsolationDeltaBetaCorr3Hits = tauIDinputs("hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits"),
        byMediumCombinedIsolationDeltaBetaCorr3Hits = tauIDinputs("hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits"),
        byTightCombinedIsolationDeltaBetaCorr3Hits = tauIDinputs("hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits"),
        byCombinedIsolationDeltaBetaCorrRaw3Hits = tauIDinputs("hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits"),
        byPhotonPtSumOutsideSignalCone = tauIDinputs("hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone"),
        byIsolationMVArun2v1DBoldDMwLTraw = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "raw"),
        byVVLooseIsolationMVArun2v1DBoldDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_VVLoose"),
        byVLooseIsolationMVArun2v1DBoldDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_VLoose"),
        byLooseIsolationMVArun2v1DBoldDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_Loose"),
        byMediumIsolationMVArun2v1DBoldDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_Medium"),
        byTightIsolationMVArun2v1DBoldDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_Tight"),
        byVTightIsolationMVArun2v1DBoldDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_VTight"),
        byVVTightIsolationMVArun2v1DBoldDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_VVTight"),
        byIsolationMVArun2v1DBnewDMwLTraw = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "raw"),
        byVVLooseIsolationMVArun2v1DBnewDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_VVLoose"),
        byVLooseIsolationMVArun2v1DBnewDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_VLoose"),
        byLooseIsolationMVArun2v1DBnewDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_Loose"),
        byMediumIsolationMVArun2v1DBnewDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_Medium"),
        byTightIsolationMVArun2v1DBnewDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_Tight"),
        byVTightIsolationMVArun2v1DBnewDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_VTight"),
        byVVTightIsolationMVArun2v1DBnewDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_VVTight"),
        chargedIsoPtSumdR03 = tauIDinputs("hpsPFTauChargedIsoPtSumdR03"),
        neutralIsoPtSumdR03 = tauIDinputs("hpsPFTauNeutralIsoPtSumdR03"),
        neutralIsoPtSumWeightdR03 = tauIDinputs("hpsPFTauNeutralIsoPtSumWeightdR03"),
        footprintCorrectiondR03 = tauIDinputs("hpsPFTauFootprintCorrectiondR03"),
        photonPtSumOutsideSignalConedR03 = tauIDinputs("hpsPFTauPhotonPtSumOutsideSignalConedR03"),
        byIsolationMVArun2v1DBdR03oldDMwLTraw = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT", "raw"),
        byVVLooseIsolationMVArun2v1DBdR03oldDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT", "_VVLoose"),
        byVLooseIsolationMVArun2v1DBdR03oldDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT", "_VLoose"),
        byLooseIsolationMVArun2v1DBdR03oldDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT", "_Loose"),
        byMediumIsolationMVArun2v1DBdR03oldDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT", "_Medium"),
        byTightIsolationMVArun2v1DBdR03oldDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT", "_Tight"),
        byVTightIsolationMVArun2v1DBdR03oldDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT", "_VTight"),
        byVVTightIsolationMVArun2v1DBdR03oldDMwLT = tauIDinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT", "_VVTight"),
        againstElectronMVA6Raw = tauIDinputs("hpsPFTauDiscriminationByMVA6rawElectronRejection", "raw"),
        againstElectronMVA6category = tauIDinputs("hpsPFTauDiscriminationByMVA6rawElectronRejection:category"),
        againstElectronVLooseMVA6 = tauIDinputs("hpsPFTauDiscriminationByMVA6ElectronRejection", "_VLoose"),
        againstElectronLooseMVA6 = tauIDinputs("hpsPFTauDiscriminationByMVA6ElectronRejection", "_Loose"),
        againstElectronMediumMVA6 = tauIDinputs("hpsPFTauDiscriminationByMVA6ElectronRejection", "_Medium"),
        againstElectronTightMVA6 = tauIDinputs("hpsPFTauDiscriminationByMVA6ElectronRejection", "_Tight"),
        againstElectronVTightMVA6 = tauIDinputs("hpsPFTauDiscriminationByMVA6ElectronRejection", "_VTight"),
    ),
    skipMissingTauID = cms.bool(False), #Allow to skip a tau ID variable when not present in the event"
    # mc matching configurables
    addGenMatch      = cms.bool(True),
    embedGenMatch    = cms.bool(True),
    genParticleMatch = cms.InputTag("tauMatch"),
    addGenJetMatch   = cms.bool(True),
    embedGenJetMatch = cms.bool(True),
    genJetMatch      = cms.InputTag("tauGenJetMatch"),

    # efficiencies
    addEfficiencies = cms.bool(False),
    efficiencies    = cms.PSet(),

    # resolution
    addResolutions  = cms.bool(False),
    resolutions     = cms.PSet()
)

