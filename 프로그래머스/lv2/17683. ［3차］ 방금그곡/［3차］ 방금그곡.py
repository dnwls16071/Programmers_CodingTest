# 각 음은 1분에 1개씩 재생된다.
# 따라서, #이 붙은 음은 하나의 음으로 바꿔주어야한다.
def getMusic(music):
    musicDic = {'C#':'c','D#':'d','F#':'f', 'G#':'g', 'A#':'a'}
    for m in musicDic:
        if m in music:
            music = music.replace(m,musicDic[m])
    return music


def solution(m, musicinfos):
    m = m.replace("A#", 'a')
    m = m.replace("C#", 'c')
    m = m.replace("D#", 'd')
    m = m.replace("F#", 'f')
    m = m.replace("G#", 'g')
    answer = []
    dic = {"A#" : 'a', "C#" : 'c', "D#" : 'd', "F#" : 'f', "G#" : 'g'}
    idx = 0
    for info in musicinfos:
        info = info.split(",")
        music_start = info[0]                   # 음악 재생시간
        music_start = music_start.split(":")
        music_start_hour, music_start_minute = music_start[0], music_start[1]        # 음악 재생시간 - 시간, 음악 재생시간 - 분
        music_end = info[1]                     # 음악 종료시간
        music_end = music_end.split(":")        
        music_end_hour, music_end_minute = music_end[0], music_end[1]                # 음악 종료시간 - 시간, 음악 종료시간 - 분
        music_title = info[2]                   # 음악 제목
        music_melody = info[3]                  # 음악 멜로디
        music_melody = getMusic(music_melody)   # 멜로디에 #이 들어있는경우 getMusic 함수로 변환을 수행
        # 음악 재생시간(음악 종료시간 - 음악 시작시간)
        play_time = (int(music_end_hour) - int(music_start_hour)) * 60 + (int(music_end_minute) - int(music_start_minute))
        # python 내장함수 divmod를 이용해서 몫과 나머지를 구함
        quotient, remain = divmod(play_time, len(music_melody))
        
        # 음악 길이보다 재생된 시간이 짧은 경우 → 처음부터 재생 시간만큼만 재생된다.(나머지까지 슬라이싱 처리)
        if len(music_melody) > play_time:
            music_melody = music_melody[:remain]
        # 음악 길이보다 재생된 시간이 긴 경우 → 몫만큼 곰하고 나머지만큼 추가
        else:
            music_melody = music_melody * quotient + music_melody[:remain]
        
        # m이 음악 멜로디 안에 들어있는경우
        if m in music_melody:
            answer.append([idx, play_time, music_title])
        idx += 1
    
    if len(answer) == 0:
        return "(None)"
    else:
        # answer 다중 정렬
        # 1순위 : 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다.
        # 2순위 : 재생된 시간도 같은 경우 먼저 입력된 음악 제목을 반환한다.(idx의 용도)
        answer = sorted(answer, key = lambda x : (-x[1], x[0]))
        return answer[0][2]