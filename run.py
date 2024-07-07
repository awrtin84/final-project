import uvicorn

if __name__ == "__run__":
    uvicorn.run('config:app', host= '0.0.0.0', port= 8000, reload= True)