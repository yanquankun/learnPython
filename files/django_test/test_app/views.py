from django.http import HttpResponse, JsonResponse


# Create your views here.
def test_view(request):
    return HttpResponse("Hello from test_app!")
