import datetime



timestart = datetime.datetime.now()
print(str(timestart) + "--Waiting for device")

time.sleep(5)
duration = (datetime.datetime.now()-timestart).minute
print(duration)
