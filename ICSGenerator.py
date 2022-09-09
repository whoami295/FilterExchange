from icalendar import Calendar, Event, vCalAddress, vText
import pytz
from datetime import datetime
import os
from pathlib import Path

cal = Calendar()
cal.add('customer', 'MAILTO:abc@example.com')

event = Event()
event.add('summary', 'Miele Filter Exchange')
event.add('dtstart', datetime(2022, 10, 9, 8, 0, 0, tzinfo=pytz.utc))
event.add('dtend', datetime(2022, 10, 9, 10, 0, 0, tzinfo=pytz.utc))
event.add('dtstamp', datetime(2022, 10, 9, 0, 10, 0, tzinfo=pytz.utc))

organizer = vCalAddress('MAILTO:hello@example.com')
organizer.params['cn'] = vText('Miele')
organizer.params['role'] = vText('Customer Support')
event['organizer'] = organizer
event['location'] = vText('Home, Sweet Home')

cal.add_component(event)

directory = str(Path(__file__).parent) + "/"
print("ics file will be generatered at", directory)
f = open(os.path.join(directory, 'FilterExchange.ics'), 'wb')
f.write(cal.to_ical())
f.close()
