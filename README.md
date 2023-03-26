# **Интернет магазин JoYstik** 

#### **Стек**
![python version](https://img.shields.io/badge/Python-3.11-green)
![django version](https://img.shields.io/badge/Django-4.2-green)
![djangorestframework](https://img.shields.io/badge/Djangorestframework-3.14-green)

### **Описание**
Пет-проект веб-приложение, использующее API для получения данных о курсах криптовалют от CoinMarketCap:

### **Цели**
 
:white_check_mark:(сделанно)  Вывод информации о всех доступных криптовалютах (символьный код, название, текущий курс, изменение за последние 24 часа, объем торгов и т.д.);
 
:white_check_mark:(сделанно)  Поиск криптовалют по названию или символьному коду;

:white_check_mark:(сделанно)  Возможность добавления криптовалют в список избранных, отображение списка избранных криптовалют;

:white_check_mark:(сделанно)  Информация о криптовалюте должна записываться в базу данных (н., в виде модели);

:white_check_mark:(сделанно)  Вывод новостей о криптовалютах (например, с помощью NewsAPI);

:white_check_mark:(сделанно)  Авторизация и регистрация пользователей, хранение данных в базе данных.

<details>
<summary>
<b>Запуск проекта в dev-режиме 
</summary>
Инструкция ориентирована на операционную систему windows и утилиту git bash.<br/>
Для прочих инструментов используйте аналоги команд для вашего окружения.

1. Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone git@github.com:Shkitskiy94/CoinMarketCap_drf_api.git
```

2. Установите и активируйте виртуальное окружение
```
python -m venv venv
``` 
```
source venv/Scripts/activate
```
```
cd coinmarketcup
```
3. Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

4. В папке с файлом manage.py выполните миграции:
```
python manage.py migrate
```

5. В папке с файлом manage.py запустите сервер, выполнив команду:
```
python manage.py runserver
```

6. В корневой папке создайте файл .env со следующим содержимым:
```
LIMIT = 5000
START = 1
CRYPTO_API_KEY = '<ваш_api_key>'
NEWS_API_KEY = '93a64ac837c34869a6bf2f162e4963cd'
```
Получить ключи к апи можно по адресам: (https://coinmarketcap.com/api/), (https://newsapi.org/)