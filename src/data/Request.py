from pydantic import BaseModel


class FoodRecomendationRequest(BaseModel):
    pass


class BMIRequest(BaseModel):
    height: float
    weight: float


class CaloriesNeeds(BaseModel):
    height: float
    weight: float
