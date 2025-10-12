times_string = '1h 45m,360s,25m,30m 120s,2h 60s'
times_string1 = times_string.replace(' ',',')
times_string2 = times_string1.split(',')
minutes = 0
for i in times_string2:
    if 'h' in i:
        minutes += int(i.replace('h',''))*60
    elif 's' in i:
        minutes += int(i.replace('s',''))/60
    else:
        minutes += int(i.replace('m', ''))
print(int(minutes))