# Intro to Javascript

JavaScript provides seven different data types which are
undefined, null, boolean, string, symbol, number, and object.

### string immutability
In JavaScript, String values are immutable, which means that they cannot be altered once created.

For example, the following code:

var myStr = "Bob";
myStr[0] = "J";
cannot change the value of myStr to "Job", because the contents of myStr cannot be altered. Note that this does not mean that myStr cannot be changed, just that the individual characters of a string literal cannot be changed. The only way to change myStr would be to assign it with a new string, like this:

var myStr = "Bob";
myStr = "Job";

### manipulate arrays with push, pop, shift, unshift
```js
// Example
var ourArray = ["Stimpson", "J", "cat"];
ourArray.push(["happy", "joy"]);
// ourArray now equals ["Stimpson", "J", "cat", ["happy", "joy"]]

// Example
var ourArray = [1,2,3];
var removedFromOurArray = ourArray.pop();
// removedFromOurArray now equals 3, and ourArray now equals [1,2]

// Example
var ourArray = ["Stimpson", "J", ["cat"]];
removedFromOurArray = ourArray.shift();
// removedFromOurArray now equals "Stimpson" and ourArray now equals ["J", ["cat"]].

// Example
var ourArray = ["Stimpson", "J", "cat"];
ourArray.shift(); // ourArray now equals ["J", "cat"]
ourArray.unshift("Happy");
// ourArray now equals ["Happy", "J", "cat"]
```

### Global Scope and Functions
Variables which are used without the var keyword are automatically created in the global scope. This can create unintended consequences elsewhere in your code or when running a function again. You should always declare your variables with var.


### boolean
```js
function trueOrFalse(wasThatTrue) {

  if (wasThatTrue){
    return "Yes, that was true";
  }
  return "No, that was false";

}
```

### strict equality

Strict equality (===) is the counterpart to the equality operator (==). Unlike the equality operator, strict equality tests both the data type and value of the compared elements.

strict notequal `!==`

### switch statement
case values are tested with strict equality (===). The break tells JavaScript to stop executing statements. If the break is omitted, the next statement will be executed.

### for loop
`for ([initialization]; [condition]; [final-expression])`

### RE
Regular expressions are used to find certain words or patterns inside of strings.

For example, if we wanted to find the word the in the string The dog chased the cat, we could use the following regular expression: /the/gi

Let's break this down a bit:

/ is the start of the regular expression.

the is the pattern we want to match.

/ is the end of the regular expression.

g means global, which causes the pattern to return all matches in the string, not just the first one.

i means that we want to ignore the case (uppercase or lowercase) when searching for the pattern.

#### RE digits
One such selector is the digit selector \d which is used to retrieve one digit (e.g. numbers 0 to 9) in a string.

In JavaScript, it is used like this: /\d/g.

Appending a plus sign (+) after the selector, e.g. /\d+/g, allows this regular expression to match one or more digits.

The trailing g is short for 'global', which allows this regular expression to find all matches rather than stop at the first match.

#### RE whitespace
We can also use regular expression selectors like \s to find whitespace in a string.

The whitespace characters are " " (space), \r (the carriage return), \n (newline), \t (tab), and \f (the form feed).

The whitespace regular expression looks like this:

/\s+/g

\S will match anything that isn't whitespace.

### Construct JavaScript Objects with Functions - like class in Python
A constructor function is given a capitalized name to make it clear that it is a constructor.

Here's an example of a constructor function:
```js
var Car = function() {
  this.wheels = 4;
  this.engines = 1;
  this.seats = 1;
};
```
In a constructor the this variable refers to the new object being created by the constructor. So when we write,
```js
  this.wheels = 4;
```
inside of the constructor we are giving the new object it creates a property called wheels with a value of 4.

To use a constructor function we call it with the new keyword in front of it like:
```js
var myCar = new Car();
```

#### private variable
```js
var Car = function() {
  // this is a private variable
  var speed = 10;

  // these are public methods
  this.accelerate = function(change) {
    speed += change;
  };

  this.decelerate = function() {
    speed -= 5;
  };

  this.getSpeed = function() {
    return speed;
  };
};
```

### iterate over arrays
The map method is a convenient way to iterate through arrays. Here's an example usage:
```js
var timesFour = oldArray.map(function(val){
  return val * 4;
});
```
The map method will iterate through every element of the array, creating a new array with values that have been modified by the callback function, and return it. Note that it does not modify the original array.

In our example the callback only uses the value of the array element (the val argument) but your callback can also include arguments for the index and array being acted on.


### Condense arrays with reduce
he array method reduce is used to iterate through an array and condense it into one value.

To use reduce you pass in a callback whose arguments are an accumulator (in this case, previousVal) and the current value (currentVal).

reduce has an optional second argument which can be used to set the initial value of the accumulator. If no initial value is specified it will be the first array element and currentVal will start with the second array element.

Here is an example of reduce being used to subtract all the values of an array:

```js
var array = [4,5,6,7,8];
var singleVal = 0;

// Only change code below this line.

singleVal = array.reduce(function(previousVal, currentVal){
  return previousVal + currentVal
}, 0); // 4+5+6+7+8

singleVal = array.reduce(function(previousVal, currentVal){
  return previousVal - currentVal
}, 0); //4-5-6-7-8
```
### Filter Arrays with filter
The filter method is used to iterate through an array and filter out elements where a given condition is not true.

filter is passed a callback function which takes the current value (we've called that val) as an argument.

Any array element for which the callback returns true will be kept and elements that return false will be filtered out.

The following code is an example of using filter to remove array elements that are equal to five:

Note: We omit the second and third arguments since we only need the value
```js
array = array.filter(function(val) {
  return val !== 5;
});
```

### sort array
You can use the method sort to easily sort the values in an array alphabetically or numerically.

Unlike the previous array methods we have been looking at, sort actually alters the array in place. However, it also returns this sorted array.

sort can be passed a compare function as a callback. The compare function should return a negative number if a should be before b, a positive number if a should be after b, or 0 if they are equal.

If no compare (callback) function is passed in, it will convert the values to strings and sort alphabetically.

Here is an example of using sort with a compare function that will sort the elements from smallest to largest number:
```
var array = [1, 12, 21, 2];
array.sort(function(a, b) {
  return a - b;
});
```

### concate array
```js
var oldArray = [1,2,3];
var newArray = [];

var concatMe = [4,5,6];

// Only change code below this line.

newArray = oldArray.concat(concatMe);//[1,2,3,4,5,6]
```
