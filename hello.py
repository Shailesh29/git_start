from flask import Flask , render_template, request ,redirect
from bs4 import BeautifulSoup
import urllib2
import re

app = Flask(__name__)


@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
	if request.method=='POST' :
		a=request.form['price']
		b=request.form['url']
		response = urllib2.urlopen(b)
		page = response.read()
		soup = BeautifulSoup(page,"lxml")
		c=soup.find(id="priceblock_ourprice").get_text(strip=True)
		rx = re.compile('[^0-9eE.]')  #converting money into floating point number
        value= rx.sub('', c)
        value=float(value)
        if a>value :
            return "Entered Price is greater than the Actual Price"
        else :
            return "Entered Price is less than the Actual Price"


if __name__ == '__main__':
   app.run()