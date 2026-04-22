import requests

def send(msg):
    TOKEN = "TOKEN" # Kendi token'ını yaz (tırnakları silme)
    CHAT_ID = "ID"  # Kendi numaranı yaz (tırnakları silme)
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    try:
        response = requests.post(url, data={
            "chat_id": CHAT_ID,
            "text": str(msg),
            "parse_mode": "HTML"  
        })
        
        if response.status_code != 200:
            print(f"Telegram Hatası: {response.text}")
            
    except Exception as e:
        print(f"Telegram bildirimi gönderilirken ağ hatası: {e}")