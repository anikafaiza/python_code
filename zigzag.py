import time, sys
i=0
incr= True

try:
    while True : 
        print(' ' * i, end='')
        print('**********')
        time.sleep(.1)

        if incr:
            i=i+1
            if i==20:
                incr=False
        
        else:
            i=i-1
            if i==0:
                incr = True
except KeyboardInterrupt:
    sys.exit()