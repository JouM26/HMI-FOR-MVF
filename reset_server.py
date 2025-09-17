# -*- coding: utf-8 -*-
from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Recuperar Contraseña</title>
    <style>
        body {
            background: #f5fafd;
            font-family: 'Segoe UI', Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 410px;
            margin: 40px auto;
            background: #fff;
            border-radius: 18px;
            box-shadow: 0 4px 24px rgba(30,163,236,0.13);
            padding: 32px 32px 24px 32px;
            text-align: center;
        }
        .titulo {
            font-size: 2.1em;
            font-weight: bold;
            color: #1ca3ec;
            letter-spacing: 2px;
            margin-bottom: 10px;
            text-shadow: 1px 2px 6px #b3e6fc;
        }
        .icono-usuario {
            width: 80px;
            height: 80px;
            background: #eaf6fb;
            border-radius: 50%;
            display: inline-block;
            margin-bottom: 12px;
            position: relative;
        }
        .icono-usuario:before {
            content: "";
            display: block;
            width: 36px;
            height: 36px;
            background: #1ca3ec;
            border-radius: 50%;
            position: absolute;
            left: 22px;
            top: 16px;
        }
        .icono-usuario:after {
            content: "";
            display: block;
            width: 60px;
            height: 30px;
            background: #1ca3ec;
            border-radius: 0 0 30px 30px / 0 0 24px 24px;
            position: absolute;
            left: 10px;
            top: 48px;
        }
        .instrucciones {
            font-size: 1em;
            color: #444;
            margin-bottom: 18px;
            text-align: left;
        }
        .input-label {
            font-size: 0.98em;
            color: #1ca3ec;
            font-weight: bold;
            display: block;
            margin-bottom: 4px;
            text-align: left;
        }
        .input-box {
            width: 100%;
            padding: 10px 12px;
            border: 1.5px solid #1ca3ec;
            border-radius: 6px;
            margin-bottom: 16px;
            font-size: 1em;
            outline: none;
            transition: border 0.2s;
        }
        .input-box:focus {
            border: 2px solid #1ca3ec;
        }
        .btn-recuperar {
            width: 100%;
            background: #1ca3ec;
            color: #fff;
            font-size: 1.1em;
            font-weight: bold;
            border: none;
            border-radius: 6px;
            padding: 12px 0;
            cursor: pointer;
            margin-top: 8px;
            box-shadow: 0 2px 8px #b3e6fc;
            transition: background 0.2s;
        }
        .btn-recuperar:hover {
            background: #1689c7;
        }
        .msg {
            margin-top: 14px;
            color: #e74c3c;
            font-weight: bold;
        }
        @media (max-width: 500px) {
            .container { width: 98vw; padding: 10px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="titulo">RECUPERAR CONTRASEÑA</div>
        <div class="icono-usuario"></div>
        <div class="instrucciones">
                        Escribe tu nueva contraseña para el usuario <strong>{{ user }}</strong>.
        </div>
        <form method="post">
            <span class="input-label">Nueva contraseña:</span>
            <input class="input-box" type="password" name="new_pass" placeholder="Nueva contraseña" required>
            <span class="input-label">Confirmar contraseña:</span>
            <input class="input-box" type="password" name="confirm_pass" placeholder="Confirmar contraseña" required>
            <input class="btn-recuperar" type="submit" value="RECUPERAR">
        </form>
        {% if msg %}
        <div class="msg">{{ msg }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/reset", methods=["GET", "POST"])
def reset():
    token = request.args.get("token")
    if not token:
        return "Token inválido", 400
    usuario = token.replace("_token", "")
    msg = ""
    if request.method == "POST":
        new_pass = request.form.get("new_pass")
        confirm_pass = request.form.get("confirm_pass")
        if new_pass != confirm_pass:
            msg = "Las contraseñas no coinciden"
        elif len(new_pass) < 3:
            msg = "La contraseña es muy corta"
        else:
            try:
                con = sqlite3.connect("registro.db")
                cur = con.cursor()
                cur.execute("UPDATE usuarios SET clave=? WHERE usuario=?", (new_pass, usuario))
                con.commit()
                if cur.rowcount == 0:
                    msg = "Usuario no encontrado"
                else:
                    msg = "Contraseña actualizada correctamente"
                cur.close()
                con.close()
            except Exception as e:
                msg = f"Error: {e}"
    return render_template_string(HTML_FORM, user=usuario, msg=msg)

if __name__ == "__main__":
    app.run(port=5000)