#!/usr/bin/python3
"""
class definition of a State and an instance
 Base = declarative_base()
"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_city import City
    from model_state import Base, State
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           ''.format(sys.argv[1], sys.argv[2],
                                     sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for st, ct in session.query(
            State, City).where(City.state_id
                               == State.id).order_by(City.id).all():
        print('{}: ({}) {}'.format(st.name, ct.id,
                                 ct.name))
    session.commit()
    session.close()
