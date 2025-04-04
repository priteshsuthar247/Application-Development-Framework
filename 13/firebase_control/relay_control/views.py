from django.shortcuts import render, redirect
from django.http import JsonResponse
from firebase_config import ref
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def relay_control(request):
    if request.method == 'POST':
        # Toggle relay state
        current_state = ref.child('relay/state').get()
        new_state = 'on' if current_state == 'off' else 'off'
        ref.child('relay/state').set(new_state)
        return JsonResponse({'status': 'success', 'new_state': new_state})
    
    # GET request - show current state
    current_state = ref.child('relay/state').get()
    return render(request, 'relay_control.html', {'current_state': current_state})