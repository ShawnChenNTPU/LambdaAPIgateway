{\rtf1\ansi\ansicpg950\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import json\
import urllib3\
http = urllib3.PoolManager()\
\
def CTF(ueID):\
   \
    data = json.dumps(\{'ue_ID':ueID\})\
    URL='https://31ce7rsi31.execute-api.us-east-1.amazonaws.com/s1/registration'\
    response = http.request('POST',URL, body=data)\
    word='registration ok'\
    print (word)\
\
\
\
\
userid="imsi-20893000000000303\'94\
CTF(userid)\
print(\'93statusCode': 200\'94)\
}