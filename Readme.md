# ModelCraft

Train and use machine learning models directly from CSV files via a simple web interface. Supports algorithm selection, target column picking, and real-time prediction.

## Tech Stack

- ⚙️ Backend: [FastAPI](https://fastapi.tiangolo.com/)
- 🧠 ML: Scikit-learn
- 🌐 Frontend: [Next.js](https://nextjs.org/) + TypeScript + Tailwind CSS
- 🔌 Communication: REST API (Axios)

## How to run locally

1. Clone the repository

```
git clone https://github.com/cryskram/algopred.git
cd algopred
```

2. Start the backend(Python + FastAPI)
   > Make sure you have Python >= 3.10 and Pipenv install... else run `pip install pipenv`

```
cd backend
pipenv install
```

Run the server:

```
pipenv run uvicorn main:app --reload
```

- will be running at `http:localhost:8000`
- API endpoints:
  - `POST /upload`
  - `POST /train`
  - `POST /pred`

3. Start the Frontend(Next.js)
   > Requires Node.js >= 18 installed

```
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:3000`

> Make sure the backend is running when using the UI

## Features

- Upload CSV File
- Choose target column
- Select Algorithm
- Train model and view accuracy
- Input test values and get predictions

## In-progress

- Support for textual dataset
- Classification support along with the already exisiting regression
- Auto test input suggestions
- Multiple model evaluation metrics

## Contributions

Pull requests welcome! If you'd like to contribute to classification support or add new ML models, feel free to fork and PR.
