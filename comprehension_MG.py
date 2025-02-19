# comprehension-excercises

Github:
<li>Fork this repository</li>
<li>Clone the repository to your local computer</li>
<li>Create a new branch named in the following format: firstname-lastname-solution</li>
<li>Push the new branch back to your repository</li>
<li>Create a new pull request so I can review your answer</li>

-------------------------------------------------------------------------------------------------
Problem 1

This is a classic problem given in technical interviews. First solve the problem WITHOUT using list comprehension.

"Write a program that prints the numbers from 1 to 100. For multiples of three print "Fizz" instead of the number. For Multiples of five print "Buzz". Finally, for numbers which are multiples of both three and five print "FizzBuzz".

Include comments for each step of your script explaining the Pseudo code/what each line is doing.

After you have solved it, write a second version of your script using list comprehension.

-------------------------------------------------------------------------------------------------

# to print the numbers from 1 to 100
for x in range(1,101):
# numbers which are multiples of both three and five print "FizzBuzz"
    if (x % 3 == 0) and (x % 5 == 0):
        print("FizzBuzz")
# For multiples of three print "Fizz" instead of the number
    elif (x % 3 == 0):
        print('Fizz')
# For Multiples of five print "Buzz"
    elif (x % 5 == 0):
        print('Buzz')
    else:
        print(x)

# as a list comprehension
number = [("fizzbuzz" if (x % 3 == 0) and (x % 5 == 0) else "Fizz" if  x % 3 == 0 else "Buzz" if x % 5==0 else x) for x in range(1,101)]
print(number)
  


