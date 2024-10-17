% ==========================================================
% Gitarrenverzerrer
% ==========================================================
clear all; close all; clc;

% wav-Datei lesen und Parameter bestimmen
% ==========================================================
[x_vect, fs]=audioread('gtr-jazz.wav'); 
% fs ist Abtastfrequenz, 1/fs ist Abtastintervall
x = x_vect(:,1)'; % Zeilenvektor s enthält mit Mono-Signal
x = x/max(abs(x)); % Amplitudenwerte im Bereich [-1,1]

N = length(x); % Anzahl Abtastwerte
t = [0:N-1]*(1/fs); % Zeitvektor

% Verstärker-Kennlinien Gitarrenverzerrer
% ===========================================================
input_level=[-1:0.01:1];

clip_level_hard = 0.1;
for n=1:201,
   output_hard(n) = input_level(n);
   if abs(output_hard(n)) > clip_level_hard,
      output_hard(n) = sign(output_hard(n))*clip_level_hard;
   end;
end 

clip_level_soft = 0.6;
alpha = 10;
output_soft = clip_level_soft*atan(alpha*input_level)/atan(alpha);

figure(1)
plot(input_level,input_level,'-',...
     input_level,output_hard,'--',...
     input_level,output_soft,'-.','LineWidth',2.0); grid;
xlabel('Input'); ylabel('Output'); 
title('Input-Output Gitarrenverzerrer');
legend('unverzerrt','hard-clipping','soft-clipping','location','NorthWest');
axis([-1,1,-1,1])

% hard-clipping
% ==========================================================
y = zeros(1,N);

% BITTE HIER CODE EINFUEGEN !!!

yhard = y;


% soft-clipping
% ==========================================================

% BITTE HIER CODE EINFUEGEN !!!

ysoft = y;


% Plot
% ==========================================================

figure(2);
subplot(3,1,1);
plot(t,x); grid,
xlabel('Zeit t / s'); ylabel('x(t)');
axis([0 10 -1 1]);

subplot(3,1,2);
plot(t,yhard); grid,
xlabel('Zeit t / s'); ylabel('y_h_a_r_d(t)');
axis([0 10 -1 1]);

subplot(3,1,3);
plot(t,ysoft); grid,
xlabel('Zeit t / s'); ylabel('y_s_o_f_t(t)');
axis([0 10 -1 1]);

% Tonausgabe, bitte Lautstärke LEISE stellen
% ==========================================================
sound([x 2*yhard ysoft],fs) % Original und clipping-Signale nacheinander
