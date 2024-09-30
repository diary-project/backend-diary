#!/bin/bash

# 환경 변수 설정
export PYTHONPATH=src

# 데이터베이스 마이그레이션
poetry run python src/manage.py migrate --no-input

# 정적 파일 수집
poetry run python src/manage.py collectstatic --no-input

# 로그 디렉토리 및 파일 설정
LOG_DIR=/app/logs
CELERY_LOG_FILE=$LOG_DIR/celery.log
GUNICORN_LOG_FILE=$LOG_DIR/gunicorn.log

# 로그 디렉토리 생성 (없으면)
mkdir -p $LOG_DIR

# 백그라운드로 Celery 실행 및 로그 저장
nohup poetry run celery -A config worker -l info > $CELERY_LOG_FILE 2>&1 &

# Gunicorn 실행 및 로그 저장
exec poetry run gunicorn src.config.wsgi:application --bind 0.0.0.0:8000 > $GUNICORN_LOG_FILE 2>&1