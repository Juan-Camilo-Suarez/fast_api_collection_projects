from datetime import date

from fastapi import FastAPI

app = FastAPI()


@app.get('/hotels')
def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        # optional validation values
        has_spa: int = None,
        starts: bool = None
):
    return date_from, date_to

# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port=8000)
