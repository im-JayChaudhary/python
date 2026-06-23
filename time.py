#importing time module
import time
from datetime import datetime, timedelta
# print(time.time())
stmptime = time.strftime("%H:%M:%S")
print(stmptime)
# print(time.strftime("%H:%M:%S"))
# print("Hours: ", time.strftime("%H"))
# print("Minutes: ", time.strftime("%M"))
# print("Seconds: ", time.strftime("%S"))

#Greetings
if time.strftime("%H:%M") >= "00:00" and time.strftime("%H:%M") <= "11:59":
    print("Good Morning")
elif time.strftime("%H:%M") >= "12:00" and time.strftime("%H:%M") <= "16:59":
    print("Good Afternoon")
else:
    print("Good Evening")

#new two times
timecurrent = time.strftime("%H:%M:%S")
print("Current Time:", timecurrent)
#ahead time
timeaheads = datetime.now() + timedelta(seconds=60)
timeaheadm = datetime.now() + timedelta(minutes=60)
timeaheadh = datetime.now() + timedelta(hours=1)
print("Time after 60 seconds:", timeaheads)
print("Time after 60 minutes:", timeaheadm)
print("Time after 1 hour:", timeaheadh)