FROM golang:1.23.3-bookworm

ARG UID=1000
ARG GID=1000

# 一般ユーザの作成
RUN groupadd -g ${GID} app && \
    useradd -m -s /bin/bash -g app app

# OS パッケージのインストール
RUN apt-get update && apt-get install -y \
        less \
        locales \
        vim \
        zip && \
    rm -rf /var/lib/apt/lists/*

# 日本語フォントの設定
RUN sed -ri -e "s/^# ja_JP.UTF-8/ja_JP.UTF-8/g" /etc/locale.gen && \
    locale-gen && \
    update-locale LANG=ja_JP.UTF-8 && \
    echo 'export LANG=ja_JP.utf8' >> ~/.bashrc

# aws-lambda-rie インストール
RUN curl -Lo /usr/local/bin/aws-lambda-rie https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie && \
    chmod +x /usr/local/bin/aws-lambda-rie

WORKDIR /workspaces
USER app

# デバックに必要な golang パッケージのインストール
RUN go install golang.org/x/tools/gopls@latest && \
    go install github.com/go-delve/delve/cmd/dlv@latest

# 日本語フォントの設定(app ユーザ)
RUN echo 'export LANG=ja_JP.utf8' >> ~/.bashrc
