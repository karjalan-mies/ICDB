set FLASK_APP=webapp && flask db migrate -m "Добавлены поля в таблицу Company"
flask db upgrade