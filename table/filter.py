class FilterTable:
    def __init__(self, queryset, *args, **kwargs):
        self.params = args[0]
        self.args = args[1:]
        self.kwargs = kwargs
        self.queryset = queryset
        self.filtered_queryset = queryset  # на случай отсутствия фильтрации
        self._get_filter()

    def _get_filter(self):
        """Проверяем метод фильтрации и вызываем соотвестствующий метод"""
        if 'filter_method' in self.params:
            if self.params['filter_method'] == '=':
                self._equals()
            elif self.params['filter_method'] == '<':
                self._smaller()
            elif self.params['filter_method'] == '>':
                self._larger()
            elif self.params != {} and self.params['filter_method'] == 'in':
                self._enters()

    def _equals(self):
        param = {self.params['filter']: self.params['value']}
        self.filtered_queryset = self.queryset.filter(**param)

    def _smaller(self):
        param = {self.params['filter']+'__lt': int(self.params['value'])}
        self.filtered_queryset = self.queryset.filter(**param)

    def _larger(self):
        param = {self.params['filter']+'__gt': int(self.params['value'])}
        self.filtered_queryset = self.queryset.filter(**param)

    def _enters(self):
        self.filtered_queryset = []
        for item in self.queryset:
            atr = getattr(item, self.params['filter'])
            if self.params['value'] in str(atr):
                self.filtered_queryset.append(item)

    def __iter__(self):
        return self.filtered_queryset.__iter__()

    def __len__(self):
        return len(self.filtered_queryset)

    def __getitem__(self, key):
        return self.filtered_queryset.__getitem__(key)
