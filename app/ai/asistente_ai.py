import os
from flask import Blueprint, render_template, request
from google import genai
from ..extensions import appbuilder  # Importamos appbuilder para pasarlo a la plantilla

asistente_bp = Blueprint('asistente', __name__, template_folder='templates', url_prefix='/ai')

def obtener_cliente_genai():
    api_key = os.environ.get("AI_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("No se configuró ninguna API key para la IA.")
    return genai.Client(api_key=api_key)

@asistente_bp.route('/asistente', methods=['GET', 'POST'])
def vista_asistente():
    respuesta = ""
    if request.method == 'POST':
        mensaje_usuario = request.form.get('pregunta', '')
        try:
            client = obtener_cliente_genai()
            prompt_sistema = (
                "Eres el asistente virtual experto de 'SmartShop', una tienda de venta de celulares y accesorios. "
                "Tu objetivo es ayudar recomendando especificaciones técnicas de smartphones (RAM, ROM, cámaras, marcas) "
                "y guiando en las compras de forma amable, profesional y comercial en español."
            )
            response = client.models.generate_content(
            model='gemini-3.8-flash',  # <--- Actualizamos el modelo aquí
                contents=f"{prompt_sistema}\n\nPregunta del cliente: {mensaje_usuario}",
            )
            respuesta = response.text
        except Exception as e:
            respuesta = f"Error al conectar con la IA: {str(e)}"
            
    # Pasamos explícitamente appbuilder=appbuilder aquí
    return render_template('ai/asistente.html', respuesta=respuesta, appbuilder=appbuilder)