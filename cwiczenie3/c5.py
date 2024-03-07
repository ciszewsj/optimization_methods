import numpy as np
import cvxopt

def least_squares_fit(X, y):
    """
    Perform least squares fitting using cvxopt.

    Parameters:
    X: numpy array of shape (n_samples, n_features), features
    y: numpy array of shape (n_samples,), target values

    Returns:
    numpy array of shape (n_features,), coefficients of the linear model
    """

    # Formulate the problem: minimize ||Ax - b||^2
    A = cvxopt.matrix(X)
    b = cvxopt.matrix(y)

    # Solve the QP problem
    solution = cvxopt.solvers.qp(A.T * A, -A.T * b)

    # Extract coefficients
    coefficients = np.array(solution['x'])

    return coefficients

# Example usage:
# Generate some sample data
np.random.seed(0)
X = np.random.rand(100, 2)  # 100 samples, 2 features
true_coeffs = np.array([2, -3])  # True coefficients
y = X.dot(true_coeffs) + np.random.normal(scale=0.1, size=100)  # Adding noise

# Perform least squares fitting
coefficients = least_squares_fit(X, y)
print("Coefficients:", coefficients)
