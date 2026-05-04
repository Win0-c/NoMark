import requests
import os
import time
from colorama import init
from pystyle import Colorate, Colors, Center

os.system("title NoMark")

init(autoreset=True)

BANNER = """
 _____ _     _____         _    
|   | | |___|     |___ ___| |_  
| | | | | . | | | | .'|  _| '_| 
|_|___|_|___|_|_|_|__,|_| |_,_| 
"""

INFO = """\
  VERSION : 1.0
  CREATOR : Win.c
  LANGUAGE: Python
"""

def print_banner():
    centered_banner = Center.XCenter(BANNER)
    print(Colorate.Horizontal(Colors.red_to_white, centered_banner))
    print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(INFO)))

def gradient_input(prompt):
    colored_prompt = Colorate.Horizontal(Colors.white_to_red, prompt)
    return input(colored_prompt)

def download_tiktok_no_watermark():
    print_banner()
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    url = gradient_input(" Enter TikTok video URL: ")
    api_url = f"https://www.tikwm.com/api/?url={url}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        if "data" in data and "play" in data["data"]:
            video_url = data["data"]["play"]
            video_content = requests.get(video_url).content
            with open("tiktok_no_watermark.mp4", "wb") as f:
                f.write(video_content)
            print(Colorate.Horizontal(Colors.green_to_white, " Download complete: tiktok_no_watermark.mp4"))
            time.sleep(3)
        else:
            print(Colorate.Horizontal(Colors.red_to_orange, " Could not find video URL"))
            time.sleep(3)
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f" Error: {e}"))
        time.sleep(3)

if __name__ == "__main__":
    download_tiktok_no_watermark()
