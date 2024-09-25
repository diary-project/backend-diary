#!/bin/bash
#DJANGO_APP = "config"

# 가상 환경 활성화
source ~/.bashrc
pyenv activate diary_backend

# PYTHONPATH 설정
export PYTHONPATH=src

# 데이터베이스 마이그레이션
poetry run python src/manage.py migrate --no-input
poetry run python src/manage.py collectstatic --no-input

# 백그라운드로 celery 실행
nohup celery -A config worker -l info > celery.log 2>&1 &

# Gunicorn 실행
exec poetry run gunicorn src.config.wsgi:application --bind 0.0.0.0:8000