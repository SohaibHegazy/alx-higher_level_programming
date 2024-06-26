#!/usr/bin/python3
'''
prints all City objects from the database hbtn_0e_14_usa
'''
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    query = session.query(City.id, City.name, State.name).join(
        State, State.id == City.state_id).order_by(City.id)

    for instace in query:
        print('{}: ({}) {}'.format(instace[2], instace[0], instace[1]))

    session.close()
