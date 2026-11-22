# Tests for the loading NLSY97 data (using synthetic fixture data)

from pathlib import Path

import pandas as pd

from dsm_project.config import ProjectConfig
from dsm_project.data import load_project_dataset

# Define path to fixture data
FIXTURE_PATH = "data/fixtures/nlsy97_synthetic_fixture.csv"


# Test structure of the synthetic dataset
def test_fixture_structure():

    # Load the synthetic dataset
    df = pd.read_csv(FIXTURE_PATH)

    # Check that it has 10 rows and 23 columns
    assert df.shape == (10, 23)

    # Check that every respondent has a unique ID
    assert df["respondent_id"].is_unique

    # Check that target exists
    assert "chronic_pain_30d_2019" in df.columns


# Test that CSV adapter works
def test_nlsy97_adapter():

    # Create simple config for testing purposes
    config = ProjectConfig(
        path=Path("configs/student.toml"),
        project={},
        dataset={
            "adapter": "csv",
            "name": "Synthetic NLSY97",
            "path": FIXTURE_PATH,
            "identifier": "respondent_id",
            "observation_unit": "one synthetic respondent",
            "feature_columns": ["age_at_interview_2015"],
        },
        tasks={
            "classification": {
                "name": "Chronic pain",
                "target": "chronic_pain_30d_2019",
                "metric": "balanced_accuracy",
            }
        },
        split={
            "random_state": 438,
            "test_fraction": 0.25,
        },
    )

    # Load the fixture through the adapter
    dataset = load_project_dataset(config)

    # Check that the data loaded correctly
    assert dataset.observations.shape == (10, 23)


# Test duplicate respondants
def test_duplicate_respondent_ids():

    # Load data
    df = pd.read_csv(FIXTURE_PATH)

    # Create a duplicate respondent ID
    df.loc[1, "respondent_id"] = df.loc[0, "respondent_id"]

    # Verify that the duplicate is detected
    assert not df["respondent_id"].is_unique
