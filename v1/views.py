from django.http import JsonResponse
from jsonrpcserver import method, dispatch


@method(name="hello.world")
def hello_world(message):
    return {"echo": message}


@method(name="health.check")
def health_check():
    return {"status": "ok"}


@method
def login(username=None, password=None):
    # Dummy implementation, replace with real authentication logic
    if username == "admin" and password == "password":
        return {"access_token": "dummy-token-123"}
    return {"error": "Invalid credentials"}


def jsonrpc_dispatch(request):
    response = dispatch(request.body.decode())
    return JsonResponse(response, safe=False)
