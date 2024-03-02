% Wczytaj dane
load('Data01.mat');

% Liczba elementów w sygnale
N = numel(y);

% Parametr q
q = 50;

% Tworzenie zmiennych optymalizacyjnych
v = optimvar('v', N, 1);
Dv = v(2:end) - v(1:end-1);

% Opcje optymalizacyjne
options = optimoptions('fmincon', 'MaxFunctionEvaluations', 6000);

% Tworzenie problemu optymalizacyjnego
p = optimproblem('Objective', norm(y - v, 2), 'ObjectiveSense', 'min');
p.Constraints.c1 = norm(Dv, 1) <= q;

% Początkowe wartości zmiennych
initial.v = zeros(N, 1);

% Rozwiązanie problemu optymalizacyjnego
sol = solve(p, initial, 'Options', options);
k = sol.v;

% Obliczenie nowej różnicy między kolejnymi elementami zmiennej v
newDv = k(2:end) - k(1:end-1);
% Obliczenie normy nowej różnicy
wynik = norm(newDv, 1);
% Obliczenie odległości między y a k (rozwiązanie optymalne)
odleglosc = norm(y - k, 2);

% Narysuj wykres
plot(t, y, 'bo');
hold on;
plot(t, k, 'r-', 'LineWidth', 2);

% Ustawienia wykresu
title('Wykres punktów');
xlabel('Oś X');
ylabel('Oś Y');
grid on;

% Wyświetl legendę
legend('Dane', 'Rozwiązanie optymalne');

% Wyświetl wyniki
fprintf('Norma nowej różnicy: %f\n', wynik);
fprintf('Odległość między y a k: %f\n', odleglosc);
