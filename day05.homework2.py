import requests
import multiprocessing
def text (path):
    list1 = []
    response = requests.get(path)
    html = response.text
    for line in html.split():
            if 'href' in line and 'chapter' in line :
                list1.append(line)
    return list1
http = text('https://www.17k.com/list/3015690.html')

def A(http):
    i = -1
    for path_ in http:
        i +=1
        response = requests.get(path_)
        txt_ = response.content
        with open('‪E:/python/homework5/novel'+http[i]+'.txt',mode='wb') as f:
            f.write(txt_)
if __name__ == "__main__":
    p1 = multiprocessing.Process(target = A,args=(http,))
    p1.start()
    p1.join()
