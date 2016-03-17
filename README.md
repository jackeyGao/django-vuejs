# Django Channels Example 

This is an example app demonstrating how to use (and deploy) [Django Channels](http://channels.readthedocs.org/en/latest/). It's a simple real-time chat app — like a very, very light-weight Slack. There are a bunch of rooms, and everyone in the same room can chat, in real-time, with each other (using WebSockets).

For more details, see (article forthcoming).

You can visit [my deployment of the example online](https://django-channels-example.herokuapp.com/), or deploy your own copy to Heroku with this button (which requires a free Heroku account):

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/jacobian/channels-example)

**WARNING:** you'll need to scale the `worker` process type up after using the button. Use the Dashboard, or run `heroku ps:scale web=1:free worker=1:free`.

## Running locally

To run this app locally, you'll need Python, Postgres, and Redis. (On my Mac, I installed [Postgres.app](http://postgresapp.com/documentation/) and Redis from Homebrew (`brew install redis`).)

Then, to run:

- Install requirements: `pip install -r requirements.txt` (you almost certainly want to do this in a virtualenv).
- Migrate: `DATABASE_URL=postgres:///... python manage.py migrate`
- If you use [heroku local](https://devcenter.heroku.com/articles/heroku-local), or [foreman](https://github.com/ddollar/foreman)/[forego](https://github.com/ddollar/forego), edit `.env` to add `DATABASE_URL` and `REDIS_URL`, then start `heroku local`/`foreman`/`forego`.
- Or, to run locally with `runserver`, set `DATABASE_URL` and `REDIS_URL` in your environ, then run `python manage.py runserver`.
- Or, to run locally with multiple proceses by setting the environ, then running the two commands (`daphne` and `runworker`) as shown in the `Procfile`.
