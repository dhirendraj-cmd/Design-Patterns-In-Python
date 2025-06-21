1. factory ka exact matlab kya hai?
factory means wo place jaha koi bhi chize produce/create ki jaa sakti hain.basically factories ka kaam object produce karna hai but wo aur bhi chize produce kar sakti hain jaise ki files, databse records, etc

2. Factory Design Pattern (FDP)
FDP bhi ek creational design pattern mein aata hai, iska kaam hai objects k creation ko manage karna bina client code ko concrete class se tighly couple kiye huye.
ye basically interface ya abstract class k through objects create karta hai jisse subclasses ya factories decide kar sake k konsa concrete object instantiate hoga.


Factory Paterns khud 3 types k hote hain:-
    1. Simple factory -- isme hum static method use karte hain and if-else condition k basis pe objects create karte hain.ye better hai for small scale apps but not for large ones. Ye client code se object creation logic hata deta hai, but Open/Closed principle break karta hai.
    2. Factory Pattern -- factory pattern mein objects create hote hain on the basis of some condition only but usme if-else chain use nhi karte instead subclasses k through object creation hota hai.yaha creater class decide karega kiska object create karna hai. Isme mein mostly ek hi product ka object creation karte hain.
    3. Abstract factory -- yaha bhi object creation hi hota hai but yaha families of products k liye creation kiya jata hai. yaha sirf ek product k liye nhi balki us product k related jo bhi uske family members honge sabke liye abstract class kiya jata hai.


| Pattern          | Control via       | Object Types        | if-else?  | Open/Closed friendly? |
| ---------------- | ----------------- | ------------------- | --------- | --------------------- |
| Simple Factory   | Static method     | Single product line | ✅ Often   | ❌ No (must edit)      |
| Factory Method   | Subclasses        | Single product line | ❌ Avoided | ✅ Yes (just subclass) |
| Abstract Factory | Family of classes | Multiple related    | ❌ Avoided | ✅ Yes                 |
