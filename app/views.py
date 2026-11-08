from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.security.sqla.models import User
from .extensions import appbuilder
from .models import Categoria, Marca, Producto, Cliente, Venta, DetalleVenta

# ==========================================
# 1. MÓDULO DE INVENTARIO
# ==========================================
class CategoriaView(ModelView):
    datamodel = SQLAInterface(Categoria)
    list_title = "Categorías de Productos"
    label_columns = {'nombre': 'Nombre', 'descripcion': 'Descripción'}

class MarcaView(ModelView):
    datamodel = SQLAInterface(Marca)
    list_title = "Marcas de Celulares"
    label_columns = {'nombre': 'Marca', 'pais_origen': 'País de Origen'}

class ProductoView(ModelView):
    datamodel = SQLAInterface(Producto)
    list_title = "Catálogo de Smartphones"
    list_columns = ['nombre', 'modelo', 'marca', 'categoria', 'almacenamiento', 'ram', 'precio', 'stock']
    label_columns = {
        'nombre': 'Dispositivo',
        'modelo': 'Modelo',
        'almacenamiento': 'Almacenamiento',
        'ram': 'RAM',
        'precio': 'Precio ($us)',
        'stock': 'Stock',
        'marca': 'Marca',
        'categoria': 'Categoría'
    }

appbuilder.add_view(CategoriaView, "Categorías", icon="fa-tags", category="Inventario", category_icon="fa-cubes")
appbuilder.add_view(MarcaView, "Marcas", icon="fa-apple", category="Inventario")
appbuilder.add_view(ProductoView, "Smartphones", icon="fa-mobile", category="Inventario")


# ==========================================
# 2. MÓDULO DE VENTAS
# ==========================================
class ClienteView(ModelView):
    datamodel = SQLAInterface(Cliente)
    list_title = "Gestión de Clientes"
    list_columns = ['nombre', 'ci_nit', 'telefono', 'direccion']
    label_columns = {'nombre': 'Nombre Completo', 'ci_nit': 'CI / NIT', 'telefono': 'Teléfono', 'direccion': 'Dirección'}

class VentaView(ModelView):
    datamodel = SQLAInterface(Venta)
    list_title = "Registro de Ventas"
    list_columns = ['id', 'fecha', 'cliente', 'metodo_pago', 'total']
    label_columns = {'fecha': 'Fecha', 'cliente': 'Cliente', 'metodo_pago': 'Método de Pago', 'total': 'Total ($us)'}

class DetalleVentaView(ModelView):
    datamodel = SQLAInterface(DetalleVenta)
    list_title = "Detalle de Ítems Vendidos"
    list_columns = ['id', 'venta', 'producto', 'cantidad', 'precio_unitario', 'imei_serie']
    label_columns = {'venta': 'Venta', 'producto': 'Producto', 'cantidad': 'Cantidad', 'precio_unitario': 'Precio Unit.', 'imei_serie': 'IMEI / Serie'}

appbuilder.add_view(ClienteView, "Clientes", icon="fa-address-book", category="Ventas", category_icon="fa-shopping-cart")
appbuilder.add_view(VentaView, "Ventas Realizadas", icon="fa-money", category="Ventas")
appbuilder.add_view(DetalleVentaView, "Detalle de Venta", icon="fa-list-alt", category="Ventas")


# ==========================================
# 3. GESTIÓN DE PERSONAL Y USUARIOS
# ==========================================
class UsuarioSmartShopView(ModelView):
    datamodel = SQLAInterface(User)
    list_title = "Personal y Cuentas de Acceso"
    list_columns = ['username', 'first_name', 'last_name', 'email', 'active']
    add_columns = ['username', 'first_name', 'last_name', 'email', 'password', 'roles', 'active']
    edit_columns = ['first_name', 'last_name', 'email', 'roles', 'active']
    
    label_columns = {
        'username': 'Usuario',
        'first_name': 'Nombre',
        'last_name': 'Apellido',
        'email': 'Correo',
        'active': 'Activo',
        'roles': 'Rol'
    }

appbuilder.add_view(
    UsuarioSmartShopView,
    "Personal y Usuarios",
    icon="fa-users",
    category="SmartShop",
    category_icon="fa-store"
)