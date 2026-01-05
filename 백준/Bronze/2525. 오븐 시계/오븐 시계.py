
now = input()        # 현재시간
turnaround = input() # 소요시간

def cooking_completion_time(now, turnaround):
    hour, minute = now.split(" ")
    hour = int(hour)
    minute = int(minute)
    turnaround = int(turnaround)

    # 현재 시간에서 걸리는 시간을 더해준다. 
    # 분단위이므로 시간 / 분 으로 변경해준 뒤 각각 더해준다.
    # 1. minute + turnaround_time > 59 라면 
    #       1.1 hour += (minute + turnaround_itme) % 60     # 몫
    #       1.2 minute = (minute + turnaround_itme) / 60    # 나머지
    #       1.3 만약 hour가 23이라면 더한 값 - 23
    # 
    # 2. 그 외는 
    #       2.1 minute += turnaround_time
    if minute + turnaround > 59:
        hour += (minute + turnaround) // 60
        minute = (minute + turnaround) % 60 
        if hour > 23:
            hour -= 24
    else:
        minute += turnaround
    

    return print(hour, minute)
cooking_completion_time(now, turnaround)
