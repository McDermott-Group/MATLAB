base_path = 'Z:\mcdermott-group\data\fluxNoise\DR1 - 2019-12-17\CorrFar\';
files = { ...
    'Q3Q4Corr\General\Parameter\csn0100hzy_correlation.hdf5', ...
    'Q3Q4Corr\General\Parameter\csn1803vvg_correlation.hdf5', ...
    'Q3Q4Corr\General\Parameter\cso0030jjg_correlation.hdf5', ...
    'Q3Q4Corr\General\Parameter\csq0128zge_correlation.hdf5', ...
    'Q3Q4Corr\General\Parameter\csy2025oeg_correlation.hdf5', ...
%     'Q3Q4Corr\General\Parameter\csz0145znf_correlation.hdf5', ...
    }
qA = 'Q3'; qB = 'Q4'; fignum = 1111; 

% base_path = 'Z:\mcdermott-group\data\fluxNoise\DR1 - 2019-12-17\CorrFar\';
% files = { ...
%     'Q1Q2Corr\General\Parameter\csu0052mrt_correlation.hdf5', ...
%     'Q1Q2Corr\General\Parameter\csv0034shs_correlation.hdf5', ...
%     'Q1Q2Corr\General\Parameter\csv0824hxv_correlation.hdf5', ...
%     }
% qA = 'Q1'; qB = 'Q2'; fignum = 1115; 

% %Combining data from last cooldown with current cooldown -Ameya
% files = { ...
%         'Z:\mcdermott-group\data\fluxNoise\DR1 - 2019-12-17\CorrFar\Q1Q3Corr\General\Parameter\csw0353opr_correlation.hdf5', ...
%         'Z:\mcdermott-group\data\fluxNoise\DR1 - 2019-12-17\CorrFar\Q1Q3Corr\General\Parameter\csx0545cpf_correlation.hdf5', ...
%         'Z:\mcdermott-group\data\fluxNoise\DR1 - 2019-12-17\CorrFar\Q1Q3Corr\General\Parameter\csx1710hcz_correlation.hdf5', ...
%         'Z:\mcdermott-group\data\fluxNoise\DR1 - 2019-12-17\CorrFar\Q1Q3Corr\General\Parameter\csy0726yvn_correlation.hdf5', ...
%         'Z:\mcdermott-group\data\fluxNoise\DR1 - 2019-11-12\CorrFar\Q4\General\Parameter\crc2345hmc_parameters.hdf5', ...
%         }
% qA = 'Q1'; qB = 'Q3'; fignum = 1115; 
        
%%%% Actually Qubits 1,3
% base_path = 'Z:\mcdermott-group\data\fluxNoise\DR1 - 2019-11-12\CorrFar\';
% files = { ...
%     'Q4\General\Parameter\csw0353opr_correlation.hdf5', ...
%     'Q4\General\Parameter\crc2345hmc_parameters.hdf5', ...
%     }
% qA = 'Q3'; qB = 'Q4'; fignum = 1113; 

% All 4
% cvc0232imo - only good for 3 of them


N_all = [];
nA_all = [];
nB_all = [];
nCorrAB_all = [];
nCorrBA_all = [];
nCorrExpected_all = [];
k=0;
for f = files
%     if k==4
%         qA = 'Q3'; qB = 'Q4'; 
%     end
%     f{1}
    [N, nA, nB, nCorrAB, nCorrBA, nCorrExpected] = AnalyzeChargeJumpCorrelations([base_path f{1}], qA, qB, fignum);
%     [N, nA, nB, nCorrAB, nCorrBA, nCorrExpected] = AnalyzeChargeJumpCorrelations([f{1}], qA, qB, fignum);
    N_all = [N_all N];
    nA_all = [nA_all nA];
    nB_all = [nB_all nB];
    nCorrAB_all = [nCorrAB_all nCorrAB];
    nCorrBA_all = [nCorrBA_all nCorrBA];
    nCorrExpected_all = [nCorrExpected_all nCorrExpected];
    k=k+1
end
N_tot = sum(N_all)
nA_tot = sum(nA_all)
nB_tot = sum(nB_all)
nCorrAB_tot = sum(nCorrAB_all)
nCorrBA_tot = sum(nCorrBA_all)
nCorrExpected_tot = sum(nCorrExpected_all)