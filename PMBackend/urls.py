
from django.http import HttpResponse

def test_view(request):
    return HttpResponse('Vercel is serving Django!')

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('test/', test_view),
    path('admin/', admin.site.urls),
    # other paths
]

