
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import redis

def create_new_sequence(redis_con, key="numbers"):
    """Create a list with one item equal to 0"""
    for _ in range(redis_con.llen(key)):
        _ = redis_con.lpop(key)
    redis_con.lpush(key, 0)
    return [0]

def add_number_to_sequence(number, redis_con, key="numbers"):
    redis_con.lpush(key, int(number))
    if redis_con.llen(key) > 10:
        _ = redis_con.ltrim(key, 0, 9)

def get_current_sequence(redis_con, key="numbers"):
    number_list = []
    for _ in range(redis_con.llen(key)):
        number_list.append(int(redis_con.rpop(key)))

    # Rebuild REDIS stored list
    redis_con.lpush(key, *number_list)
    return number_list


# Create Redis connection to store our sequence
redis_con = redis.Redis(host="redis", port=6379, db=0)

sequence = create_new_sequence(redis_con)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from the Sequence Generator"}


@app.get("/sequence")
async def getCurrentSeqeuence():
    sequence = get_current_sequence(redis_con)
    return JSONResponse(sequence)


@app.post("/sequence/add_to_last/{number}")
async def add_to_last(number: int):
    last_val = int(redis_con.lpop("numbers"))
    next_in_sequence = last_val + number
    add_number_to_sequence(last_val, redis_con)
    add_number_to_sequence(next_in_sequence, redis_con)

    return {"message": {"received": number, "next_in_sequence": next_in_sequence}}


@app.delete("/sequence")
async def reset_sequence():
    global sequence
    sequence = create_new_sequence(redis_con)
    return JSONResponse({"message": {"sequence reset to": sequence}})
