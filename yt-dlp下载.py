import yt_dlp
import you_get
import os

url = ''

#  $Env:http_proxy="http://127.0.0.1:3030";$Env:https_proxy="http://127.0.0.1:3030"

os.chdir("E:/下载/视频")
os.system('youtube-dl --write-sub --sub-lang en -f "bestvideo+bestaudio" -o "%(title)s.%(ext)s" ' + url)
os.system('youtube-dl --write-auto-sub --sub-lang zh-Hans --skip-download -o "%(title)s.%(ext)s" ' + url)
os.chdir("../")

# 无字幕 腾讯 会员视频 MP4
os.system("yt-dlp --merge-output-format 'mp4' --external-downloader 'aria2c' --cookies-from-browser edge --downloader-args aria2c:'-x 16 -k 1M' --embed-thumbnail --embed-metadata")
# 无字幕 油管 频道全视频 MP4 频道+标题
os.system("yt-dlp -f 'bv+ba' --merge-output-format 'mp4' -o '%(channel)s/%(title)s.%(ext)s' --external-downloader aria2c --downloader-args aria2c:'-x 16 -k 1M' ")

# 油管频道 有存档 MP4
os.system("yt-dlp -f 'bv+ba' --merge-output-format 'mp4' -o '%(channel)s/%(title)s.%(ext)s' --external-downloader aria2c --downloader-args aria2c:'-x 16 -k 1M' --download-archive './%(channel)s/archive.txt'")
# 油管音频 元数据 封面 FLAC
os.system("yt-dlp -f 'ba' --external-downloader aria2c --downloader-args aria2c:'-x 16 -k 1M' -o '%(title)s.%(ext)s' --recode-video 'mp3' --embed-thumbnail --embed-metadata")
# 中文,英语,英语(美),日语字幕 油管 MKV
os.system("yt-dlp -f 'bv+ba' --embed-subs --sub-langs 'zh.*,en.*,ja' --merge-output-format 'mkv' --external-downloader aria2c --downloader-args aria2c:'-x 16 -k 1M' -o '%(title)s.%(ext)s'")

os.system("yt-dlp -f 'bv+ba' --embed-subs --sub-langs 'zh.*,en.*,ja' --embed-thumbnail --embed-metadata --merge-output-format 'mkv' --external-downloader aria2c  --downloader-args aria2c:'-x 16 -k 1M ' https://www.youtube.com/watch?v=8lUgdf-zkQMM")
# 中文,英语,日语字幕 vtt-->srt 油管 mkv 有存档
os.system("yt-dlp -f 'bv+ba' --embed-subs --sub-langs 'zh.*,en.*,ja' --merge-output-format 'mkv' --downloader-args aria2c:'-x 16 -k 1M' --write-auto-subs  -o '%(title)s.%(ext)s'  --download-archive 'archive.txt' --sub-format vtt --convert-subs srt https://www.youtube.com/watch?v=XZSYv_aG3J4")
# 无字幕 油管 MP4 有存档
os.system("yt-dlp -f 'bv+ba' --merge-output-format 'mp4' --downloader-args aria2c:'-x 16 -k 1M' -o '%(title)s.%(ext)s'  --download-archive 'archive.txt' https://www.youtube.com/watch?v=qvJ8uJLEDzY")
# 油管 封面 元数据 MP4
os.system("yt-dlp -f 'bv+ba' --embed-thumbnail --embed-metadata --merge-output-format 'mp4' --external-downloader aria2c  --downloader-args aria2c:'-x 16 -k 1M' https://www.bilibili.com/video/BV11K411o7Gd/")

os.system("yt-dlp -f 'bv+ba' --embed-subs --sub-langs 'zh.*,en.*,ja' --embed-thumbnail --embed-metadata --merge-output-format 'mkv' --external-downloader aria2c  --downloader-args aria2c:'-x 16 -k 1M' https://www.youtube.com/watch?v=e1xCOsgWG0M")

os.system("yt-dlp https://www.youtube.com/watch?v=AfE3dq-cpLU -f 'bv+ba' --merge-output-format 'mp4'  --external-downloader 'aria2c' -o '%(title)s.%(ext)s' --downloader-args aria2c:'-x 16 -k 1M' --download-archive './%(channel)s/archive.txt'")

# 推特视频下载 MP4
os.system("yt-dlp -o '%(title)s.%(ext)s' --external-downloader aria2c --downloader-args aria2c:'-x 16 -k 1M' --merge-output-format 'mp4' --cookies-from-browser edge https://twitter.com/i/status/1621833713360281600") 

# B站视频列表 有存档 读cookie
os.system("yt-dlp -f 'bv+ba' --merge-output-format 'mp4' -o '%(title)s.%(ext)s' --external-downloader aria2c --downloader-args aria2c:'-x 16 -k 1M' --download-archive 'archive.txt' --embed-thumbnail --embed-metadata --cookies-from-browser edge https://space.bilibili.com/172085/channel/collectiondetail?sid=1023078")

# ffmpeg命令 mp4转码HEVC 保留字幕
os.system("ffmpeg -i input.mp4 -c:v hevc_nvenc -c:s copy -crf 18 -preset slow output.mp4","-c:v h264_nvenc -b:a 256k -b:v 3000k")

# 油管视频 封面 元数据 字幕 MP4
os.system("yt-dlp -f 'bv+ba' -o '%(title)s.%(ext)s' --external-downloader aria2c --downloader-args aria2c:'-x 16 -k 1M' --embed-subs --sub-langs 'zh.*,en.*,ja.*' --merge-output-format 'mp4'  --embed-thumbnail --embed-metadata https://www.youtube.com/watch?v=QIFzmD_9GBw")

# twitch直播回放下载 
# yt-dlp -o '%(title)s.%(ext)s' --external-downloader aria2c --downloader-args aria2c:'-x 16 -k 1M' --embed-subs --sub-langs 'zh.*,en.*,ja.*' --merge-output-format 'mp4'  --embed-thumbnail --embed-metadata --cookies-from-browser chrome https://www.twitch.tv/videos/1825868435 

# 油管1080P AAC+AVC
140+137

# yt-dlp -f '140+137' -o '%(title)s.%(ext)s' --external-downloader aria2c --downloader-args aria2c:'-x 16 -k 1M' --embed-subs --sub-langs 'zh.*,en.*,ja.*' --merge-output-format 'mp4'  --embed-thumbnail --embed-metadata --convert-subs srt --write-auto-subs

# xvideo批量下载 有存档 读cookie MP4
# yt-dlp -o '%(title)s.%(ext)s' --external-downloader aria2c --downloader-args aria2c:'-x 16 -k 1M' --embed-subs --sub-langs 'zh.*,en.*,ja.*' --merge-output-format 'mp4'  --embed-thumbnail --embed-metadata --download-archive 'archive.txt' -a 'urls.txt' --cookies-from-browser chrome

# yt-dlp -f 'ba+bv' -o '%(title)s.%(ext)s' --external-downloader aria2c --downloader-args aria2c:'-x 16 -k 1M' --embed-subs --sub-langs 'zh.*,en.*,ja.*' --merge-output-format 'mp4'  --embed-thumbnail --embed-metadata  --cookies-from-browser edge --sub-format ttml --convert-subs ass --write-subs https://www.youtube.com/watch?v=KfZR9jVP6tw