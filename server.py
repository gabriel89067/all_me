import os
import json
import requests
from flask import Flask, request, jsonify

import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/analysis', methods=['POST'])
def tago_analysis():
    """
    Este endpoint recebe os dados enviados pela Analysis do Tago.io.
    """
    print("Recebida requisição do Tago.io!")

    # Pega o corpo da requisição (geralmente uma lista de objetos)
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "Nenhum dado recebido"}), 400

    # O Tago.io envia um array. Vamos pegar o dado mais recente (o primeiro).
    # Ajuste isso conforme a lógica do seu dispositivo.
    latest_data = data[0]
    device_status = latest_data.get('value')
    device_variable = latest_data.get('variable')

    print(f"Variável: {device_variable}, Valor: {device_status}")

    # Formata a mensagem e envia para o WhatsApp
    message_sent =send_email(device_variable, device_status)

    if message_sent:
        return jsonify({"status": "success", "message": "Mensagem do WhatsApp enviada."})
    else:
        return jsonify({"status": "error", "message": "Falha ao enviar mensagem do WhatsApp."}), 500


def send_email(variable_name, status):
    # Configuração da mensagem
    msg = EmailMessage()
    msg["Subject"] = "Teste de Envio Python"
    msg["From"] = "pur.equipamentos@gmail.com"
    msg["To"] = "gabrielsouza.oliveira630@gmail.com"
    msg.set_content(f"Mensagem de teste enviada .vari = {variable_name} // status = {status}.")

# Credenciais (Use Senha de Aplicativo se for conta pessoal!)
    email_login = "pur.equipametos@gmail.com"
    senha_app = "kjczghkwnvajnubq" 

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()      # Identifica-se para o servidor (boa prática)
            smtp.starttls()  # Criptografa a conexão
            smtp.ehlo()      # Re-identifica após criptografia (necessário em alguns servidores)
        
            smtp.login(email_login, senha_app)
            smtp.send_message(msg)
        
        print("Email enviado com sucesso!")

    except Exception as e:
        print(f"Erro ao enviar: {e}")

if __name__ == '__main__':
    # Roda o servidor na porta 5000, acessível por qualquer IP na sua rede.
    app.run(host='0.0.0.0', port=5000, debug=True)
