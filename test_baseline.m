% test_baseline.m
% Load Qf2.mat, apply baseline, and save the result for comparison with Python

% Load the data
load('Qf2.mat');
Qf2=double(data_variable);
clear data_variable
B=1000;
% Assuming the variable in Qf2.mat is named 'Qf2' - adjust if different
% Apply baseline with default structuring function
baseline_result = baseline(Qf2, B);
% plot([Qf2 baseline_result])

% Save the result for Python comparison
save('baseline_matlab_output.mat', 'baseline_result', 'Qf2');

fprintf('MATLAB baseline computation complete.\n');
fprintf('Results saved to baseline_matlab_output.mat\n');
