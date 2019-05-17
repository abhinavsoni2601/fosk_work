tuple1=('Monday', 'Wednesday', 'Thursday', 'Saturday')
tuple2=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
for x in tuple2:
    if x in tuple1:
        continue
    tuple1+=(x,)