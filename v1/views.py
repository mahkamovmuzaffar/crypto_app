from django.http import JsonResponse
from jsonrpcserver import method, dispatch


@method
def echo(message):
    return {"echo": message}


@method
def status():
    return {"status": "ok"}


@method
def login(username=None, password=None):
    # Dummy implementation, replace with real authentication logic
    if username == "admin" and password == "password":
        return {"access_token": "dummy-token-123"}
    return {"error": "Invalid credentials"}


def rpc_view(request):
    response = dispatch(request.body.decode())
    return JsonResponse(response, safe=False)
