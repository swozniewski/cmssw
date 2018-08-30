import FWCore.ParameterSet.Config as cms

#Full Event content
RecoTauTagFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep *_ak4PFJetsRecoTauPiZeros_*_*',
        'keep *_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauDiscrimination*_*_*',
        'keep *_hpsPFTau*PtSum_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*'
    )
)
#RECO content
RecoTauTagRECO = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*',                               ## kept for Configuration/Skimming/python/PDWG_TauSkim_cff.py
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*',                        ## kept for Configuration/Skimming/python/PDWG_TauSkim_cff.py
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*',
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByLooseElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*',
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*',
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*',
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*',
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*',
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*',
        'keep *_hpsPFTauNeutralIsoPtSum_*_*',
        'keep *_hpsPFTauPUcorrPtSum_*_*',
        'keep *_hpsPFTauChargedIsoPtSum_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*',
        'keep *_hpsPFTauFootprintCorrection_*_*',
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*',
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*',
        #'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_category_*',
        'keep *_hpsPFTauDiscriminationByMVA6ElectronRejection_*_*',
        #'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*',
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT_*_*',
        #'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*',
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT_*_*',
        #'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*',
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLT_*_*',
        #'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*',
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLT_*_*',
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*',
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*',
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*',
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*',
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*',
        #'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*',
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT_*_*',
        #'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*',
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLT_*_*',
    )
)
#AOD content
RecoTauTagAOD = cms.PSet(
    outputCommands = cms.untracked.vstring(
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*',
        'keep recoPFTaus_hpsPFTauProducer_*_*',
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*',
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*',
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*',                               ## kept for Configuration/Skimming/python/PDWG_TauSkim_cff.py
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*',                        ## kept for Configuration/Skimming/python/PDWG_TauSkim_cff.py
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*',
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*',
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*',
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*',
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*',
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*',
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*',
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*',
        'keep *_hpsPFTauNeutralIsoPtSum_*_*',
        'keep *_hpsPFTauPUcorrPtSum_*_*',
        'keep *_hpsPFTauChargedIsoPtSum_*_*',
        'keep *_hpsPFTauTransverseImpactParameters_*_*',
        'keep *_hpsPFTauFootprintCorrection_*_*',
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*',
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*',
        #'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*',
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_category_*',
        'keep *_hpsPFTauDiscriminationByMVA6ElectronRejection_*_*',
        #'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*',
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT_*_*',
        #'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*',
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT_*_*',
        #'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*',
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLT_*_*',
        #'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*',
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLT_*_*',
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*',
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*',
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*',
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*',
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*',
        #'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*',
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT_*_*',
        #'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*',
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLT_*_*',
    )
)

