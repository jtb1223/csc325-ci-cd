# CSC325 CI/CD

A small Django + Django REST Framework backend with a GitHub Actions pipeline.

## Pages

| Path | Description |
| --- | --- |
| `/` | Home page, shows `Hello, World!` and a button to the About page |
| `/about/` | About page, with an animated cow GIF as the background |

## API

| Method | Path | Description |
| --- | --- | --- |
| GET | `/api/health/` | Health check, returns `{"status": "ok"}` |
| GET, POST | `/api/tasks/` | List or create tasks |
| GET, PUT, PATCH, DELETE | `/api/tasks/<id>/` | Read, update or delete one task |

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
python manage.py migrate
python manage.py runserver
```

Then open <http://127.0.0.1:8000/>.

## Tests

```bash
python manage.py test -v 2
```

## Pipeline

`.github/workflows/csc325_ci_cd.yml` runs on every push to `main`:

1. **Setup**: checks out the code and installs Python 3.12
2. **Dependencies**: installs `requirements.txt` and runs `pip check`
3. **Test**: runs the full Django test suite; a failing test fails the pipeline
4. **Deploy**: runs only after Test passes (`needs: test`); migrates, starts the server, and
   smoke-tests `/`, `/about/` and `/api/health/`
