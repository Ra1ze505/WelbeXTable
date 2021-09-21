from django import forms


FILTER_FIELD = (
    ('', '----'),
    ('title', 'Название'),
    ('count', 'Количество'),
    ('distance', 'Дистанция'))

FILTER_METHOD = (
    ('', '----'),
    ('=', 'Равно'),
    ('in', 'Содержит'),
    ('>', 'Больше'),
    ('<', 'Меньше'))


class NameForm(forms.Form):
    filter = forms.TypedChoiceField(choices=FILTER_FIELD, coerce=int)
    filter_method = forms.TypedChoiceField(choices=FILTER_METHOD, coerce=int)
    value = forms.CharField()