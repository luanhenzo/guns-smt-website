from guns import create_app

app = create_app("configs.py")

if __name__ == '__main__':
    app.run()

