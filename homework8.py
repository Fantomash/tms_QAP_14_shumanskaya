class Movie:
    # 1 Реализовать конструкторы для инициализации
    def __init__(self, name, rating, year, director):
        self.name = name
        self.rating = rating
        self.year = year
        self.director = director

    # 4 Реализовать инкапсуляцию методов
    def __set_director(self, new_director):
        self.director = new_director
    # 2 Реализовать вывод данных в основном и дополнительном классе
    # 3 Реализовать полиморфизм (перегрузка)
    def print_info(self, viewer_name=None):
        if viewer_name is not None:
            print("\nHello,", viewer_name, "\nYou are going to watch", self.name, "film directed by", self.director,
                  "\n(this is call for Parent class, there is viewer name)")
        else:
            print("\nYou are going to watch", self.name, "film directed by", self.director,
                  "\n(this is call for Parent class, there is no viewer name)")


# 3 Реализовать полиморфизм (наследование)
class Comedy(Movie):

    # 1 Реализовать конструкторы для инициализации
    def __init__(self, name, rating, year, director, country, _is_funny=True):
        super().__init__(name, rating, year, director)
        self.country = country
        #4 Реализовать инкапсуляцию свойств
        self._is_funny = _is_funny


    # 2 Реализовать вывод данных в основном и дополнительном классе
    # 3 Реализовать полиморфизм (переопределение)
    def print_info(self, platform, viewer_name=None):
        if viewer_name is not None:
            print("\nHello,", viewer_name, "\nYou are going to watch the funniest movie", self.name, "directed by", self.director,
                  "on the platform", platform, "\nThis film was produced in", self.country,
                  "\n(this is call for Child class, there is no viewer name)")
        else:
            print("\nYou are going to watch the funniest movie", self.name, "directed by", self.director,
                  "\nThis film was produced in", self.country,
                  "\n(this is call for Child class, there is viewer name)")



movie_1 = Movie("Zodiak", 8.0, 2007, "David Fincher")
movie_1.print_info()
movie_1.print_info("John")

movie_2 = Comedy("Zodiak", 8.0, 2007, "David Fincher", "USA")
movie_2.print_info("Netflix")
movie_2.print_info("Netflix", "Josef")
