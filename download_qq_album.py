import os
import requests
import json
from config import COOKIES, QQ_NUMBER

headers = {
    "cookie": COOKIES,
    "user-agent": "Mozilla/5.0"
}

def get_g_tk(p_skey):
    hash = 5381
    for c in p_skey:
        hash += (hash << 5) + ord(c)
    return hash & 0x7fffffff

def fetch_photo_list():
    uin = QQ_NUMBER
    p_skey = ""
    for kv in COOKIES.split(";"):
        if "p_skey" in kv:
            p_skey = kv.split("=")[-1].strip()
    gtk = get_g_tk(p_skey)

    url = f"https://user.qzone.qq.com/proxy/domain/photo.qzone.qq.com/fcg-bin/cgi_list_photo?g_tk={gtk}&uin={uin}&albumid=&callback=shine0_Callback&plat=qzone&outtype=json&source=qzone"

    res = requests.get(url, headers=headers)
    if "shine0_Callback" in res.text:
        json_str = res.text.replace("shine0_Callback(", "")[:-1]
        data = json.loads(json_str)
        return data.get("data", {}).get("photoList", [])
    else:
        print("⚠️ 无法访问相册，请检查 Cookie 是否过期或账号权限")
        return []

def download_photos(photo_list):
    os.makedirs("photos", exist_ok=True)
    count = 0
    for photo in photo_list:
        url = photo.get("url", "")
        if not url:
            continue
        try:
            img_data = requests.get(url).content
            with open(f"photos/photo_{count}.jpg", "wb") as f:
                f.write(img_data)
            print(f"✅ 下载第 {count+1} 张图片")
            count += 1
        except:
            print(f"❌ 下载失败: {url}")
        if count >= 50:
            break

def zip_photos():
    from zipfile import ZipFile
    with ZipFile("qq_album.zip", "w") as zipf:
        for root, _, files in os.walk("photos"):
            for file in files:
                full_path = os.path.join(root, file)
                zipf.write(full_path, os.path.relpath(full_path, "photos"))
    print("📦 相册已打包为 qq_album.zip")

if __name__ == "__main__":
    print("📥 正在获取相册列表...")
    photo_list = fetch_photo_list()
    if photo_list:
        download_photos(photo_list)
        zip_photos()
