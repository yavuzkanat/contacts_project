import base64
import glob
import json
import os

import instaloader
import requests

# URL Imgbb API
key_imgbb = "ef73bee1eca392d765d403bd825b49ab"
imgbb_url = "https://api.imgbb.com/1/upload"


def instadownloader(profile_name):
    obj = instaloader.Instaloader()
    obj.download_profile(profile_name, profile_pic_only=True)
    user_path = os.getcwd() + f"/{profile_name}"
    file_path = glob.glob(f"{user_path}/*.jpg")[0]
    img_url = ""
    with open(file_path, "rb") as file:
        payload = {
            "key": key_imgbb,
            "image": base64.b64encode(file.read()),
        }
        r = requests.post(imgbb_url, payload)
        img_url = json.loads(r.text)["data"]["display_url"]
    return img_url
