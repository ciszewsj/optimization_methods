clear all
close all
clc
load('Data01.mat')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

n = length(y);
D = diag(ones(n-1,1),1) - diag(ones(n,1));
tau=1;

cvx_begin
    variable v(n);
    minimize(norm(y - v, 2) + tau*norm( v(2:end)-v(1:end-1), 1))
cvx_end


figure;
h = plot(1:n, y, 'bo', 1:n, v, 'r');
set(h,'markersize',1)
xlabel('t');
ylabel('y');





