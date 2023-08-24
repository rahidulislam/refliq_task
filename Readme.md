### Task Description

I will write a Django app to track corporate assets such as phones, tablets, laptops
and other gears handed out to employees.

### Task Goal

1. The application might be used by several companies
2. Each company might add all or some of its employees
3. Each company and its staff might delegate one or more devices to employees for a certain period of time
4. Each company should be able to see when a Device was checked out and returned
5. Each device should have a log of what condition it was handed out and returned

### Permission List

1. Only Superuser or Staff User create a company
2. Company's Owner can create his/her employee, Other user only see or get list
3. Company's Owner can create Device, other user only see list
4. Company's Owner can create Device Log, other user only see list

#### Create Virtual Envirionment

python -m venv venv

#### Activate Virtual Environment

source venv/bin/activate

#### Install Package

pip install -r requirements.txt

#### Run Server

python manage.py runserver

#### Makemigrations

python manage.py makemigrations
python manage.py migrate

#### Create Superuser

python manage.py createsuperuser
