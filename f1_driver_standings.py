@service
def f1_driver_standings():
  import requests
  import json
  from prettytable import PrettyTable

  url = "https://ergast.com/api/f1/2022/driverStandings.json?limit=30"
  response = task.executor(requests.get, url)
  data = json.loads(response.text)

  # Telegram bot configurations
  token = 'XYZ'
  chatId = '-XYZ'
 
  # Create table and columns
  table = PrettyTable(["Pos.", "Driver", "Points"])
  table.align = "l"
  
  for result in data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']:
      pos = f"P{result['position']}"
      name = f"{result['Driver']['givenName']} {result['Driver']['familyName']}" 
      table.add_row([ pos, name,  result['points'] ])
  # Create message variable and clean it from + signs
  message = f"<pre>{table}</pre>"
  formattedMessage = message.replace("+", "%2B")

  # Send message
  telegramUrl = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatId}&disable_notification=true&parse_mode=HTML&text={formattedMessage}"
  task.executor(requests.get, telegramUrl)
