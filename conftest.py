import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    c = BooksCollector()
    c.add_new_book('Гордость и предубеждение и зомби')
    c.add_new_book('Что делать, если ваш кот хочет вас убить')
    c.add_new_book('Война и мир')
    c.add_new_book('Дюна')
    
   
    c.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
    c.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
    c.set_book_genre('Война и мир', 'Классика')
    c.set_book_genre('Дюна', 'Фантастика')
    
    return c  