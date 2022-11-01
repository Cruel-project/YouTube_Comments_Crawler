import scraper
import file_witer
  
sr = scraper  
fl = file_witer

video_id = input()
last_video_id = fl.read_last_video_id()

print("영상 아이디를 입력하거나, Enter를 눌러서 마지막 아이디로 진행")
if video_id != "":
    sr.get_comments(video_id)
else:
    print("영상 아이디가 누락되어있습니다.")
    print("마지막에 사용된 아이디를 사용합니다.")
    print("파일명: " + fl.read_last_video_id())
    sr.get_comments(last_video_id)