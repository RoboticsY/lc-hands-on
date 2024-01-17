# lc-hands-on

## 概要

生成AI基礎講座の LangChain ハンズオン用リポジトリです。

## ハンズオンの流れ

### 1. リポジトリのクローン

```bash
$ git clone https://github.com/RoboticsY/lc-hands-on.git
```

### 2. .env ファイルの作成

プロジェクトルートに `.env` ファイルを作成し、以下の内容を記述します。

```
OPENAI_API_KEY=xxxxxxxxxxx
```

API キーの値を配布された API キーに置き換えてください。

### 3. 実行

```bash
$ docker compose up --build
```