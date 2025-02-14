import yaml

# ログ周りの設定
from fastapi import FastAPI

# 環境変数の設定はここで
ENV = "development"
DATABASE_URL = "hogehoge"

app = FastAPI()

# グローバル例外ハンドラーの登録もここ
# app.add_exception_handler()
# ...

# ルータの追加もここ
# app.include_router()


# ルートパスへのアクセス
@app.get("/")
def hello_world():
    return {"message": "Hello World"}



with open(r"log_config.yaml") as f:
    config = yaml.safe_load(f)

print('test')


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",  # モジュール名:アプリ名
        host="0.0.0.0",
        port=8080,
        reload=True,
        log_config=config,  # ログ設定の読み込み
    )
