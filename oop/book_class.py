class Book:
  def __init__(title, author, year):
    self.title = title
    self.author = author
    self.year = year
  
  def __str__(self):
    return f"{self.title} by {self.author}, published in {self.year}"
  
  def __repr__(self):
    return f"Book( title={repr(self.title)}, author={repr(self.author)}, year={self.year})"
  
  def __del__(self):
    return f"deleting {self.title}" 
    
    
    
