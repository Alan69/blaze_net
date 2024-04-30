from werkzeug.exceptions import HTTPException
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from jinja2 import Environment, FileSystemLoader
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class BlazeNet:
    def __init__(self, template_path='blaze_net/templates/'):
        self.url_map = Map()
        self.template_env = Environment(loader=FileSystemLoader(template_path))
        self.engine = create_engine('sqlite:///:memory:', echo=True)
        self.Session = sessionmaker(bind=self.engine)

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
        response = self.dispatch_request(request)
        
        # Check if response is a string
        if isinstance(response, str):
            # If response is a string, create a Response object
            response = Response(response, content_type='text/html')
        
        return response(environ, start_response)

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return endpoint(request, **values)
        except HTTPException as e:
            # Handle HTTP exceptions
            return e

app = BlazeNet()
