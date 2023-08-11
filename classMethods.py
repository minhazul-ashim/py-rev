# Class methods are mainly like the getter and setter for the class variables, which is for the "private" variable like behaviour in Python.

class Book : 
    discount = 500;

    # Class methods;
    @classmethod
    def setDiscount(cls, newDiscount) :
        cls.discount = cls.discount + newDiscount;

    @staticmethod
    def is_new(publishing_year) :
        if(publishing_year > 2020) :
            print("Yes");
        else :
            print("No");

print(Book.discount);
Book.setDiscount(700);
print(Book.discount);