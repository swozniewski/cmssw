import FWCore.ParameterSet.Config as cms

import RecoTauTag.Configuration.HPSPFTaus_cff as RecoModules #Working point indices are extracted from here

def tauIDMVAinputs(module, wp):
    return cms.PSet(inputTag = cms.InputTag(module), workingPointIndex = cms.int32(-1 if wp=="raw" else -2 if wp=="category" else getattr(RecoModules, module).workingPoints.index(wp)))
def tauIDbasicinputs(module, wp):
    index = RecoModules.getBasicTauDiscriminatorRawIndex(getattr(RecoModules, module), wp, True)
    if index==None:
        index = RecoModules.getBasicTauDiscriminatorWPIndex(getattr(RecoModules, module), wp, True)
    else:
        index = -index - 1 #use negative indices for raw values
    if index!=None:
        return cms.PSet(inputTag = cms.InputTag(module), workingPointIndex = cms.int32(index))
    print "Basic Tau Discriminator <{}> <{}> for PAT configuration not found!".format(module, wp)
    raise Exception

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
        decayModeFinding = cms.PSet( inputTag = cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding"), workingPointIndex=cms.int32(-99)),
        decayModeFindingNewDMs = cms.PSet( inputTag = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"), workingPointIndex=cms.int32(-99)),
        chargedIsoPtSum = tauIDbasicinputs("hpsPFTauBasicDiscriminators", "ChargedIsoPtSum"),
        neutralIsoPtSum = tauIDbasicinputs("hpsPFTauBasicDiscriminators", "NeutralIsoPtSum"),
        puCorrPtSum = tauIDbasicinputs("hpsPFTauBasicDiscriminators", "PUcorrPtSum"),
        neutralIsoPtSumWeight = tauIDbasicinputs("hpsPFTauBasicDiscriminators", "NeutralIsoPtSumWeight"),                  
        footprintCorrection = tauIDbasicinputs("hpsPFTauBasicDiscriminators", "TauFootprintCorrection"),
        photonPtSumOutsideSignalCone = tauIDbasicinputs("hpsPFTauBasicDiscriminators", "PhotonPtSumOutsideSignalCone"),
        againstMuonLoose3 = tauIDbasicinputs("hpsPFTauDiscriminationByMuonRejection3", "ByLooseMuonRejection3"),
        againstMuonTight3 = tauIDbasicinputs("hpsPFTauDiscriminationByMuonRejection3", "ByTightMuonRejection3"),
        byLooseCombinedIsolationDeltaBetaCorr3Hits = tauIDbasicinputs("hpsPFTauBasicDiscriminators", "ByLooseCombinedIsolationDBSumPtCorr3Hits"),
        byMediumCombinedIsolationDeltaBetaCorr3Hits = tauIDbasicinputs("hpsPFTauBasicDiscriminators", "ByMediumCombinedIsolationDBSumPtCorr3Hits"),
        byTightCombinedIsolationDeltaBetaCorr3Hits = tauIDbasicinputs("hpsPFTauBasicDiscriminators", "ByTightCombinedIsolationDBSumPtCorr3Hits"),
        byCombinedIsolationDeltaBetaCorrRaw3Hits = tauIDbasicinputs("hpsPFTauBasicDiscriminators", "ByRawCombinedIsolationDBSumPtCorr3Hits"),
        byPhotonPtSumOutsideSignalCone = tauIDbasicinputs("hpsPFTauBasicDiscriminators", "ByPhotonPtSumOutsideSignalCone"),
        byIsolationMVArun2v1DBoldDMwLTraw = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "raw"),
        byVVLooseIsolationMVArun2v1DBoldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_WPEff95"),
        byVLooseIsolationMVArun2v1DBoldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_WPEff90"),
        byLooseIsolationMVArun2v1DBoldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_WPEff80"),
        byMediumIsolationMVArun2v1DBoldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_WPEff70"),
        byTightIsolationMVArun2v1DBoldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_WPEff60"),
        byVTightIsolationMVArun2v1DBoldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_WPEff50"),
        byVVTightIsolationMVArun2v1DBoldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT", "_WPEff40"),
        byIsolationMVArun2v1DBnewDMwLTraw = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "raw"),
        byVVLooseIsolationMVArun2v1DBnewDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_WPEff95"),
        byVLooseIsolationMVArun2v1DBnewDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_WPEff90"),
        byLooseIsolationMVArun2v1DBnewDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_WPEff80"),
        byMediumIsolationMVArun2v1DBnewDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_WPEff70"),
        byTightIsolationMVArun2v1DBnewDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_WPEff60"),
        byVTightIsolationMVArun2v1DBnewDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_WPEff50"),
        byVVTightIsolationMVArun2v1DBnewDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT", "_WPEff40"),
        byIsolationMVArun2v1PWoldDMwLTraw = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLT", "raw"),
        byVLooseIsolationMVArun2v1PWoldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLT", "_WPEff90"),
        byLooseIsolationMVArun2v1PWoldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLT", "_WPEff80"),
        byMediumIsolationMVArun2v1PWoldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLT", "_WPEff70"),
        byTightIsolationMVArun2v1PWoldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLT", "_WPEff60"),
        byVTightIsolationMVArun2v1PWoldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLT", "_WPEff50"),
        byVVTightIsolationMVArun2v1PWoldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLT", "_WPEff40"),
        byIsolationMVArun2v1PWnewDMwLTraw = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLT", "raw"),
        byVLooseIsolationMVArun2v1PWnewDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLT", "_WPEff90"),
        byLooseIsolationMVArun2v1PWnewDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLT", "_WPEff80"),
        byMediumIsolationMVArun2v1PWnewDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLT", "_WPEff70"),
        byTightIsolationMVArun2v1PWnewDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLT", "_WPEff60"),
        byVTightIsolationMVArun2v1PWnewDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLT", "_WPEff50"),
        byVVTightIsolationMVArun2v1PWnewDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLT", "_WPEff40"),
        chargedIsoPtSumdR03 = tauIDbasicinputs("hpsPFTauBasicDiscriminatorsdR03", "ChargedIsoPtSumdR03"),
        neutralIsoPtSumdR03 = tauIDbasicinputs("hpsPFTauBasicDiscriminatorsdR03", "NeutralIsoPtSumdR03"),
        neutralIsoPtSumWeightdR03 = tauIDbasicinputs("hpsPFTauBasicDiscriminatorsdR03", "NeutralIsoPtSumWeightdR03"),
        footprintCorrectiondR03 = tauIDbasicinputs("hpsPFTauBasicDiscriminatorsdR03", "TauFootprintCorrectiondR03"),
        photonPtSumOutsideSignalConedR03 = tauIDbasicinputs("hpsPFTauBasicDiscriminatorsdR03", "PhotonPtSumOutsideSignalConedR03"),
        byIsolationMVArun2v1DBdR03oldDMwLTraw = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT", "raw"),
        byVVLooseIsolationMVArun2v1DBdR03oldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT", "_WPEff95"),
        byVLooseIsolationMVArun2v1DBdR03oldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT", "_WPEff90"),
        byLooseIsolationMVArun2v1DBdR03oldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT", "_WPEff80"),
        byMediumIsolationMVArun2v1DBdR03oldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT", "_WPEff70"),
        byTightIsolationMVArun2v1DBdR03oldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT", "_WPEff60"),
        byVTightIsolationMVArun2v1DBdR03oldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT", "_WPEff50"),
        byVVTightIsolationMVArun2v1DBdR03oldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT", "_WPEff40"),
        byIsolationMVArun2v1PWdR03oldDMwLTraw = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLT", "raw"),
        byVLooseIsolationMVArun2v1PWdR03oldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLT", "_WPEff90"),
        byLooseIsolationMVArun2v1PWdR03oldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLT", "_WPEff80"),
        byMediumIsolationMVArun2v1PWdR03oldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLT", "_WPEff70"),
        byTightIsolationMVArun2v1PWdR03oldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLT", "_WPEff60"),
        byVTightIsolationMVArun2v1PWdR03oldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLT", "_WPEff50"),
        byVVTightIsolationMVArun2v1PWdR03oldDMwLT = tauIDMVAinputs("hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLT", "_WPEff40"),
        againstElectronMVA6Raw = tauIDMVAinputs("hpsPFTauDiscriminationByMVA6ElectronRejection", "raw"),
        againstElectronMVA6category = tauIDMVAinputs("hpsPFTauDiscriminationByMVA6ElectronRejection", "category"),
        againstElectronVLooseMVA6 = tauIDMVAinputs("hpsPFTauDiscriminationByMVA6ElectronRejection", "_WPeff98"),
        againstElectronLooseMVA6 = tauIDMVAinputs("hpsPFTauDiscriminationByMVA6ElectronRejection", "_WPeff90"),
        againstElectronMediumMVA6 = tauIDMVAinputs("hpsPFTauDiscriminationByMVA6ElectronRejection", "_WPeff80"),
        againstElectronTightMVA6 = tauIDMVAinputs("hpsPFTauDiscriminationByMVA6ElectronRejection", "_WPeff70"),
        againstElectronVTightMVA6 = tauIDMVAinputs("hpsPFTauDiscriminationByMVA6ElectronRejection", "_WPeff60"),
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

