""" 
Logistic regression using gradient descent 

"""

import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin

class BatchLogisticRegression(ClassifierMixin, BaseEstimator):
    """
    Binary logistic regression trained using gradient descent
    
    """

    def __init__(self, learning_rate=0.02, max_iterations=5000, tolerance=1e-8):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.tolerance = tolerance

    @staticmethod
    def _sigmoid(z):
        """
        Implement the sigmoid function to convert a number into a probability between 0 and 1
        
        """
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        """
        Train the model to learn weights and bias
        
        """

        # Convert inputs into numpy arrays
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float)

        # Check that the training data is valid
        if X.ndim != 2 or X.shape[0] == 0 or X.shape[1] == 0:
            raise ValueError("X must be a nonempty 2D array")

        if y.shape != (X.shape[0],):
            raise ValueError("X and y must have the same number of rows")

        if not np.isfinite(X).all() or not np.isfinite(y).all():
            raise ValueError("X and y must contain finite numbers")

        if not np.isin(y, [0, 1]).all():
            raise ValueError("y must contain only 0 and 1")

        if len(np.unique(y)) != 2:
            raise ValueError("Training data must contain both classes")

        if self.learning_rate <= 0 or self.max_iterations <= 0:
            raise ValueError("Learning rate and iterations must be positive")

        if self.tolerance < 0:
            raise ValueError("Tolerance can't be negative")

        # Get num. samples and features
        num_samples, num_features = X.shape

        # Initialize weights and bias to zero
        weights = np.zeros(num_features)
        bias = 0.0

        # Store the loss during training
        loss_history = []

        # Repeat gradient descent 
        for iteration in range(self.max_iterations):

            # Calculate predicted probabilities
            z = X @ weights + bias
            predictions = self._sigmoid(z)

            # Calculate binary cross-entropy loss
            loss = np.mean(np.logaddexp(0, z) - y * z)
            loss_history.append(loss)

            # Calculate the gradients
            errors = predictions - y

            weight_gradient = (X.T @ errors) / num_samples
            bias_gradient = np.mean(errors)

            # Stop early if gradients are very small
            gradient_size = np.sqrt(
                np.sum(weight_gradient**2) + bias_gradient**2
            )

            if gradient_size <= self.tolerance:
                break

            # Update weights and bias
            weights -= self.learning_rate * weight_gradient
            bias -= self.learning_rate * bias_gradient

        # Save the learned values
        self.coef_ = weights
        self.intercept_ = bias
        self.classes_ = np.array([0, 1])
        self.n_features_in_ = num_features
        self.n_iter_ = len(loss_history)
        self.loss_history_ = np.array(loss_history)

        return self

    def predict_proba(self, X):
        """
        Predict the probability of each class
        
        """

        if not hasattr(self, "coef_"):
            raise RuntimeError("Train the model first using fit()")

        X = np.asarray(X, dtype=float)

        if X.ndim != 2 or X.shape[1] != self.n_features_in_:
            raise ValueError("X has the wrong number of features")

        if not np.isfinite(X).all():
            raise ValueError("X must contain finite numbers")

        # Calculate probabilities for class 1
        z = X @ self.coef_ + self.intercept_
        probability_1 = self._sigmoid(z)

        # Probability of class 0 is 1 - probability of class 1
        probability_0 = 1 - probability_1

        return np.column_stack((probability_0, probability_1))

    def predict(self, X):
        """
        Predict class 0 or 1 using a threshold of 0.5
        """

        probabilities = self.predict_proba(X)[:, 1]

        return (probabilities >= 0.5).astype(int)
