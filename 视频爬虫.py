import yt_dlp
import you_get
import os

url = ''

os.chdir("E:/下载/视频")
os.system('youtube-dl --write-sub --sub-lang en -f "bestvideo+bestaudio" -o "%(title)s.%(ext)s" ' + url)
os.system('youtube-dl --write-auto-sub --sub-lang zh-Hans --skip-download -o "%(title)s.%(ext)s" ' + url)
os.chdir("../")

# 无字幕 腾讯 会员视频 MP4
os.system("yt-dlp --merge-output-format 'mp4' --external-downloader 'aria2c' --cookies-from-browser edge --downloader-args aria2c:'-x 16 -k 1M' ")
# 无字幕 油管 频道全视频 MP4 频道+标题
os.system("yt-dlp -f 'bv+ba' --merge-output-format 'mp4' -o '%(channel)s/%(title)s.%(ext)s' --external-downloader aria2c --downloader-args aria2c:'-x 16 -k 1M' ")

os.system("yt-dlp -f 'bv+ba' --merge-output-format 'mp4' -o '%(channel)s/%(title)s.%(ext)s' --external-downloader aria2c --downloader-args aria2c:'-x 16 -k 1M' ")

# 中文,英语,英语(美),日语字幕 油管 MKV
os.system("yt-dlp -f 'bv+ba' --embed-subs --sub-langs 'zh.*,en.*,jp,fr,de,ko' --merge-output-format 'mkv' --downloader-args aria2c:'-x 16 -k 1M' ")

os.system("yt-dlp -f 'bv+ba' --embed-subs --sub-langs 'zh.*,en.*,jp,fr,de,ko' --embed-thumbnail --embed-metadata --merge-output-format 'mkv' --external-downloader aria2c  --downloader-args aria2c:'-x 16 -k 1M ' https://www.youtube.com/watch?v=8lUgdf-zkQMM")

os.system("yt-dlp -f 'bv+ba' --embed-thumbnail --embed-metadata --merge-output-format 'mp4' --external-downloader aria2c  --downloader-args aria2c:'-x 16 -k 1M' https://www.bilibili.com/video/BV11K411o7Gd/")

os.system("yt-dlp -f 'bv+ba' --embed-subs --sub-langs 'zh.*,en.*,ja' --embed-thumbnail --embed-metadata --merge-output-format 'mkv' --external-downloader aria2c  --downloader-args aria2c:'-x 16 -k 1M' https://www.youtube.com/watch?v=e1xCOsgWG0M")