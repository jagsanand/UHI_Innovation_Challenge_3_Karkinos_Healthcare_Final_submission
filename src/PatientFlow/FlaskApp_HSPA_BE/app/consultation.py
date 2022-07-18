'''file where all routes of flask app are available'''
from app import app
from flask import Flask, redirect, url_for, render_template, request ,session,g,make_response
from flask_executor import Executor
import requests 
import os 
import json
import time  

executor = Executor(app)
queue = []
def cronc():
    data = "{\"message\":{\"intent\":null,\"order\":null,\"catalog\":{\"descriptor\":{\"name\":\"OncologyHSPA\"},\"items\":[{\"id\":\"0\",\"descriptor\":{\"name\":\"Consultation\"},\"price\":{\"currency\":\"INR\",\"value\":\"700.0\"},\"fulfillment_id\":\"0\"}],\"fulfillments\":[{\"id\":\"0\",\"type\":\"PhysicalConsultation\",\"agent\":{\"id\":\"ashwin@karkinos.in\",\"name\":\"Dr.AshwinPrakash\",\"gender\":\"M\",\"tags\":{\"@abdm/gov/in/first_consultation\":\"500.0\",\"@abdm/gov/in/experience\":\"7.0\",\"@abdm/gov/in/languages\":\"Eng,Hin\",\"@abdm/gov/in/speciality\":\"Oncology\",\"@abdm/gov/in/education\":\"MS\",\"@abdm/gov/in/signature\":null}},\"start\":{\"time\":{\"timestamp\":\"T15:28+05:30\"}},\"end\":{\"time\":{\"timestamp\":\"T15:28+05:30\"}}}]},\"order_id\":null},\"context\":{\"domain\":\"nic2004:85111\",\"country\":\"IND\",\"city\":\"std:080\",\"action\":\"on_search\",\"timestamp\":\"2022-07-14T09:58:16.837097Z\",\"core_version\":\"0.7.1\",\"consumer_id\":\"Karkinos.in.Innovation-EUA\",\"consumer_uri\":\"https://karkinos-in-innovation-hspa.herokuapp.com/eua\",\"provider_id\":\"Karkinos.in.Innovation-HSPA\",\"provider_uri\":\"https://abdm-consultation.herokuapp.com/hspa\",\"transaction_id\":\"7b459b60-035b-11ed-8882-a5e3ac18090e\",\"message_id\":\"7b459b60-035b-11ed-8882-a5e3ac18090e\"}}"
    headers = {'Content-Type':'application/json'}
    request_body = requests.post('http://121.242.73.120:8083/api/v1/on_search',headers=headers,data = data)
    print(request_body.json())
    queue.pop()
    return "success"

@app.route('/hspa/search', methods=['post'])
def Consultation():
    
    data = json.loads(request.data)
    #data = "{\"context\":{\"domain\":\"nic2004:85111\",\"country\":\"IND\",\"city\":\"std:080\",\"action\":\"search\",\"timestamp\":\"2022-07-07T10:43:48.705082Z\",\"core_version\":\"0.7.1\",\"consumer_id\":\"Karkinos.in.Innovation-EUA\",\"consumer_uri\":\"https://webhook.site/743f24d0-0c55-475a-b6ca-b989db17aa62\",\"transaction_id\":\"ae9e6d90-fde1-11ec-b66a-f551703a8c52\",\"message_id\":\"ae9e6d90-fde1-11ec-b66a-f551703a8ca2\"},\"message\":{\"intent\":{\"fulfillment\":{\"agent\":{\"tags\":{\"@abdm/gov/in/system_of_med\":\"Allopathy\",\"@abdm/gov/in/med_speciality\":\"Oncology\"}},\"start\":{\"time\":{\"timestamp\":\"2022-06-22T15:41:36\"}},\"end\":{\"time\":{\"timestamp\":\"2022-06-22T23:59:59\"}},\"type\":\"PhysicalConsultation\"}}}}"
    type = data['message']['intent']['fulfillment']['type']
    result_json = "{'error': {}, 'message': {'ack': {'status': 'ACK'}}}"
    if type == 'PhysicalConsultation':
        queue.append('PhysicalConsultation')
    if len(queue) != 0:
        executor.submit(cronc)
    else:
        os.wait()
    return result_json
