import rest_framework.generics
from django.shortcuts import render

from .filter import FilterTable
from .models import Table
from .forms import NameForm
from .serializer import TableSerializer


def main(request):
    template = 'table.html'
    return render(request, template, {'form': NameForm(request.GET)})


class ViewTable(rest_framework.generics.ListAPIView):
    """Собственно api с фильтрацией и пагинацией значений"""
    serializer_class = TableSerializer
    filter = FilterTable

    def get_queryset(self):
        queryset = self.filter(Table.objects.all(), self.request.GET)
        return queryset

