# test_app.py
import pytest
from app import train_model


def test_train_model():
    # Test if the model trains successfully and returns expected outputs
    model, accuracy = train_model()

    # Check if model is trained
    assert model is not None, "Model should not be None"

    # Check if accuracy is within expected range
    assert 0.0 <= accuracy <= 1.0, "Accuracy should be between 0 and 1"


if __name__ == "__main__":
    pytest.main()
