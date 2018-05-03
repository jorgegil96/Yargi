<img src="res/yargi.png" width="30%;"/>  

# Yargi Programming Language
A statically typed object-oriented programming language written in Python

## Features
* [Variables](#primitives--variables)  
* [Operators](#operators)  
* [Functions](#functions)  
* [Flow control statements](#flow-control)  
* [Loops](#loops)  
* [Classes](#classes)  
* [Data Classes](#data-classes)  
* [Interfaces](#interfaces)  

### Primitives & Variables
Variables can be declared in single variable form `int x;` or multiple variable form `int x, y;`
```  
int x;
float y;
bool z;
string s;

x = 5;
y = 10;
z = true;
w = "Hi!";
```

### Operators
Arithmetic: `+`, `-`, `*`, `/`  
Logic: `and`, `or`  
Relational: `>`, `<`, `>=`, `<=`, `==`, `!=`  

### Functions
Function declaration follows the syntax:
```  
fun FUN_NAME( [<ARGS>,] ) [: RETURN_TYPE] {
  < DECLARATIONS >
  < STATEMENTS >
}
```  
#### Examples
A function with no return value:
```
fun sayHi() {
  write("Hi");
}
```  
A function with return value:  
```  
fun sum(int a, int b): int {
  return a + b;
}  
```

### Flow Control
#### If / Else Statements
The syntax for `if|else` flow control statements is as follows:  
```  
if (< expression >) {
  < statements >
} else {
  < statements >
}  
```
##### Example  
```  
if (10 > 5 + 4) {
  write("Hi!");
} else {
  write("Bye!");
}
```  
Yargi does not support traditional `else if` branches, instead we have the `when` flow control statement.

#### When Statements
The syntax for `when` flow control statements is as follows:
```  
when {
  < expresion > -> { < statements > }
  < expresion > -> { < statements > }
  [ else -> { <statements> } ]
}
```
##### Examples
```  
when {
  5 > a -> { write("Hi"); }
  true -> {
     write("Hola");
     ....
  }
  1 + 1 == 2 -> { write("1 plus 1 is two); }
  else -> {
    write("None of the above");
  }
}
```
The `else` branch is optional:  
```  
when {
  true -> { write("Hi"); }
  false -> { write("Hola"); }
}
```

### Loops
#### ForIn Loops
The syntax for `for in` loops is as follows:  
```  
for (< var > in < start >..< end >) {
  < statements >
}
```  
##### Examples
```  
for (i in 0..10) {
  write(i);
}
```

```  
for (i in a..b) {
  write(i);
}
```  

#### While Loops
The syntax for `while` loops is as follows:
```  
while ( <expression> ) {
  < statements >
}
```
##### Example  
```  
while (x < 10) {
  write(x);
  x = x + 1;
}
```  

### Classes
Classes are defined with the following syntax:  
```
class CLASS_NAME( [CONSTRUCTOR_ARGS,] ) [: PARENT_CLASS_NAME( [ARGS,] )] {
  [ global vars ]
  
  [ functions ]
  
  [ main() { < statements >} ]
}
```
#### Examples
```
class Calculator(int total) {

    fun total(): int {
        return total;
    }

    fun add(int n) {
        total = total + n;
    }

    fun sum(int a, int b): int {
        return a + b;
    }

    fun sub(int a, int b): int {
        return a - b;
    }
}
```
```
class Main {

    Calculator calculator;

    main() {
        calculator = Calculator(50);

        write(calculator.total()); // prints 50
        calculator.add(30);
        write(calculator.total()); // prints 80
        
        write(calculator.sum(2, 2)); // prints 4
        write(calculator.sub(2, 2)); // prints 0
    }
}
```
```  
class Person(int id, string name) {
  fun talk() {
    write("Hi! My name is ", name);
  }
  
  fun walk() {
    write(name, " is walking...");
  }
}

class Student(int id, string name, string major, int year) : Person(id, name) {
  fun talk() {
    write("Hi! My name is ", name, " and I'm a ", major, " student");
  }
}

class Main {
  
  Person bigTuna;
  Student nardDog;
  
  fun main() {
     bigTuna = Person(1, "Jim");
     nardDog = Student(2, "Andy", "CS", 3);
     
     bigTuna.talk(); // prints "Hi! My name is Jim"
     nardDog.talk(); // prints "Hi! My name is Andy and I'm a CS student"
     bigTuna.walk(); // prints "Jimothy is walking..."
     nardDog.walk(); // prints "Andy is walking..."
  }
}

```

### Data Classes
Yargi supports a special type of class whose main purpose is to hold data. Its fields are public and immutable.  
Its syntax is as follows:  
```  
data class CLASS_NAME([<ARGS>,])
```
#### Examples
```  
data class Person(int id, string name, string lastname)
```
```  
data class Dog(
  int id,
  string name,
  string breed,
  int age,
  string color,
  int owner
)
```

### Interfaces
Interfaces are defined with the following syntax:
```
interface INTERFACE_NAME {
    < interface funs >
}
```
#### Examples
```
interface Bike {
    fun accelerate();

    fun brake();

    fun changeGear(int newGear);
}
```
Then to implement it:
```
class RoadBike : Bike {
    fun accelerate() {
        // TODO: implement
    }

    fun brake() {
        // TODO: implement
    }

    fun changeGear(int newGear) {
        // TODO: implement
    }
}
```
To implement multiple interfaces separate them with comas:
```
interface AccidentListener {
    onCrash();
}

class RoadBike : Bike, AccidentListener {
    fun accelerate() {
        // TODO: implement
    }

    fun brake() {
        // TODO: implement
    }

    fun changeGear(int newGear) {
        // TODO: implement
    }

    fun onCrash() {
        // TODO: implement
    }
}
```
To extend a class and have it implement interfaces at the same time put the superclass constructor call at the very end:
```
class RoadBike : Bike, AccidentListener, BaseBike() {
    ...
}
```
