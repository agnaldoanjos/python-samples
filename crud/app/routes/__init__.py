from app.routes.people import people_bp

def register_routes(app):
    app.register_blueprint(people_bp, url_prefix='/people')
