# ベースイメージとしてPython 3.9を使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なシステムパッケージをインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    graphviz \
    libgl1-mesa-glx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ファイルをコピー
COPY simulator.ipynb \
    remote.ipynb \
    requirements.txt \
    commonLogic.py \
    img/ \
    /app/

# //ーーーーーーーーーーーーーーーーーーーーー
# pipをアップグレード
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# //ーーーーーーーーーーーーーーーーーーーーー
# Jupyter Notebookを起動するコマンドを指定
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]


