# Rust Language

## The core conception about ownership in Rust.

Where is data actually allocated?

Heap vs Stack.

The heap data only allows one valid connection to it at any time.

While the stack data allows multiple valid connections to it.

The way to change ownership for different data.
* Move the data from the heap
* Copy the data from the stack

## References and Borrowing
If references and borrowing are just used to avoid the ownership return trouble but makes the language so complex, then it may be not so necessary in practice programming.

Let’s recap what we’ve discussed about references:

* At any given time, you can have either one mutable reference or any number of immutable references.
* References must always be valid.
