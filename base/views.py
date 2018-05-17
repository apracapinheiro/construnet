from django.shortcuts import render
from django.views import View

# Create your views here.


class IndexView(View):
    """Template view index"""
    template_name = "index.html"
    context_object_name = "pagina_inicial"

    def get(self, request):
        return render(request, 'index.html')
