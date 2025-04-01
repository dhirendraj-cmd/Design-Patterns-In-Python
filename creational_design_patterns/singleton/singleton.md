<!-- Hindi Explanation -->

singleton ka matlab hai k ek hi instance matlab k ek hi object banega ek class ka and instead of creating new object wo bana hua object hi circulate hoga resources mein so basically wo object pure application mein share hota hai.

Question :- koi sirf ek hi instance q bana chahega usse kya fayda hai?
Singleton pattern ka idea yeh hai ki kuch situations mein ek se zyada instances banane se problem ho sakti hai ya resources waste ho sakte hain, toh ek hi instance 
banake usko reuse karna better option hota hai

kaha kaha use hoga:
    - jaha global control chahiye like logging, database connection
    - resource sharing 
    - consistency in data behaviour


<!-- English Explanation -->

"Singleton means that there will be only one instance, meaning only one object of a class will be created, and instead of creating a new object, that already created object will circulate in the resources. So basically, that object is shared throughout the entire application.
Question: Why would someone want to create only one instance, and what’s the benefit of it?
The idea of the Singleton pattern is that in some situations, creating more than one instance can cause problems or waste resources. So, creating a single instance and reusing it is a better option.
Where it will be used:  
Where global control is needed, like logging, database connection.  

Resource sharing.  

Consistency in data behavior."

