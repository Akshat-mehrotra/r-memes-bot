import praw
import requests
from instagram import *
import os
from datetime import datetime

rc = praw.Reddit(client_id="362R_F8jZdyhiw",
			 client_secret="5TXAT7FswvB07UsRAp4i4aI-3Ik",
			 user_agent="unexpected bot")

subreddit = rc.subreddit("memes")

def not_uploaded(id):
	with open("record.txt","r") as f:
		files = f.read().split("\n")
	if not id in files:
		return True
	return False

def get_content_upload():
	while 1:
		if datetime.now().hour >= 9:
			cont = 0
			for sub in subreddit.top('day'):
				if cont >= 1: break

				id=sub.url.split("/")[-1]
				url = sub.url
				if not sub.stickied and not_uploaded(id) and not url.endswith("gif"):
					base = "F:/instagram bot/Unexpected/"
					path = os.path.join(base,f"{id}")
					req = requests.get(url)
					if req.ok:
						with open(path, "wb") as f:
							f.write(req.content)
						uploadimg(sub.title+"\n\n\n\n\n\n #meme #memes #funny #dankmemes #memesdaily #funnymemes #lol #dank #humor #follow #like #dankmeme #lmao #love #anime #ol #edgymemes #dailymemes #comedy #instagram #fun #offensivememes #fortnite #funnymeme #tiktok #memer #memez #memepage #memestagram #bhfyp", path)
						# with client(user, passwrd) as cli:
						# 	cli.upload(path, sub.title+"\n\n\n\n\n\n #meme #memes #funny #dankmemes #memesdaily #funnymemes #lol #dank #humor #follow #like #dankmeme #lmao #love #anime #ol #edgymemes #dailymemes #comedy #instagram #fun #offensivememes #fortnite #funnymeme #tiktok #memer #memez #memepage #memestagram #bhfyp")
						with open("record.txt", "a+") as f:
							f.write(id+"\n")
						cont+=1
		sleep(0.5 * 60*60)
get_content_upload()
