from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
            }
            .container {
                max-width: 600px;
                margin: auto;
                padding: 20px;
                background: white;
                box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            }
            .card {
                box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
                text-align: center;
                padding: 20px;
            }
            .title {
                color: grey;
                font-size: 18px;
            }
            button {
                border: none;
                outline: 0;
                display: inline-block;
                padding: 8px;
                color: white;
                background-color: #000;
                text-align: center;
                cursor: pointer;
                width: 100%;
                font-size: 18px;
            }
            input {
                width: 100%;
                padding: 10px;
                margin: 5px 0;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            button:hover {
                opacity: 0.7;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Registro de Usuario</h2>
            <div class="card">
                <img src="https://via.placeholder.com/150" alt="Usuario" style="width:100%">
                <h1>Registro Rápido</h1>
                <p class="title">Únete a nosotros y disfruta de nuestros servicios.</p>
                <form>
                    <input type="text" placeholder="Nombre" required>
                    <input type="email" placeholder="Correo Electrónico" required>
                    <p><button type="submit">Registrar</button></p>
                </form>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
