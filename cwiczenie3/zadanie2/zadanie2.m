
clear all
close all
clc
load('Data01.mat')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

n = length(y);
m = n - 1;
tau = 2;
D = spdiags([ones(n-1,1) -ones(n-1,1)], [0 1], n-1, n);
q = 2;

A = [
        [eye(n), -eye(n), zeros(n, m)],
        [-eye(n),-eye(n), zeros(n, m)],
        [zeros(1, n), zeros(1, n), transpose(ones(m,1))],
        [-D, zeros(m, n), -eye(m)],
        [D, zeros(m, n), -eye(m)]
    ];

b = [
    y;
    -y;
    q;
    zeros(m, 1);
    zeros(m, 1);
];

v = optimvar('v', n, 1);
E = optimvar('E', n, 1);
Q = optimvar('Q', m, 1);

c = [zeros(1,n), ones(1, n), zeros(1, m)];

x = linprog(c,A,b); 

v = optimvar('v', n, 1);
E = optimvar('E', n, 1);
Q = optimvar('Q', m, 1);

p = optimproblem('ObjectiveSense', 'min');
p.Objective = ones(1, n) * E;
p.Constraints.c1 = v - E <= y;
p.Constraints.c2 = -v - E <= -y;
p.Constraints.c3 = ones(1, m) * Q <= q;
p.Constraints.c4 = -D * v -Q <= 0;
p.Constraints.c5 = D * v - Q <= 0;
options = optimoptions('linprog', 'Algorithm', 'dual-simplex', 'OptimalityTolerance', 1e-10);
sol = solve(p, 'Options', options);
x2 = sol.v;

plot(t, y, '.g')
hold on;
plot(t, x(1:n), 'r')
hold on;
plot(t, x2(1:n), 'b')
legend('Pomiar sygnału', 'solver', "linprog");
