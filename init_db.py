from app import app, db
from app.models import Categoria, Marca, Producto, Cliente, Venta, DetalleVenta

with app.app_context():
    metadata = Categoria.metadata
    engine = db.engine
    for tabla in metadata.sorted_tables:
        print("--", tabla.name)
        
    metadata.create_all(bind=engine)
    print("creado correctamente")