# 18/12/2021
# guilherme Silva Toledo
# code to read my twitter timeline and generate me some new banner every few seconds

def fazerBanner(twt):
    nomeBanner = 'tweetAtual.png'
    wg.download(tweet.user.profile_banner_url)
    if os.path.isfile('tweetAtual.png'):
        os.remove(nomeBanner)
        
    os.rename(tweet.user.profile_banner_url.split('/')[5],nomeBanner)

    print('\n'+twt.user.profile_banner_url)

    with Image.open(nomeBanner) as banner:
    	#banner.convert('RGBA')
    	banner.convert('RGBA').filter(ImageFilter.GaussianBlur()).point(lambda p: p *0.5).save(nomeBanner)
    	
def fazerCor():
	nomeBanner = 'tweetAtual.png'
	if os.path.isfile('tweetAtual.png'):
		os.remove(nomeBanner)
	banner = Image.new(mode="RGBA", size=(1500, 500),color=(67,176,114)).save(nomeBanner)
	
def colocarMensagem(twt):	
	nomeBanner = 'tweetAtual.png'
	with Image.open(nomeBanner) as banner:
		fonte = ImageFont.truetype("/home/guilherme/Prog1/backgrounder/symbola/Symbola.ttf", 30, encoding='unic')
		desenharBanner = ImageDraw.Draw(banner)
		desenharBanner.text((150,150), str(twt.text), (255,255,255), font = fonte)
		banner.save('tweetAtual.png')
	
	
import tweepy as tw
import wget as wg
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import time
import os

caminhoAtual = os.getcwd()
print(caminhoAtual)

with open('key.txt','r') as tfile:
    consumer_key = tfile.readline().strip('\n')
    consumer_secret = tfile.readline().strip('\n')
    access_token = tfile.readline().strip('\n')
    access_secret = tfile.readline().strip('\n')

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tw.API(auth)
while True:
	public_tweets = tw.Cursor(api.home_timeline, count = 60, exclude_replies=True, include_rts=False).items()
	#public_tweets = api.user_timeline(count=60, exclude_replies=True, include_rts=False)
	for tweet in public_tweets:
	    print(tweet.text)
	    print(tweet.user.name)
	    print(tweet.user.screen_name)
	    print (hasattr(tweet.user, 'profile_banner_url'))
	    if (hasattr(tweet.user, 'profile_banner_url')):
	    	fazerBanner(tweet)
	    else:
	    	fazerCor()
	    colocarMensagem(tweet)
	    os.system(f'gsettings set org.gnome.desktop.background picture-uri {caminhoAtual}/tweetAtual.png')
	    time.sleep(10)
	print("pulls", api.rate_limit_status()['resources']['statuses']['/statuses/home_timeline'])
