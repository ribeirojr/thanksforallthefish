from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Thanks, Base

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def insert_thanks(email, message):
    """Creates new Thank you note."""
    thanks = Thanks(email=email, message=message)
    session.add(thanks)
    session.commit()


def get_all_thanks():
    """Returns all the thank you notes created."""
    return session.query(Thanks).all()
