import uvicorn
from fastai.vision import *
from io import BytesIO
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles
from secure import SecureHeaders

classes = ['Normal', 'Pneumonia']
path = Path(__file__).parent

app = Starlette()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])
app.mount('/static', StaticFiles(directory='app/static'))

secure_headers = SecureHeaders()
learn = load_learner('/model')

@app.route('/')
async def homepage(request):
    html_file = path / 'view' / 'index.html'
    return HTMLResponse(html_file.open().read())


@app.route('/analyze', methods=['POST'])
async def analyze(request):
    img_data = await request.form()
    img_bytes = await (img_data['file'].read())
    img = open_image(BytesIO(img_bytes))
    prediction = learn.predict(img)[0]
    return JSONResponse({'result': str(prediction)})

@app.middleware("http")
async def set_secure_headers(request, call_next):
    response = await call_next(request)
    secure_headers.starlette(response)
    return response

if __name__ == '__main__':
    if 'serve' in sys.argv:
        uvicorn.run(app=app,
                    host='0.0.0.0',
                    port=443,
                    log_level="info",
                    ssl_certfile='/run/secrets/cert.pem',
                    ssl_keyfile='/run/secrets/key.pem')
