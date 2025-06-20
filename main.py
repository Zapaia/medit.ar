import os
from twilio.rest import Client
from dotenv import load_dotenv

# Cargar variables de entorno del archivo .env
load_dotenv()

# Variables de entorno
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_SANDBOX_NUMBER")
my_number = os.getenv("MY_WHATSAPP_NUMBER")

# Crear cliente Twilio
client = Client(account_sid, auth_token)

def send_whatsapp_message(body, to):
    message = client.messages.create(
        body=body,
        from_=twilio_number,
        to=to
    )
    print(f"Mensaje enviado con SID: {message.sid}")

if __name__ == "__main__":
    texto = "Hola desde tu bot de meditación 🧘‍♂️. Este es un mensaje de prueba desde Twilio Sandbox."
    send_whatsapp_message(texto, my_number)
