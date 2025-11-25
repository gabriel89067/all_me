import os
import json
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)


WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
RECIPIENT_WAID = os.getenv("RECIPIENT_WAID")
WHATSAPP_API_URL = f"https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/messages"

@app.route('/analysis', methods=['POST'])
def tago_analysis():
    """
    Este endpoint recebe os dados enviados pela Analysis do Tago.io.
    """
    print("Recebida requisição do Tago.io!")

   
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "Nenhum dado recebido"}), 400

    latest_data = data[0]
    device_status = latest_data.get('value')
    device_variable = latest_data.get('variable')

    print(f"Variável: {device_variable}, Valor: {device_status}")

  
    message_sent = send_whatsapp_message(device_variable, device_status)

    if message_sent:
        return jsonify({"status": "success", "message": "Mensagem do WhatsApp enviada."})
    else:
        return jsonify({"status": "error", "message": "Falha ao enviar mensagem do WhatsApp."}), 500


def send_whatsapp_message(variable_name, status):
    """
    Função que monta e envia a mensagem usando a API Cloud da Meta.
    Usa um TEMPLATE pré-aprovado.
    """
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json",
    }
    
    payload = {
        "messaging_product": "whatsapp",
        "to": RECIPIENT_WAID,
        "type": "template",
        "template": {
            "name": "device_status_update", 
            "language": {
                "code": "pt_BR"
            },
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": str(variable_name)
                        },
                        {
                            "type": "text",
                            "text": str(status)
                        }
                    ]
                }
            ]
        }
    }

    try:
        response = requests.post(WHATSAPP_API_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  
        
        print("Resposta da API do WhatsApp:", response.json())
        return True
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar mensagem para o WhatsApp: {e}")
        print("Corpo da resposta:", e.response.text if e.response else "Nenhuma resposta")
        return False


if __name__ == '__main__':
   
    app.run(host='0.0.0.0', port=5000, debug=True)
