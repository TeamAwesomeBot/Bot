import urllib.request
import urllib.parse
import re
import pytube
import os
from moviepy.editor import *

download_path = str(os.path.dirname(os.path.realpath(__file__))) + '\\Downloads\\files\\'

def download(url):
	print("testd")
	video_id = split_url(url)
	if check_id(video_id) == False:  # if video isnt already downloaded
	    split_url(video_id)
	    get_video(video_id)
	    converter(video_id)
	    delete_video(video_id)


def get_video(video_id):
    url = 'https://www.youtube.com/watch?v=' + video_id
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    video.download(download_path)
    os.rename(download_path + youtube.streams.first().default_filename,
              download_path + video_id + '.mp4')
    print('Video downloaded successfully.')


def converter(video_id):
    video = VideoFileClip(os.path.join(
        download_path, download_path, video_id + ".mp4"))
    video.audio.write_audiofile(os.path.join(
        download_path, download_path, video_id + ".mp3"))
    video.close()


def delete_video(video_id):
    os.remove(download_path + video_id + '.mp4')


def delete_audio(video_id):
    os.remove(download_path + video_id + '.mp3')


def split_url(url):
    if "youtube.com/" in url:
        video_id_list = url.split("watch?v=")
        video_id = video_id_list[1]
    else:
        video_id = url
    return video_id


def check_id(video_id):
    print('Checking id \'' + video_id + '\'')
    if os.path.isfile(download_path + video_id + '.mp4') or os.path.isfile(download_path + video_id + '.mp3'):
        print('File \'' + video_id + '\' exists.')
        return True
    else:
        return False


def search_video(searchf):
    search = searchf
    search = urllib.parse.quote(search)
    html = urllib.request.urlopen(
        'https://www.youtube.com/results?search_query=' + search)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    if not len(video_ids) <= 0:
        print('Returning \'' + video_ids[0] + '\'.')
        return video_ids[0]
    else:
        return '1102'