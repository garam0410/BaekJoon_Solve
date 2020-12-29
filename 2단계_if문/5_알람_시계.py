hour, minute = input().split()

hour = int(hour)
minute = int(minute)

if minute >= 45 : 
    minute = minute - 45
    print("%d %d" %(hour,minute))

elif minute < 45 : 
    
    if hour == 0 : 
        hour = 23
    else : 
        hour = hour - 1

    minute = minute + 15

    print("%d %d" %(hour,minute))