
from fastapi import FastAPI
from fastapi.responses import JSONResponse

def create_new_sequence():
    """Create a list with one item equal to 0"""
    return [0]

# Object to store the numbers we receive
sequence = create_new_sequence()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/sequence")
async def getCurrentSeqeuence():
    return JSONResponse(sequence)


@app.post("/sequence/add_to_last/{number}")
async def add_to_last(number: int):
    next_in_sequence = sequence[-1] + number
    sequence.append(next_in_sequence)

    # Only keep last 10 digits
    while len(sequence) > 10:
        _ = sequence.pop(0)

    return {"message": {"received": number, "next_in_sequence": next_in_sequence}}


@app.delete("/sequence")
async def reset_sequence():
    global sequence
    sequence = create_new_sequence()
    return JSONResponse({"message": {"sequence reset to": sequence}})
