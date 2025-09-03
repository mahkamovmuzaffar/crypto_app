from django.http import JsonResponse
from jsonrpcserver import method, dispatch


@method
def ping():
    return "pong"


def rpc_view(request):
    response = dispatch(request.body.decode())
    return JsonResponse(response, safe=False)
