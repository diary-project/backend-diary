#!/bin/bash

# 스크립트가 에러 발생 시 종료하도록 설정
set -e

# 변수 선언
IMAGE_NAME="diary-backend"
CONTAINER_NAME="diary-app"

DEFAULT_DJANGO_ENV="local"
DEFAULT_PLATFORM="linux/arm64"

DJANGO_ENV=${1:-$DEFAULT_DJANGO_ENV}
PLATFORM=${2:-$DEFAULT_PLATFORM}

# DJANGO_ENV 값 확인
if [ "$DJANGO_ENV" != "dev" ] && [ "$DJANGO_ENV" != "local" ]; then
  echo "Error: Invalid environment '$DJANGO_ENV'. Please use 'dev' or 'local'."
  exit 1
fi

# 실행 중인 동일한 이름의 컨테이너가 있는지 확인
RUNNING_CONTAINER=$(docker ps -q -f name=$CONTAINER_NAME)
if [ ! -z "$RUNNING_CONTAINER" ]; then
    echo "동일한 이름의 컨테이너($CONTAINER_NAME)가 실행 중입니다. 컨테이너를 중지합니다."
    docker stop $RUNNING_CONTAINER
    docker rm $RUNNING_CONTAINER
    echo "컨테이너 삭제 및 중지 완료."
else
    echo "동일한 이름의 실행 중인 컨테이너가 없습니다."
fi

# Docker 빌드 및 실행
IMAGE_TOTAL_NAME=$IMAGE_NAME:$DJANGO_ENV
echo "Starting build for environment: $DJANGO_ENV with platform: $PLATFORM"
docker build --platform $PLATFORM -t $IMAGE_TOTAL_NAME .

echo "Docker 이미지 빌드 완료: $IMAGE_TOTAL_NAME"
docker run --name $CONTAINER_NAME \
-d -p 8000:8000 \
-e DJANGO_ENV=$DJANGO_ENV \
$IMAGE_TOTAL_NAME