# ベースイメージとしてPython 3.9を使用
FROM python:3.9-slim

# コンテナ内での作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
# ここで ping を含む net-tools をインストール
RUN apt-get update && apt-get install -y iputils-ping curl && apt-get clean

# 必要なPythonパッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコンテナにコピー
COPY . /app

# コンテナ内でFastAPIアプリを起動
CMD ["python", "src/main.py"]
