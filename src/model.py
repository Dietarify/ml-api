import pickle
import os
from typing import Literal
from pydantic import BaseModel


model = pickle.load(
    open((os.path.dirname(os.path.abspath(__file__)))+"/model/model.pk", "rb"))


class ModelData(BaseModel):
    sex: Literal["Male", "Female"]
    age: int
    caloriesNeed: float


def get_recomendation(data: ModelData):
    sex_F = 0
    sex_M = 0

    if data.sex == "Male":
        sex_M = 1

    if data.sex == "Female":
        sex_F = 1

    result = model.predict([
        [
            sex_F,
            sex_M,
            data.age,
            data.caloriesNeed,
            1, 0, 0
        ],
        [
            sex_F,
            sex_M,
            data.age,
            data.caloriesNeed,
            0, 1, 0
        ],
        [
            sex_F,
            sex_M,
            data.age,
            data.caloriesNeed,
            0, 0, 1
        ]
    ])

    return [int(result[0][0]), int(result[1][0]), int(result[2][0])]
