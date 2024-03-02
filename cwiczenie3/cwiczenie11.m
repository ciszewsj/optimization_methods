clear all
close all
clc

load('Data01.mat')

q = 1500;

v = optimvar('v', numel(y), 1);

Dv = v(2:end) - v(1:end-1);

p = optimproblem('Objective', norm(y - v, 2));
p.Objective = 0;

normDv = norm(Dv, 1);

p.Constraints.c1 = normDv <= q;

initial.v = rand(numel(y), 1);

sol = solve(p, initial);

newv = sol.v;

Dvn = newv(2:end) - newv(1:end-1);

ls = norm(Dvn,1);

