from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from train import train_model, predict

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
model = None
df_cache = None


class PredictInput(BaseModel):
    test_input: list[float]


class TrainRequest(BaseModel):
    target_column: str
    algorithm: str
    task: str


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    global df_cache
    df_cache = pd.read_csv(file.file)
    return {"columns": df_cache.columns.to_list()}


@app.post("/train")
async def train(data: TrainRequest):
    global model, df_cache
    if df_cache is None:
        return {"error": "No CSV uploaded"}

    try:
        model, acc, features = train_model(
            df_cache, data.target_column, data.algorithm, data.task
        )
        return {
            "message": f"Model trained using {data.algorithm}",
            "accuracy": acc,
            "features": features,
        }
    except ValueError as e:
        return {"error": str(e)}


@app.post("/pred")
def pred(data: PredictInput):
    if model is None:
        return {"error": "Model is not trained"}
    prediction = predict(model, data.test_input)
    return {"prediction": prediction}
