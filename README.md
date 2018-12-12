# Trading Sentiment Analyzer

## Summary
Trading Sentiment Analyzer will analyze any trading instrument by retrieving archived news articles and will subsequently compute a normalized score for the sentiment of that instrument.

## What is the function of the tool?
Traders are well acquainted with the phenomenon of ‘sentiment’ in stock markets and trading. A professional trader must not only consult fundamental technical indicators when contemplating whether to purchase an instrument, but must also observe the sentiment regarding that individual instrument. The Trading Sentiment Analyzer will analyze any currency, commodity, cryptocurrency, stock or index that the user requests by retrieving textual information from news articles from the Google News API. Subsequently after analyzing various articles, the tool will provide a quantified score on the one day, one week, one month and overall ‘sentiment’ of that instrument. A perfectly bullish (positive) sentiment will receive a score of 1.0 whereas a perfectly bearish (negative) sentiment will receive a score of -1.0. Any score that is in between will indicate to what extent that trading instrument has a positive or negative sentiment. The sentiment value is normalized and can be used to compare to other trading instruments the market. 

## Who will benefit from such a tool?
The entire trading community can benefit from such a tool, including but not limited to private investors, institutional investors, banks, insurers etc. Basically, any individual or entity that intends to make a more empirical decision when trading could benefit from this tool by knowing what the short-term future may hold for that trading instrument, thereby increasing their possibility of returns. However it is necessary to acknowledge, that such technical indicators are not always or entirely accurate and user discretion must be exercised at all times.

## Installation

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

** Account user name

*** Root directory of pip-18.1 installation folder

#### newsapi
Type the following lines of code into command prompt (line interpreter):

`set path=%path%;C:/Python34/Scripts/`

`pip install newsapi`

#### requests
Type the following lines of code into command prompt (line interpreter):

`set path=%path%;C:/Python34/Scripts/`

`pip install requests`

#### tkinter
Type the following lines of code into command prompt (line interpreter):

`set path=%path%;C:/Python34/Scripts/`

`pip install tkinter`

#### metapy
Type the following lines of code into command prompt (line interpreter):

`set path=%path%;C:/Python34/Scripts/`

`pip install metapy`

#### collections
Type the following lines of code into command prompt (line interpreter):

`set path=%path%;C:/Python34/Scripts/`

`pip install collections`
