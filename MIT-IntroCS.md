# MITx: 6.00.1x Introduction to Computer Science and Programming Using Python

## Lecture 1 Intro

* Knowledge:
	+ Declarative knowledge: statement of a fact
	+ Imperative knowledge: how-to knowledge/recipe to find sth
* Algorithms:
	+ recipes, sequence of mechanical steps for doing sth
* Mechanically
	+ Fixed Program Computers
		- Computers which only do one thing that they are designed to do
	+ Stored Program Computers
		- a machine that stores and manipulates instructions
			* sequence of instructions (programs) stored inside computer
			* special program (interpreter) executes each instruction in order
		- 6 primitives sufficient to compute anything - **Turing complete**
			* ways to abstract methods to create new `primitives`

* Aspects of languages
	+ Primitive constructs
		- numbers/strings/operators -> words in English
	+ Syntax - well-formed
	+ Semantics - meaning
		- static semantics: which syntactically valid strings have a meaning
		- Semantics (语义): no statics semantics, the meaning intended to do

> Computational mode of thinking: taking a problem description and breaking it down into a recipe, a sequence of how-to steps

## Lecture 2: Core elements of Programs

* low level language - similar to internal control unit
	- source code -> checker -> interpreter -> output
* high level - more abstract terms
	- source code -> checker -> compiler -> object code -> interpreter -> output
* interpreted language - slower, easier to find errors

### Python objects
* scalar objects
	+ int
	+ float
	+ boolean
* Non-scalar objects
	+ string

## Lecture 3: Simple Algorithms

* Iteration
	+ reuse a piece of code
	+ need an iteration variable
	+ need to test variable
	+ `Guess and check`
		- need good way to generate *Guess*
	+ `Exhaustive enumeration`

* dealing with floats
	+ binary #
	+ conversion
		- **If there is no integer p such that x*(2**p) is a whole number,
		then internal representation is always an approximation**
		- testing floats by `abs(x-y)<0.0001` instead of `x == y`
* iterative Algorithms
	* approximation methods - stepwise
	* bisection search
		+ cutting half
		+ radically reduce computation time
	* Newton-Raphson Algorithms
		+ root for polynomial = 0
		+ `p-p(g)/p'(g)`
