# ubuntu-banner-with-twitter
I was bored and wanted a new banner for my virtual machine, so I created a code to read my twitter timeline and generate me some new banner every few seconds

---
# HOW TO RUN
**ADENDUM:** *you can manualy search and set your proportions to 1504x500 so that it fits well with the program's generated images however if you're using a virtual machine as well I left another python code there that does the work to you, so you just need to run "proportionSetter.py"*

if you download this project and want to give it a try, you first of all need to open the key.txt file and replace in each line your:
- consumer key
- consumer secret
- access token
- access secret

those can be found in the [twitter developer site](https://developer.twitter.com)

then you'll need to install the things in requirements with "pip install -r requirements.txt"[^1]
and at last you can use "python3.8 bannerv1.py" in the main folder to run the code
[^1]: good practice is to set a python virtual environment beforehand

---
## what I used
first of all, I made this project focusing on my ubuntu virtual machine so it is not curently supported for neither mac nor windows

for this python project I used a virtual environment with those installed through pip and all it's dependencies:
- tweepy
- wget
- pillow

I imported "time" and "os" as well
