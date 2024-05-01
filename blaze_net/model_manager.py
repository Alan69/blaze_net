from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class ModelManager:
    Base = declarative_base()
    def __init__(self, database_url='sqlite:///blazenet.db'):
        self.engine = create_engine(database_url, echo=True)
        self.Base = declarative_base(bind=self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.metadata = MetaData(bind=self.engine)

    def create_all(self):
        self.Base.metadata.create_all(self.engine)

    def drop_all(self):
        self.Base.metadata.drop_all(self.engine)

    def migrate(self, model):
        model.__table__.create(self.engine, checkfirst=True)

    def rollback(self, model):
        model.__table__.drop(self.engine, checkfirst=True)

    def get_session(self):
        return self.Session()

    def get_engine(self):
        return self.engine