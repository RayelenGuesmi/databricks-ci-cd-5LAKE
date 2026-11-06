# Databricks CI/CD for Machine Learning — 5LAKE

**Student:** Rayelen Guesmi  
**Course:** 5LAKE — Data Engineering / MLOps  
**Project:** Implementing CI/CD for Data Science Projects with Databricks

## 1. Project Overview

This project demonstrates the implementation of a Machine Learning workflow using **Databricks, GitHub Actions, MLflow, Scikit-learn, and Pytest**.

The objective is to develop, test, track, version, and execute a machine learning model using modern MLOps practices.

The implementation includes automated Continuous Integration (CI), a Databricks training Job, and model versioning through Unity Catalog.

**Important:** The GitHub Actions CI pipeline is fully operational. The Databricks training Job was also successfully executed. However, automatic triggering of the Databricks Job from GitHub Actions was not completed because the available Databricks Free Edition workspace does not provide the required personal access token permissions, and an alternative OAuth/OIDC configuration could not be established.

## 2. Project Objectives

- Integrate a Databricks Git folder with a GitHub repository.
- Develop a Random Forest classification model.
- Implement unit tests with Pytest.
- Track experiments and metrics using MLflow.
- Register and version the trained model in Unity Catalog.
- Create and execute a Databricks Serverless Job.
- Automate Python testing using GitHub Actions.
- Validate the workflow and document deployment limitations.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.12 | Machine learning development |
| Scikit-learn | Random Forest training and evaluation |
| MLflow | Experiment tracking and model logging |
| Unity Catalog | Registered model management and versioning |
| Databricks Free Edition | Serverless model training and job execution |
| GitHub | Source code version control |
| GitHub Actions | Automated Continuous Integration |
| Pytest | Automated Python testing |
| Git | Code synchronization |

## 4. Architecture

The implemented workflow consists of two validated execution paths.

### Continuous Integration

```text
Developer
    |
    v
GitHub Repository (main)
    |
    v
GitHub Actions
    |
    +-- Checkout repository
    |
    +-- Set up Python 3.12
    |
    +-- Install dependencies
    |
    +-- Execute Pytest
    |
    v
CI Validation: SUCCESS
```

### Databricks Training and Model Versioning

```text
GitHub Repository (main)
    |
    v
Databricks Job
    |
    v
Serverless Python Execution
    |
    v
Random Forest Training
    |
    v
MLflow Experiment Tracking
    |
    v
Unity Catalog Model Registry
    |
    v
Registered Model Versions
```

The two paths have been validated independently. Automatic GitHub Actions-to-Databricks job triggering remains a deployment limitation.

## 5. Project Structure

```text
databricks-ci-cd-5LAKE/
|
|-- .github/
|   |-- workflows/
|       |-- ci_cd_pipeline.yml
|
|-- notebooks/
|   |-- train_model.py
|
|-- tests/
|   |-- test_train_model.py
|
|-- screenshots/
|
|-- .gitignore
|-- README.md
|-- requirements.txt
```

### Main Files

**notebooks/train_model.py**

Contains the Random Forest training workflow, evaluation, MLflow tracking, model signature generation, and Unity Catalog registration.

**tests/test_train_model.py**

Contains the Pytest test validating successful training and the model's accuracy threshold.

**.github/workflows/ci_cd_pipeline.yml**

Defines the GitHub Actions workflow that automatically installs dependencies and runs tests after pushes to the main branch. It also supports manual workflow execution.

**requirements.txt**

Contains the Python dependencies required for training and testing.

**screenshots/**

Contains evidence of the implementation and successful executions, added for the final submission.

## 6. Machine Learning Model

### Dataset

The project uses the Iris dataset provided by Scikit-learn.

The dataset contains:

- 150 samples
- 4 numerical input features
- 3 Iris flower classes

### Algorithm

A Random Forest Classifier is used to classify Iris flower species.

The main training configuration is:

| Parameter | Value |
|---|---|
| Algorithm | RandomForestClassifier |
| Number of estimators | 100 |
| Random state | 42 |
| Training split | 80% |
| Testing split | 20% |
| Evaluation metric | Accuracy |

### Results

The validated executions achieved:

**Accuracy: 1.0000 (100%)**

This result was obtained on the dataset's test split. It should not be interpreted as a guarantee of perfect generalization to unseen real-world data.

## 7. Local Installation

### Clone the repository

```bash
git clone https://github.com/RayelenGuesmi/databricks-ci-cd-5LAKE.git
cd databricks-ci-cd-5LAKE
```

### Create a virtual environment

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Run model training

```bash
python notebooks/train_model.py
```

The validated local execution produced:

```text
Model accuracy: 1.0000
```

The training script uses a configured MLflow experiment path. Local executions may require adapting the experiment configuration to the local tracking backend.

## 8. Unit Testing with Pytest

Pytest is used to validate the training function.

The test checks that:

- The training function executes successfully.
- The returned accuracy is between 0 and 1.
- The model achieves at least 80% accuracy.

Execute:

```bash
python -m pytest tests/ -v
```

### Validated Result

```text
tests/test_train_model.py::test_model_training PASSED

1 passed
```

A non-blocking SQLAlchemy deprecation warning was observed during local testing.

## 9. MLflow Experiment Tracking

MLflow is used to record model training information.

The implementation logs:

- The number of estimators
- The random state
- Model accuracy
- The trained Scikit-learn model
- The model input/output signature
- An example of model input data

### MLflow Experiment

```text
/Users/rayelen.guesmi@supinfo.com/Iris-RandomForest
```

### Model Serialization

The implementation uses the `cloudpickle` serialization format for compatibility with the Databricks Serverless runtime used during the exercise.

Serialized models should only be loaded from trusted sources because pickle-based deserialization can execute arbitrary Python code.

## 10. Unity Catalog Model Registry

The trained model is registered in Databricks Unity Catalog.

**Registered model:**

```text
workspace.default.irisrfmodel_rayelen_5lake
```

### Validated Versions

| Model Version | Result |
|---|---|
| Version 1 | Registered after interactive Databricks execution |
| Version 2 | Registered after successful Databricks Job execution |
| Version 3 | Registered after an additional successful Job execution |
| Version 4 | Registered after an additional successful Job execution |

All four model versions were successfully registered and are visible in Unity Catalog.

## 11. Databricks Git Integration

The GitHub repository was connected to the Databricks workspace using a Databricks Git folder.

Repository:

https://github.com/RayelenGuesmi/databricks-ci-cd-5LAKE

Branch:

```text
main
```

Changes made in Databricks can be committed and pushed to GitHub using the Git integration.

The Databricks Job is configured to use Git as its source.

## 12. Databricks Job

A Databricks Job was created to execute the training script.

### Job Configuration

| Configuration | Value |
|---|---|
| Job name | 5LAKE-Iris-Training |
| Job ID | 520730348936614 |
| Task name | train_random_forest |
| Task type | Python script |
| Source | Git provider |
| Branch | main |
| Python file | notebooks/train_model.py |
| Compute | Serverless |

### Execution Validation

The first attempt failed because the Python file path was incorrectly configured as an absolute workspace path.

The task was corrected to use the repository-relative path:

```text
notebooks/train_model.py
```

The repaired execution completed successfully.

**Validated result:**

```text
Task: train_random_forest
Status: SUCCESS
Accuracy: 1.0000
Registered model version: 2
```

This confirms that the Databricks Job can retrieve the source code, train the model, and register a new model version.

## 13. GitHub Actions — Continuous Integration

GitHub Actions is configured in:

```text
.github/workflows/ci_cd_pipeline.yml
```

The workflow is triggered by:

- Push events on the `main` branch
- Manual execution using `workflow_dispatch`

### Automated Steps

1. Checkout the GitHub repository.
2. Configure Python 3.12.
3. Install project dependencies.
4. Execute Pytest.
5. Report the CI result.

### Validated GitHub Actions Execution

| Field | Result |
|---|---|
| Workflow | 5LAKE - CI Pipeline |
| Commit | 1a13d43 |
| Trigger | Push to main |
| Status | SUCCESS |
| Jobs passed | 1/1 |
| Duration | 52 seconds |

This confirms that automated Continuous Integration is operational.

## 14. Continuous Deployment Limitation

The exercise also aimed to trigger Databricks Jobs automatically from GitHub Actions after successful tests.

This final integration was not completed in the available Databricks Free Edition environment.

### Encountered Restriction

The workspace did not permit generation of personal access tokens.

The settings interface displayed:

```text
Tokens are disabled for your organization
or you do not have permissions to use them.
```

OAuth/OIDC authentication was considered as an alternative, but the required administrative capabilities were not confirmed as available in the workspace.

### Implemented Alternative

The following components were successfully validated:

- Automatic testing with GitHub Actions
- Git-based source retrieval by Databricks
- Serverless training through Databricks Jobs
- MLflow experiment logging
- Model registration and versioning

The Databricks Job can be executed separately through the Databricks interface.

### Future Improvement

In an appropriately configured Databricks workspace, GitHub Actions could authenticate through workload identity federation (OIDC) and automatically trigger the Databricks Job following successful tests.

This would complete the automated CI/CD workflow without storing a long-lived personal access token.

## 15. Validation Summary

| Requirement | Result |
|---|---|
| GitHub repository creation | Completed |
| Databricks Git folder integration | Completed |
| Random Forest training | Completed |
| Unit testing with Pytest | Completed |
| MLflow experiment tracking | Completed |
| Model signature logging | Completed |
| Unity Catalog registration | Completed |
| Model versioning | Completed |
| Databricks Serverless Job | Completed |
| GitHub Actions CI pipeline | Completed |
| Automated GitHub-to-Databricks deployment | Not completed — authentication restriction |
| Final deployment validation | Databricks Job validated separately |

## 16. Screenshots and Evidence

The final submission includes screenshots showing:

1. GitHub repository structure
2. Databricks Git folder integration
3. MLflow experiment execution
4. Unity Catalog registered model versions
5. Successful Databricks Job execution
6. Successful GitHub Actions workflow

These screenshots are stored in the `screenshots/` directory.

## 17. Conclusion

This hands-on project demonstrates the main components of an MLOps workflow using Databricks, GitHub, Scikit-learn, Pytest, and MLflow.

The implementation successfully validates automated Python testing, Git-based code integration, Serverless training, experiment tracking, and centralized model versioning.

Although the final GitHub Actions-to-Databricks deployment trigger could not be enabled due to authentication restrictions in the available environment, the individual CI and Databricks execution workflows were tested successfully.

The project provides a foundation for implementing a fully automated CI/CD pipeline in a Databricks workspace with the required authentication and administrative capabilities.

---

**Author:** Rayelen Guesmi
**Repository:** https://github.com/RayelenGuesmi/databricks-ci-cd-5LAKE