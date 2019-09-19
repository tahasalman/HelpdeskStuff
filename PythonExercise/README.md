# Python Exercise

## What is this?
This is a somewhat convoluted exercise that covers some subtleties of Python

## What to Do?
First: 
1) In *utils/util.py*, write a method called **true_or_false()** which returns *True* 60 percent of the time and *False*
40 percent of the time.

Now write a class called **Dog** in *main.py* such that:

1) It is a subclass of the Animal class
2) It has an attribute called **owner**. This attribute takes the value of the owner specified in
the dictionary - **DOG_OWNERS** if an owner exists for the dog of the same name. Otherwise, it takes the value **None**.
3) It has a method called **owner_nearby()**. If the dog has no owner, this method returns *False*,
otherwise, it calls the method **true_or_false()** in *utils/utils.py*
4) It has a static method **encrypt(words)** which takes as an argument a string **words**. It then
returns a string containing *'WOOF '* repeated the same number of times as the number of words in the argument.
5) It has a method called **talk**. This method takes a string argument _words_. Call the method **owner_nearby**. 
If this method returns False then simply print out 
> '{dog.name}: {words}'

Otherwise, encrypt the words using the *encrypt* method and print out the message in the same format as above.

