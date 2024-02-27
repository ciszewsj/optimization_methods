import cvxopt

# Definicja macierzy P, q, G, h, A, b (można je dostosować do konkretnego problemu)
P = cvxopt.matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 0.0]])  # Macierz zawierająca zmienne x, a, b
q = cvxopt.matrix([-2.0, -3.0, 0.0])  # Uwzględnienie zmiennej b w funkcji celu
G = cvxopt.matrix([[1.0, 2.0, 0.0], [3.0, 4.0, 0.0]])  # Macierz ograniczeń uwzględniająca zmienne a i b
h = cvxopt.matrix([1.0, 1.0])
A = cvxopt.matrix([1.0, 1.0, 0.0], (1, 3))  # Macierz uwzględniająca zmienną a w równaniu liniowym
b = cvxopt.matrix(1.0)

# Rozwiązanie problemu optymalizacji
solution = cvxopt.solvers.qp(P, q, G, h, A, b)

# Wyświetlenie wyniku optymalizacji
print(solution['x'])
