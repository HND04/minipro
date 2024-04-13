import asyncio
from django.shortcuts import render
from websocketss import websocket_view
from django.http import JsonResponse
from django.shortcuts import render
import json
async def async_websocket_view(request):
    return await websocket_view(request)

def websocket_view_sync(request):
    asyncio.run(async_websocket_view(request))
    return render(request, 'data.html')
def sample(request):
    return render(request,'sample.html')

def receive_data(request):
    # Default data value
    data = 10
    
    if request.method == 'POST':
        try:
            # Load JSON data from request body
            received_data = json.loads(request.body)
            
            # Process the received data as needed
            # Example: data = received_data['key']
            # ...
            
            # Set data to the processed data
            data = received_data
        except json.JSONDecodeError:
            # Handle JSON decoding error
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except KeyError:
            # Handle missing key error
            return JsonResponse({'error': 'Missing key'}, status=400)
    
    # Return JsonResponse for POST requests
    if request.method == 'POST':
        return JsonResponse(data, status=200)
    else:
        # Render the template for GET requests
        return render(request, 'data.html', {'data': data})
