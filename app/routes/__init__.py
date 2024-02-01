from .predict import register_predict_route

def init_routes(app):
    register_predict_route(app)