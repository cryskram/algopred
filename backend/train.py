from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd

feature_names = []


def train_model(df: pd.DataFrame, target_column: str, algorithm: str):
    global feature_names
    X = df.drop(columns=[target_column])
    y = df[target_column]

    feature_names = X.columns.to_list()

    if algorithm == "random_forest":
        model = RandomForestRegressor()
    elif algorithm == "gradient_boosting":
        model = GradientBoostingRegressor()
    elif algorithm == "linear_regression":
        model = LinearRegression()
    else:
        raise ValueError("Invalid Algo")

    model.fit(X, y)
    y_pred = model.predict(X)
    acc = r2_score(y, y_pred)

    return model, acc


def predict(model, input_list):
    global feature_names
    input_df = pd.DataFrame([input_list], columns=feature_names)
    return model.predict(input_df)[0]
