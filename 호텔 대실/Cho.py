# book_time을 순회
# book_time을 스케쥴링
# Greedy 한 방법 사용하기 -> sort하고 아래 알고리즘 사용
# 1. Room을 순회하면서 시간이 비는지 확인
# 2. 시간을 비는 Room이 있으면 넣음
# 3. 없으면 만들어서 넣음

def convert_time(time):
    h, m = time.split(":")
    new_time = int(h) * 60 + int(m)
    
    return new_time

def solution(book_time):
    new_book_time = []
    for bt in book_time:
        new_book_time.append([convert_time(bt[0]), convert_time(bt[1])])
        
    sorted_new_book_time = sorted(new_book_time, key = lambda x : x[0])
    rooms = [sorted_new_book_time.pop(0)[1]]

    for bt in sorted_new_book_time:
        entering_time = bt[0]
        out_time = bt[1]
        
        for i in range(len(rooms)):
            if rooms[i] + 10 <= entering_time:
                rooms[i] = out_time
                break
            
            if i == len(rooms)-1:
                rooms.append(out_time)
    
    
        
    answer = len(rooms)
    return answer
