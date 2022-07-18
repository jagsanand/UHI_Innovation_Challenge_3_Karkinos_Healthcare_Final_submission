'''file where all routes of flask app are available'''
from crypt import methods
from app import app
from flask import Flask, redirect, url_for, render_template, request ,session,g,make_response
import requests  
import json ,os,time 

global fileno

@app.route('/eua/on_search',methods = ['post'])
def OnSearchResponse():
    global fileno
    fileno = 'output_files'
    path = os.path.abspath(os.path.dirname(__file__))
    data = json.loads(request.data)
    messageid = data['context']['message_id']
    json_object = json.dumps(data, indent=4)
    with open(f'{path}/{fileno}/{messageid}.json', "w") as outfile:
        outfile.write(json_object)
    print(messageid)
    return data


@app.route('/searchphysician',methods = ['post'])
def SearchInternal():
    global fileno 
    path = os.path.abspath(os.path.dirname(__file__))

    data = "{\"context\":{\"domain\":\"nic2004:85111\",\"country\":\"IND\",\"city\":\"std:080\",\"action\":\"search\",\"timestamp\":\"2022-07-07T10:43:48.705082Z\",\"core_version\":\"0.7.1\",\"consumer_id\":\"eua-nha\",\"consumer_uri\":\"https://karkinos-in-innovation-hspa.herokuapp.com/eua\",\"transaction_id\":\"ae9e6d90-fde1-11ec-b66a-f551703a8c52\",\"message_id\":\"035eb9ca-f6bb-424e-ad71-49160fa02aaf\"},\"message\":{\"intent\":{\"fulfillment\":{\"agent\":{\"name\":\"GunA\"},\"start\":{\"time\":{\"timestamp\":\"2022-06-22T15:41:36\"}},\"end\":{\"time\":{\"timestamp\":\"2022-06-22T23:59:59\"}},\"type\":\"PhysicalConsultation\"}}}}"
    json_data = json.loads(data)
    fileno = f'output_files'
    isdir = os.path.exists(f'{path}/{fileno}')
    print(isdir) 
    if not isdir:
        os.mkdir(f'{path}/{fileno}')
    headers = {'Content-Type':'application/json'}
    request_body = requests.post('http://121.242.73.120:8083/api/v1/search',headers=headers,data = data)
    json_args = json.loads(request.data)
    response_data =''
    time.sleep(7)
    while True:
        output_Data = []
        dir = os.listdir(f'{path}/{fileno}')
        if len(dir) != 0:
            for json_file in dir:
                f = open(f'{path}/{fileno}/{json_file}')
                text = f.read()
                text_json = json.loads(text)
                output_Data.append(text_json)
                os.remove(f'{path}/{fileno}/{json_file}')
            return {"list":output_Data}
        else:
            time.sleep(2)
    os.remove(f'{fileno}')
    return response_data