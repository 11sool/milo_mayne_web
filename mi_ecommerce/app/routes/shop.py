from flask import Blueprint, render_template

shop_bp = Blueprint("shop", __name__)


@shop_bp.route("/")
def index():
    return "<h1>Servidor iniciado correctamente</h1><p>E-commerce en marcha.</p>"


@shop_bp.route("/carrito")
def carrito():
    return render_template("carrito.html")