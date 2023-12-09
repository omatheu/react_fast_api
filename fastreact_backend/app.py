from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI();

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["http://localhost:3000"]
)

@app.get('/get_data')
async def get_data():
    return {'body' : 'renderizar esse texto. MAIS TEXTO'}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port='7777')