from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    RandomForestClassifier,
    GradientBoostingClassifier,
)
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.svm import SVC, SVR
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import r2_score, accuracy_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd

feature_names = []
task_type = "regression"
label_encoder = None


def train_model(df: pd.DataFrame, target_column: str, algorithm: str, task: str):
    global feature_names, task_type, label_encoder
    task_type = task.lower()
    X = df.drop(columns=[target_column])
    y = df[target_column]

    feature_names = X.columns.to_list()

    if task_type == "classification":
        if y.dtype == object:
            label_encoder = LabelEncoder()
            y = label_encoder.fit_transform(y)
        else:
            label_encoder = None

        if algorithm == "random_forest":
            model = RandomForestClassifier()
        elif algorithm == "gradient_boosting":
            model = GradientBoostingClassifier()
        elif algorithm == "logistic_regression":
            model = LogisticRegression(max_iter=200)
        elif algorithm == "knn":
            model = KNeighborsClassifier()
        elif algorithm == "svm":
            model = SVC()
        elif algorithm == "naive_bayes":
            model = GaussianNB()
        else:
            raise ValueError("Unsupported classification algo")

    elif task_type == "regression":
        label_encoder = None
        if algorithm == "random_forest":
            model = RandomForestRegressor()
        elif algorithm == "gradient_boosting":
            model = GradientBoostingRegressor()
        elif algorithm == "logistic_regression":
            model = LinearRegression()
        elif algorithm == "knn":
            model = KNeighborsRegressor()
        elif algorithm == "svm":
            model = SVR()
        else:
            raise ValueError("Unsupported regression algo")

    else:
        raise ValueError("Invalid task type. Pick either regression or classification")

    model.fit(X, y)
    y_pred = model.predict(X)

    if task_type == "classification":
        score = accuracy_score(y, y_pred)
    else:
        score = r2_score(y, y_pred)

    return model, score, feature_names


def predict(model, input_list):
    global feature_names, task_type, label_encoder
    input_df = pd.DataFrame([input_list], columns=feature_names)
    prediction = model.predict(input_df)[0]

    if task_type == "classification" and label_encoder is not None:
        prediction = label_encoder.inverse_transform([int(prediction)])[0]

    return prediction
