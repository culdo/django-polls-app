# Django 投票APP
The demo app of the official tutorial with additional features and also deploy on Heroku
# Features
* User register / login
* Admin site
* Polls list
* Voting
* Vote detail
# Database
* Heroku Postgres
# Developing
Run `python3 manage.py runserver`
# Unit testing locally
Run `python3 manage.py test`
# Unit testing on GitHub Action
Check out `.github/workflows/main.yaml` file to see how it works
# Deploy on Heroku
1. Use GitHub action at `.github/workflows/main.yaml`
2. Run `heroku config:set SECRET_KEY <your-secret-key>` to config vars
3. Run `heroku run python manage.py migrate` to migrate db
4. Run `heroku run python manage.py createsuperuser` to create admin
## Production requirements
* gunicorn
* whitenoise

# To-do-list
- [ ] Integration testing
