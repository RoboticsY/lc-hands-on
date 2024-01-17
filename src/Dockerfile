FROM python:3.10.5

# アプリケーションディレクトリを作成する
WORKDIR /usr/src/python

# pipのアップデート
RUN pip install --upgrade pip

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

# RUN pip install -U langchain
# RUN pip install -U langchain-community
# RUN pip install -U langchain-openai

# アプリケーションコードをコンテナにコピー
COPY . .
