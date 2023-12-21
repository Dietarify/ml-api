from fastapi import FastAPI
import model

app = FastAPI()


@app.get("/")
async def status_check():
    return {
        "status": "success",
        "message": "server is running",
        "data": None
    }


@app.post("/models/food-recomendation")
async def food_recomendation(data: model.ModelData):
    result = model.get_recomendation(data)

    return {
        "status": "success",
        "message": "success",
        "data": result
    }
