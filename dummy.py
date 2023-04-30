"""dummy"""


from fastapi import FastAPI


def addition(first_number: int, second_number: int):
    """
    addtion of first number and second number
    """
    return first_number + second_number



DEVICES = ["device_01", "device_02", "device_03"]

app = FastAPI()


@app.get("/devices")
async def get_devices():
    """
    get all devices
    """
    return DEVICES
