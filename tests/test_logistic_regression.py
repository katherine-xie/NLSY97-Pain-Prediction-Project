import numpy as np
import pytest
from sklearn.linear_model import LogisticRegression
from dsm_project.algorithms.student.logistic_regression import BatchLogisticRegression

# Check whether model can learn a simple pattern
def test_model_learning():

    # Create simple dataset with two classes
    X = np.array([[-2], [-1], [1], [2]])
    y = np.array([0, 0, 1, 1])

    model = BatchLogisticRegression(learning_rate=0.1)
    model.fit(X, y)

    # Check that predictions are correct
    np.testing.assert_array_equal(model.predict(X), y)

    # Check that training reduced the loss
    assert model.loss_history_[-1] < model.loss_history_[0]

# Check that the model predicts probabilities correctly for known inputs
def test_known_probabilities():

    # Create a dataset where the model should predict 0.5 for all inputs
    X = np.zeros((4, 2))
    y = np.array([0, 1, 0, 1])

    model = BatchLogisticRegression().fit(X, y)

    np.testing.assert_allclose(
        model.predict_probability(X),
        np.full((4, 2), 0.5)
    )

# Test that the model raises errors for invalid inputs
def test_invalid_inputs():

    # Create model instance
    model = BatchLogisticRegression()

    # Predictions should not work before training
    with pytest.raises(RuntimeError):
        model.predict([[1, 2]])

    # Labels must be 0 or 1
    with pytest.raises(ValueError):
        model.fit([[1], [2]], [0, 3])

# Check whether my predictions are close to sklearn's LogisticRegression on a random dataset
def test_against_sklearn():

    # Generate reproducible sample data
    rng = np.random.default_rng(438)
    X = rng.normal(size=(150, 3))
    probabilities = 1 / (
        1 + np.exp(-(0.3 + X @ [0.7, -1.0, 0.5]))
    )
    y = rng.binomial(1, probabilities)

    # Train both models
    my_model = BatchLogisticRegression(
        learning_rate=0.1
    ).fit(X, y)

    reference_model = LogisticRegression(
        C=1e6,
        max_iter=10000
    ).fit(X, y)

    # Compare results
    np.testing.assert_allclose(
        my_model.predict_probability(X),
        reference_model.predict_proba(X),
        atol=0.02
    )
