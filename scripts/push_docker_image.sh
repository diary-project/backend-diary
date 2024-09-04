
# 변수 선언
DOCKER_USER="geuttaen"
DOCKER_PASSWORD="gdA96vCj59nKv5#"

IMAGE_NAME="diary-backend"
DEFAULT_PLATFORM="linux/amd64"
DEFAULT_DJANGO_ENV="dev"

DJANGO_ENV=${1:-$DEFAULT_DJANGO_ENV}  # 첫 번째 인자: dev 또는 prod 환경 (기본값: dev)
PLATFORM=${2:-$DEFAULT_PLATFORM}  # 두 번째 인자: 플랫폼 (기본값: linux/arm64)
TAG_NAME=${DJANGO_ENV}  # 태그는 환경 이름만 사용
TAG_TOTAL_NAME="$IMAGE_NAME:$TAG_NAME"

# 로그인 확인
echo "Docker Hub에 로그인합니다."
docker logout
echo $DOCKER_PASSWORD | docker login -u $DOCKER_USER --password-stdin

# 이미지가 존재하는지 확인
#EXISTING_IMAGE=$(docker images -q $IMAGE_TOTAL_NAME 2> /dev/null)

echo "Docker 빌드를 시작합니다: $IMAGE_NAME"
docker build --platform $PLATFORM -t $IMAGE_NAME .
echo "Docker 빌드 완료: $IMAGE_NAME"


#if [ -n "$EXISTING_IMAGE" ]; then
#  echo "Docker 이미지가 존재합니다: $IMAGE_TOTAL_NAME"
#else
#  echo "이미지가 존재하지 않습니다. Docker 빌드를 시작합니다: $IMAGE_TOTAL_NAME"
#  docker build --platform $PLATFORM -t $IMAGE_TOTAL_NAME .
#  echo "Docker 빌드 완료: $IMAGE_TOTAL_NAME"
#fi

docker tag $IMAGE_NAME $DOCKER_USER/$TAG_TOTAL_NAME
echo "추가 태그 완료: $DOCKER_USER/$TAG_TOTAL_NAME"

# Docker 이미지를 push
echo "Docker 이미지를 push합니다: $DOCKER_USER/$TAG_TOTAL_NAME"
docker push $DOCKER_USER/$TAG_TOTAL_NAME

echo "Docker push가 완료되었습니다: $DOCKER_USER/$TAG_TOTAL_NAME"