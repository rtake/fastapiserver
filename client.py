import requests

# ファイルのパス
file_path = "test.csv"
question = "What is the 10th fibonacci number?"

# FastAPIエンドポイントのURL
url = "http://127.0.0.1:8000/uploadfile/"

# ファイルを開いてrequestsを使用して送信
with open(file_path, "rb") as file:
    files = {"form_file": (file.name, file, "text/csv")}
    data = {"question": question}
    response = requests.post(url, files=files, data=data)

# レスポンスの表示
if response.status_code == 200:
    result = response.json()
    print("Response received successfully:")
    print(result)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
