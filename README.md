# CSC325 CI/CD

A small Django + Django REST Framework backend with a GitHub Actions pipeline.

## API

| Method | Path | Description |
| --- | --- | --- |
| GET | `/api/health/` | Health check, returns `{"status": "ok"}` |
| GET, POST | `/api/tasks/` | List or create tasks |
| GET, PUT, PATCH, DELETE | `/api/tasks/<id>/` | Read, update or delete one task |

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
python manage.py migrate
python manage.py runserver
```

## Tests

```bash
python manage.py test
```

## Pipeline

`.github/workflows/csc325_ci_cd.yml` runs on every push to `main`:

1. **Lint**: flake8
2. **Test**: migration check and Django tests
3. **Build**: system checks, collectstatic, packages the app as an artifact
4. **Deploy**: unpacks the artifact, migrates, starts the server, and smoke-tests the API
