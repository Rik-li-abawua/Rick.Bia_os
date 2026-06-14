from fastapi import FastAPI

app = FastAPI(title='Ricardo AI OS')

@app.get('/')
def root():
    return {'status':'online','project':'Ricardo AI OS'}
