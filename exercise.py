import time

timeStamp = time.strftime("%I:%M:%S:%p")

print(timeStamp)

hour = int(time.strftime("%H"))

if (hour > 0 and hour < 12):
    print('Good Morning sir')
else:
    print("Your morning time has been over")
