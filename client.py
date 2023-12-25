import requests

# ファイルのパス
file_path = "test.csv"
user_input_text = "このデータについてわかることを分析して"

# FastAPIエンドポイントのURL
url = "http://127.0.0.1:8000/uploadfile/"

# ファイルを開いてrequestsを使用して送信
with open(file_path, "rb") as file:
    files = {"form_file": (file.name, file, "text/csv")}
    data = {"user_input_text": user_input_text}
    response = requests.post(url, files=files, data=data)

# レスポンスの表示
if response.status_code == 200:
    result = response.json()
    print("Response received successfully:")
    print(result)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
