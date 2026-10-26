import asyncio, time
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
app = FastAPI(title="AquaSustain simulated telemetry")
@app.get("/")
def dashboard():
    return FileResponse(__import__('pathlib').Path(__file__).with_name('index.html'))
@app.websocket("/ws")
async def telemetry(ws: WebSocket):
    await ws.accept()
    step = 0
    try:
        while True:
            await ws.send_json({"timestamp":time.time(), "source":"SIMULATED",
                                "turbidity_raw":1800 + step % 100, "unit":"ADC counts"})
            step += 1
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        pass
