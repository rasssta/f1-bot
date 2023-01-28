@service
def f1_last_race():
  import requests
  import json
  from prettytable import PrettyTable

  url = "https://ergast.com/api/f1/current/22/results.json"
  response = task.executor(requests.get, url)
  data = json.loads(response.text)

  # Telegram bot configurations
  token = 'XYZ'
  chatId = '-XYZ'
 
  # Create table and columns
  table = PrettyTable(["Pos.", "Driver", "Time"])
  table.align = "l"
  
  for result in data['MRData']['RaceTable']['Races'][0]['Results']:
      pos = f"P{result['position']}"
      name = f"{result['Driver']['givenName']} {result['Driver']['familyName']}" 
      if result['status'] == "Finished":
          table.add_row([ pos, name,  result['Time']['time'] ])
      else:
          table.add_row([ pos, name, result['status'] ])
  # Create message variable and clean it from + signs
  message = f"<pre>{table}</pre>"
  formattedMessage = message.replace("+", "%2B")

  # Send message
  telegramUrl = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatId}&disable_notification=true&parse_mode=HTML&text={formattedMessage}"
  task.executor(requests.get, telegramUrl)
