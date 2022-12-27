import datetime

ssname = str(datetime.datetime.now().ctime())

ssname = ssname.replace('.','_')
ssname = ssname.replace(':','_')[0:-5]

print(ssname)

print(str(datetime.datetime.now().ctime()))

# current time fetch in pyton?