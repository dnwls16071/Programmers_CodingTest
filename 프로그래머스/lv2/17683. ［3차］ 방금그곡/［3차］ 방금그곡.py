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
        music_start = info[0]
        music_start = music_start.split(":")
        music_start_hour = music_start[0]
        music_start_minute = music_start[1]
        music_end = info[1]
        music_end = music_end.split(":")
        music_end_hour = music_end[0]
        music_end_minute = music_end[1]
        music_title = info[2]
        music_melody = info[3]
        music_melody = getMusic(music_melody)
        play_time = (int(music_end_hour) - int(music_start_hour)) * 60 + (int(music_end_minute) - int(music_start_minute))
        quotient, remain = divmod(play_time, len(music_melody))
        
        # 음악 길이보다 재생된 시간이 짧은 경우 → 처음부터 재생 시간만큼만 재생된다.
        if len(music_melody) > play_time:
            music_melody = music_melody[:remain]
        else:
            music_melody = music_melody * quotient + music_melody[:remain]
        
        if m in music_melody:
            answer.append([idx, play_time, music_title])
        idx += 1
    
    if len(answer) == 0:
        return "(None)"
    else:
        answer = sorted(answer, key = lambda x : (-x[1], x[0]))
        return answer[0][2]