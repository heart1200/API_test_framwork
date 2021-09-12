from django.http import HttpResponse
from django.shortcuts import render
import json


# Create your views here.
def login(request):
    result = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        result['username'] = username
        result['password'] = password
        result = json.dumps(result)
        return HttpResponse(result, content_type='application/json; charset=utf-8')
    else:
        return render(request, 'Login.html')
