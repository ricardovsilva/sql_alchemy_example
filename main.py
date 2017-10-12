from database.schema import Event
from database.schema import Database
import datetime

db = Database()
db.create()

event = Event()
event.session_id = 'foo_session'
event.datetime = datetime.datetime.now()
event.url = 'http://foo.com.br'

db.get_session().add(event)
import pdb
pdb.set_trace()