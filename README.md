# WelbeXTable
## Установка
Создайте clone:
```
git clone https://github.com/Ra1ze505/WelbeXTable.git
```
Перейдите в корневой каталог проекта:
``` 
cd TestDomClick
```

И установите зависимости: 
```
pip install -r requirements.txt
```
## Начало работы
В файле settings.py проверьте настройки DATABASE по умолчанию postgresql, но вы можете подключить любую базу данных, подробнее: https://docs.djangoproject.com/en/3.2/ref/databases/
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
## Функционал
- Реализовано api для таблицы
- Пагинация
- Фильтрация
- Все обновление данных на странице происходят с помощью ajax запросов