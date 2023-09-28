import time

def time_req(func):
    times = []
    def dec(*args, **kwargs):
        ctime = time.time()
        if len(times) and ctime - times[0] > 1:
            times.clear()
            return 
        if len(times) >= 3 and ctime - times[-3] < 1:
            print('skip func')
            return 
        func()
        times.append(ctime)
    return dec
    
@time_req
def reqSend():
    print("request")
    

    
# for _ in range(10):
#     reqSend()

# time.sleep(1)

# for _ in range(10):
#     reqSend()