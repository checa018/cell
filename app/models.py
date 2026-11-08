from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime

class Categoria(Model):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    descripcion = Column(String(250), nullable=True)
    
    productos = relationship("Producto", back_populates="categoria")

    def __repr__(self):
        return self.nombre


class Marca(Model):
    __tablename__ = "marcas"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    pais_origen = Column(String(100), nullable=True)
    
    productos = relationship("Producto", back_populates="marca")

    def __repr__(self):
        return self.nombre


class Producto(Model):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    modelo = Column(String(100), nullable=False)
    almacenamiento = Column(String(50), nullable=True)  # Ej. 128GB, 256GB
    ram = Column(String(50), nullable=True)             # Ej. 6GB, 8GB
    precio = Column(Numeric(12, 2), default=0, nullable=False)
    stock = Column(Integer, default=0, nullable=False)
    
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    categoria = relationship("Categoria", back_populates="productos")

    marca_id = Column(Integer, ForeignKey("marcas.id"), nullable=False)
    marca = relationship("Marca", back_populates="productos")

    def __repr__(self):
        return f"{self.nombre} {self.modelo} ({self.almacenamiento})"


class Cliente(Model):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
    ci_nit = Column(String(50), unique=True, nullable=False)
    telefono = Column(String(30), nullable=True)
    direccion = Column(String(250), nullable=True)

    ventas = relationship("Venta", back_populates="cliente")

    def __repr__(self):
        return f"{self.nombre} (CI/NIT: {self.ci_nit})"


class Venta(Model):
    __tablename__ = "ventas"
    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime, default=datetime.datetime.now, nullable=False)
    total = Column(Numeric(12, 2), default=0, nullable=False)
    metodo_pago = Column(String(50), default="Efectivo", nullable=False)

    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    cliente = relationship("Cliente", back_populates="ventas")

    detalles = relationship("DetalleVenta", back_populates="venta", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Venta #{self.id} - Total: {self.total}"


class DetalleVenta(Model):
    __tablename__ = "detalles_venta"
    id = Column(Integer, primary_key=True)
    cantidad = Column(Integer, default=1, nullable=False)
    precio_unitario = Column(Numeric(12, 2), nullable=False)
    imei_serie = Column(String(100), unique=True, nullable=False)

    venta_id = Column(Integer, ForeignKey("ventas.id"), nullable=False)
    venta = relationship("Venta", back_populates="detalles")

    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    producto = relationship("Producto")

    def __repr__(self):
        return f"Detalle #{self.id} - IMEI: {self.imei_serie}"