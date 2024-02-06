##Серверная часть проекта ArchMotorcucle.

## Для запуска проекта:
* Клонируйте реепозиторий `git clone https://github.com/GusevADresume/archMotoBack`
* Создайте виртуальную среду `python -m venv venv`
* Активируйте виртуальную среду `source venv/bin/activate`
* Перейдите в каталог с проектом
* Установите зависимости `pip install -r requirements.txt`
* Установите БД postgresql `sudo apt install postgresql`
* Войдите в БД `sudo -i -u postgres` `psql`
* Создайте пользователя `CREATE USER archadmin1 WITH PASSWORD '123456789'`
* Создайте БД `CREATE DATABASE archbase1 OWNER archadmin1;`
* Запустите проект `uvicorn main:app`
