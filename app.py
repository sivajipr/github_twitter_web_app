from flask import Flask, render_template,request,session,flash,redirect,url_for
import requests
import json
import oauth2 as oauth
app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/github', methods=['POST','GET'])
def github():
	a=[]
	if request.form.get('sbmt'):
		name=request.form.get('val')
		url = 'https://api.github.com/users/'+name+'/repos'
		req=requests.get(url).json()
		for value in req:
			a.append(value['name'])
		return render_template('gitout.html',a=a)
	return render_template('github.html',a=a)

@app.route('/twitter', methods=['POST','GET'])
def twitter():
	b=[]
	if request.form.get('sbmt'):
		name=request.form.get('val')
		Consumer_Key = "*********************************************"
		Consumer_Secret = "******************************************"
		Access_Key = "***********************************************"
		Access_Secret = "********************************************"
	
		consumer = oauth.Consumer(key=Consumer_Key, secret=Consumer_Secret)
		access_token = oauth.Token(key=Access_Key, secret=Access_Secret)
		client = oauth.Client(consumer, access_token)
	
	
		post = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+name+"&count=10"
	
		response, data = client.request(post)
		tweets = json.loads(data)
		for tweet in tweets:
			b.append(tweet['text'])
			return render_template('twetout.html',b=b)
	return render_template('twitter.html',b=b)
@app.route('/')
def home():
	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True)

