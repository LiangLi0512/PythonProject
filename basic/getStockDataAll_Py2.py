import urllib2, time, os, json

def fetchGF(googleticker):
	link="http://www.google.com/finance/info?infotype=infoquoteall&q="
	url=link + googleticker
	u = urllib2.urlopen(url)
	content = u.read()
	data = json.loads(content[3:])
	return data


# display time corresponding to your location
print(time.ctime())
print

# Set local time zone to NYC
os.environ['TZ'] = 'America/New_York'
time.tzset()
t = time.localtime()  # string
print(time.ctime())
print


ticker="NASDAQ:AAPL"
#tickers = ["NASDAQ:AAPL", "NASDAQ:GOOG", "NASDAQ:BIDU", "NYSE:IBM", "NASDAQ:INTC", "NASDAQ:MSFT", "NYSEARCA:SPY"]
print(fetchGF(ticker))