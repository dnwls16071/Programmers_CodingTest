def solution(keyinput, board):
    # [x좌표 값, y좌표 값]
    answer = [0, 0]
    
    width = board[0]
    height = board[1]
    minus_height = (-height // 2) + 1   # y축 음의 방향
    plus_height = (height // 2)         # y축 양의 방향
    minus_width = (-width // 2) + 1     # x축 음의 방향
    plus_width = (width // 2)           # x축 양의 방향
    for direction in keyinput:
        temp_x, temp_y = answer[0], answer[1]
        
        if direction == "left":
            temp_x -= 1
        elif direction == "right":
            temp_x += 1
        elif direction == "up":
            temp_y += 1
        elif direction == "down":
            temp_y -= 1
        
        # 새로 이동한 좌표가 영역 내에서 움직일 수 있는 경우에만 반영함
        if minus_width <= temp_x <= plus_width and minus_height <= temp_y <= plus_height:
            answer[0] = temp_x
            answer[1] = temp_y
    return answer