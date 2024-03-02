clear all
close all
clc

load('Data01.mat')

%%%%%%%%%%%%%%%%%%%%%

problem = optimproblem;

v = optimvar('v', size(1001,1));

Dv = v(2:end) - v(1:end-1);

problem.Objective = sum((y - r).^);

problem.Constraints.cons1 = norm(Dv, 1) <= q;

options = optimoptions(@fmincon, 'Algorithm', 'interior-point');

[sol, fval] = solve(problem, 'Options', options);
