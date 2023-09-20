#!/usr/bin/python3
"""
8-model_state_fetch_first module
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    instance = session.query(State).order_by(State.id).first()
    if instance:
        print("{}: {}".format(instance.id, instance.name))
    else:
        print("Nothing")

    session.close()
