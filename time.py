import time

currentTime = time.localtime()

# use current time to show current time in formatted string
print('Current System time is :', time.asctime(currentTime))

print('Formatted Time is :', time.strftime("%d/%m/%Y", currentTime))