import json

from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

@app.get("/aggregate")
async def aggregate_data():
    async with httpx.AsyncClient() as client:
        try:

            service1_response = await client.get("http://ec2-3-22-186-8.us-east-2.compute.amazonaws.com:5000/")
            service2_response = await client.get("https://1qajdtdqj3.execute-api.us-west-2.amazonaws.com")
            service3_response = await client.get("https://cloudcomputing-worldmingle.ue.r.appspot.com/")

            if not service1_response.status_code == 200 or not service2_response.status_code == 200 or not service3_response.status_code == 200:
                raise HTTPException(status_code=502, detail="Bad Gateway: One of the services is not responding correctly")

            service1_data = service1_response.json()
            service2_data = service2_response.json()
            service3_data = service3_response.json()

            aggregated_data = {
                "service1_data": service1_data,
                "service2_data": service2_data,
                "service3_data": service3_data
            }
            return aggregated_data

        except json.decoder.JSONDecodeError:
            raise HTTPException(status_code=500, detail="Invalid JSON received from one of the services")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
