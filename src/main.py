from fastapi import FastAPI
from data.Request import BMIRequest, CaloriesNeeds


app = FastAPI()


@app.get("/")
async def status_check():
    return {
        "status": "success",
        "message": "server is running",
        "data": None
    }


@app.post("/models/food-recomendation")
async def food_recomendation():
    return {
        "status": "success",
        "message": "success",
        "data": [1, 2, 3]
    }


@app.post("/calculate/bmi")
async def calculate_bmi(userData: BMIRequest):
    userWeight = userData.weight
    userHeight = userData.height

    # TODO: add real calculation

    return {
        "status": "success",
        "message": "success",
        "data": 40.2
    }


@app.post("/calculate/calories-needs")
async def calculate_calories_needs(userData: CaloriesNeeds):
    userWeight = userData.weight
    userHeight = userData.height

    # TODO: add real calculation

    return {
        "status": "success",
        "message": "success",
        "data": 2190
    }
