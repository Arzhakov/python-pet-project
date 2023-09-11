from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import settings

manager = settings.SettingsManager()
db_path = manager.get_setting('database', '~/.ppp/library.db')

engine = create_engine(f'sqlite:///{db_path}')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Book(Base):
    __tablename__ = 'Book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String)
    title = Column(String)
    url = Column(String)
    folder = Column(String)

Base.metadata.create_all(engine)

def create_book(author, title, url, folder):
    new_book = Book(author=author, title=title, url=url, folder=folder)
    session.add(new_book)
    session.commit()

def find_book_by_url(url):
    book = session.query(Book).filter_by(url=url).first()
    return book

session.close()