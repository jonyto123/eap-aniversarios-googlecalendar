from cal_setup import get_calendar_service

def main():
   service = get_calendar_service()
   eventos = service.events().list(calendarId='3n9foltmpq9c5h6isepsqurmlc@group.calendar.google.com', maxResults=2500).execute()

   # Call the Calendar API
   print('Getting list of calendars')
   calendars_result = service.calendarList().list().execute()

   calendars = calendars_result.get('items', [])

   if not calendars:
       print('No calendars found.')
   for calendar in calendars:
       summary = calendar['summary']
       id = calendar['id']
       primary = "Primary" if calendar.get('primary') else ""
       print("%s\t%s\t%s" % (summary, id, primary))

if __name__ == '__main__':
   main()

# from datetime import datetime, timedelta
# from cal_setup import get_calendar_service

# def main():
#    # creates one hour event tomorrow 10 AM IST
#    service = get_calendar_service()

#    d = datetime.now().date()
#    tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
#    start = tomorrow.isoformat()
#    end = (tomorrow + timedelta(hours=1)).isoformat()

#    event_result = service.events().insert(calendarId='75ce43ak86rp59m99508b2im4k@group.calendar.google.com',
#        body={
#            "summary": 'Automating calendar',
#            "description": 'This is a tutorial example of automating google calendar with python',
#            "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
#            "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
#        }
#    ).execute()

#    print("created event")
#    print("id: ", event_result['id'])
#    print("summary: ", event_result['summary'])
#    print("starts at: ", event_result['start']['dateTime'])
#    print("ends at: ", event_result['end']['dateTime'])

# if __name__ == '__main__':
#    main()