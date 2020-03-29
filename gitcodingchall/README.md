# Git Coding Challenge

## Problem 1
Given that a user submits a string of 16 alphanumeric characters:
- Convert each alphanumeric character to an ASCII hex value
- Join all the ASCII hex values into one string

For example:
```
Enter your 16 characters: a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p
Your ASCII value is: 61626364656667686970717273747576
```
## Problem 2
Create a function that takes a variable number of groups of items, and returns the number of ways the items can be arranged, with one item from each group. Order does not matter.

```
Enter your number of items in each group (each group seperated by commas): 2, 3
There are 6 combinations in total.

Enter your number of items in each group (each group seperated by commas): 3, 7, 4
There are 84 combinations in total.

Enter your number of items in each group (each group seperated by commas): 2, 3, 4, 5
There are 120 combinations in total.
```

## Problem 3
Create a function that can perform a shift cipher by increasing the Ascii HEX value of a character based on the 'k' value. For example:
```
Key in your input: acc3nt
Key in your shift value (k): 3

Your encrypted value is: dff6qw
```

## Problem 4
Create a function that ensures the provided string meets the following requirements:
- At least 2 alphanumeric characters
- At least 1 upper case alphabet
- At least 1 symbol in use
- String length is at least 12 characters

Function should print the outcome if the provided string is a pass or a fail.

```
Please submit your user input here: helloworld
Function result: FAIL

Please submit your user input here: H3ll0w0rld1337!
Function result: PASS
```

## Problem 5
Create a function that checks if the provided string is a palindrome (meaning or form of string value is the same when reversed)

```
Please submit your user input here: helloworld
Function result: FAIL

Please submit your user input here: 8008
Function result: PASS
```

## Problem 6
Create a function that generates a hash of the provided string and is Base64 encoded.

```
Please submit your user input here: my name is hamzah
Your hashed + Base64 encoded value is: ZjgyYTRiMWJkYTEzMmU4ZGY1NDFiNmFmMjk5NjlhYzkgIAo=
```
