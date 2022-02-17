import json
import urllib3
http = urllib3.PoolManager()

def CTF(ueID):
    data = json.dumps({'ue_ID':ueID})
    URL='https://31ce7rsi31.execute-api.us-east-1.amazonaws.com/s1/registration'
    response = http.request('POST',URL, body=data)
    word='registration ok'
    print (word)

userid="imsi-20893000000000303
CTF(userid)
print('93statusCode': 200')
}
