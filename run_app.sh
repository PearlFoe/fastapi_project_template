#!/bin/bash
uv run gunicorn "main:get_app()" --chdir src/ --bind 0.0.0.0:8000 --worker-class uvicorn.workers.UvicornWorker  # run web server