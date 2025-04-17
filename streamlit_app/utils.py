import requests

def call_hiregenius_api(file_path, job_description):
    url = "https://genie-5hgp.onrender.com/upload-resume/"
    with open(file_path, "rb") as f:
        files = {"file": f}
        data = {"job_description": job_description}
        response = requests.post(url, files=files, data=data)
        return response.json()
