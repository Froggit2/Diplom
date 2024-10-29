from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get(path='/hello')
def hello_1(request: Request):
    return templates.TemplateResponse('Hello_1.html', {'request': request, 'text': 'Привет 1'})


@app.get(path='/hello_2')
def hello_2(request: Request):
    text_1 = 'Привет 2'
    text_2 = 'Привет 3'
    content = {'request': request,
               'text_1': text_1,
               'text_2': text_2}
    return templates.TemplateResponse('Hello_2.html', content)