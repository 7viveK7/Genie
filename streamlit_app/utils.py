import requests

def call_hiregenius_api(file_path, job_description):
    url = "http://127.0.0.1:8000/upload-resume/"
    with open(file_path, "rb") as f:
        files = {"file": f}
        data = {"job_description": job_description}
        response = requests.post(url, files=files, data=data)
        return response.json()
