from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask in Docker!"

@app.route("/about")
def about():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>О компании</title>
    </head>
    <body>
        <h1>О нашей компании</h1>
        <p>Мы изучаем Flask и Docker!</p>
    </body>
    </html>
    """
@app.route("/contacts")
def contacts():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Контакты</title>
    </head>
    <body>
        <h1>Контакты нашей компании</h1>
        <p>Мы обязательно сообщим вам наши контакты, если это будет необходимо</p>
    </body>
    </html>
    """    

@app.route("/posts")
def posts():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Список постов</title>
    </head>
    <body>
        <h1>Публикации нашей компании</h1>
        <p>Мы разместим здесь список наших постов, когда они появятся</p>
    </body>
    </html>
    """        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)