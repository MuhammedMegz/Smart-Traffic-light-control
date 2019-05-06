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

while 1:
    #read from socket.io
    '''
    right_traffic_num=x
    forward_traffic_num=y
    
    '''
    right_traffic_num=int(input("right"))
    if right_traffic_num==122 :
        break
    forward_traffic_num=int(input("forward"))
    
   
        
    if turn==0:
        # the turn is on right
        time=waited_time(right_traffic_num,forward_traffic_num)
        right_traffic=1
        forward_traffic=0
      
    if turn==1:
        # the turn is on forward
        time=waited_time(forward_traffic_num,right_traffic_num)
        right_traffic=0
        forward_traffic=1
    print(str(right_traffic)+"    "+str(forward_traffic))
    print(time)
    
    print("----------------------------------------")
    
            
    turn=(turn+1)%2
    
    
    time.sleep(waited_time)
    
        
        
        
    
    


