from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    session_id = Column(String)
    datetime = Column(DateTime)
    url = Column(String)

    def __repr__(self):
        return "<Event(session_id='%s', datetime='%s', url='%s')>" % (
            self.session_id, str(self.datetime), self.url
        )

class Database:   
    def __init__(self, connection_string = None):
        self.engine = create_engine(connection_string or 'sqlite:///foo.db')
        self.session = None

    def create(self):
        Base.metadata.create_all(self.engine)

    def get_session(self):
        if self.session:
            return self.session
        
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()
        return self.session