import os 
import sys  

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
        
#마지막 아이디 저장
def save_video_id(input):
    f = open(resource_path("./files/video_id.txt"), "w")
    f.write(input)
    f.close()
#마지막 아이디 불러오기
def read_last_video_id():
    f = open(resource_path("./files/video_id.txt"), "r")
    return (f.read())
