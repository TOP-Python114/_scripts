from sqlalchemy import create_engine, text, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String

from pprint import pprint


Base = declarative_base()

author_publisher = Table(
    'author_publisher',
    Base.metadata,
    Column('author_id', Integer, ForeignKey('author.author_id')),
    Column('publisher_id', Integer, ForeignKey('publisher.publisher_id')),
)
book_publisher = Table(
    'book_publisher',
    Base.metadata,
    Column('book_id', Integer, ForeignKey('book.book_id')),
    Column('publisher_id', Integer, ForeignKey('publisher.publisher_id')),
)


class Author(Base):
    __tablename__ = 'author'

    id = Column('author_id', Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    publishers = relationship('Publisher',
                              secondary=author_publisher,
                              back_populates='authors')

    def __repr__(self):
        return f"<Author: {self.first_name} {self.last_name}>"


class Book(Base):
    __tablename__ = 'book'

    id = Column('book_id', Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('author.author_id'))
    publishers = relationship('Publisher',
                              secondary=book_publisher,
                              back_populates='books')

    def __repr__(self):
        return f"<Book: {self.title}>"


class Publisher(Base):
    __tablename__ = 'publisher'

    id = Column('publisher_id', Integer, primary_key=True)
    name = Column(String)
    authors = relationship('Author',
                           secondary=author_publisher,
                           back_populates='publishers')
    books = relationship('Book',
                         secondary=book_publisher,
                         back_populates='publishers')

    def __repr__(self):
        return f"<Publisher: {self.name}>"


# тесты
if __name__ == '__main__':
    sqlite_file = 'sqlite:///db.sqlite'
    engine = create_engine(sqlite_file)

    Session = sessionmaker(bind=engine)
    session = Session()

    # select * from author
    result = session.query(Author)
    # print(result)
    # print(type(result), end='\n\n')

    data = result.all()
    # pprint(data)
    # print(type(data), end='\n\n')

    clancy = data[2]
    # print(clancy)
    # print(clancy.__dict__)

    king_books = (session.query(Book)
                         .join(Author)
                         .where(text('author.last_name = "King"')))
    # print(king_books, '\n')
    king_books = (session.query(Book)
                         .join(Author, and_(Book.author_id == Author.id,
                                            Author.last_name == "King")))
    # print(king_books, '\n')
    # pprint(king_books.all())

    rh = session.query(Publisher).all()[0]
    # print(rh.authors)
    # print(rh.books)

    king = session.query(Author).all()[3]
    print(king.publishers)

