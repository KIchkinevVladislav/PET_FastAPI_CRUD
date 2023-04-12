from fastapi import FastAPI
from db.base import databese
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {'messange': 'Hello World!'} 

@app.on_event('startup')
async def startup():
    await databese.connect()

@app.on_event('shutwodw')
async def shutdown():
    await databese.disconnect()

    
if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)
