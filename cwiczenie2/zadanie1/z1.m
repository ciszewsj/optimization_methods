clear all
close all
clc
load('isoPerimData.mat')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

y = optimvar('y', N+1, 1);
h = a/N;
x = (0:N) * h;

p = optimproblem('Objective',h*sum(y),'ObjectiveSense','max');

p.Constraints.c1 = y(1) == 0;
p.Constraints.c2 = y(N+1) == 0;
p.Constraints.c3 = y(F) == y_fixed(F);

for i = 1:N-1
    p.Constraints.(['c4_' num2str(i)]) = (y(i+2) - 2*y(i+1) + y(i))^2 <= (C*(h^2))^2;
end


norm_sum = 0;
for i = 1:N
    norm_sum = norm_sum + norm([h; y(i+1) - y(i)]);
end

p.Constraints.c4 = norm_sum <= L; 




options = optimoptions('fmincon','Algorithm','interior-point','MaxFunctionEvaluations',4000);

initial.y = zeros(N+1, 1);
%options = optimoptions('linprog','Algorithm','interior-point','OptimalityTolerance',1e-10);
sol = solve(p,initial,'Options',options);

A = sum(sol.y)*h

figure;
hold on;
plot(x, sol.y, '-'); % Punkty optymalne y w zależności od x
plot( x(F),y_fixed(F), 'ro'); % Punkty y_fixed(F) dla odpowiadających x(F)
xlabel('y');
ylabel('x');
title('Wykres optymalnej wartości y i punktów y\_fixed(F) dla odpowiadających x');
legend('Optymalna wartość y', 'Punkty y\_fixed(F)', 'Location', 'northwest');
grid on;
hold off;





