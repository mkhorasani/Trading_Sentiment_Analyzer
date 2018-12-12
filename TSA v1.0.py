#####################################################################
###               Trading Sentiment Analyzer 2018(C)              ###
###                CS410: Text Information Systems                ###
###           All rights reserved by: Mohammad Khorasani          ###
###                      mhmmdkh2@illinois.edu                    ###
#####################################################################


#################################################
###            Importing Libraries            ###
#################################################

from newsapi import NewsApiClient
import datetime
import time
from time import gmtime, strftime, sleep 
import requests
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
import metapy
from collections import Counter

#################################################
###        Graphical User Interface           ###
#################################################

def gui():
    def kill():
        sleep(1)
        app.destroy()
        sleep(1)
        
    global language
    language=''
    def beenClicked3():
        radioValue = 'Please select a language'
        tkinter.messagebox.showinfo('Please select a language', radioValue)
        return
    def beenClicked4():
        radioValue = 'Please fill in the name of your trading instrument'
        tkinter.messagebox.showinfo('Please fill in the name of your trading instrument', radioValue)
        return
    def close_window1():
        global language
        language='English'
        if custName.get()=='':
            beenClicked4()
        if custName.get() != '':
            app.destroy()
        return

    app = Tk()
    app.configure(background='white')
    app.title('Trading Sentiment Analyzer')
    app.geometry('355x220+200+200')
    logo = PhotoImage(file='C:/Users/Mohammad Khorasani/Desktop/Illinois Logo.gif')
    w1 = Label(app, image=logo,bg='white').pack(side='top')

    app.title('Trading Sentiment Analyzer')
    labelText = StringVar()
    labelText.set('Enter the name of your trading instrument e.g. (AAPL)')
    label1 = Label(app, textvariable=labelText,bg='white', height=2)
    label1.pack()

    global custName
    custName = StringVar(None)
    yourName = Entry(app, textvariable=custName,bg='light grey', width=47)
    yourName.pack()

    labelText = StringVar()
    labelText.set('')
    label2 = Label(app, textvariable=labelText,bg='white',height=0)
    label2.pack()

    button2 = Button(app, text='Generate Report', width=40, bg='light grey', command=close_window1)
    button2.pack(side='top',padx=15,pady=5)
    app.after(300000, lambda: kill())
    app.mainloop()
    import time
    global a
    a=custName.get()

    return

gui()

#################################################
###           Date & Query Formation          ###
#################################################

#Query Formation
entry = a
query_base = ' trading'
query = entry + query_base

#Date Formation
date = datetime.datetime.now()
date_1 = date+datetime.timedelta(days=-1)
date_1 = date_1.strftime("%Y-%m-%d")
date_2 = date+datetime.timedelta(days=-7)
date_2 = date_2.strftime("%Y-%m-%d")
date_3 = date+datetime.timedelta(days=-30)
date_3 = date_3.strftime("%Y-%m-%d")



#################################################
###             One Day Sentiment             ###
#################################################

#Google News API News Article Retrieval
url1 = ('https://newsapi.org/v2/everything?'
       'q={0}&'
       'domains=fxstreet.com,marketpulse.com,rnsdaily.com,marketwatch.com,investorplace.com,seekingalpha.com,dailyfx.com,cnbc.com,investors.com,nasdaq.com,barrons.com,zacks.com&'
       'from={1}&'
       'sortBy=publishedAt&'
       'language=en&'
       'pageSize=100&'
       'apiKey=6fd0091055f944df84469bb87e3d878c'
        .format(query,date_1)
       )

response1 = requests.get(url1)
parsed_response1 = str(response1.json())

#Tokenization
tok1 = metapy.analyzers.ICUTokenizer(suppress_tags=True)

#Length Filter
tok1 = metapy.analyzers.LengthFilter(tok1, min = 2, max = 7)

#Lower Case Filter
tok1 = metapy.analyzers.LowercaseFilter(tok1)

#Stop Word Filtering
tok1 = metapy.analyzers.ListFilter(tok1, "C:/Users/Mohammad Khorasani/Desktop/lemur-stopwords.txt", metapy.analyzers.ListFilter.Type.Reject)

#Stemming
tok1 = metapy.analyzers.Porter2Filter(tok1)
tok1.set_content(parsed_response1)
tokens1 = [token for token in tok1]

count1 = Counter(tokens1)

#Positive Sentiment Termn Frequency Count
PS1 = 0
PS1 = count1['bull'] + count1['bullish'] + count1['positive'] + count1['increase'] + count1['rise'] + count1['soar'] + count1['raise'] + count1['good'] + count1['great'] + count1['elevate']

#Negative Sentiment Term Frequency Count
NS1 = 0
NS1 = count1['bear'] + count1['bearish'] + count1['negative'] + count1['decrease'] + count1['fall'] + count1['sink'] + count1['lower'] + count1['bad'] + count1['aweful'] + count1['reduce']

Score1 = 'N/A'
if PS1 + NS1 > 0:
    Score1 = round((PS1 - NS1)/(PS1 + NS1),2)


#################################################
###             One Week Sentiment            ###
#################################################

#Google News API News Article Retrieval
url2 = ('https://newsapi.org/v2/everything?'
       'q={0}&'
       'domains=fxstreet.com,marketpulse.com,rnsdaily.com,marketwatch.com,investorplace.com,seekingalpha.com,dailyfx.com,cnbc.com,investors.com,nasdaq.com,barrons.com,zacks.com&'
       'from={1}&'
       'sortBy=publishedAt&'
       'language=en&'
       'pageSize=100&'
       'apiKey=6fd0091055f944df84469bb87e3d878c'
        .format(query,date_2)
       )

response2 = requests.get(url2)
parsed_response2 = str(response2.json())

#Tokenization
tok2 = metapy.analyzers.ICUTokenizer(suppress_tags=True)

#Length Filter
tok2 = metapy.analyzers.LengthFilter(tok2, min = 2, max = 7)

#Lower Case Filter
tok2 = metapy.analyzers.LowercaseFilter(tok2)

#Stop Word Filtering
tok2 = metapy.analyzers.ListFilter(tok2, "C:/Users/Mohammad Khorasani/Desktop/lemur-stopwords.txt", metapy.analyzers.ListFilter.Type.Reject)

#Stemming
tok2 = metapy.analyzers.Porter2Filter(tok2)
tok2.set_content(parsed_response2)
tokens2 = [token for token in tok2]

count2 = Counter(tokens2)

#Positive Sentiment Term Frequency Count
PS2 = 0
PS2 = count2['bull'] + count2['bullish'] + count2['positive'] + count2['increase'] + count2['rise'] + count2['soar'] + count2['raise'] + count2['good'] + count2['great'] + count2['elevate']

#Negative Sentiment Term Frequency Count
NS2 = 0
NS2 = count2['bear'] + count2['bearish'] + count2['negative'] + count2['decrease'] + count2['fall'] + count2['sink'] + count2['lower'] + count2['bad'] + count2['aweful'] + count2['reduce']

Score2 = 'N/A'
if PS2 + NS2 > 0:
    Score2 = round((PS2 - NS2)/(PS2 + NS2),2)


#################################################
###            One Month Sentiment            ###
#################################################

#Google News API News Article Retrieval
url3 = ('https://newsapi.org/v2/everything?'
       'q={0}&'
       'domains=fxstreet.com,marketpulse.com,rnsdaily.com,marketwatch.com,investorplace.com,seekingalpha.com,dailyfx.com,cnbc.com,investors.com,nasdaq.com,barrons.com,zacks.com&'
       'from={1}&'
       'sortBy=publishedAt&'
       'language=en&'
       'pageSize=100&'
       'apiKey=6fd0091055f944df84469bb87e3d878c'
        .format(query,date_3)
       )

response3 = requests.get(url3)
parsed_response3 = str(response3.json())

#Tokenization
tok3 = metapy.analyzers.ICUTokenizer(suppress_tags=True)

#Length Filter
tok3 = metapy.analyzers.LengthFilter(tok3, min = 2, max = 7)

#Lower Case Filter
tok3 = metapy.analyzers.LowercaseFilter(tok3)

#Stop Word Filtering
tok3 = metapy.analyzers.ListFilter(tok3, "C:/Users/Mohammad Khorasani/Desktop/lemur-stopwords.txt", metapy.analyzers.ListFilter.Type.Reject)

#Stemming
tok3 = metapy.analyzers.Porter2Filter(tok3)
tok3.set_content(parsed_response3)
tokens3 = [token for token in tok3]

count3 = Counter(tokens3)

#Positive Sentiment Term Frequency Count
PS3 = 0
PS3 = count3['bull'] + count3['bullish'] + count3['positive'] + count3['increase'] + count3['rise'] + count3['soar'] + count3['raise'] + count3['good'] + count3['great'] + count3['elevate']

#Negative Sentiment Term Frequency Count
NS3 = 0
NS3 = count3['bear'] + count3['bearish'] + count3['negative'] + count3['decrease'] + count3['fall'] + count3['sink'] + count3['lower'] + count3['bad'] + count3['aweful'] + count3['reduce']

Score3 = 'N/A'
if PS3 + NS3 > 0:
    Score3 = round((PS3 - NS3)/(PS3 + NS3),2)


#################################################
###               Error Message               ###
#################################################

def gui2():

    def kill():
        sleep(1)
        app.destroy()
        sleep(1)
        
    app = Tk()
    app.configure(background='white')
    app.title('Trading Sentiment Analyzer')
    app.geometry('355x180+200+200')
    logo = PhotoImage(file='C:/Users/Mohammad Khorasani/Desktop/Illinois Logo.gif')
    w1 = Label(app, image=logo,bg='white').pack(side='top')
    
    labelText1 = StringVar()
    labelText1.set('No information found for this instrument.')
    label1 = Label(app, textvariable=labelText1,bg='white', height=2)
    label1.pack()
    
    labelText2 = StringVar()
    labelText2.set('Please try another trading instrument.')
    label2 = Label(app, textvariable=labelText2,bg='white', height=2)
    label2.pack()
    
    app.after(300000, lambda: kill())
    app.mainloop()
    
    return

if (PS1 + NS1) < 3 or query == ' trading':
    gui2()

    
#################################################
###             Score & Report GUI            ###
#################################################

def gui3():

    global Score1
    global Score2
    global Score3
    
    def kill():
        sleep(1)
        app.destroy()
        sleep(1)
        
    app = Tk()
    app.configure(background='white')
    app.title('Trading Sentiment Analyzer')
    app.geometry('530x350+200+200')
    logo = PhotoImage(file='C:/Users/Mohammad Khorasani/Desktop/Illinois Logo.gif')
    w1 = Label(app, image=logo,bg='white').pack(side='top')
    
    labelText1 = StringVar()
    labelText1.set('Sentiment Ranges From -1 to 1          -1 = Negative Sentiment          +1 = Positive Sentiment')
    label1 = Label(app, textvariable=labelText1,bg='white', height=2)
    label1.pack()
    
    labelText2 = StringVar()
    labelText2.set('------------------------------------------- Results -------------------------------------------')
    label2 = Label(app, textvariable=labelText2,bg='white', height=2)
    label2.pack()

    labelText4 = StringVar()
    labelText4.set('Trading Instrument: %s' % (a))
    label4 = Label(app, textvariable=labelText4,bg='white', height=2)
    label4.pack()

    labelText5 = StringVar()
    labelText5.set('One Day Sentiment: %s' % (Score1))
    label5 = Label(app, textvariable=labelText5,bg='white', height=2)
    label5.pack()

    labelText6 = StringVar()
    labelText6.set('One Week Sentiment: %s' % (Score2))
    label6 = Label(app, textvariable=labelText6,bg='white', height=2)
    label6.pack()

    labelText7 = StringVar()
    labelText7.set('One Month Sentiment: %s' % (Score3))
    label7 = Label(app, textvariable=labelText7,bg='white', height=2)
    label7.pack()

    if Score1 != 'N/A' or Score2 != 'N/A' or Score3 != 'N/A':
        
        if Score1 == 'N/A':
            Score1 = 0
        if Score2 == 'N/A':
            Score2 = 0
        if Score3 == 'N/A':
            Score3 = 0
            
        Overall_score = round((Score1 + Score2 + Score3)/3,2)

    labelText8 = StringVar()
    labelText8.set('Overall Sentiment: %s' % (Overall_score))
    label8 = Label(app, textvariable=labelText8,bg='white', height=2)
    label8.pack()
    
    app.after(300000, lambda: kill())
    app.mainloop()
    
    return

if query != ' trading':
    if (PS1 + NS1) > 2:
        gui3()


        
