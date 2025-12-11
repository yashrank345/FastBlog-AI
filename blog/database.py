from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


SQLALCHAMY_DATABASE_URL = 'mysql+mysqlconnector://root:@localhost/blog'


engine  = create_engine(SQLALCHAMY_DATABASE_URL )

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
        
    finally:    
        db.close()