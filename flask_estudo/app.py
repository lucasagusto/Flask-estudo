# flask_estudo/app.py
from flask import Flask

# sempre relativos, pois o ficheiro reside dentro de flask_estudo/
from .routes.home    import home_route
from .routes.cliente import cliente_route


def create_app(testing: bool = False):
    app = Flask(__name__)
    app.register_blueprint(home_route)
    app.register_blueprint(cliente_route, url_prefix="/clientes")
    if testing:
        app.config.update(TESTING=True)
    return app


if __name__ == "__main__":
    # este bloco só roda em execução direta:
    #   python -m flask_estudo.app
    create_app().run(debug=True, port=5050)