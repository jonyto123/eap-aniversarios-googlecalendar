import csv
from Elemento import Elemento
from datetime import datetime
from cal_setup import get_calendar_service
import time 

Elementos = []
with open('grupo-74-aniversarios - Grupo.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, )
    for idx, row in enumerate(reader):
        if idx == 0:
            continue
        # print(str(idx) + str(row))
        data = datetime.strptime(row[4],'%Y-%m-%d' )
        elem = Elemento(row[1], data, row[2])
        Elementos.append(elem)


service = get_calendar_service()

eventos = service.events().list(calendarId='3n9foltmpq9c5h6isepsqurmlc@group.calendar.google.com', maxResults=2500).execute()

for ev in eventos['items']:
    service.events().delete(calendarId='3n9foltmpq9c5h6isepsqurmlc@group.calendar.google.com', eventId=ev['id']).execute()

# # service.calendars().delete(calendarId='75ce43ak86rp59m99508b2im4k@group.calendar.google.com')
# calendario = service.calendars().insert(body = {
#     #"id": "A String", # Identifier of the calendar. To retrieve IDs call the calendarList.list() method.
#     "summary": "AniversariosGrupo", # Title of the calendar.
#     # "conferenceProperties": { # Conferencing properties for this calendar, for example what types of conferences are allowed.
#     #   "allowedConferenceSolutionTypes": [ # The types of conference solutions that are supported for this calendar.
#     #       # The possible values are:
#     #       # - "eventHangout"
#     #       # - "eventNamedHangout"
#     #       # - "hangoutsMeet"  Optional.
#     #     "A String",
#     #   ],
#     # },
#     "description": "Aniversario do grupo", # Description of the calendar. Optional.
#     # "location": "A String", # Geographic location of the calendar as free-form text. Optional.
#     "kind": "calendar#calendar", # Type of the resource ("calendar#calendar").
#     # "etag": "A String", # ETag of the resource.
#     "timeZone": "Europe/Lisbon", # The time zone of the calendar. (Formatted as an IANA Time Zone Database name, e.g. "Europe/Zurich".) Optional.
#   }).execute()
for elem in Elementos:
    #time.sleep(0.3)
    print({
           "summary": 'Aniversario - ' + str(elem.divisao) + ' - ' + str(elem.nome),
           "description": 'Aniversario do ' + str(elem.divisao),
           "start": {"dateTime": elem.dataNascimento.isoformat(), "timeZone": 'Europe/Lisbon'},
           "end": {"dateTime": elem.dataNascimento.isoformat(), "timeZone": 'Europe/Lisbon'},
           "recurrence": [
                  'RRULE:FREQ=YEARLY'
             ]
           
       })
    event_result = service.events().insert(calendarId='3n9foltmpq9c5h6isepsqurmlc@group.calendar.google.com',
       body={
           "summary": 'Aniversario - ' + str(elem.divisao) + ' - ' + str(elem.nome),
           "description": 'Aniversario do ' + str(elem.divisao),
           "start": {"dateTime": elem.dataNascimento.isoformat(), "timeZone": 'Europe/Lisbon'},
           "end": {"dateTime": elem.dataNascimento.isoformat(), "timeZone": 'Europe/Lisbon'},
           "recurrence": [
                  'RRULE:FREQ=YEARLY'
             ]
           
       }
    ).execute()
    
    