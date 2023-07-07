from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from starlette.responses import FileResponse 

import json

app = FastAPI()

@app.get("/")
async def get():
    return FileResponse('index.html')


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    message_id = 1

    while True:
        data = json.loads(await websocket.receive_text())
        
        if data['msg'] == '__ping__':
            await websocket.send_json({"msg": "__pong__"})
            continue
        
        await websocket.send_json({"msg": data["msg"], "id": message_id})

        message_id += 1 