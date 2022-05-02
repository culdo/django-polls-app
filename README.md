# Django 投票APP
The demo app of the official tutorial with additional features and also deploy on Heroku
# Features
* 2-step user registration
* Login
* Admin site
* Polls list
* Voting
* Vote detail
# Database
* Heroku Postgres
# Developing
1. You need to add your gmail username and token to env vars as `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`
2. Run `python3 manage.py runserver`
# Unit testing locally
Run `python3 manage.py test`
# Unit testing on GitHub Action
* Add env vars to `Repository Settings > Environments > Environments secrets`
* Check out `.github/workflows/main.yaml` file to see how it works
# Deploy on Heroku
1. Use GitHub action at `.github/workflows/main.yaml`
2. Add env vars to `App Settings > Config Vars` or use Heroku CLI to add config vars
3. Run `heroku run python manage.py migrate` to migrate db
4. Run `heroku run python manage.py createsuperuser` to create admin
## Production requirements
* gunicorn
* whitenoise

# To-do-list
- [ ] Integration testing
