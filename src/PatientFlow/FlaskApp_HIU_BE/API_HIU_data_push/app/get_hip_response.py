from app import app
import requests
import json
import os,time
from flask import Flask, request

@app.route('/abdm_hip_response', methods=['POST'])
def get_hip_data():
    global fileno
    fileno = 'output_files'
    path = os.path.abspath(os.path.dirname(__file__))
    data = json.loads(request.data)
    json_object = json.dumps(data, indent=4)
    with open(f'{path}/{fileno}/abcd.json', "w") as outfile:
        outfile.write(json_object)
    return data


@app.route('/health_interface_provider',methods = ['POST'])
def Health_interface_provider():
    global fileno 
    path = os.path.abspath(os.path.dirname(__file__))

    fileno = f'output_files'
    isdir = os.path.exists(f'{path}/{fileno}')
    if not isdir:
        os.mkdir(f'{path}/{fileno}')
    headers = {'Content-Type':'application/json'}
    request_body = requests.post('https://fhir-bundle.herokuapp.com/fhir_response', headers=headers)
    response_data =''
    time.sleep(5)
    for ti in range(0,5):
        # output_Data = []
        dir = os.listdir(f'{path}/{fileno}')
        if len(dir) != 0:
            for json_file in dir:
                f = open(f'{path}/{fileno}/{json_file}')
                text = f.read()
                text_json = json.loads(text)
                # output_Data.append(text_json)
                os.remove(f'{path}/{fileno}/{json_file}')
            return text_json # {"list":output_Data}
        else:
            time.sleep(1)
    text_json = '' 
    os.remove(f'{fileno}')
    return text_json