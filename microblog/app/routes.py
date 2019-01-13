from app import app

@app.route('/')
@app.route('/index')
@app.route('/hello_world')
def index():
    return "Hello, World!"

