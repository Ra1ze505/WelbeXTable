from django.http import Http404
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .filter import FilterTable
from .models import Table
from .forms import NameForm


class ViewTable(ListView):
    template_name = 'table.html'
    model = Table
    filter = FilterTable

    def get_context_data(self, **kwargs):
        context = super(ViewTable, self).get_context_data(**kwargs)
        context['form'] = NameForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = self.filter(Table.objects.all(), self.request.GET)
        return queryset

    @api_view(('GET',))
    def get_ajax(self, request, context):
        return Response(context)

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(_('Empty list and “%(class_name)s.allow_empty” is False.') % {
                    'class_name': self.__class__.__name__,
                })
        print(request.is_ajax())
        context = self.get_context_data()
        if request.is_ajax():
            return self.get_ajax(request, context)
        return self.render_to_response(context)