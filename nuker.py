import requests
import time

# ASCII art logo
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

def send_discord_message(webhook_url, message, channel, delay_seconds):
    payload = {
        "content": message,
        "username": "CustomBot"
    }

    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        print(f"Message sent to #{channel}: {message}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")

    time.sleep(delay_seconds)

def main():
    webhook_url = input("Enter your Discord webhook URL: ")
    message = input("Enter the message you want to send: ")
    channel = input("Enter the channel name (without the '#'): ")
    delay_seconds = float(input("Enter the delay between messages (in seconds): "))

    while True:
        send_discord_message(webhook_url, message, channel, delay_seconds)

if __name__ == "__main__":
    print(logo)  # Display the ASCII art logo
    main()
