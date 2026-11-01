from main import BooksCollector
import pytest 



# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre(self, collector):
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert collector.books_genre['Гордость и предубеждение и зомби'] == 'Ужасы'

    def test_get_book_genre(self, collector):
        result = collector.get_book_genre('Гордость и предубеждение и зомби')
        assert result == 'Фантастика'

    @pytest.mark.parametrize("genre_input, expected_result", [
    ('Фантастика', {'Гордость и предубеждение и зомби', 'Дюна'}), 
    ('Детективы', [])])
    def test_get_books_with_specific_genre(self, collector, genre_input, expected_result):
        result = collector.get_books_with_specific_genre(genre_input)
        assert set(result) == set(expected_result)

    def test_get_books_genre(self, collector):
        result = collector.get_books_genre()
        assert result == collector.books_genre

    def test_get_books_for_children(self, collector):
        result = collector.get_books_for_children()
        assert 'Гордость и предубеждение и зомби' in result
        assert 'Дюна' in result 
        assert 'Война и мир' not in result                  

    def test_add_book_in_favorites(self, collector):
        book_title = 'Гордость и предубеждение и зомби'
        collector.add_book_in_favorites(book_title)
        assert book_title in collector.favorites
      
    def test_delete_book_from_favorites(self, collector):
        book_title = 'Гордость и предубеждение и зомби'
        collector.delete_book_from_favorites(book_title)
        assert book_title not in collector.favorites

    def test_get_list_of_favorites_books(self, collector):
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        result = collector.get_list_of_favorites_books()
        assert result == ['Дюна', 'Гордость и предубеждение и зомби']    


    def test_add_new_book_add_one_book(self, collector):
        collector.add_new_book('Мастер и Маргарита')
        assert collector.get_book_genre('Мастер и Маргарита') == ''  