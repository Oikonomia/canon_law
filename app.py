from canon_law import __init__ as handler

if __name__ == "__main__":
    app = handler.create_app()
    app.run()