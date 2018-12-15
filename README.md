# Trading Sentiment Analyzer

## Summary
Trading Sentiment Analyzer will compute a normalized 'sentiment' score for any stock, currency, comodity or index by analyzing relevant and current news articles on the internet.

## What is the function of the tool?
Traders are well acquainted with the phenomenon of ‘sentiment’ in stock markets and trading. A professional trader must not only consult fundamental technical indicators when contemplating whether to purchase an instrument, but must also observe the sentiment regarding that individual instrument. The Trading Sentiment Analyzer will analyze any currency, commodity, cryptocurrency, stock or index that the user requests by retrieving textual information from news articles from the Google News API. Subsequently after analyzing various articles, the tool will provide a quantified score on the one day, one week, one month and overall ‘sentiment’ of that instrument. A perfectly bullish (positive) sentiment will receive a score of 1.0 whereas a perfectly bearish (negative) sentiment will receive a score of -1.0. Any score that is in between will indicate to what extent that trading instrument has a positive or negative sentiment. The sentiment value is normalized and can be used to compare to other trading instruments the market. 

## Who will benefit from such a tool?
The entire trading community can benefit from such a tool, including but not limited to private investors, institutional investors, banks, insurers etc. Basically, any individual or entity that intends to make a more empirical decision when trading could benefit from this tool by knowing what the short-term future may hold for that trading instrument, thereby increasing their possibility of returns. However it is necessary to acknowledge, that such technical indicators are not always or entirely accurate and user discretion must be exercised at all times.

## Running online
To run this program online please visit the following URL [mkhorasani.pythonanywhere.com](https://mkhorasani.pythonanywhere.com/).


## Running locally 
To install and run this program on your local machine please execute the following steps in order.

### Python 3.4
If you do not already have a Python installation, please install Python 3.4 or a later version from [here.](https://www.python.org/downloads/release/python-340/)

### Toolkits

#### pip
First install the pip toolkit by downloading and extracting [pip-18.1.tar.gz.](https://pypi.org/project/pip/#files)
Then type the following lines of code into command prompt (line interpreter):

```
set path=%path%;C:/Python34/
cd C:/Users/**/***/pip-18.1/
python setup.py install
```

** *Account user name*

*** *Root directory of pip-18.1 installation folder*

#### newsapi
Type the following lines of code into command prompt (line interpreter):

```
set path=%path%;C:/Python34/Scripts/
pip install newsapi
```

#### requests
Type the following lines of code into command prompt (line interpreter):

```
set path=%path%;C:/Python34/Scripts/
pip install requests
```

#### tkinter
Type the following lines of code into command prompt (line interpreter):

```
set path=%path%;C:/Python34/Scripts/
pip install tkinter
```

#### metapy
Type the following lines of code into command prompt (line interpreter):

```
set path=%path%;C:/Python34/Scripts/
pip install metapy
```

#### collections
Type the following lines of code into command prompt (line interpreter):

```
set path=%path%;C:/Python34/Scripts/
pip install collections
```

To run this script locally, please copy and paste the following files in your root directory:

1. [TSA v1.0.py](https://github.com/mkhorasani/Trading_Sentiment_Analyzer/blob/master/TSA%20v1.0.py)
2. [lemur-stopwords.txt](https://github.com/mkhorasani/Trading_Sentiment_Analyzer/blob/master/lemur-stopwords.txt)
3. [Illinois Logo.gif](https://github.com/mkhorasani/Trading_Sentiment_Analyzer/blob/master/Illinois%20Logo.gif)

Subsequently you must modify the following lines of code to reflect the location of your root directory:

**Line 50:** `logo = PhotoImage(file='C:/Users/**/***/Illinois Logo.gif')`

**Line 269:** `logo = PhotoImage(file='C:/Users/**/***/Illinois Logo.gif')`

**Line 310:** `logo = PhotoImage(file='C:/Users/**/***/Illinois Logo.gif')`

**Line 130:** `tok1 = metapy.analyzers.ListFilter(tok1, "C:/Users/**/***/lemur-stopwords.txt", metapy.analyzers.ListFilter.Type.Reject)`

**Line 181:** `tok2 = metapy.analyzers.ListFilter(tok2, "C:/Users/**/***/lemur-stopwords.txt", metapy.analyzers.ListFilter.Type.Reject)`

**Line 232:** `tok3 = metapy.analyzers.ListFilter(tok3, "C:/Users/**/***/lemur-stopwords.txt", metapy.analyzers.ListFilter.Type.Reject)`

** *Account user name*

*** *Root directory of Trading Sentiment Analyzer installation folder*

### Google News API
Please register with Google News API [here](https://newsapi.org/s/google-news-api) to receive your own API Key. Subsequently replace the current API Key with your own in the following lines of the code:

**Line 113:** 'apiKey=6fd0091055f944df84469bb87e3d878c'

**Line 164:** 'apiKey=6fd0091055f944df84469bb87e3d878c'

**Line 215:** 'apiKey=6fd0091055f944df84469bb87e3d878c'

## Usage

### Running online
To use this program online, simply type the name of the trading instrument in the entry field and click on the button 'Generate Report'. You will be taken to a page that displays the following information:

```
----------------------------------- TRADING SENTIMENT ANALYZER RESULTS -----------------------------------

Sentiment Values Range From -1 to +1             -1 = Negative Sentiment           +1 = Positive Sentiment

                                         Trading Instrument: aapl

                                         One Day Sentiment: -0.22

                                         One Week Sentiment: -0.05

                                         One Month Sentiment: -0.13

                                         Overall Sentiment: -0.13
```                                                              
Please note that by 'trading instrument' we are referring to any stock, currency, commodity, index fund etc. 
Please do not enter irrelevant words or phrases into the entry field as you will receive a 'N/A' value in the report as shown below. 

```
----------------------------------- TRADING SENTIMENT ANALYZER RESULTS -----------------------------------

Sentiment Values Range From -1 to +1             -1 = Negative Sentiment           +1 = Positive Sentiment

                                         Trading Instrument: berlin

                                         One Day Sentiment: N/A

                                         One Week Sentiment: N/A

                                         One Month Sentiment: N/A

                                         Overall Sentiment: N/A
``` 

Under exceptional circumstances you may receive a score for an irrelevant entry, however the scores will simply reflect the sentiment regarding your entry and will generally be unpurposeful.  

### Running locally
After the successful installation of all the required toolkits and code modifications explained in the previous section, you may simply execute the TSA v1.0.py script by hitting your 'F5' key when the Python IDE is open with the script. Subsequently a window will appear that will prompt you to enter the name of your trading instrument and then you may click on the button 'Generate Report'. A new window with the following information will be displayed:

```
----------------------------------- TRADING SENTIMENT ANALYZER RESULTS -----------------------------------

Sentiment Values Range From -1 to +1             -1 = Negative Sentiment           +1 = Positive Sentiment

                                         Trading Instrument: aapl

                                         One Day Sentiment: -0.22

                                         One Week Sentiment: -0.05

                                         One Month Sentiment: -0.13

                                         Overall Sentiment: -0.13
``` 

In the event of an irrelevant entry into the entry field, another window appear displaying the following message:

```
                                  No information found for this instrument.
                                         
                                    Please try another trading instrument.
```                                          

### Interpreting the scores
The 'sentiment' score range from a relative score of -1 to +1. -1 represents a perfectly negative sentiment, whereas +1 represents a perfectly positive sentiment, and 0 a perfectly neutral sentiment. Most often the scores will be somewhere in between, displayed with upto 2 decimal places. The scores a presented as follows:

**One Day Sentiment:** (the sentiment for one day's worth of news articles on the internet)

**One Week Sentiment:** (the sentiment for one week's worth of news articles on the internet)

**One Month Sentiment:** (the sentiment for one month's worth of news articles on the internet)

**Overall Sentiment:** (the arithmetic mean for the one day, one week and one month sentiment scores with equal weighting)

Therefore a negative score suggests that the sentiment regarding the trading instrument is negative and perhaps it is best not to buy that instrument, or if you already own any of that instrument you may want to sell it. Vice versa, a positive score suggests that the sentiment regarding the trading instrument is positive and perhaps it best to buy that instrument, or if you already own any of that instrument you may want to hold on to it.

## Disclaimer 
**THE RESULTS OF THIS TOOL ARE NOT ALWAYS OR ENTIRELY ACCURATE. USER DISCRETION IS ADVISED AT ALL TIMES.**

**NO LIABILITY OR RESPONSIBILITY WILL BE ACCEPTED IF THIS PROGRAM'S USE RESULTS IN FINANCIAL LOSSES FOR ANY INDIVIDUAL OR ENTITY.**

