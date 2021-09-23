from rest_framework.test import APITestCase
from django.test import RequestFactory
from parameterized import parameterized


from .filter import FilterTable
from .models import Table


class TableTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Table.objects.create(title='test-title1',
                                   count=10,
                                   distance=100,
                                   date='08:43:00')
        Table.objects.create(title='test-title2',
                                   count=100,
                                   distance=10,
                                   date='08:43:00')
        Table.objects.create(title='test-title3',
                                   count=101,
                                   distance=1234,
                                   date='08:43:00')
        Table.objects.create(title='test-title4',
                                   count=1,
                                   distance=10,
                                   date='08:43:00')
        Table.objects.create(title='test-title5',
                                   count=1054,
                                   distance=1543,
                                   date='08:43:00')
        Table.objects.create(title='test-title6',
                                   count=5430,
                                   distance=54,
                                   date='08:43:00')

    def setUp(self) -> None:
        self.table = Table.objects.all()
        self.factory = RequestFactory()

    @parameterized.expand([
        ('count', '<', '100', 'lt'),
        ('distance', '=', '10', ''),
        ('count', '>', '1000', 'gt'),
    ])
    def test_filter(self, filter, filter_method, value, orm_method):
        data = {
            'filter': filter,
            'filter_method': filter_method,
            'value': value
        }
        self.request = self.factory.get('/', data)
        self.filter = FilterTable(self.table, self.request.GET)
        if orm_method != '':
            param = {filter + '__' + orm_method: int(data['value'])}
        else:
            param = {filter: int(data['value'])}
        wq = self.table.filter(**param)
        waiting_queryset = []
        for i in wq:
            waiting_queryset.append(i)
        filter_items = []
        for i in self.filter:
            filter_items.append(i)
        self.assertEqual(waiting_queryset, filter_items)
