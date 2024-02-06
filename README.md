Проект REST API для туристических горных перевалов. Описание:
Этот проект разрабатывается для Федерации Спортивного Туризма и Развития с целью упростить процесс учета горных перевалов и сократить время обработки данных. По заданию необходимо усовершенствовать REST API для ведения базы горных перевалов, которая пополняется туристами.
 Реализованы методы:
 API POST/submitData для добавления туристом информации о новом перевале; 
GET /submitData/ — получение одной записи о перевале по ее id, в том числе статус модерации; 
PATCH /submitData/ — редактирование существующей записи, если она еще не поступила в работу модератору, 
 GET /submitData/?user__email= — список данных обо всех объектах, которые пользователь с почтой отправил на сервер. 
1.При подготовке проекта использована база данных PostgreSQL, установка производится командой:
pip install psycopg2
Порт, логин, пароль и путь к базе данных берется из переменных окружения с использованием библиотеки dotenv:
pip install python-dotenv
2.В файле requirements.txt приведен список внешних зависимостей, который формируется командoй pip freeze > requirements.txt. Установите зависимости командой:
pip install -r requirements.txt
Добавлен визуальный интерфейс Swagger. За основу при установке взят следующий источник Его работа доступна по адресу /api/schema/swagger-ui, для генерирования документации /api/schema/redoc/
Код приложения был покрыт тестами, установлена библиотека coverage.
Проект размещен на хостинге http://akchuranne.pythonanywhere.com . В нем используется база данных db.sqlite3. Рабочий проект на базе данных PostgreSQL (конвертация с помощью /manage.py dumpdata > dump.json, ./manage.py loaddata dump.json).
 Примеры вызова REST API с хостинга http://akchuranne.pythonanywhere.com/api/submitData/pereval/3/ - получение информации о перевале по его id. http://akchuranne.pythonanywhere.com/api/submitData/user__email= shelomencevandrey@yandex.ru - список данных обо всех объектах, созданных пользователем с электронной почтой shelomencevandrey@yandex.ru
По адресу /api/submitData/pereval/ или api/schema/swagger-ui/#/api/api_submitData_pereval_create можно создать информацию о новом перевале с помощью POST.
По адресу /api/submitData/pereval/id или api/schema/swagger-ui/#/api/api_submitData_pereval_retrieve можно получить одну запись о перевале по ее id, в том числе статус модерации c помощью GET;
По адресу /api/submitData/pereval/id или /api/schema/swagger-ui/#/api/api_submitData_pereval_partial_update можно редактировать существующую запись, если она еще не поступила в работу модератору с помощь PATCH;
Сменить статус модерации можно только через админ-панель. 



