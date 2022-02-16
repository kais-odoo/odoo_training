import os
from urllib import response
import redis
from werkzeug import run_simple
from werkzeug.urls import url_parse
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader

class werkzueg:
    def __init__(self, config):
        self.redis = redis.Redis(config['redis_host'],config['redis_port'])
        template_path = os.path.join(os.path.dirname(__file__), 'template')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)




        self.url_map = Map([
            Rule('/', endpoint='HomePage'),
            # Rule('/<short_id>', endpoint='follow_short_link'),
            # Rule('/<short_id>+', endpoint='short_link_details')
        ])




    def on_HomePage(self, request):
        return self.render_template('index.html')


    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')



    def dispatch_request(self, request):
        # return Response('hello world!!!')
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, f'on_{endpoint}')(request, **values)
        except HTTPException as e:
            return e




    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)




    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)



def create_app(redis_host='localhost', redis_port=6379, with_static=True):
        app = werkzueg({
            'redis_host' : redis_host,
            'redis_port' : redis_port
        })
        if with_static:
            app.wsgi_app = SharedDataMiddleware(app.wsgi_app,{
                '/static' : os.path.join(os.path.dirname(__file__),'static')
            })
            return app


if __name__ == '__main__':
    app = create_app()
    run_simple('127.0.0.1', 8000, app, use_debugger=True, use_reloader=True)
        
 
 
