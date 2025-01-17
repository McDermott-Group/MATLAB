% Simulate QP Tunneling curves

N = 5*8192; % length of line to calc self cpsd
n = 100; % number of files to average
charge_dispersion = 3e6; %pk-pk Hz
offset = 0e6;
idle_time = 166e-9;
cycle_time = 100e-6;
T_qp = 10e-3; % QP tunneling rate

% general methods:
%   calc rand ng
%   choose odd or even parity
%   calc detuning due to ng
%   calc rotation in stationary frame
%   project

Fs = 1/cycle_time;
ng = 0.5*ones(n,N); % rand(n, N);
dP = rand(n, N) < 1/T_qp*cycle_time;
parity = 2*mod(cumsum(dP,2),2)-1;
detuning = offset + charge_dispersion/2*parity.*abs(sin(pi*ng)); % this is just using a sin instead of the actual fn for parity bands
rotation = 2*pi*detuning*idle_time;
M = rand(n, N) < (0.3 + 0.3*sin(rotation));

[avg_cpsd, psd_freq] = noiselib.partition_and_avg_psd(M, Fs);
window_avg_psd = noiselib.window_averaging(avg_cpsd');

%Plot
figure(112);hold on
title('1/f Averaged PSD')
plot(psd_freq,abs(window_avg_psd));%, 'DisplayName', [samples(1:end-1),qubit(1:end-1)])
set(gca,'xscale','log')
set(gca,'yscale','log')
xlabel('Frequency (Hz)')
ylabel('S_\eta (\eta^2/Hz)')
grid on