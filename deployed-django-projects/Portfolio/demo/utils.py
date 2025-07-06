from moviepy import VideoFileClip
from django.core.files import File

def generate_thumbnail(video_path):
    try:
        clip = VideoFileClip(video_path)
        thumbnail_path = video_path.replace('.mp4', '.jpg')
        clip.save_frame(thumbnail_path, t=1.00)  # 取影片第 1 秒的畫面
        return File(open(thumbnail_path, 'rb'))
    except Exception as e:
        print(f"生成縮圖時發生錯誤: {e}")
        return None