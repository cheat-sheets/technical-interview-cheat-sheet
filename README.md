# Technical Interview Cheat Sheet

### Table of Contents

- [Behavioral Questions](#behavioral-questions)
- [Algorithms and Data Structures](#algorithms-and-data-structures)
- [Operating Systems](#operating-systems)
- [Scalability and Design](#scalability-and-design)
- [Object-Oriented Programming](#object-oriented-programming)
- [Resources](#resources)


## Interview Preparation Grid

![Interview Preparation Grid](./assets/interview-preparation-grid.jpg)

**Evaluated skills**:
- Analytical skills
- Coding skills
- Technical knowledge / Computer Science fundamentals
- Experience
- Culture fit / Communication skills


## Behavioral Questions

- Be specific, not arrogant
- Limit Details
- Focus on yourself, not your team
- Give structured answers: **Nugget first**, situation, action, result

#### Tell Me About Yourself

- Current Role (Headline Only)
- College
- Post College & Onwards
- Current Role (Details)
- Outside of Work
- Wrap Up


## Algorithms and Data Structures

### Big-O

- Big O - upper bound
- Big Omega - lower bound
- Big Theta - upper and lower bound - that's what's usually used but called Big O.

**Divide and Conquer** - Recursive  - Ex. Merge Sort.

**Master Method** (allows to estimate time complexity of a recursive the algorithm):

`T(n) <= a*T(n/b) + O(n^d)`

![Master Method](./assets/master-method.jpg)

**Guiding principles for algorithms analysis**:
- Worst case analysis (other are average case, best case)
- Drop constant factors, lower-order terms
- Asymptotic analysis (focus on running time for large input)

#### Amortized time

An ArrayList is implemented with an array. When the array hits capacity, the ArrayList class will 
create a new array with double the capacity and copy all the elements over to the new array.

For most inserts it takes O(1) time. For those inserts where the array is doubling it takes X time. 
`X + X/2 + X/4 + Y/8 + ... + 1` is roughly 2X. 

Therefore X insertions take O(X) time. The amortized time for each insertion is O(1).


## Operating Systems

http://pages.cs.wisc.edu/~remzi/OSTEP/


## Scalability and Design

- List all assumptions - needed to scope the project
- Draft high-level solution
- List limitations
- List Hard problems - what will take most effort


## Object-Oriented Programming

- Abstraction - represent real-world entities with their abstraction i.e. classes in code.
- Encapsulation - hide the implementation details and expose the interface.
- Inheritance - build class hierarchy to represent subset/superset relationships in real world.  
- Polymorphism - write your code with interfaces, the implementation will be chosen at runtime.


## Resources

- Cracking The Coding Interview https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850
- Operation Systems http://pages.cs.wisc.edu/~remzi/OSTEP/
- Algorithms Specialization on Coursera https://www.coursera.org/specializations/algorithms

