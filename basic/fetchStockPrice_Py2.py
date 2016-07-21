import urllib, time, os, re, csv

def fetchGF(googleticker):
    url = "http://www.google.com/finance?&q="
    txt = urllib.urlopen(url + googleticker).read()
    k = re.search('id="ref_(.*?)">(.*?)<', txt)
    if k:
        tmp = k.group(2)
        q = tmp.decode().replace(',', '')
    else:
        q = "Nothing found for: " + googleticker
    return q


# display time corresponding to your location
print(time.ctime())
print

# Set local time zone to NYC
os.environ['TZ'] = 'America/New_York'
time.tzset()
t = time.localtime()  # string
print(time.ctime())
print

def combine(ticker):
    quote=fetchGF(ticker) # use the core-engine function
    t=time.localtime()    # grasp the moment of time
    output=[t.tm_year,t.tm_mon,t.tm_mday,t.tm_hour,t.tm_min,t.tm_sec,ticker,quote] # build a list
    return output

ticker="NASDAQ:AAPL"
tickers = ["NASDAQ:AAPL", "NASDAQ:GOOG", "NASDAQ:BIDU", "NYSE:IBM", "NASDAQ:INTC", "NASDAQ:MSFT", "NYSEARCA:SPY"]

# define the name of an output file
fname = "portfolio.dat"
# remove a file, if exist
os.path.exists(fname) and os.remove(fname)

freq = 60  # fetch data every 600 sec (10 min)

with open(fname, 'a') as f:
    writer = csv.writer(f, dialect="excel")  # ,delimiter=" ")
    while (t.tm_hour <= 16):
        if (t.tm_hour == 16):
            while (t.tm_min < 31):
                for ticker in tickers:
                    data = combine(ticker)
                    print(data)
                    writer.writerow(data)
                time.sleep(freq)
            else:
                break
        else:
            for ticker in tickers:
                data = combine(ticker)
                print(data)
                writer.writerow(data)
            time.sleep(freq)

f.close()
print(str(t.tm_hour) + ":" + str(t.tm_min))