import requests

output_file = "D:\\Python Projects\\Advanced\\Multi-Threaded File Downloader\\downloads\\downloaded_file.pdf"


def download(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"File downloaded successfully and saved to {output_file}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")


download("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf")
