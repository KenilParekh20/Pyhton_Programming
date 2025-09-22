class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def display_details(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)

    def apply_discount(self,percent):
        self.price=self.price-self.price*percent/100

#creating 2 book
book1=Book("Python Basics","Mitesh Sir",350)
book2=Book("Python Programming","Harikesh Sir",400)

print("Book 1 details:")
book1.display_details()

print("\nBook 2 details:")
book2.display_details()

# 10% discount book 2
book2.apply_discount(10)

print("\nBook 2 details after 10% discount:")
book2.display_details()
