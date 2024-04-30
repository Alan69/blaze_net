from blaze_net import app
from blaze_net.routes import *

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple('localhost', 5000, app, use_reloader=True)