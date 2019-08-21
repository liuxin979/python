import multiprocessing
import os
import json
import requests
# 获取歌曲URL
def get_(path):
    song_play_url_list = []
    song_name_list = []
    with open(path,mode='r') as f:
        res = f.readlines()[0].strip('\n').split('}')
        for json_ in res[:-1]:
            _json = json_ + '}'
            _json = json.loads(_json)
            song_play_url = _json['song_play_url']
            song_name = _json['song_name']
            if song_play_url is not None:
                song_play_url_list.append(song_play_url)
                song_name_list.append(song_name)
        return song_play_url_list,song_name_list
song_url,song_name = get_("‪‪E:/python/homework5/top_500.txt")
# 下载歌曲
def download(song_url,song_name):
    i = -1
    for path_ in song_url:
        i += 1 
        response = requests.get(path_)
        mp3_ = response.content
        with open('‪E:/python/homework5/music/'+song_name[i]+'.mp3',mode='wb') as f:
            f.write(mp3_)

if __name__ == "__main__":
    x = int(len(song_url)/2)
    p1 = multiprocessing.Process(target = download,args=(song_url[0:x],song_name[0:x]))
    p2 = multiprocessing.Process(target = download,args=(song_url[x:],song_name[x:]))
    p1.start()
    p2.start()
    p1.join()
    p2.join()