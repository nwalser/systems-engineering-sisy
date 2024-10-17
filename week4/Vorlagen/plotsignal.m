%% Signale plotten
clear;          % removes all variables from the workspace
close all;      % schliesst alle Figuren
clc;            % setzt "prompt" ganz nach oben im Fenster

% Parameter
f0 = 1e3;         % Frequenz f0 = 1000 Hz
N = 10;           % Anzahl Samples

% Signale generieren
t = [0:N-1];          % Zeit-Zeilenvektor (bitte ergaenzen)
x = zeros(1,N);       % Signal x(t)
y = 0.75*ones(1,N);   % Signal y(t)
z = [0:N-1]/N;        % Signal z(t)

%% Signal plotten 

%subplot(2,1,1);     % Figur nur in oberer Hälfte des Bilds
plot(t,x,'-b',t,y,'--r',t,z,':k','LineWidth',2.0); grid;
xlabel('Zeit'); ylabel('Amplitude'); title('Signale');
legend('x','y','z'); % erstellt eine Legende (oben rechts)
%axis([0 N-1 0 1.2]); % wählt Achsenausschnitt
%print -dpng Abb1    % erstellt ein png-Bild im Arbeitsverz.
                     % z.B. zwecks Import in Word 