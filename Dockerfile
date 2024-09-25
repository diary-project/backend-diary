# 1. 기본 Python 이미지를 지정합니다.
FROM python:3.12-slim

# 2. 환경 변수 설정
ENV VIRTUAL_ENV_NAME="diary_backend"
ENV PYTHONPATH="/app/src"
ENV PYTHON_VERSION="3.12.5"

# 3. 필수 패키지를 설치합니다.
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

# 4. pyenv 설치
RUN curl https://pyenv.run | bash

# 5. pyenv 환경 설정
ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"

# 6. pyenv-virtualenv 설치
RUN rm -rf ~/.pyenv/plugins/pyenv-virtualenv
RUN git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
RUN echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc
RUN echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# 7. 프로젝트에 설정된 Python 버전 설치 및 가상 환경 생성
RUN /bin/bash -c "source ~/.bashrc && pyenv install $PYTHON_VERSION && pyenv virtualenv $PYTHON_VERSION $VIRTUAL_ENV_NAME"

# 8. 가상 환경 활성화 및 사용 설정
RUN echo "pyenv activate $VIRTUAL_ENV_NAME" >> ~/.bashrc

# 9. Poetry 설치
RUN curl -sSL https://install.python-poetry.org | python3 -

# 10. Poetry 환경 설정
ENV PATH="/root/.local/bin:$PATH"

# 11. 프로젝트 파일 복사 및 의존성 설치
WORKDIR /app
COPY pyproject.toml /app/pyproject.toml
COPY poetry.lock /app/poetry.lock
RUN /bin/bash -c "source ~/.bashrc && pyenv activate $VIRTUAL_ENV_NAME && poetry install --no-root"

# 12. 프로젝트 소스 코드 복사
COPY . /app

# 13. ENTRYPOINT 설정
RUN chmod +x ./scripts/start_app.sh
RUN /bin/bash -c "source ~/.bashrc && pyenv activate $VIRTUAL_ENV_NAME && poetry install --no-root"
ENTRYPOINT ["/bin/bash", "./scripts/start_app.sh"]

# 14. Gunicorn이 8000 포트에서 수신하도록 EXPOSE
EXPOSE 8000