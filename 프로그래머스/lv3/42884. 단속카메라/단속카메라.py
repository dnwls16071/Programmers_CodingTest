def solution(routes):
    routes = sorted(routes, key=lambda x : x[1])    # 고속도로에서 나가는 시점을 기준으로 오름차순 정렬
    answer = 0
    camera = -30001

    for route in routes:
        if route[0] > camera:
            camera = route[1]
            answer += 1
    return answer

# 과정 설명
# 초기 CCTV의 위치는 -30001에 있다고 선언
# -15지점에서 첫 번째 차량이 고속도로에서 나가는 경우 : CCTV가 -15지점에 설치되어있어야함
# -18지점에서 두 번째 차량이 나가는데 이는 -15지점에 설치된 CCTV가 있으므로 촬영이 가능함
# -14지점에서 세 번째 차량이 들어오는데 -15지점에 있는 CCTV로 촬영할 수 없으므로 세 번째 차량이 나가는 시점인 -5지점에 CCTV를 설치함
# -5지점에서 네 번째 차량이 들어오는데 -5지점에 CCTV가 설치되어있으므로 촬영이 가능함 → 따라서, 필요한 최소 CCTV의 개수는 2개