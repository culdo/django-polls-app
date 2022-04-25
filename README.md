# Django 投票 APP
The demo app made by following the official tutorial and also deploy on Heroku
# Database
* Heroku Postgres
# Developing
Run `python3 manage.py runserver`
# Testing
Run `python3 manage.py test`
# Testing on GitHub Action
Check out `.github/workflows/main.yaml` file to see how it works
# Deploy on Heroku
1. Use GitHub action at `.github/workflows/main.yaml`
2. Run `heroku config:set SECRET_KEY <your-secret-key>` to config vars
3. Run `heroku run python manage.py migrate` to migrate db
4. Run `heroku run python manage.py createsuperuser` to create admin
## Production requirements
* gunicorn
* whitenoise
