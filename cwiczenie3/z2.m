clear all
close all
clc
load('Data01.mat')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

n = length(y);
D = diag(ones(n-1,1),1) - diag(ones(n,1));
tau=1;


y = optimvar('y', N+1, 1);
h = a/N;
x = (0:N) * h;

p = optimproblem('Objective',h*sum(y),'ObjectiveSense','max');

p.Constraints.c1 = y(1) == 0;
p.Constraints.c2 = y(N+1) == 0;





options = optimoptions('fmincon','Algorithm','interior-point','MaxFunctionEvaluations',4000);

initial.y = zeros(N+1, 1);
%options = optimoptions('linprog','Algorithm','interior-point','OptimalityTolerance',1e-10);
sol = solve(p,initial,'Options',options);









