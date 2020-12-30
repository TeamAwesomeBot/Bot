import urllib
import urllib.request
import json
import configparser

config = configparser.ConfigParser()
config.sections()
config.read('config.ini')
config.sections()
api = config['YOUTUBE_API']


def get_channel_videos(channel_id, count=2):
    video_info = []
    try:
        api_key = api['token']

        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
        base_info_url = 'https://www.googleapis.com/youtube/v3/videos?part=statistics%2CcontentDetails%2Cstatistics&id='

        search_url = base_search_url + \
            f'key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults={count}'

        url = search_url

        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for item in resp['items']:
            if item['id']['kind'] == "youtube#video":
                video_info.append(item['id']['videoId'])        #0
            
            video_info.append(item['snippet']['title'])         #1
            video_info.append(item['snippet']['channelTitle'])  #2
            video_info.append(item['snippet']['publishedAt'])   #3
        
        info_url = f'https://www.googleapis.com/youtube/v3/videos?part=statistics%2CcontentDetails%2Cstatistics&id={video_info[0]}&key={api_key}'
        info_inp = urllib.request.urlopen(info_url)
        info_resp = json.load(info_inp)

        for item in info_resp['items']:
            video_info.append(item['statistics']['viewCount'])  #4
            video_info.append(item['statistics']['likeCount'])      #5
            video_info.append(item['statistics']['dislikeCount'])   #6
            video_info.append(item['contentDetails']['duration'])   #7
    except Exception as e:
        print(f'An error occurred while trying to access the youtube-api. Exception: {str(e)}')

    return video_info
