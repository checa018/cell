from flask import Flask
from .extensions import appbuilder, db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)
    with app.app_context():
        appbuilder.init_app(app, db.session)

        
        
        # Importante: Carga modelos y vistas
        from . import models
        from . import views  

        # Registrar el blueprint de IA
        from .ai.asistente_ai import asistente_bp
        app.register_blueprint(asistente_bp)

        # Enlace del Asistente IA
        appbuilder.add_link("Asistente IA", href="/ai/asistente", icon="fa-robot")

    return app

app = create_app()