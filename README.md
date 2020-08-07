# jesFinance
[![Actions Status](https://github.com/agstrike/jesFinance/workflows/Test%20and%20Lint/badge.svg)]
[![codecov](https://codecov.io/gh/agstrike/jesFinance/branch/master/graph/badge.svg)]

Webapp based on Django to manage personal finances

## Get jesFinance running on your machine
python3 -m venv demo/env
source demo/env/bin/activate
python setup.py develop
source env/bin/activate
python manage.py migrate
python manage.py createsuperuser
source env/bin/activate
python manage.py runserver
