class Robot :
    def __init__(self, name, version) :
        self.name = name;
        self.version = version;

    def moveForward(self) :
        print(f'{self.name} is moving forward');

    def moveBack(self) : 
        print(f'{self.name} is moving backward');

    def sayName(self) :
        print(f'Hello, I am {self.name} robot');

    def sayVersion(self) :
        print(f'Hello, My version is {self.version}');


# We have Inherited all the properties and method of the parent class Robot into the child class HouseBot. This is called -------INHERITANCE-----------
class HouseBot(Robot) :
    def __init__(self, name, version, areaCovered) :
        super().__init__(name, version) #Here we just overridden the constructor function of the mother class or super class.
        self.areaCovered = areaCovered;

    def clean(self) : 
        if(self.areaCovered > 30) :
            print(f'I am cleaning the house. And 30 meters area is covered.');
            self.areaCovered -= 30;
        else :
            print(f'I am out of areas. Please reset');

    def resetArea(self, area) :
        self.areaCovered += area;
        print(f'Hurray, Area recharged. Now I can clean {self.areaCovered} meters.')

    def sayName(self) :
        print(f'Hello, I am {self.name}. And I am a happy house bot to assist you.'); 
        #Here we have overridden or overwritten the sayName method of the parent class. This is called -----METHOD OVERRIDING. AND PROPERTY OF POLYMORPHISM.

    @staticmethod
    def hault() :
        print("Okay, I am haulted. Be happy now! :(");


# We have Inherited all the properties and method of the parent class Robot into the child class FightBot. This is called -------INHERITANCE-----------
class FightBot(Robot) :
    def __init__(self, name, version, ammo):
        super().__init__(name, version);
        self.ammo = ammo;

    def fire(self) :
        if(self.ammo >= 10) :
            self.ammo -= 10;
            print(f'Fired. Dadadadada!!! {self.ammo} ammo is remaining');
        else :
            print(f'Not enough ammo. Please send supplies.');

    def supplyAmmo(self, ammo) :
        self.ammo += ammo;
        print(f'Yess.. Recharged. {self.ammo} is in stock.');

    def sayName(self) :
        print(f'Hello, I am {self.name}. And I am a super fight bot. I will kick asses for you!!'); 
        #Here we have overridden or overwritten the sayName method of the parent class. This is called -----METHOD OVERRIDING. AND PROPERTY OF POLYMORPHISM.
        super().sayName();
        #Also we can call the original mother classes method with the actual properties.

    @staticmethod
    def standDown() :
        print("Okay, I stood down. No more fighting. I am a good bot now.");


# hbot = HouseBot("Atom", 1, 40);
# hbot.moveForward();
# hbot.moveBack();
# hbot.sayName();
# hbot.clean();
# hbot.clean();
# hbot.resetArea(40);
# hbot.resetArea(50);
# hbot.clean();

# fbot = FightBot("Bumblebee", 2, 20);
# fbot.moveBack();
# fbot.moveForward();
# fbot.sayName();
# fbot.sayVersion();
# fbot.fire();
# fbot.fire();
# fbot.fire();
# fbot.supplyAmmo(100);
# fbot.fire();

