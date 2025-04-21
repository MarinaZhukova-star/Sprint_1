string = '1h 45m,360s,25m,30m 120s,2h 60s' 
for str in string.split(','):
    times = str.split() 
    min = 0 
    for time in times:
        if 'h' in time:
            min += int(time[:-1]) * 60 
        if 'm' in time:
            min += int(time[:-1]) 
        if 's' in time:
            min += int(time[:-1]) // 60 
print(min) 