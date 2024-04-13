import asyncio
import websockets
import json,os
from django.template import loader
from django.shortcuts import render
async def connect_to_server(request):
    raspberry_pi_ws_url = os.getenv("RASPBERRY_PI_WS_URL", "ws://192.168.1.10:8000")
    data_points = []
    try:
        async with websockets.connect(raspberry_pi_ws_url) as websocket:
            print("Connected to WebSocket server")
            while True:
                data_json = await websocket.recv()
                data = json.loads(data_json)
                data_points.append(data)
                # Update the frontend with the received data
    except Exception as e:
        print(f"Error: {e}")
async def websocket_view(request):
    data_points = await connect_to_server(request)
    return render(request, 'data.html', {'data_points': data_points})