class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    
class EBook(Book):
  def __init__ (self, title, author, file_size):
    super().__init__(title, author)
    self.file_size = file_size
    
class PrintBook(Book):
  def __init__(self, title, author, page_count):
    super().__init__(title, author)
    self.page_count = page_count
    
  def __str__(self, title, author, page_count):
    return f""{self.title}" , "{self.author}" , "{self.page_count}""
  

class Library(books):
  def __init__(self):
    self.books = []
    
  def add_books(self, books):
    self.books.append(books)

  def list_books(self):
    for book in self.books:
      print (book)
