import pytest
import requests
import base64


@pytest.fixture
def pdf_file():
    with open("CV.pdf", "rb") as f:
        yield f.read()


def test_parse_pdf_with_file(pdf_file):
    url = "http://127.0.0.1:8000/parse-pdf-file/"
    response = requests.post(url, files={"file": ("CV.pdf", pdf_file, "application/pdf")})

    print(response.json())
    assert response.status_code == 200


def test_parse_pdf_with_base64(pdf_file):
    url = "http://127.0.0.1:8000/parse-pdf-base64/"
    base64_pdf = base64.b64encode(pdf_file).decode("utf-8")
    response = requests.post(url, json={"base64_pdf": base64_pdf})

    print(response.json())
    assert response.status_code == 200
