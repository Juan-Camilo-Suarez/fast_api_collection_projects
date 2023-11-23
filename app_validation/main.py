from datetime import date

import uvicorn
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def get_root():
    return {'message': 'Hello World'}


# data to validate interaction with api
class SHotel(BaseModel):
    address: str
    name: str
    starts: int


@app.get('/hotels')
def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        # optional validation values
        has_spa: bool = None,
        starts: int = Query(default=None, gt=1, le=5)
) -> list[SHotel]:
    hotels = [
        {
            "address": "bratievska 1",
            "name": "Resort 5",
            "starts": 1
        }
    ]
    return hotels


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
