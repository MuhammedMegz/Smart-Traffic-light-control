min_waited_time = 10
max_waited_time = 60

def ratio (q,x):
    return q/x


def waited_time(q,x):
    if q==0 and x==0:
        return min_waited_time
    ratio=q/(q+x)
    waited_time=ratio*max_waited_time
    if waited_time < min_waited_time :
        waited_time = min_waited_time
    elif waited_time > max_waited_time :
        waited_time = max_waited_time
    return int(waited_time-(waited_time%5))


def calcTime(forward_traffic_num, right_traffic_num, turn):   
        
    if turn=="EW":
        # the turn is on EW
        if right_traffic_num >= forward_traffic_num:
            return "no change"
        return waited_time(right_traffic_num,forward_traffic_num)

      
    if turn=="NS":
        # the turn is on NS
        if forward_traffic_num >= right_traffic_num:
            return "no change"
        return waited_time(forward_traffic_num,right_traffic_num)
