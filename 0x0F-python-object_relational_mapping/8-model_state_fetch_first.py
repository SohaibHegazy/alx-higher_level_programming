#!/usr/bin/python3
'''
a script that prints the first State object from the database hbtn_0e_6_usa
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    query = session.query(State).order_by(State.id).first()

    if query is None:
        print('Nothing')
    else:
        print('{}: {}'.format(query.id, query.name))

    session.close()
