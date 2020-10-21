import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        HEADERS = {"Authorization": f"OAuth {self.token}"}
        response = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            headers=HEADERS,
            params={"path": file_path, "overwrite": "True"},
        )
        if response.status_code != 200:
            raise Exception(
                f"Ответ API не соответствует ожидаемому. Код: {response.status_code}"
            )
        result = response.json()["href"]
        with open("file.txt", "rb") as f:
            response = requests.put(result, files={"file": f})
        return f"Файл загружен на яндекс диск! Код: {response.status_code}"


if __name__ == "__main__":
    uploader = YaUploader("here some token")
    result = uploader.upload("here name filet.txt")
first_upload = YaUploader("here some token")
result = first_upload.upload("here name file.txt")
print(result)
