<div align="center">
```
 _____ _     _____         _    
|   | | |___|     |___ ___| |_  
| | | | | . | | | | .'|  _| '_| 
|_|___|_|___|_|_|_|__,|_| |_,_| 
```
Download TikTok videos without a watermark — straight from your terminal.
![Version](https://img.shields.io/badge/version-1.0-red?style=flat-square)
![Python](https://img.shields.io/badge/python-3.8+-red?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-red?style=flat-square)
</div>
---
#Overview
NoMark is a Python terminal tool that pulls TikTok videos without the watermark using the tikwm.com API. Run it, paste a URL, get a clean MP4.
---
#Requirements
Python 3.8+
`requests`
`colorama`
`pystyle`
Install dependencies:
```bash
pip install requests colorama pystyle
```
---
#Usage
```bash
python nomark.py
```
You'll see the banner, then paste your TikTok URL when prompted. The video saves as `tiktok_no_watermark.mp4` in the same directory.
---
#How it works
NoMark sends your URL to the tikwm.com API, grabs the direct video link from the response, and writes the raw bytes to disk. No browser. No login. No watermark.
---
#Notes
Output is always saved as `tiktok_no_watermark.mp4` — rename it after if you need
Only works on public videos
If a download fails, double check the URL is valid and the video is publicly accessible
---
#Credits
```
VERSION : 1.0
CREATOR : Win.c
LANGUAGE: Python
```
---
Legal
For personal use only. Downloading TikTok content may violate TikTok's Terms of Service. Don't redistribute or monetize content you download with this tool.
