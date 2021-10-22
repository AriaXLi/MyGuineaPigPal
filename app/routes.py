from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World! My guinea pigs are named Amy and Leela"