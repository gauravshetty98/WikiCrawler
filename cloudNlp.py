# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 16:47:22 2021

@author: gaurav
"""

import import_ipynb
import pandas as pd
import DataCleaner as dc
from google.cloud import language

#authentication 
client = language.LanguageServiceClient.from_service_account_json('services.json')

filename= "rawText.csv"

#sentiment analysis function
def analyze_text_sentiment(text):
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    for k, v in results.items():
        print(f"{k:10}: {v}")


#cleaning the raw text        
cleanText = dc.cleaner(filename)

for i in range (0,len(cleanText.index)):
    analyze_text_sentiment(cleanText.iloc[i,1])

