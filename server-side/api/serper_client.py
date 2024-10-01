import json
import os
import requests
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()
serper_api_key = os.getenv('SERPER_API_KEY')
google_serp_api_key = os.getenv('GOOGLE_SERP_API_KEY')
print("GOOGLE SERP API KEY", google_serp_api_key)

class SerperProvider:
    @staticmethod
    def module_image_from_web(submodules):
        print('FETCHING IMAGES...')
        keys_list = list(submodules.keys())
        url = "https://google.serper.dev/images"
        headers = {
            'X-API-KEY': serper_api_key,
            'Content-Type': 'application/json'
        }
        images_list=[]
        for key in keys_list:
            payload = json.dumps({
                "q": submodules[key]
            })
            response = requests.request("POST", url, headers=headers, data=payload)
            json_response = json.loads(response.text)
            image_results = json_response["images"]
            image_links = [i["imageUrl"] for i in image_results]
            images_list.append(image_links)
        return images_list
    
    @staticmethod
    def module_videos_from_web(submodules):
        print('FETCHING VIDEOS...')
        keys_list = list(submodules.keys())
        videos_list=[]
        for key in keys_list:
            params = {
                "q": submodules[key],
                "engine": "google_videos",
                "ijn": "0",
                "api_key": google_serp_api_key
            }

            search = GoogleSearch(params)
            results = search.get_dict()
            video_results = results["video_results"]
            yt_links = [i['link'] for i in video_results[:10]]
            videos_list.append(yt_links)
        return videos_list