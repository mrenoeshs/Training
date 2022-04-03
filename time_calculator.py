def add_time(start, duration, day=None):
    daysOfWeek = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
    startDay = 0
  
    startElements = start.split()
    startHandM = startElements[0]
    startAMPM = startElements[1]
    startTimes = startHandM.split(':')
    startHours = int(startTimes[0])
    startMinutes = int(startTimes[1])
  
    if startAMPM == 'PM':
        startHours = startHours + 12

    durationElements = duration.split(':')
    durationHours = int(durationElements[0])
    durationMinutes = int(durationElements[1])
  
    daysLater = 0
    finalMinutes = startMinutes + durationMinutes
    finalHours = startHours + durationHours
    if finalHours >= 12:
        finalAMPM = 'PM'
    else:
        finalAMPM = 'AM'
      
    if finalMinutes > 60:
        finalHours += 1
        finalMinutes = finalMinutes % 60

    if finalHours > 24:
        daysLater = finalHours // 24
        finalHours = finalHours % 24
        if finalHours < 12:
            finalAMPM = 'AM'
    if finalHours >= 12:
        finalAMPM = 'PM'
        if finalHours > 12:
            finalHours = finalHours % 12

    finalMinutesString = str(finalMinutes)

    if day != None:
        day = day.capitalize()
        startDay = daysOfWeek.index(day)
        finalDay = daysOfWeek[startDay]
        if daysLater > 0:
            finalDay = daysOfWeek[(startDay + daysLater) % 7]
  
    if finalMinutes < 10:
        finalMinutesString = '0' + finalMinutesString

    if finalHours == 0:
        finalHours = 12
  
    new_time = str(finalHours) + ':' + finalMinutesString + ' ' + finalAMPM

    if day != None:
        new_time = new_time + ', ' + finalDay
  
    if daysLater > 1:
        new_time = new_time + ' (' + str(daysLater) + ' days later)'
    elif daysLater > 0:
        new_time = new_time + ' (next day)'
    return new_time