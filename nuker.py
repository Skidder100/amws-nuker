import requests
import time

logo = """
                                        /$$                                  /$$                                
                                      | $/                                 | $$                                
  /$$$$$$  /$$$$$$/$$$$  /$$  /$$  /$$|_//$$$$$$$       /$$$$$$$  /$$   /$$| $$   /$$  /$$$$$$   /$$$$$$       
 |____  $$| $$_  $$_  $$| $$ | $$ | $$  /$$_____/      | $$__  $$| $$  | $$| $$  /$$/ /$$__  $$ /$$__  $$      
  /$$$$$$$| $$ \ $$ \ $$| $$ | $$ | $$ |  $$$$$$       | $$  \ $$| $$  | $$| $$$$$$/ | $$$$$$$$| $$  \__/      
 /$$__  $$| $$ | $$ | $$| $$ | $$ | $$  \____  $$      | $$  | $$| $$  | $$| $$_  $$ | $$_____/| $$            
|  $$$$$$$| $$ | $$ | $$|  $$$$$/$$$$/  /$$$$$$$/      | $$  | $$|  $$$$$$/| $$ \  $$|  $$$$$$$| $$            
 \_______/|__/ |__/ |__/ \_____/\___/  |_______/       |__/  |__/ \______/ |__/  \__/ \_______/|__/            
"""

def send_discord_message(webhook_url, message, channel, bot_name, delay_seconds):
    payload = {
        "content": message,
        "username": bot_name
    }

    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        print(f"Message sent to #{channel} by {bot_name}: {message}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")

    time.sleep(delay_seconds)

def main():
    webhook_url = input("Enter your Discord webhook URL: ")
    message = input("Enter the message you want to send: ")
    channel = input("Enter the channel name (without the '#'): ")
    bot_name = input("Enter the bot name: ")
    delay_seconds = float(input("Enter the delay between messages (in seconds): "))

    while True:
        send_discord_message(webhook_url, message, channel, bot_name, delay_seconds)
        
if __name__ == "__main__":
    print(logo)
    print("BE WARNED! Discord rate limits can make the bot be slower over time. There is no way to by pass this.")
    main()
