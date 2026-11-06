
import mlflow
import mlflow.sklearn

from mlflow.models import infer_signature
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def main():
    # 1. Load Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # 2. Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3. Train Random Forest
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
    model.fit(X_train, y_train)

    # 4. Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # 5. Define MLflow model signature
    signature = infer_signature(X_test, y_pred)

    # 6. Configure MLflow experiment
    mlflow.set_experiment(
        "/Users/rayelen.guesmi@supinfo.com/Iris-RandomForest"
    )

# Use Unity Catalog Model Registry in Databricks
    if mlflow.get_tracking_uri().startswith("databricks"):
        mlflow.set_registry_uri("databricks-uc")

    # 7. Log experiment and model
    with mlflow.start_run():
        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("random_state", 42)
        mlflow.log_metric("accuracy", accuracy)

    mlflow.sklearn.log_model(
        sk_model=model,
        name="random_forest_model",
        serialization_format="cloudpickle",
        signature=signature,
        input_example=X_test[:5],
        registered_model_name="workspace.default.IrisRFModel"
    )   

    print(f"Model accuracy: {accuracy:.4f}")
    return accuracy


if __name__ == "__main__":
    main()
