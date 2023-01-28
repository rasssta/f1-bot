@service
def f1_help():
  import requests
  from prettytable import PrettyTable

  # Telegram bot configurations
  token = 'XYZ'
  chatId = '-XYZ'
 
  # Create table and columns
  table = PrettyTable(["Command", "Description"])
  table.align = "l"

  table.add_row([ "/constructors", "Constructor standings" ])
  table.add_row([ "/days", "Days until next race" ])
  table.add_row([ "/drivers", "Driver standings" ])
  table.add_row([ "/help", "Overview of all bot commands" ])
  table.add_row([ "/last", "Drivers result from last race" ])
  table.add_row([ "/next", "Information about next race" ])

  # Create message variable and clean it from + signs
  message = f"<pre>{table}</pre>"
  formattedMessage = message.replace("+", "%2B")

  # Send message
  telegramUrl = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatId}&parse_mode=HTML&disable_notification=true&text={formattedMessage}"
  task.executor(requests.get, telegramUrl)
