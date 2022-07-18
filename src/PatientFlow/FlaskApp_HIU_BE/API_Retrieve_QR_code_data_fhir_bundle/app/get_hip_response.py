from app import app
import requests
import json
import os,time
from flask import Flask, request

@app.route('/fhir_response', methods=['POST'])
def get_fhir_response():
	"""
  api = "https://dev.abdm.gov.in/gateway/v0.5/health-information/cm/request"
  uuid_ = str(uuid.uuid4())
  timestamp = datetime.now(timezone.utc).isoformat()
  timestamp = timestamp.replace('+00:00',  'Z')

  data = {
      "requestId": f"{uuid_}",
      "timestamp": f"{timestamp}",
      "hiRequest": {
          "consent": {
              "id": "11dd232b-cf1a-4ebd-9e54-f3c520f826f1"
          },
          "dateRange": {
          "from": "2022-01-25T12:30:29.592Z",
          "to": "2022-07-16T16:33:29.592Z"
          },
          "dataPushUrl": "https://webhook.site/b5de1d31-7333-4011-8a32-8a0f9628e613",
          "keyMaterial": {
      "cryptoAlg": "ECDH",
      "curve": "Curve25519",
      "dhPublicKey": {
          "expiry": "2022-12-31T12:30:29.592Z",
          "parameters": "Curve25519/32byte random key",
          "keyValue": "MIIBMTCB6gYHKoZIzj0CATCB3gIBATArBgcqhkjOPQEBAiB/////////////////////////////////////////7TBEBCAqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqYSRShRAQge0Je0Je0Je0Je0Je0Je0Je0Je0Je0Je0JgtenHcQyGQEQQQqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq0kWiCuGaG4oIa04B7dLHdI0UySPU1+bXxhsinpxaJ+ztPZAiAQAAAAAAAAAAAAAAAAAAAAFN753qL3nNZYEmMaXPXT7QIBCANCAAQZMBQ1oTvYhhB6m+UrpCO7yLzPFjxLQx7/WxnIHRE6WxotY99ktCmO7mZ8biUKOfYpBTj7EAA6kJubro7XyAyF"
      },
      "nonce": "umPiJaWuE6TThReeTbgW2w7M6JhcdqrO+06eRz/OTwo="
      }
      }
  }

   # private_key = "B508XUPr5StoCLg2SFTVhSPzxs1Q4rajjg655D126Oc="
   headers = {
       "Content-Type":"application/json", 
       "Authorization":f"Bearer {requests.get('https://edge-abdm.qa.karkinos.in/ndhmRouter/get-auth-token').json()['accessToken']}",
       "X-CM-ID":"sbx"
       }
   response = requests.post(api, headers=headers, data=json.dumps(data))
   res = str(response.headers)
  """
    data = {"Ack":"ok"}
    return data

