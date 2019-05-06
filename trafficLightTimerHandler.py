import time



right_traffic_num=0
forward_traffic_num=0
right_traffic=0
forward_traffic=0
min_waited_time=10
max_waited_time=90
turn=0




def ratio (q,x):
    return q/x
def waited_time(q,x):
    if q==0 and x==0:
        return 10
    ratio=q/(q+x)
    waited_time=ratio*90
    if waited_time<10 :
        waited_time=10
    elif waited_time > 90 :
        waited_time=90
    return int(waited_time-(waited_time%5))