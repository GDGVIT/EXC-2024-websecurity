from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Setup
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

# Query using ORM
user_id = 1  # Safe to use, the ORM takes care of parameterization
user = session.query(User).filter(User.id == user_id).one()

print(user.name, user.email)

# Close the session
session.close()
