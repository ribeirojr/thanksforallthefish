from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Thanks, Base

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def insertThanks(email, message):
	model = Thanks(email=email, message=message)
	session.add(model)
	session.commit()

def GetAllThanks():
	return session.query(Thanks).all()