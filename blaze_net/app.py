import os
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from jinja2 import Environment, FileSystemLoader
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug.serving import run_simple
import json

class BlazeNet:
    def __init__(self, template_path='blaze_net/templates/', static_path='static', database_url='sqlite:///blazenet.db'):
        self.url_map = Map()
        self.template_env = Environment(loader=FileSystemLoader(template_path))
        self.engine = create_engine(database_url, echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.static_path = static_path

    def route(self, rule):
        def decorator(f):
            def wrapper(*args, **kwargs):
                return f(*args, **kwargs)
            rule_obj = Rule(rule, endpoint=f)
            self.url_map.add(rule_obj)
            return wrapper
        return decorator

    def __call__(self, environ, start_response):
        request = Request(environ)
        if request.path.startswith('/static/'):
            return self.serve_static(environ, start_response)
        else:
            response = self.dispatch_request(request)
            if isinstance(response, str):
                response = Response(response, content_type='text/html')
            return response(environ, start_response)
        
    def json_response(self, data, status_code=200):
        json_data = json.dumps(data)
        return Response(json_data, status=status_code, content_type='application/json')

    def serve_static(self, environ, start_response):
        path = environ['PATH_INFO']
        if path.startswith('/static/'):
            full_path = os.path.join(self.static_path, path.lstrip('/static/'))
            if os.path.exists(full_path) and os.path.isfile(full_path):
                with open(full_path, 'rb') as f:
                    content = f.read()
                mime_type = self.get_mimetype(full_path)
                response = Response(content, mimetype=mime_type)
                return response(environ, start_response)
        raise NotFound()

    def get_mimetype(self, path):
        mime_types = {
            '.css': 'text/css',
            '.js': 'application/javascript',
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.svg': 'image/svg+xml'
        }
        _, ext = os.path.splitext(path)
        return mime_types.get(ext.lower(), 'application/octet-stream')

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return endpoint(request, **values)
        except HTTPException as e:
            # Handle HTTP exceptions
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        if isinstance(response, str):
            response = Response(response, content_type='text/html')
        return response(environ, start_response)

    def run(self, host='localhost', port=5000, use_reloader=False):
        run_simple(host, port, self.wsgi_app, use_reloader=use_reloader)
