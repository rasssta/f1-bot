@service
def f1_next_race():
  import requests
  from datetime import datetime

  # Telegram bot configurations
  token = 'XYZ'
  chatId = '-XYZ'

  raceInformationAttrs = state.getattr('sensor.formula1_race_information')
  circuitInformationAttrs = state.getattr('sensor.formula1_circuit_information')
  locationInformationAttrs = state.getattr('sensor.formula1_location_information')

  message = f"It's time for the {raceInformationAttrs['raceName']} (R{raceInformationAttrs['round']}) at {circuitInformationAttrs['circuitName']} ({locationInformationAttrs['country']})\n\n"

  fp1 = state.get('sensor.formula1_fp1')
  fp1Attrs = state.getattr('sensor.formula1_fp1')
  fp1Day = datetime.strptime(fp1Attrs['date'], '%Y-%m-%d').date().strftime("%a")
  message += f"FP1:\t{fp1Attrs['date']} {fp1} ({fp1Day})\n"

  fp2 = state.get('sensor.formula1_fp2')
  fp2Attrs = state.getattr('sensor.formula1_fp2')
  fp2Day = datetime.strptime(fp2Attrs['date'], '%Y-%m-%d').date().strftime("%a")
  message += f"FP2:\t{fp2Attrs['date']} {fp2} ({fp2Day})\n"

  fp3 = state.get('sensor.formula1_fp3')
  fp3Attrs = state.getattr('sensor.formula1_fp3')
  fp3Day = datetime.strptime(fp3Attrs['date'], '%Y-%m-%d').date().strftime("%a")
  message += f"FP3:\t{fp3Attrs['date']} {fp3} ({fp3Day})\n"

  qual = state.get('sensor.formula1_qualification')
  qualAttrs = state.getattr('sensor.formula1_qualification')
  qualDay = datetime.strptime(qualAttrs['date'], '%Y-%m-%d').date().strftime("%a")
  message += f"Qual:\t{qualAttrs['date']} {qual} ({qualDay})\n"

  race = state.get('sensor.formula1_race')
  raceAttrs = state.getattr('sensor.formula1_race')
  raceDay = datetime.strptime(raceAttrs['date'], '%Y-%m-%d').date().strftime("%a")
  message += f"Race:\t{raceAttrs['date']} {race} ({raceDay})\n\n"

  # Send message
  telegramUrl = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatId}&disable_notification=true&parse_mode=HTML&text={message}"
  task.executor(requests.get, telegramUrl)
