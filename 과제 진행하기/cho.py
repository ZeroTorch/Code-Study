# 과제를 끝낸 시간에 진행하던 과제가 있으면 과제 진행하기
# 과제를 하던 도중에 새로운 과제가 들어오면 새로운 과제를 진행
    # 하던 과제를 진행한만큼 저장해놓기
    # 최근에 멈춘 과제부터 진행해야 하므로 stack 구조를 사용
def convert_time(time):
    h, m = time.split(":")
    new_time = int(h) * 60 + int(m)
    
    return new_time

def convert_plan(plan):
    name, start, playtime = plan
    new_time = convert_time(start)
    
    return [name, new_time, int(playtime)]
    
def solution(plans):
    plans = list(map(convert_plan, plans))
    plans = sorted(plans, key = lambda x:x[1])
    print(plans)
    task = []
    answer = []
    
    for plan in plans:
        # 새로 들어오는 일과 진행하던 task 사이 처리
        while(task):
            cur_task = task.pop(-1)
            name, start, playtime = cur_task

            # 일이 끝나지 않았으면
            if start+playtime > plan[1]:
                remain = (start+ playtime) -plan[1]
                new_schedule = plan[1] + plan[2]
                task.append([name, new_schedule, remain])
                
                # 스케쥴링 다시 해줌
                for i in range(len(task)-2, -1, -1):
                    new_schedule = task[i+1][1] + task[i+1][2]
                    task[i][1] = new_schedule
                break
            # 일이 끝났으면 answer에 넣어줌
            else :
                answer.append(name)
        
        # 새로운 일 task에 넣기
        task.append(plan)
    
    # 남은 일 순서대로 처리
    while(task):
        answer.append(task.pop()[0])

    return answer
