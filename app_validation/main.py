from datetime import date

import uvicorn
from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/')
def get_root():
    return {'message': 'Hello World'}


@app.get('/hotels')
def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        # optional validation values
        has_spa: bool = None,
        starts: int = Query(default=None, gt=1, le=5)
):
    return date_from, date_to, has_spa, starts


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
