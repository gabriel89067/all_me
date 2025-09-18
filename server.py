import os
import json
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# --- CONFIGURAÇÕES DA API DO WHATSAPP (pegue do seu painel da Meta) ---
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
RECIPIENT_WAID = os.getenv("RECIPIENT_WAID") # Número de destino no formato internacional (ex: 5531999998888)
WHATSAPP_API_URL = f"https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/messages"

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
    
    # IMPORTANTE: O payload depende do seu template pré-aprovado na Meta.
    # Este é um exemplo para um template chamado 'device_status_update'
    # com dois parâmetros: {{1}} para o nome da variável e {{2}} para o status.
    payload = {
        "messaging_product": "whatsapp",
        "to": RECIPIENT_WAID,
        "type": "template",
        "template": {
            "name": "device_status_update", # Nome do seu template
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
        response.raise_for_status()  # Lança um erro para respostas HTTP 4xx/5xx
        
        print("Resposta da API do WhatsApp:", response.json())
        return True
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar mensagem para o WhatsApp: {e}")
        print("Corpo da resposta:", e.response.text if e.response else "Nenhuma resposta")
        return False


if __name__ == '__main__':
    # Roda o servidor na porta 5000, acessível por qualquer IP na sua rede.
    app.run(host='0.0.0.0', port=5000, debug=True)
