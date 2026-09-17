from app import create_app

# Creamos la instancia de la aplicación Flask
app = create_app()

if __name__ == '__main__':
    # Arranca el servidor local en modo depuración (se reinicia solo si cambias algo)
    app.run(debug=True, port=5000)