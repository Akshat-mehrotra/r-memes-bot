import praw
import requests
from instagram import Instagram
import os
from datetime import datetime
from credentials import *
from PIL import Image
from time import sleep


def not_uploaded(id, file="record.txt"):
	with open(file,"r") as f:
		files = f.read().split("\n")
	if not id in files:
		return True
	return False


def make_square(img_path, min_size=256, fill_color=(0, 0, 0, 0)):
	im = Image.open(img_path)
	x, y = im.size
	size = max(min_size, x, y)
	new_im = Image.new('RGB', (size, size), fill_color)
	new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
	img_path = img_path[:-3] + "jpg"
	new_im.save(img_path)

rc = praw.Reddit(client_id="362R_F8jZdyhiw",
			 client_secret=clientscrt,
			 user_agent="unexpected bot")


subreddit = rc.subreddit("memes")
caption_bottom = "\n\n\n\n\n\n #meme #memes #funny #dankmemes #memesdaily #funnymemes #lol #dank #humor #follow #like #dankmeme #lmao #love #anime #ol #edgymemes #dailymemes #comedy #instagram #fun #offensivememes #fortnite #funnymeme #tiktok #memer #memez #memepage #memestagram #bhfyp"
base = "/home/akshat"
uploaded_number=0

instagram_client = Instagram(user, passwrd)


while 1:
	if 1:
		cont = 0
		for sub in subreddit.top('day'):
			if cont >= 1: break

			id=sub.url.split("/")[-1]
			url = sub.url
			path = os.path.join(base,f"{id}")
			id = id[:-3] + "jpg"

			if not sub.stickied and not_uploaded(id):

				req = requests.get(url)
				if req.ok:
					with open(path, "wb") as f:
						f.write(req.content)

					make_square(path)
					instagram_client.upload(sub.title+caption_bottom, id)

					with open("record.txt", "a+") as f:
						f.write(id+"\n")

					cont+=1
					uploaded_number+=1

					if uploaded_number >=10:
						for file in os.listdir(base):
							if file.endswith("jpg"):
								os.remove(os.path.join(base,file))
	sleep(0.5 * 60*60)
