from blaze_net.app import app

@app.route('/')
def index(request):
    return app.template_env.get_template('index.html').render()