# 1. 기본 Python 이미지를 지정합니다.
FROM python:3.12-slim

# 2. 필수 패키지를 설치합니다.
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    python3-openssl \
    default-libmysqlclient-dev \
    libmariadb-dev-compat \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# 3. pyenv 설치
RUN curl https://pyenv.run | bash

# 4. pyenv 환경 설정
ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"

# 5. pyenv-virtualenv 설치
RUN rm -rf ~/.pyenv/plugins/pyenv-virtualenv
RUN git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
RUN echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc
RUN echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# 6. 프로젝트에 설정된 Python 버전 설치 및 가상 환경 생성
RUN /bin/bash -c "source ~/.bashrc && pyenv install 3.12.5 && pyenv virtualenv 3.12.5 diary_backend"

# 7. 가상 환경 활성화 및 사용 설정
RUN echo 'pyenv activate diary_backend' >> ~/.bashrc

# 8. Poetry 설치
RUN curl -sSL https://install.python-poetry.org | python3 -

# 9. Poetry 환경 설정
ENV PATH="/root/.local/bin:$PATH"

# 10. 프로젝트 소스를 컨테이너에 복사합니다.
WORKDIR /app
COPY . /app

# 11. Poetry를 사용하여 패키지 설치
RUN /bin/bash -c "source ~/.bashrc && pyenv activate diary_backend && poetry install --no-root"

# 12. 가상 환경을 활성화한 상태로 Django 서버 실행
CMD ["bash", "-c", "source ~/.bashrc && pyenv activate diary_backend && poetry run python src/manage.py runserver 0.0.0.0:8000"]