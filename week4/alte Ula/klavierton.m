% =====================================================
% Grund- und Oberschwingungen eines Klaviertons
% =====================================================
clear; close all; clc;

% Parameter
% =====================================================
fs = 44100; % Abtastfrequenz
Ts = 1/fs;
f0 = 441;   % Grundschwingung
T0 = 1/f0;  
N = round(T0/Ts);

% read wav-data and plot piano signal 
% =====================================================
x = audioread('klavierton_a_441.wav'); x=x';
sound(x,fs);

figure(1)
subplot(2,1,1)
plot(x); grid;
xlabel('samples'); ylabel('Amplitude');
xp = zeros(1,N); % BITTE ÜBERSCHREIBEN !!!  
subplot(2,1,2)
plot(xp); grid;
xlabel('Samples'); ylabel('Amplitude');


% Amplituden von Grund- und Oberschwingungen
% ======================================================
M = ones(1,23);  % BITTE ÜBERSCHREIBEN !!!
M = M/max(abs(M));

figure(2)
plot([0:22]*f0,20*log10(abs(M)),'x','LineWidth',2.0); grid;
xlabel('Frequenz f / Hz'); ylabel('abs(M_k) / dB');