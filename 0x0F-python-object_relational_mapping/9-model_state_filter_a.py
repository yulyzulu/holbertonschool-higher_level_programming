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
    s = Session()

    for i in s.query(State).filter(State.name.like('%a%')).order_by(State.id):
        print("{:d}: {:s}".format(i.id, i.name))
