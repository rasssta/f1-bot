@service
def f1_days(days=None, circuit=None):
  import requests

  # Telegram bot configurations
  token = 'XYZ'
  chatId = '-XYZ'
 
  message = f"{days} days until the next race at {circuit}."

  # Send message
  telegramUrl = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatId}&disable_notification=true&parse_mode=HTML&text={message}"
  task.executor(requests.get, telegramUrl)
