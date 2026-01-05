

setting_time = input()

def wakeup(setting_time):
    hour, minute = setting_time.split(" ")
    hour = int(hour)
    minute = int(minute)
    
    # 현재 hour가 0이라면 23으로 변경

    # 1. 만약 minute - 45 < 0 라면 
    #   1) hour - 1 
    #      hour == 0 ? 23 : hour - 1
    #   2) minute + 60 - 45 

    # 2. 만약 minute - 45 > 0 라면
    #   1) minute - 45
    if  minute - 45 < 0:
        if hour == 0:
            hour = 23
        else:
            hour -= 1
        minute = minute + 60 - 45
    else:
        minute = minute - 45
        
    return print(hour, minute)
        
wakeup(setting_time)