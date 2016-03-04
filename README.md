# Django Channels Example 

what is this? chat app example, showing that "it's still django", butt....
see [article]

## Running on Heroku

[button]

Or, manual instructions:

- create app
- addons: postgres, redis
- settings: SECRET_KEY
- `git push heroku master`
- `heroku run python manage.py migrate`
- `heroku ps:scale web=1:free worker=1:free`

## Running locally

- postgres, redis (homebrew/postgres.app)
- locally w/o redis (postgres channel backend)
- migrate
- `h local` (not runserver)