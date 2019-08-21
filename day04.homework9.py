def tiem():
    import time
    ticks = time.time()*60
    localtime = time.localtime(time.time())
    print ("本地时间为 :", localtime)
    print ("当前时间毫秒:", ticks)

if __name__ == "__main__":
    tiem()
