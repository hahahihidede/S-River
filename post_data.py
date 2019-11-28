#in this case i used my website which is inoprex.com
import requests
import json
servername = 'http://inoprex.com/post-esp-data.php'
apiKeyValue = 'tPmAT5Ab3j7F9'
sensorName = 'SensorName'
sensorLocation = 'SensorLocation'
#data = 'api_key=' + apiKeyValue + '&sensor=' + sensorName+ '&location=' + sensorLocation + '&value1=' + str(321)+ '&value2=' + str(987) + '&value3=' + str(123) + ""
#url = 'http://inoprex.com/post-esp-data.php'
'''
ldrvalue = '50'
data='ldrvalue='+ldrvalue
'''
data = { "api_key" : api_key, "ph" : 12, "load_balance" : 12 }
dataJson = json.dumps(data, ensure_ascii = 'False')
url ='http://www.inoprex.com/server.php'
headers = {'Content-Type':'application/x-www-form-urlencoded'}
requests.post(url,headers=headers,data=data)
