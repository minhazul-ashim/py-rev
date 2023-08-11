class Book :

    # Class Variables which belongs to all the instances of the class and class itself;
    num_of_instances = 0;
    discount = 100;
    def __init__(self, name, author, pages, price) :
        self.name = name;
        self.author = author;
        self.pages = pages;
        self.price = price;

        # incrementing number of instances with every instance creation within the main Book class.
        Book.num_of_instances += 1;

    def applyDiscount(self) :
        self.price = self.price - self.discount;
 

book1 = Book('Song of Fire and Ice', 'R.R Martin', 120, 300);
book2 = Book('Harry Potter', 'Geroge', 450, 250);

print(book1.price);
book1.applyDiscount();
print(book1.price);