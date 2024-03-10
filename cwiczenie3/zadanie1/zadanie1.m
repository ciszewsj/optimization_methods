
clear all
close all
clc
load('Data01.mat')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

n = length(y);
tau = 2;
D = spdiags([ones(n-1,1) -ones(n-1,1)], [0 1], n-1, n);
q = 2;

cvx_begin
    variable v(n);
    minimize(norm(y - v, 2) + tau*norm(D*v, 1))
cvx_end

cvx_begin
    variable v2(n);
    minimize(norm(y - v2, 2))
    subject to
        norm(D*v2, 1) <= q
cvx_end

figure;
plot(1:n, y, 'bo', 1:n, v, 'r',1:n , v2, 'g');
xlabel('Indeks próbki');
ylabel('Wartość sygnału');
legend('Pomiar sygnału', 'Estymacja r', "Estymacja q");
