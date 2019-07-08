import requests

headers={
    "User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language" : "en-us",
    "Connection" : "keep-alive",
    "Accept-Charset" : "GB2312,utf-8;q=0.7,*;q=0.7"
}

html = requests.get("https://www.google.com", headers=headers, timeout=5)
with open("./src/tmp/test.html", 'w+', encoding="utf-8") as file:
    file.write(html.text)