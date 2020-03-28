#!/usr/bin/python3
'''Module to execute functions'''

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localho\
st/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    f = 0
    for name in session.query(State).filter(State.name == sys.argv[4]):
        print("{}".format(name.id))
        f = 1
    if f == 0:
        print("Not found")
