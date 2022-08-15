import hashlib

import uvicorn
from fastapi import FastAPI, Path
from starlette.responses import FileResponse, Response

app = FastAPI()


@app.get("/birthday_gift/{hash_string}")
async def get_aircraft_flight_data(
        hash_string: str = Path(...),
):
    string_hash = '1d6442ddcfd9db1ff81df77cbefcd5afcc8c7ca952ab3101ede17a84b866d3f3'
    if hash_string == string_hash:
        path = 'happy_birthday.png'
        return FileResponse(path)
    return Response('Wrong string, LUL)00))00))0')


if __name__ == "__main__":
    # print(hashlib.sha3_256('1234'.encode()).hexdigest())
    uvicorn.run(app)
