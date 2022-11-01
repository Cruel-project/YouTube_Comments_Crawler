#마지막 아이디 저장
def save_video_id(input):
    f = open("files/video_id.txt", "w")
    f.write(input)
    f.close()
#마지막 아이디 불러오기
def read_last_video_id():
    f = open("files/video_id.txt", "r")
    return (f.read())