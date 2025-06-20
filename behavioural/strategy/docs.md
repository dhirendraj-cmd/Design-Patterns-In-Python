Strategy Design Pattern kya hai?
    1. Strategy pattern ek behavioural design pattern k andar aata hai.
    2. ye run time pe behaviour switch karne k kaam aat hai without changing the class structure

Isme hum multiple algortihms define kar sakte hain and unhe interchangeably use kar sakte hain without changing the client code

Structure:
    1. strategy: interface ya abstract class hota hai
    2. concrete strategy: above strategy class ka implementation
    3. context: isme strategy use hoti hai and wo object ko hold karta hai


basically jaha bhi choices jada honge ya aisa lag rha hai k if-else condition kaafi ho sakte hain jiske wajah se runtime pe behaviour change ho waha startegy pattern use kar sakte hain

Strategy Pattern tab use hota hai jab tumhara focus “object kaunsa banega” nahi, balki “banne ke baad wo kaise behave karega” pe hota hai.

basically client kya karta hai k wo factory method ko call karta hai and factory method object creation k baad strategy ko call karta hai to do the implemtations


 Simple Language Mein:

    Factory Pattern:

        “Mujhe ek object chahiye, lekin mujhe nahi pata kaunsa subclass banana hai — factory decide kare.”

    Strategy Pattern:

        “Mere paas object already hai — ab uska behavior plug karna hai (aur future mein kabhi bhi switch kar sakta hoon).”


isme client context ko call karta hai and context internally apne pass rakhe strategies ko call/delegate karta hai.

Client  ──▶  Context.execute(...args...)  ──▶  Strategy.do_operation(...args...)

