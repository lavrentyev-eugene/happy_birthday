import uvicorn
from fastapi import FastAPI, Path
from starlette.responses import FileResponse, Response

app = FastAPI()


@app.get("/birthday_gift/{query_hash}")
async def get_aircraft_flight_data(
        query_hash: str = Path(...),
):
    solution_hash = 'ab7a34ca99e00dbfe131be4c320b5f0578880defb62b8d29066fce2bfa96ebdc'
    if query_hash == solution_hash:
        path = 'gift_card.pdf'
        return FileResponse(path)
    return Response('Wrong string, LUL)00))00))0')


@app.get("/")
async def get_aircraft_flight_data():
    return Response('Hi there, general Kenobi')


if __name__ == "__main__":
    uvicorn.run(app)
