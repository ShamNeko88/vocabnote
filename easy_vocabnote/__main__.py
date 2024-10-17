import os
import sqlite3 as s3

# データベース接続
db = s3.connect("./data/test_db.db")
cur = db.cursor()

# アプリケーション開始メッセージ
print("===========================================")
print("========= ようこそ！vocabnoteへ！ =========")
print("===========================================")
print("")  # 改行

# 「一度操作が終わればメニューを表示」を繰り返す。
while True:
    print("▼▼▼▼▼▼▼▼ メニュー ▼▼▼▼▼▼▼▼")
    print(" 1. 単語帳で学習")
    print(" 2. 単語の新規登録")
    print(" 3. 単語の削除")
    print(" 4. 単語の一覧表示")
    print("99. アプリケーションを終了する")

    # 操作を選択する為に数字の入力を求める
    print("")  # 改行
    number = input("半角で数字を入力してください >>> ")

    # 学習の開始 ==========================================
    if number == "1":
        input("学習の開始")

    # 単語の新規登録
    elif number == "2":
        new_word = input("単語を入力してください >>> ")
        description = input("説明を入力してください >>> ")
        sql = f"""
            INSERT INTO words(word, description)
            VALUES('{new_word}', '{description}');
        """
        cur.execute(sql)  # sqlの実行
        db.commit()  # コミット

    # 単語の削除
    elif number == "3":
        pass

    # 単語の一覧表示
    elif number == "4":
        pass

    # アプリケーションを終了する
    elif number == "99":
        input("アプリケーションを終了します！！何かキー入力してください！！")
        break

    # 何度も処理を回すと見づらいので対策をとる
    print("\n" * 30)  # 下の処理でクリアできなかった時の為改行入れる
    os.system("cls")  # 画面クリア
