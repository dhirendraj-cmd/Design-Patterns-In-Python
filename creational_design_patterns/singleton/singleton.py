# haaving full control on singleton using __new__ method
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance  = super(Singleton, cls).__new__(cls)
        return cls._instance
    

    def say_hello(self):
        print("Its singleton!!")


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()

    s1.say_hello()
    print(s1 is s2)
    print(s1 == s2)


"""

Hindi explanation :- 

cls -- ek class parameter hai jo class ko represent karta hai. jab singleton() likhkar object banta hai toh cls mein singleton class khud paas hoti hai
__new__ -- ye ek static method hai jo __init__ se bhi pehle kaam call hoti hai and objection creation mein interfere karke usse control karti hai, isliye ye instance k badle class k sath kaam karti hai. __new__ ek special method hai jo object ka actual creation handle karta hai – matlab memory allocate karta hai aur ek naya instance banata hai.



super(Singleton, cls) -- ye super class means parent class jo ki object class hoti hai python mein usko call kar rha hai 

super(Singleton, cls).__new__(cls) -- yaha parent class i.e. object class k new method ko call kar rhi hai or usko cls i.e. Singleton class hi pass kar rhi hai. so basically yaha singleton class ka naya instance ban rha hai

cls._instance --- isme bane huye instance ko store karte hai and har baar jab ye class call hoti hai toh iski ko check karte hain k variable mein value hai ya nhi.


Kyun super() Use Kiya?
Agar hum directly Singleton() ya koi doosra tareeka use karte, toh infinite recursion ho jata kyunki __new__ khud ko baar-baar call karta.

super() parent class ke __new__ ko call karta hai, jo base-level object creation karta hai bina recursion ke.


English explanation :-- 

cls -- This is a class parameter that represents the class. When you write Singleton() to create an object, the Singleton class itself is passed into cls.
__new__ -- This is a static method that gets called even before __init__ and interferes with object creation to control it. That’s why it works with the class instead of the instance. __new__ is a special method that handles the actual creation of the object – meaning it allocates memory and creates a new instance.

super(Singleton, cls) -- This calls the superclass, i.e., the parent class, which in Python is the object class.

super(Singleton, cls).__new__(cls) -- Here, it calls the __new__ method of the parent class (i.e., the object class) and passes cls, which is the Singleton class. So basically, a new instance of the Singleton class is being created here.

cls._instance -- The created instance is stored in this, and every time the class is called, it checks whether this variable has a value or not.

Why use super()?
If we directly used Singleton() or some other method, it would lead to infinite recursion because __new__ would keep calling itself.

super() calls the __new__ method of the parent class, which performs base-level object creation without recursion."




"""