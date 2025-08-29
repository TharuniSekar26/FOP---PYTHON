Q-1 : Sum and Difference
Write a python program to get 2 numbers from the user and calculate their sum and difference using '+' and '-' operators respectively. Print the corresponding sum and difference of the numbers as output in the console. Input format: First input: an integer Second input: an integer Output format: First output will be the sum of two integers Second output will be the difference of two integers


Input (stdin)
55
34
Output (stdout)
89
21
Input (stdin)
45
14
Output (stdout)
59
31
 
Program:
a=int(input())
b=int(input())
print(a+b)
print(a-b)
Q-2 : Product and Division
Write a python program to get 2 numbers from the user and calculate their product, quotient and remainder using '*', '/' and '%' operators respectively. Print the corresponding product, quotient and remainder of the numbers as output in the console. Input format: First input: an integer Second input: an integer Output format: The first output will be the product of two integers The second output will be the quotient The third output will be the remainder


Input (stdin)
50
10
Output (stdout)
500
5
0
Input (stdin)
47
23
Output (stdout)
1081
2
1
 
Program:
import math
a=int(input())
b=int(input())
print(a*b)
print(int(a/b))
print(a%b)
Q-3 : Swapping two numbers
Write a python program to get 2 numbers from the user and swap their values without any loss of data. You can make use of additional 3rdvariable for swapping. Print the corresponding swapped values of the two numbers as output in the console. Input format: First input: an integer Second input: an integer Output format: The output will be integers(swapped values)


Input (stdin)
20
10
Output (stdout)
10
20
Input (stdin)
58
45
Output (stdout)
45
58
 
Program:
a=input()
b=input()
temp=a
a=b
b=temp
print(a)
print(b)
Q-4 : Swapping without third variable
Write a python program to swap two values without the use of 3rd variable. Input format: First input: an integer Second input: an integer Output format: The output will be integers(swapped values)
Input (stdin)
10
20
Output (stdout)
20
10
Input (stdin)
3
1
Output (stdout)
1
3
 
Program:
a=input()
b=input()
a,b=b,a
print(a)
print(b)
Q-5 : Average Calculation
A teacher wants to compute the average of 5 students in her class. Write a program to help her to find the average. The average is the sum of all the numbers, then divided by the total numbers. Input format: First input: 1st student mark in float Second input: 2nd student mark in float Third input: 3rd student mark in float Fourth input:4th student mark in float Fifth input: 5th student mark in float Output format: The output value should be in float with 2 decimal places.


Input (stdin)
10
20
30
40
50
Output (stdout)
30.00
Input (stdin)
12
14
15
16
12
Output (stdout)
13.8
 
Program:
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
avg=(a+b+c+d+e)/5
print(avg)
Q-6 : Area calculation
Sheela has three things in her bag. She wants to compute the area of 3 things but 3 things are in different shapes. The three things are in square shape, rectangular shape, and circular shape respectively. Write a program to help Sheela to calculate the area of different shapes. Input format: First input: a side of a square in integer Second input: length of a rectangle in integer Third input: breadth of a rectangle in integer Fourth input: radius of a circle in float Output format: The first output should be the area of a square in integer The second output should be the area of a rectangle in integer The third output should be the area of a circle in float with 2 decimal places

Input (stdin)
5
5
4
2.0
Output (stdout)
25
20
12.56
Input (stdin)
4
2
5
1.0
Output (stdout)
16
10
3.14
 
Program:
side=int(input())
length=int(input())
breadth=int(input())
radius=float(input())
print(side**2)
print(length*breadth)
print("%0.2f"%(3.14*radius*radius))
Q-7 : Simple Interest
Sara wished to build a new house but she didn't have a sufficient amount. So, she is planning to borrow some money from the bank on simple interest. When she is borrowing some money from the bank, she has to pay back the original amount accompanied by a certain amount of interest on that amount. She wants to find the interest for borrowed money within a certain period. Help her to find the simple interest. Input format: The first line containing integer value denoting the borrowed amount(principal amount) The second line containing integer value denoting the period in years The third line containing float value denoting the rate of interest Output format: Print the simple interest with 2 decimal places.


Input (stdin)
15000
2
2.8
Output (stdout)
840.00
Input (stdin)
5000
5
4.2
Output (stdout)
1050.0
 
Program:
p=int(input())
r=int(input())
t=float(input())
si=(p*t*r)/100
print(si)
Q-8 : Power of a number
pow() function is used to calculate the power of any base and it is defined in math header file. Write a program to read X as the base and N as the power and calculate the result (X^N - X to the power of N). Input format: The first line containing integer denotes the base(X) The second line containing integer denotes the power(N) Output format: Print the power of a number


Input (stdin)
2
3
Output (stdout)
8
Input (stdin)
5
2
Output (stdout)
25
 
Program:
a=int(input())
b=int(input())
print(pow(a,b))
Q-9 : Ternary Operator
The conditional operator is also known as ternary operator can be used to make an either-or choice. Write a python program to get a number from the user and find out whether it is odd or even.
Input format:
The input containing integer denotes the given number 
Output format:
If given number is even, print "Even". Otherwise, print "Odd".
 
Input (stdin)
5
Output (stdout)
Odd
Input (stdin)
4
Output (stdout)
Even
 
Program:
a=int(input())
print("Even" if a%2==0 else "Odd")
Q-10 : Fencing the Ground
The college ground is rectangular in shape. The Management decides to build a fence around the ground. In order to help the construction workers to build a straight fence, they planned to place a thick rope around the ground. They wanted to buy only the exact length of the rope that is needed. They also wanted to cover the entire ground with a thick carpet during rainy season. They wanted to buy only the exact quantity of carpet that is needed. They requested your help. Can you please help them by writing a program to find the exact length of the rope and the exact quantity of carper that is required? Input Format: Input consists of 2 integers. The first integer corresponds to the length of the ground and the second integer corresponds to the breadth of the ground. Output Format: Refer Sample Input and Output for exact formatting specifications.


Input (stdin)
50
20
Output (stdout)
Required length is 140m
Required quantity of carpet is 1000sqm
Input (stdin)
15
4
Output (stdout)
Required length is 38m
Required quantity of carpet is 60sqm
 
Program:
l = int(input())
b = int(input())
p = 2*(l+b)
C = l*b
print("Required length is %dm"%p)
print("Required quantity of carpet is %dsqm"%C)
Q-11 : Splitting into teams
During the Physical Education hour, PT sir has decided to conduct some team games. He wants to split the students in the class into equal sized teams. In some cases, there may be some students who are left out from teams and he wanted to use the left out students to assist him in conducting the team games. For instance, if there are 50 students in the class and if the class has to be divided into 7 equal sized teams, 7 students will be there in each team and 1 student will be left out. PT sir asks your help to automate this team splitting task. Can you please help him out? Input Format: Input consists of 2 integers. The first integer corresponds to the number of students in the class and the second integer corresponds to the number of teams. Output Format: Refer sample input and output for formatting specifications.


Input (stdin)
60
8
Output (stdout)
The number of students in each team is 7 and left out is 4
Input (stdin)
10
2
Output (stdout)
The number of students in each team is 5 and left out is 0
 
Program:
a=int(input())
b=int(input())
c=a//b
e=a%b
print("The number of students in each team is {} and left out is {}".format(c,e))
Q-12 : Three Idiots
Ajay, Binoy and Chandru were very close friends at school. They were very good in Mathematics and they were the pet students of Emily Mam. Their gang was known as 3-idiots. Ajay, Binoy and Chandru live in the same locality. A new student Dinesh joins their class and he wanted to be friends with them. He asked Binoy about his house address. Binoy wanted to test Dinesh's mathematical skills. Binoy told Dinesh that his house is at the midpoint of the line joining Ajay's house and Chandru's house. Dinesh was puzzled. Can you help Dinesh out? Given the coordinates of the 2 end points of a line (x1,y1) and (x2,y2), write a python program to find the midpoint of the line. Input Format: Input consists of 4 integers. The first integer corresponds to x1 . The second integer corresponds to y1. The third and fouth integers correspond to x2 and y2 respectively. Output Format: Refer Sample Input and Output for exact formatting specifications. [All floating point values are displayed correct to 1 decimal place]
Input (stdin)
[All text in bold corresponds to input and the rest corresponds to output]
 
2
4
10
15
Output (stdout)
Binoy's house is located at (6.0,9.5)
Input (stdin)
5
5
5
5
Output (stdout)
Binoy's house is located at (5.0,5.0)
 
Program:
X1=int(input())
Y1=int(input())
X2=int(input())
Y2=int(input())
a=((X1+X2)/2.0)
b=((Y1+Y2)/2.0)
print("Binoy's house is located at ({},{})".format(a,b))
Q-13 : Profit Calculation
Each Sunday, a newspaper agency sells x copies of a certain newspaper for Rs.a per copy. The cost to the agency of each newspaper is Rs.b . The agency pays a fixed cost for storage, delivery and so on of Rs.100 per Sunday. The newspaper agency wants to calculate the profit obtained on sundays. Can you please help them out by writing a python program to compute the profit given x, a and b. Input Format: Input consists of 3 integers --- x, a and b. X is the number of copies sold, a is the cost per copy and b is the cost the agency spends per copy. Output Format: Refer Sample Input and Output for exact formatting specifications. 
Input (stdin)
1000
2
1
Output (stdout)
The profit obtained is Rs. 900
Input (stdin)
200
5
4
Output (stdout)
The profit obtained is Rs. 100
 
Program:
x=int(input())
a=int(input())
b=int(input())
p=((x*a)-(x*b))-100
print("The profit obtained is Rs. %d"%p)
Q-14 : Alice in wonderland
Alice was bored that day,so she was sitting on the riverbank .Suddenly she notices a talking, White Rabbit with a pocket watch .It ran fast,and she followed it, down a rabbit hole .She fell into the hole and found a magical wonderland with dark trees, beautiful flowers.She found many ways numbered from 1,2,3,........18.she was confused which is the right way that will lead her to her home. She found a cute bird, standing in one of the tree. Alice asked the bird the way to go back to her home.The bird said a two digit number( say 23 ) and asked her to find the sum of its digits (2+3=5) and that numbered way will lead her to her home.Alice was already confused, so pls help Alice in finding the route to her home.... Input Format: Input consists of an integer corresponding to the 2-digit number. Output Format: Output consists of an integer corresponding to the sum of its digits. Refer sample input and output for formatting specifications. [All text in bold corresponds to input and the rest corresponds to output]
Input (stdin)
23
Output (stdout)
Alice must go in path-5
Input (stdin)
10
Output (stdout)
Alice must go in path-1
 
Program:
a=int(input())
b=a/10
c=a%10
e=int(b+c)
print("Alice must go in path-%d"%e)
DECISION MAKING STATEMENTS
Q-1 : compare two strings
Get two integers x and y from the user and write a python program to relate 2 integers as equal to, less than or greater than. Input format: Input consist of 2 integers The first input corresponds to the first number(x) The second input corresponds to the second number(y) Output format: If the first number is equal to the second number, print "x and y are equal". Otherwise, print "x greater than y" or "x less than y"


Input (stdin)
17
12
Output (stdout)
17 greater than 12
Input (stdin)
3
4
Output (stdout)
3 less than 4
 
Program:
x=int(input())
y=int(input())
if(x==y):
               print("{} and {} are equal".format(x,y))
elif x>y:
               print("{} greater than {}".format(x,y))
else:
               print("{} less than {}".format(x,y))
Q-2 : Checking Alphabets
Write a python program to check whether the given character is vowel or consonant. Input format: The input consist of a character Output format: The output consists of a below-given string “Vowel” / “Consonant” / “Not an alphabet”


Input (stdin)
a
Output (stdout)
Vowel
Input (stdin)
l
Output (stdout)
Consonant
 
Program:
l=input()
if l.lower() in ('a','e','i','o','u'):
  print("Vowel")
elif l.upper() in ('A','E','I','O','U'):
  print("Vowel")
elif l.lower() in ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'):
  print("Consonant")
elif l.upper in ('B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z'):
   print("Consonant")
else:
               print("Not an alphabet")
Q-3 : Profit or Loss
A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a python program to determine the profit or loss in Rs. for the fruitseller. Input format: Input consists of 2 floating point numbers The first input corresponds to the total cost(X) The second input corresponds to the sold cost(Y) Output format: Print "Profit or Loss" with Rupees. Sample Input: 60.0 4 Sample Output: Loss : Rs.12.00


Input (stdin)
60.0
4
Output (stdout)
Loss : Rs. 12.00
Input (stdin)
40.3
2
Output (stdout)
Loss : Rs. 16.30
 
Program:
x=float(input())
y=float(input())
y=y*12
if(x<y):
    print("profit : Rs. {0:.2f}".format(y-x))
#elif(x==y):
#             print("Neither profit nor loss")
else:
               print("Loss : Rs. {0:.2f}".format(x-y))
Q-4 : Fee Collection
Write a python program to determine the fee amount to be collected from a student.
Refer the table below for fee details.
 Input format:
The first input corresponds to the student type
The second input corresponds to the tuition fee
The third input corresponds to the bus fee
The fourth input corresponds to the hostel fees
Output format:
Print the total fee amount of the corresponding student.
Refer below sample output for formatting
Input (stdin)
MSH
40000
12000
50000
Output (stdout)
90000
Input (stdin)
MGSDS
50000
12000
10000
Output (stdout)
87000
 
Program:
t=input()
f=int(input())
b=int(input())
h=int(input())
if (t=='MSDS'):
               print(f+b)
elif(t=='MSH'):
   print(f+h)
elif(t=='MGSDS'):  
               print(((f/100)*150)+b)
else:
               print(((f/100)*150)+h)
Q-5 : Age Detector
Ask a user for their birth year encoded as two digits (like "62") and for the current year, also encoded as two digits (like "99"). Write a python program to find the users current age in years.
Input format:
Input consists of 2 integers
The first integer corresponds to the last 2 digits of the birth year
The second integer corresponds to the last 2 digits of the current year
Output format:
Print the user's current age
Refer below sample output for formatting.
Input (stdin)
62
00

Output (stdout)
38
Input (stdin)
36
45

Output (stdout)
9
 
Program:
a=int(input())
b=int(input())
if(a>b):
               print((100-a)+b)
else:
               print(b-a)
Q-6 : Mango Tree I
Dora is interested so much in gardening and she plants more trees in her garden. She plants trees in a rectangular fashion with the order of rows and columns and numbered the trees in row-wise order. She planted the mango tree only in a 1st row, 1st column and last column. So given the tree number, your task is to find whether the given tree is a mango tree or not? Write a program to check whether the given number is a mango tree or not. Input format: Input consists of 3 integers The first input denotes the number of rows The second input denotes the number of columns The third input denotes the tree number Output format: If the given number is a mango tree, print "Yes". Otherwise, print "No" Refer the sample output for formatting


Input (stdin)
5
5
11
Output (stdout)
Yes
Input (stdin)
2
2
4
Output (stdout)
Yes

Program:
row=int(input()) 
col=int(input())
tree=int(input())
if(tree>=1 and tree<=row or tree%col==0 or tree%col==1):
               print("Yes")
else:
               print("No")
Q-7 : Hotel Tariff Calculator
Write a python program to calculate the hotel tariff. The room rent is 20% high during peak seasons [April-June, November-December]. Input format: The first input containing an integer which denotes the number of the month The second input containing the floating point number which denotes the room rent per day The third input containing an integer which denotes the number of days stayed in the hotel Output format: Print the hotel tariff to be paid in floating point with 2 decimal places Refer the sample output for formatting


Input (stdin)
3
1500
2
Output (stdout)
3000.00
Input (stdin)
1
1500
3
Output (stdout)
4500.00
 
Program:
a=int(input())
b=float(input())
c=int(input())
if a in(4,5,6,11,12):
               e=((b/100)*20)+b
               print("{:.2f}".format(e*c))
else:
               print("{:.2f}".format(b*c))
Q-8 : Budget
t’s your job to calculate the cost of replacing damaged battle droids and to check whether it is within the budget limit of Rs. 15000. The cost of the equipment and parts is given below. Blast Rifle Rs. 350.34 Visual Sensors Rs. 230.90 Auditory Sensors Rs. 190.55 Arms Rs. 125.30 Legs Rs. 180.90 Write a python program to solve this problem. Input format: Input consists of 5 integers The first input denotes the number of blast rifles needed The second input denotes the number of visual sensors needed The third input denotes the number of auditory sensors needed The fourth input denotes the number of arms needed The fifth input denotes the number of legs needed Output format: If the total cost of replacing damaged battle droids is within the sanctioned budget of Rs. 15000, print "Yes". Otherwise, print "No" Refer the sample output for formatting


Input (stdin)
20
10
14
3
9
Output (stdout)
Yes
Input (stdin)
20
4
12
15
2
Output (stdout)
Yes
 
Program:
a=int(input())
b=int(input())
c=int(input())
e=int(input())
f=int(input())
g=float((350.34*a)+(230.90*b)+(190.55*c)+(125.30*e)+(180.90*f))
if(g <= 15000):
               print("Yes")
else:
               print("No")
Q-9 : Sece Dining
The catering staff in the SECE mess are known for their good cooking skills as well as hospitality. We all know that the dining table arrangement needs to be different for left handed and right handed persons. So whenever any VIP guests come to SECE, they would make the table arrangements based on whether they are left handed or right handed. The mess is situated on the 15th floor of the hostel building. SECE hostel building has superfast elevators to help to travel from one floor to another. Each elevator has 2 doors, the front one and the rear one. If a person enters the elevator through the front door, he goes out through the rear door and vice-versa. The elevator has 2 rails numbered as 1 and 2. Rail 1 is located to the left of the entrance to the front door (or correspondingly, to the right of the entrance to the rear door). Rail 2 is located opposite it, to the right of the entrance to the front door and to the left of the entrance to the rear door. We know that each person holds on the rail with his/her strongest hand. There is an IP camera in the elevator and based on the camera output, the catering staff will be easily able to identify whether a guest is left handed or right handed. They have decided to automate this task and they asked the help of Image Processing Group. The Image Processing Group has written a program to perform this task and the program will output the door through which the person entered and the rail number which the person held. Based on this input, write a program to determine whether a person is left handed or right handed?


Input format:
The first input containing a string denotes “front” or “rear”
The second input containing an integer denotes rail 1 or 2
Output format:
Print the string "Left Handed" or "Right Handed"
Input (stdin)
front
1
Output (stdout)
Left Handed
Input (stdin)
rear
2
Output (stdout)
Left Handed
 
Program:
a=input()
b=int(input())
if(a=="front" and b==1):
               print("Left Handed")
elif(a=="front" and b==2):
               print("Right Handed")
elif(a=="rear" and b==1):
               print("Right Handed")
else:
               print("Left Handed")
Q-11 : Circle Intersection
Write a python program to determines if two circles intersect each other. Input format: Input consists of 6 integers The first input containing an integer which denotes the x-coordinate of the center of the first circle. The second input containing an integer which denotes the y-coordinate of the center of the first circle. The third input containing an integer which denotes the radius of the first circle. The next 3 integers denote the x,y, and radius of the second circle. Output format: The output consists of a single line which contains any of these 3 strings. “Tangential”, “Overlap”, “Do not overlap”


Input (stdin)
10
10
3
10
6
1
Output (stdout)
Tangential
Input (stdin)
2
3
5
6
4
5
Output (stdout)
overlap
 
Program:
import math
x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())
d1 = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
d=int(d1)
radSumSq = (r1 + r2)
if (radSumSq == d):
  print("Tangential")
elif (radSumSq > d):
  print("overlap")
else:
  print("Do not overlap")
Q-12 : Time sheet
Jeevitha just started work as a programming trainer for UIT's Placement Cell. She is paid Rs.100 an hour, with a few exceptions. She earns an extra Rs.15 an hour for any part of a day where she works more than 8 hours, and an extra Rs.25 an hour for hours beyond 40 in any one week. Also, she earns a 25% bonus for working on Saturday and a 50% bonus for working on Sunday. The bonuses for Saturday and Sunday are computed based on the hours worked those days; they are not used to calculate any bonus for working more than 40 hours in a week. You'll be given the number of hours Jeevitha worked on each day in a week (Sunday, Monday, ..., Saturday), and you need to compute her salary for the week. Input format: Input consists of 7 integers less than or equal to 24 on separate lines Output format: Print the Jeevith's salary for a week.


Input (stdin)
0
8
8
8
10
6
0
Output (stdout)
4030
Input (stdin)
3
3
6
9
8
7
4
1
Output (stdout)
4265
 
Program:
n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
n5=int(input())
n6=int(input())
n7=int(input())
r1=n1*150
r7=n7*125
if(n2<=8):
    r2=n2*100
else:
    b=n2-8
    brate=b*115
    r2=brate+800  
if(n3<=8):
    r3=n3*100
else:
    b=n3-8
    brate=b*115
    r3=brate+800
if(n4<=8):
    r4=n4*100
else:
    b=n4-8
    brate=b*115
    r4=brate+800
if(n5<=8):
    r5=n5*100
else:
    b=n5-8
    brate=b*115
    r5=brate+800
if(n6<=8):
    r6=n6*100
else:
    b=n6-8
    brate=b*1
if(n6<=8):
    r6=n6*100
else:
    b=n6-8
    brate=b*115
    r6=brate+800
total=n2+n3+n4+n5+n6
if(total>40):
    edays=total-40
    r8=edays*25
totalrate=r1+r2+r3+r4+r5+r6+r7
print(totalrate)   
Q-13 : Microwave Oven
A microwave oven manufacturer recommends that when heating two items, add 50% to the heating time, and when heating three items double the heating time. Heating more than three items at once is not recommended. Write a python program to find out the recommended heating time. Input format: The first input containing an integer which denotes the number of items The second input containing the floating point number which denotes the single item heating time. Output format: Print the recommended heating time in floating point with 2 decimal places. If the number of items is more than three, print "Number of items is more" Refer the sample output for formatting


Input (stdin)
2
5.0
Output (stdout)
7.50
Input (stdin)
3
6.5
Output (stdout)
13.00
 
Program:
a = int(input())
b = float(input())
if(a==2):
               print(((b/100)*50)+b)
elif(a==3):
               print(b*2)
else:
               print("Number of items is more")
Q-14 : Movie Tickets
Ask the customer's age and for the time on a 24-hour clock (where noon is 12.00 and 4:30 PM is 16.30). The show timings are 10.15, 13.30, 18.00 and 22.00. The normal adult ticket price is $8.00, however, the adult matinee price is $5.00. Adults are those over 13 years. The normal children's ticket price is $4.00, however, the children's matinee price is $2.00. Write a python program that determines the price of a movie ticket Input format: The first input containing an integer which denotes the age The second input containing the floating point number which denotes the show timing. Output format: Print the price of a movie ticket. Refer the sample output for formatting


Input (stdin)
16
10.5
Output (stdout)
$8.00
 
 
Input (stdin)
24
12.3
 
Output (stdout)
$8.00
 
Program:
a = int(input())   #age
b = float(input()) #show timing
if(b >  10.15 and b < 13.30 or a>13):
               print("$8.00")
elif(b > 18.00 and b<22.00 or a>13):
               print("$5.00")
elif(b >  10.15 and b < 13.30 or a<13):
               print("$4.00")
elif(b > 18.00 and b<22.00 or a<13):
               print("$2.00")
    Control Structures I
Control Structures-I
Q-1 : Amoeba Multiplication
The environmental eco club has discovered a new Amoeba that grows in the order of a Fibonacci series every month. They are exhibiting their amoeba in a national conference. They want to know the size of the amoeba at a particular time instant. If a particular month’s index is given, write a program to displays the amoeba’s size……??? For Example, The size of the amoeba on month 1, 2, 3, 4, 5, 6, ..will be 0, 1, 1, 2, 3, 5, 8 respectively. Input format: The first input containing an integer which denotes the number of the month Output format: Print the amoeba size. Refer the sample output for formatting.


Input (stdin)
7
Output (stdout)
8
Input (stdin)
3
Output (stdout)
1
 
Program:
n1=0
n2=1
num=int(input())
for i in range(2,num):
  n3=n1+n2
  n1=n2
  n2=n3
print(n3) 
Q-2 : Factorial
Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'. Input format: The input containing an integer 'n' which denotes the given number. Output format: If the given number is factorial, print "Yes". Otherwise, print "No". Refer the sample output for formatting.


Input (stdin)
6
Output (stdout)
Yes
Input (stdin)
2
Output (stdout)
Yes
 
Program:
n=int(input())
i=1                
while(True):   
  if(n%i==0):
    n=n//i
  else:
    break
  i=i+1 
if(n==1):
  print("Yes")
else:
  print("No")
Q-3 : Lucas Sequence
a = 0, b=0, c=1 are the 1st three terms. All other terms in the Lucas sequence are generated by the sum of their 3 most recent predecessors. Write a program to generate the first n terms of a Lucas Sequence. Input format: The input containing an integer 'n' which denotes the given number Output format: Print the 'n' terms of the Lucas Sequence, separated by a single space. There are no leading or trailing spaces in the output. Refer the sample output for formatting.


Input (stdin)
5
Output (stdout)
0 0 1 1 2
Input (stdin)
3
Output (stdout)
0 0 1
 
Program:
n=int(input())
a=0
b=0
c=1
for i in range(0,n):
  print(a,end=" ")
  d=a+b+c
  a=b
  b=c
  c=d
Q-4 : Collatz problem
The rules for generating Collatz Sequence are: If n is even: n = n / 2 If n is odd: n = 3n + 1 For example, if the starting number is 5 the sequence is: 5 -> 16 -> 8 -> 4 -> 2 -> 1 It has been proved for almost all integers, the repeated application of the above rule will result in a sequence that ends at 1. Input format: The input containing an integer 'n' which denotes the given number Output format: Print the numbers in the sequence and also print the number of times the rule has to be applied in order to reach 1. Refer the sample output for formatting.


Input (stdin)
5
Output (stdout)
5
16
8
4
2
1
5
Input (stdin)
8
Output (stdout)
8
4
2
1
3
 
Program:
import math
b=0
a=int(input())
print(a)
while(a!=1):
  b=b+1
  if(a%2==0):
    a=a//2
    print(a)
  else:
    a=(a*3)+1
    print(a)
print(b)
Q-5 : Trendy Numbers
Write a program to check whether the given number is a trendy number or not. A number is said to be a trendy number if and only if it has 3 digits and the middle digit is divisible by 3. Input format: The input containing an integer 'n' which denotes the given number Output format: If the given number is a trendy number, then print "Trendy Number". Otherwise, print "Not a Trendy Number". Refer the sample output for formatting.


Input (stdin)
791
Output (stdout)
Trendy Number
Input (stdin)
153
Output (stdout)
Not a Trendy Number
 
Program:
n=int(input())
n1=n/10
res=n1%10
rem=res%3
x=round(rem)
if(x==0):
               print("Trendy Number")
else:
               print("Not a Trendy Number")  
Q-6 : Viva on Odd Numbers
A maths teacher asks her students to give 3 examples for positive odd numbers. When the student specifies a correct answer, his/her score is incremented by 1. When the student specifies a positive even number, his/her score is decremented by 0.5. When the student specifies a negative number, he/she will not be given any more chances to correct his or her mistake and his/her score will be decremented by 1. So a student's turn comes to an end when he/she has correctly specified 3 positive odd numbers or when the student has specified a negative number. Few students didn't know the difference between odd numbers and even numbers and they made many mistakes and so it was difficult for the teacher to maintain the scores. The teacher asks for your help. Can you please help her by writing a program to calculate the score? Input Format: Input consists of a list of integers. Output Format: Output consists of a single line. The score needs to be displayed correct to 1 decimal place. Refer sample output for details. [For this exercise, don't worry about duplicate odd numbers. Even if the students specifies the same odd number thrice, it is accepted].


Input (stdin)
1
3
5
Output (stdout)
3.0
 
Program:
count=1
score=0
while count<=3:
               n=int(input())
               if(n%2!=0):
                              count = count+1
                              score = score+1
               else:
                              score = score-0.5
print(float(score))
Q-7 : Kaprekar Number
Consider an n-digit number k. Square it and add the right n digits to the left n or n-1 digits. If the resultant sum is k, then k is called a Kaprekar number. For example, 9 is a Kaprekar number since 92 = 81 & 8+1=9. and 297 is a Kaprekar number since 2972 = 88209 & 88+209 = 297 Input Format: Input consists of a single integer. Output Format: Refer sample output for details.


Input (stdin)
9
Output (stdout)
Kaprekar Number
Input (stdin)
5
Output (stdout)
Not A Kaprekar Number
 
Program:
a=int(input())
n=a
c=0
while(n):
               c=c+1
               n=n//10
sq=a*a
po=pow(10,c)
f=sq%po
s=sq//po
if((f+s)==a):
  print("Kaprekar Number")
else:
  print("Not A Kaprekar Number")
Q-8 : Target Practise
Drona normally trains his disciples using a board which consists of concentric circles. When the student correctly hits the center of the concentric circles, his score is 100. The score gets reduced depending on where the students hits on the board. When the student hits outside the board, his score is 0. Drona will not allow a student to have his food unless he scores 100. Arjuna will always hit the target in his first attempt and he will leave early. Others may take more turns to reach the score of 100. Can you write a program to determine the number of turns a disciple takes to reach the target score of 'n' ? Input Format: Input consists of a list of positive integers. The first integer corresponds to the target score 'n'. Assume that all the other integers input are less than or equal to n. Output Format: Output consists of a single line. Refer sample output for format details.


Input (stdin)
100
4
40
60
Output (stdout)
The number of turns is 3
Input (stdin)
80
4
50
60
Output (stdout)
The number of turns is 3
 
Program:
sum=0
attempt=0
target=int(input())
while(sum<target):
               score=int(input())
               sum=sum+score
               attempt=attempt+1
print("The number of turns is",attempt)
Q-9 : Data Mining
In the University Examinations conducted during the past 5 years, the toppers registration numbers were 7126, 82417914, 7687 and 6657. Your father is an expert in data mining and he could easily infer a pattern in the toppers registration numbers. In all the registration numbers listed here, the sum of the odd digits is equal to the sum of the even digits in the number. He termed the numbers that satisfy this property as Probable Topper Numbers. Write a program to find whether a given number is a probable topper number or not. Input Format: Input consists of a single integer. Output Format: Output consists of a single line. Refer sample output for details.


Input (stdin)
143
Output (stdout)
yes
Input (stdin)
153
Output (stdout)
no
 
Program:
sum=0
sum1=0
n=int(input())
while(n>0):
               n1=n%10
               if(n1%2==0):
                              sum=sum+n1
               else:
                              sum1=sum1+n1
               n=n//10
if(sum==sum1):
               print("yes")
else:
               print("no")
Q-10 : Special number
Wil Wheaton who has filled in the shoes of Professor Proton in the show Professor Proton Fun with Mathematics wanted the kids to learn about Special number.(A 2-digit number is said to be a special number if the sum of sum of its digits and the product of its digits is equal to the number itself. For example, 19 is a special number. The digits in 19 are 1 and 9. The sum of the digits is 10 and the product of the digits is 9. 10+9 = 19.) Can you help Wil to write a Python program to find all special numbers between 2 limits m and n(both inclusive). Assume that m and n are 2-digit numbers.
Input Format:
Input consists of 2 integers m and n.
Output Format:
The output consists of a list of integers.
Refer to sample output for the output format.
Sample Input 1:
11
30
Sample Output 1:
19
29
Explanation:
Between 11 and 30, 19 and 29 are the numbers whose sum of digits and product of digits when added gives the same number itself.
Hence, the two outputs possible are 19 & 29.
Sample Output 1:
11
19
Sample Output 2:
19
Explanation:
Between 11 and 19, 19 is the only number whose sum of digits and product of digits when added gives 19 itself.
Hence, the only output possible is 19.
Input (stdin)
12
45
Output (stdout)
19
29
39
Input (stdin)
11
19
Output (stdout)
19
 
Program:
a=int(input())
b=int(input())
for i in range(a,b+1):
               sum=(i%10)+(i//10)
               prod=(i%10)*(i//10)
               if((sum+prod)==i):
                              print(i)
Q-11 : Print continous Number
Write a program to print all numbers between a and b (a and b inclusive) using a while loop. Input Format: Input consists of 2 integers. The first integer corresponds to a and the second integer corresponds to b. Assume a>=b. Output Format: Refer Sample Input and Output for formatting specifications. [All text in bold corresponds to input and the rest corresponds to output] 
Input (stdin)
4
10

Output (stdout)
4
5
6
7
8
9
10
Input (stdin)
5
15
Output (stdout)
5
6
7
8
9
10
11
12
13
14
15
 
Program:
n1=int(input())
n2=int(input())
for i in range(n1,n2+1):
               print(i)
Q-12 : Print the number in reverse
Write a program to print all numbers between a and b (a and b inclusive) using a while loop. Input Format: Input consists of 2 integers. The first integer corresponds to a and the second integer corresponds to b. Assume a>=b. Output Format: Refer Sample Input and Output for formatting specifications. [All text in bold corresponds to input and the rest corresponds to output] 
Input (stdin)
10
4
Output (stdout)
10
9
8
7
6
5
4
Input (stdin)
5
1
Output (stdout)
5
4
3
2
1
 
Program:
n1=int(input())
n2=int(input())
for  i in reversed(range(n2,n1+1)):
               print(i)
   
#while(n1>=n2):
#             print(n1)
#             n1=n1-1
Q-13 : Count positive or negative
Write a program to that allows the user to enter 'n' numbers and finds the number of positive numbers entered and the number of negative numbers entered using a while loop. Input Format: Input consists of n+1 integers. The first integer corresponds to n. The next n integers correspond to the numbers to be added. Consider 0 to be a positive number. Output Format: Refer Sample Input and Output for formatting specifications. [All text in bold corresponds to input and the rest corresponds to output]


Input (stdin)
4
5
-2
-1
6
Output (stdout)
Number of positive numbers entered is 2 and the sum is 11
Input (stdin)
5
-6
5
-9
4
5
Output (stdout)
Number of positive numbers entered is 3 and the sum is 14
 
Program:
c=0
sum=0
list=[]
n=int(input())
for i in range(0,n):
  a=int(input())
  list.append(a)
for i in range(0,n):
  if(list[i]>0):
    sum=sum+list[i]
    c=c+1
print("Number of positive numbers entered is",c,"and the sum is",sum)
Q-14 : Multiplication table
Write a program to print the multiplication table of an integer n upto m rows using a while loop. Input Format: Input consists of 2 integers. The first integer corresponds to n. The second integer corresponds to m. Output Format: Refer Sample Input and Output for formatting specifications. [All text in bold corresponds to input and the rest corresponds to output]


Input (stdin)
5
4
Output (stdout)
The multiplication table of 5 is
1*5=5
2*5=10
3*5=15
4*5=20
Input (stdin)
2
5
Output (stdout)
The multiplication table of 2 is
1*2=2
2*2=4
3*2=6
4*2=8
5*2=10
 
Program:
n1=int(input())
n2=int(input())
print("The multiplication table of",n1,"is")
for i in range(1,n2+1):
               pro=i*n1
               print("%d"%i+"*""%d"%n1+"=""%d"%pro)
Q-15 : Valid
A number is said to be valid iff it is divisible by 8. Write a program that allows the user to keep entering numbers as long as the input is valid and also displays a count of the valid numbers entered using a while loop. Input Format: Input consists of integers. Output Format: Refer Sample Input and Output for formatting specifications. [All text in bold corresponds to input and the rest corresponds to output]


Input (stdin)
8
16
96
6
Output (stdout)
The number of valid numbers entered is 3
Input (stdin)
24
64
80
4
Output (stdout)
The number of valid numbers entered is 3
 
Program:
c=0
while(1):
               a=int(input())
               if(a%8==0):
                              c+=1
               else:
                              break
print("The number of valid numbers entered is",c)  
Control Structures II
Q-1 : Series I
Write a program to generate the following series --- 1,4,9,16,25, .... Input format: The input containing an integer which denotes 'n' Output format: Print the series and refer the sample output for formatting


Input (stdin)
7
Output (stdout)
1 4 9 16 25 36 49
 
Input (stdin)
5
Output (stdout)
1 4 9 16 25
 
Program:
n=int(input())
for i in range(1,n+1):
                   res=i*i
                   print(res,end=" ")
Q-2 : Series II
Write a program to generate the following series --- 6,11,21,36,56,... Input format: The input containing an integer which denotes 'n' Output format: Print the series and refer the sample output for formatting.


Input (stdin)
6
Output (stdout)
6
11
21
36
56
81
Input (stdin)
5
Output (stdout)
6
11
21
36
56
 
Program:
n=int(input())
a=6
for i in range(1,n+1):
                   print(a)
                   res=5*i
                   a=a+res
Q-3 : Series III
Write a program to generate the first n terms in the series --- 3, 9, 27, 81,...,... Input format: The input containing an integer which denotes 'n' Output format: Print the series and refer the sample output for formatting 
Input (stdin)
6
Output (stdout)
3 9 27 81 243 729
Input (stdin)
5
Output (stdout)
3 9 27 81 243
 
Program:
n=int(input())
a=3
b=3
for i in range(1,n+1):
                   print(a,end=" ")
                   a=b*a
Q-4 : Series IV
Write a program to generate the following series --- 0.5,1.5,4.5,13.5,... Input format: The input containing an integer which denotes 'n' Output format: Print the series and refer the sample output for formatting.


Input (stdin)
5
Output (stdout)
0.5 1.5 4.5 13.5 40.5
Input (stdin)
3
Output (stdout)
0.5 1.5 4.5
 
Program:
n=int(input())
a=0.5
b=3
for i in range(1,n+1):
                   print(a,end=" ")
                   a=b*a
Q-5 : Series V
Write a program to generate the following series --- 121,225,361,... Input format: The input containing an integer which denotes 'n' Output format: Print the series and refer the sample output for formatting.


Input (stdin)
4
Output (stdout)
121 225 361 529
Input (stdin)
6
Output (stdout)
121 225 361 529 729 961
 
Program:
n=int(input())
a=11
b=4
for i in range(1,n+1):
                   mul=a**2
                   print(mul,end=" ")
                   a=a+b
Q-6 : Series VI
Write a program to generate the following series --- 0,2,8,14,...,34 Input format: The input containing an integer which denotes 'n' Output format: Print the series and refer the sample output for formatting.


Input (stdin)
6
Output (stdout)
0 2 8 14 24 34
Input (stdin)
5
Output (stdout)
0 2 8 14 24
 
Program:
n=int(input())
a=0
for i in range(1,n+1):
                   if(i%2!=0):
                                      print((i*i-1),end=" ")
                   else:
                                      print((i*i-2),end=" ")
Q-7 :Series VII
Write a program to generate the following series --- 1, 2.0, 3.0, 6.0, 9.0, 18.0, 27.0,... Input format: The input containing an integer which denotes 'n' Output format: Print the series and refer the sample output for formatting


Input (stdin)
6
Output (stdout)
1 2.0 3.0 6.0 9.0 18.0
Input (stdin)
2
Output (stdout)
1 2.0
 
Program:
n = int(input())
a = 1
b = 2.0
print(a,b,end=" ")
for i in range(3,n+1):
  if i%2==1:
    a=a*3
    print(float(a),end=" ")
  else:
    b=b*3
    print(float(b),end=" ")
Q-8 : Series VIII
Write a program to generate the following series 4, 5, 9, 18, 34,... Input format: The input containing an integer which denotes 'n' Output format: Print the series and refer the sample output for formatting.


Input (stdin)
6
Output (stdout)
4
5
9
18
34
59
Input (stdin)
5
Output (stdout)
4
5
9
18
34
 
Program:
import math
n = int(input())
a,b=4,5
sum = 0
print(a)
print(b)
sum = a+b
for i in range(3,n+1):
  print(sum)
  sum=sum+pow(i,2)
Q-9 : Series IX
Write a program to generate the following series 2, 3, 8, 63, 3968 Input format: The input containing an integer which denotes 'n' Output format: Print the series and refer the sample output for formatting


Input (stdin)
5
Output (stdout)
2
3
8
63
3968
Input (stdin)
7
Output (stdout)
2
3
8
63
3968
15745023
247905749270528
Input (stdin)
3
Output (stdout)
2
3
8
 
Program:
n=int(input())
a=2
for i in range(1,n+1):
                   print(a)
                   a=(a**2)-1
Q-10 : Series XI
In a cricket game, the run rate starts with a value of 95.0. For each over there is an increase in the run rate. Based on the increase rate a series is generated. Write a program to generate the following series 95.0, 115.5, 138.0,..., 189.0
Input Format:
The input is an integer that denotes 'n'.
Output Format:
Print the series and refer to the sample output for formatting.
Sample Input 1:
5
Sample Output 1:
95 115.5 138 162.5 189
Explanation:
Here the input is 5 and hence 5 terms are printed.
Sample Input 2:
3
Sample Output 2:
95 115.5 138
Explanation:
Here the input is 3 and hence 3 terms are printed.
Input (stdin)
5
Output (stdout)
95.0 115.5 138.0 162.5 189.0
Input (stdin)
3
Output (stdout)
95.0 115.5 138.0
Input (stdin)
10

Output (stdout)
95.0 115.5 138.0 162.5 189.0 217.5 248.0 280.5 315.0 351.5
 
Program:
n = int(input())
x = 95.0
ctr = 1
i = 20.5
while ctr<=n:
    print(x,end=" ")
    x=x+i
    i=i+2
    ctr+=1
Q-11 : Series XI
Write a program to generate the following series 9, 11, 20, 31,..., 82 Input format: The input containing an integer which denotes 'n' Output format: Print the series and refer the sample output for formatting.


Input (stdin)
6
Output (stdout)
9 11 20 31 51 82
Input (stdin)
10
Output (stdout)
9 11 20 31 51 82 133 215 348 563
 
Program:
n = int(input())
a = 9
b = 11
print(a,b,end=" ")
for i in range(3,n+1):
  sum=a+b
  a=b
  b=sum
  print(sum,end=" ")
Q-12 : Series XII
Write a program to generate the following series 5, 16, 49, 104, 181... Input format: The input containing an integer which denotes 'n' Output format: Print the series and refer the sample output for formatting.


Input (stdin)
5
Output (stdout)
5
16
49
104
181
Input (stdin)
10
Output (stdout)
5
16
49
104
181
280
401
544
709
896
 
Program:
n = int(input())
for i in range(1,n+1):
  t = (11*i*i)-(22*i)+16
  print(t)
Q-13 : Series XIII
Write a program to generate the following series 2, 5, 11, 23, 47, 95, 191........... Input format: The input containing an integer which denotes 'n' Output format: Print the series and refer the sample output for formatting


Input (stdin)
6
Output (stdout)
2 5 11 23 47 95
Input (stdin)
10
Output (stdout)
2 5 11 23 47 95 191 383 767 1535
 
Program:
n = int(input())
x = 2
print(x,end=" ")
for i in range(2,n+1):
  x=x*2+1
  print(x,end=" ")
Q-14 : Series XIV
Write a program to generate the following series 3, 8, 13, 24, 41, 70, 117, 194,....... Input format: The input containing an integer which denotes 'n' Output format: Print the series. Refer the sample output for formatting
Input (stdin)
6
Output (stdout)
3 8 13 24 41 70
Input (stdin)
5
Output (stdout)
3 8 13 24 41
 
Program:
n = int(input())
x,y=3,8
sum = 0
print(x,y,end=" ")
for i in range(3,n+1):
  sum=x+y+(i-1)
  x=y
  y=sum
  print(sum,end=" ")
List
Q-1 : List
Sita has been promoted as a Team Leader and she has been shifted to Multimedia Team. As she needs to extensively work on audio, image and video signals, she is planning to spend a day in mastering the basics of 1-D and 2-D arrays. Can you please help her out? Write a program to find the maximum element in an array. Input Format: Input consists of n+1 integers. The first line of the input contains an integer corresponds to ‘n’ , the size of the array. The next ‘n’ integers correspond to the elements in the array. Assume that the maximum value of n is 15. Output Format: Refer sample input and output for formatting details.
Input (stdin)
5
2
3
6
8
1
Output (stdout)
8
Input (stdin)
4
6
3
2
1
Output (stdout)
6
Input (stdin)
3
4
5
7
Output (stdout)
7
Program:
list =[]
n = int(input())
for i in range(1,n+1):
  list.append(int(input()))
max = list[0]
for i in list:
  if i>max:
    max=i
print(max)
Q-2: Maximum Element in an Array Sum of array elements
Write a Python program to find the sum of the elements in an array. Input Format: Input consists of n+1 integers. The first integer corresponds to ‘n’ , the size of the array. The next ‘n’ integers correspond to the elements in the array. Assume that the maximum value of n is 15. Output Format: Refer sample input and output for formatting details.
Input (stdin)
5
2
3
6
8
1
Output (stdout)
20
Input (stdin)
4
3
2
1
5
Output (stdout)
11
Program:
list=[]
n=int(input())
for i in range(1,n+1):
  list.append(int(input()))
sum=0
for i in list:
  sum+=i
print(sum)
Q-3: Compatible Arrays
2 arrays are said to be compatible if they are of the same size and if the ith element in the first array is greater than or equal to the ith element in the second array for all i. Write a program to find whether 2 arrays are compatible or not. Input Format: Input consists of 2n+1 integers. The first integer corresponds to ‘n’ , the size of the array. The next ‘n’ integers correspond to the elements in the first array. The last 'n' integers correspond to the elements in the second array. Assume that the maximum value of n is 15. Output Format: Refer sample input and output for formatting details.
Input (stdin)
5
2
3
6
8
1
1
1
1
1
1
Output (stdout)
Compatible
Program:
list=[]
lst=[]
n=int(input())
for i in range(1,n+1):
  list.append(int(input()))
for i in range(1,n+1):
  lst.append(int(input()))
  flag=0
for i in list:
  for j in lst:
    if i>=j:
      flag=1
      break
if flag == 1:
  print("Compatible")
Q-3: Compatible Arrays
2 arrays are said to be compatible if they are of the same size and if the ith element in the first array is greater than or equal to the ith element in the second array for all i. Write a program to find whether 2 arrays are compatible or not. Input Format: Input consists of 2n+1 integers. The first integer corresponds to ‘n’ , the size of the array. The next ‘n’ integers correspond to the elements in the first array. The last 'n' integers correspond to the elements in the second array. Assume that the maximum value of n is 15. Output Format: Refer sample input and output for formatting details.
Input (stdin)
5
2
3
6
8
1
1
1
1
1
1
Output (stdout)
Compatible
Program:
list=[]
lst=[]
n=int(input())
for i in range(1,n+1):
  list.append(int(input()))
for i in range(1,n+1):
  lst.append(int(input()))
  flag=0
for i in list:
  for j in lst:
    if i>=j:
      flag=1
      break
if flag == 1:
  print("Compatible")
Q-4: No. of Distinct Elements in a sorted array
Write a program to find the number of distinct elements in a sorted array. Input Format: Input consists of n+1 integers. The first integer corresponds to n, the number of elements in the array. The next n integers correspond to the elements in the array. Assume that the maximum value of n is 15. Output Format: Output consists of a single integer which corresponds to the number of distinct elements in the array.
Input (stdin)
5
3
3
3
78
90
Output (stdout)
3
Program:
list1=[]
list2=[]
ctr = 0
n=int(input())
for i in range(1,n+1):
  list1.append(int(input()))
  for i in list1:
    if i not in list2:
      list2.append(i)
print(len(list2))
Q-5: Array Mean
Write a program to find the mean of the elements in the array. Input Format: Input consists of n+1 integers where n corresponds to the number of elements in the array. The first integer corresponds to n and the next n integers correspond to the elements in the array. Assume that the maximum number of elements in the array is 20. Output Format: Output consists of a double value which corresponds to the mean of the array. It is printed upto 2 digits of precision. Refer sample input and output for formatting specifications. [All text in bold corresponds to input and the rest corresponds to output.]
Input (stdin)
5
2
4
1
3
1
Output (stdout)
2.20
Input (stdin)
4
1
5
9
8
Output (stdout)
5.75
Program:
list=[]
sum=0
n=int(input())
for i in range(1,n+1):
  list.append(int(input()))
for i in list:
  sum+=i
print(sum/len(list))
Q-6: Create a list
Write a program to create a list and display it. Input format: Input consist of n+1 integers First integer corresponds to the size of the list Next n inputs corresponds to the elements in the list Output format: Output is an integer list.
Input (stdin)
4
1
2
3
4
Output (stdout)
[1, 2, 3, 4]
Input (stdin)
3
4
5
8
Output (stdout)
[4, 5, 8]
Program:
list=[]
n=int(input())
for i in range(1,n+1):
  list.append(int(input()))
print(list)
Q-7: find the largest number in the list
QUESTION: Write a program to find the largest number in the list Input format: Input consist of n+1 integers First integer corresponds to the size of the list Next n inputs corresponds to teh elements in the list Output format: Output is an integer list
Input (stdin)
5
3
2
6
1
7
Output (stdout)
7
Input (stdin)
5
1
4
7
8
9
Output (stdout)
9
Program:
list=[]
n=int(input())
for i in range(1,n+1):
  list.append(int(input()))
  max=list[0]
for i in list:
  if i>max:
    max=i
print(max)
Q-8: Find the smallest number in the list
Write a program to find the smallest number in the list Input format: Input consist of n+1 integers First integer corresponds to the size of the list Next n inputs corresponds to the elements in the list Output format: Output is an integer list
Input (stdin)
5
3
2
6
1
7
Output (stdout)
1
Input (stdin)
3
1
2
3
Output (stdout)
1
Program:
list=[]
n=int(input())
for i in range(1,n+1):
  list.append(int(input()))
  min=list[0]
for i in list:
  if i<min:
    min=i
print(min)
Q-9: Put even or odd number in a list
Python Program to Put Even and Odd elements in a List into Two Different Lists Problem Description The program takes a list and puts the even and odd elements in it into two separate lists. Problem Solution 1. Take in the number of elements and store it in a variable. 2. Take in the elements of the list one by one. 3. Use a for loop to traverse through the elements of the list and an if statement to check if the element is even or odd. 4. If the element is even, append it to a separate list and if it is odd, append it to a different one. 5. Display the elements in both the lists. 6. Exit. Input Format: Input consists of n + 1 integers. First integer corresponds to the size , The next n inputs corresponds to the elements in the list. Output Format First line corresponds to the even list Second line corresponds to the odd list
Input (stdin)
5
67
43
44
22
455
Output (stdout)
[44, 22]
[67, 43, 455]
Program:
list=[]
l1=[]
l2=[]
n = int(input())
for i in range(1,n+1):
  list.append(int(input()))
for i in list:
  if i%2==0:
    l1.append(i)
  else:
    l2.append(i)
print(l1)
print(l2)
Q-10: Find the second largest number in a list
Python Program to Find the Second Largest Number in a List Problem Description The program takes a list and prints the second largest number in the list. Problem Solution 1. Take in the number of elements and store it in a variable. 2. Take in the elements of the list one by one. 3. Sort the list in ascending order. 4. Print the second last element of the list. 5. Exit. Input Format: Input consists of n + 1 integers. First integer corresponds to the size , The next n inputs corresponds to the elements in the list.
Input (stdin)
4
23
56
39
11
Output (stdout)
39
  
Input (stdin)
5
41
25
36
74
85
Output (stdout)
74
Program:
list=[]
n=int(input())
for i in range(1,n+1):
  list.append(int(input()))
z=len(list)
list.sort()
for i in range(z-2,-1,-1):
  if list[i]!=list[z-1]:
    print(list[i])
    break
Q-11: Sort the list of Tuples
The program takes a list of tuples and sorts the list of tuples in increasing order by the last element in each tuple. Problem Solution 1. Take a list of tuples from the user. 2. Define a function which returns the last element of each tuple in the list of tuples. 3. Define another function with the previous function as the key and sort the list. 4. Print the sorted list. 5. Exit.
Input (stdin)
[(2,5),(1,2),(4,4),(2,3)]
Output (stdout)
Sorted:
[(1, 2), (2, 3), (4, 4), (2, 5)]
Program:
def last(n): return n[-1]
def sort_list_last(tuples):
  return sorted(tuples, key=last)
print("Sorted:")
print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3)]))
Q-12: Remove the Duplicate
The program takes a lists and removes the duplicate items from the list. Problem Solution Take the number of elements in the list and store it in a variable. Accept the values into the list using a for loop and insert them into the list. Use a for loop to traverse through the elements of the list. Use an if statement to check if the element is already there in the list and if it is not there, append it to another list. Print the non-duplicate items of the list. Exit.
Input (stdin)
5
10
10
20
20
20
  
Output (stdout)
Non-duplicate items:

[10, 20]
Input (stdin)
4
2
6
9
8
Output (stdout)
Non-duplicate items:

[2, 6, 9, 8]
Input (stdin)
3
4
4
5
Output (stdout)
Non-duplicate items:

[4, 5]
 
Program:
list=[]
list2=[]
n=int(input())
for i in range(1,n+1):
  list.append(int(input()))
for i in list:
  if i not in list2:
    list2.append(i)
print("Non-duplicate items:")
print(list2)
Tuples
Q-1 : Add an Item
Write a Python program to add an item in a tuple. Problem Solution 1.create a tuple 2.use merge of tuples with the + operator you can add an element and it will create a new tuple 3.add items in a specific index[:5] 4.convert the tuple to list 5.append the list(30)
Input (stdin)
(4, 6, 2, 8, 3, 1)                                             
(4, 6, 2, 8, 3, 1, 9)
(4, 6, 2, 8, 3, 15, 20, 25, 4, 6, 2, 8, 3)   
Output (stdout)
(4, 6, 2, 8, 3, 15, 20, 25, 4, 6, 2, 8, 3, 30)
Program:
tuplex=(4,6,2,8,3,1)
tuplex=tuplex[ :5]+(15,20,25)+tuplex[ :5]
listx=list(tuplex)
listx.append(30)
tuplex=tuple(listx)
print(tuplex)
Q-2 : Length of the tuple
Write a Python program to find the length of a tuple.
Input (stdin)
face
Output (stdout)
('f', 'a', 'c', 'e')
4
Program:
t = tuple(input())
print(t)
print(len(t))
Q-3: Sort a tuple
The program takes a list of tuples and sorts the list of tuples in increasing order by the last element in each tuple. Solution: 1. Take a list of tuples from the user. 2. Define a function which returns the last element of each tuple in the list of tuples. 3. Define another function with the previous function as the key and sort the list. 4. Print the sorted list. 5. Exit.
Input (stdin)
[(2,5),(1,2),(4,4),(2,3)]
Output (stdout)
[(1, 2), (2, 3), (4, 4), (2, 5)]
Input (stdin)
[(2,5),(1,2),(4,4)]
Output (stdout)
[(1, 2), (4, 4), (2, 5)]
Program:
def last(n): return n[-1]
def sort_tuple(tuples):
  return sorted(tuples, key=last)
l1=eval(input())
print(sort_tuple(l1))
Q-3: Sort a tuple
The program takes a list of tuples and sorts the list of tuples in increasing order by the last element in each tuple. Solution: 1. Take a list of tuples from the user. 2. Define a function which returns the last element of each tuple in the list of tuples. 3. Define another function with the previous function as the key and sort the list. 4. Print the sorted list. 5. Exit.
Input (stdin)
[(2,5),(1,2),(4,4),(2,3)]
Output (stdout)
[(1, 2), (2, 3), (4, 4), (2, 5)]
Input (stdin)
[(2,5),(1,2),(4,4)]
Output (stdout)
[(1, 2), (4, 4), (2, 5)]
Program:
def last(n): return n[-1]
def sort_tuple(tuples):
  return sorted(tuples, key=last)
l1=eval(input())
print(sort_tuple(l1))
Q-4: Reverse a Tuple
Write a Python program to reverse a tuple
Input (stdin)
python
Output (stdout)
('n', 'o', 'h', 't', 'y', 'p')
Program:
a = input()
print(tuple(reversed(a)))
Q-5: Unzip a list of tuple
Write a Python program to unzip a list of tuples into individual lists.
Input (stdin)
[(1,2), (3,4), (8,9)]
Output (stdout)
[(1, 3, 8), (2, 4, 9)]
Program:
l=[(1,2),(3,4),(8,9)]
print(list(zip(*l)))
Q-6: Indexing
Write a python program to find the index of an item of a tuple
Input (stdin)
permit
r
Output (stdout)
2
Program:
tuple = input()
index = tuple.index('r')
print(index)
Q-7: Repeated element in a tuple
Write a python program to find the repeated items of a tuple.
Input (stdin)
2,4,7,8,5,2,4,9,4
4
Output (stdout)
3
Program:
tuple,n = input(),int(input())
print(tuple.count('4'))
Dictionary
Q-1: Key value pair
The program takes a key-value pair and adds it to the dictionary. Problem Solution 1. Take a key-value pair from the user and store it in separate variables. 2. Declare a dictionary and initialize it to an empty dictionary. 3. Use the update() function to add the key-value pair to the dictionary. 4. Print the final dictionary. 5. Exit.
Input (stdin)
12
34
Output (stdout)
{12: 34}
Input (stdin)
34
35
Output (stdout)
{34: 35}
Program:
key=int(input(""))
value=int(input(""))
d={}
d.update({key:value})
print(d)
Q-2: Check key exist
The program takes a dictionary and checks if a given key exists in a dictionary or not. Problem Solution 1. Declare and initialize a dictionary to have some key-value pairs.{'A':1,'B':2,'C':3} 2. Take a key from the user and store it in a variable. 3. Using an if statement and the in operator, check if the key is present in the dictionary using the dictionary.keys() method. 4. If it is present, print the value of the key. 5. If it isn’t present, display that the key isn’t present in the dictionary. 6. Exit.
Input (stdin)
A
Output (stdout)
1
Input (stdin)
D
Output (stdout)
Key isn't present
Program:
d={'A':1,'B':2,'C':3}
key=input("")
if key in d.keys():
      print(d[key])
else:
      print("Key isn't present")
Q-3: Expression in (x,x*x)
The program takes a number from the user and generates a dictionary that contains numbers (between 1 and n) in the form (x,x*x). Problem Solution 1. Take a number from the user and store it in a separate variable. 2. Declare a dictionary and using dictionary comprehension initialize it to values keeping the number between 1 to n as the key and the square of the number as their values. 3. Print the final dictionary. 4. Exit.
 
 
Input (stdin)
5
Output (stdout)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
Program:
n=int(input(""))
d={x:x*x for x in range(1,n+1)}
print(d)
Q-4: Sum of all Items
The program takes a dictionary and prints the sum of all the items in the dictionary. Problem Solution 1. Declare and initialize a dictionary to have some key-value pairs.{'A':100,'B':540,'C':239} 2. Find the sum of all the values in the dictionary. 3. Print the total sum. 4. Exit.
Input (stdin)

Output (stdout)
Total sum of values in the dictionary:
879
Program:
d={'A':100,'B':540,'C':239}
print("Total sum of values in the dictionary:")
print(sum(d.values()))
Q-5: Concatenate
The program takes two dictionaries and concatenates them into one dictionary. Problem Solution 1. Declare and initialize two dictionaries with some key-value pairs d1={'A':1,'B':2} d2={'C':3} 2. Use the update() function to add the key-value pair from the second dictionary to the first dictionary. 3. Print the final dictionary. 4. Exit.
 Input (stdin)

Output (stdout)
Concatenated dictionary is:
{'A': 1, 'C': 3, 'B': 2}
Program:
d1={'A':1,'B':2}
d2={'C':3}
d1.update(d2)
print("Concatenated dictionary is:")
print(d1)
Functions
Q-1: Maximum Value
Write a python program to find maximum value using function concept
Input (stdin)
5
2
Output (stdout)
5
Input (stdin)
5
6
3
2
Output (stdout)
6
Program:
a =int(input());
b =int(input());
 
def find_Biggest():
  if(a >= b):
    largest=a
  else:
    largest=b
  print('',largest)
find_Biggest();
Q-2: Func_Square root
Find the square of a number using a function declaration using the return statement.
Input (stdin)
5
Output (stdout)
The square number is:25
Input (stdin)
4
Output (stdout)
The square number is:16
Program:
def sq(n):
  print("The square number is:{}".format(n**2))
num=int(input())
sq(num)
Q-3: Func_cube root
To find the cube of a number using a function declaration using the return statement.
Input (stdin)
5
 
Output (stdout)
The cube number is:125
Input (stdin)
10
Output (stdout)
The cube number is:1000
Program:
def cube(n):
  print("The cube number is:{}".format(n**3))
num=int(input())
cube(num)
Recursion
Q-1: Binary equivalent of a number using recursion
Write a python program takes a number and finds the binary equivalent of a number recursively.
Input (stdin)
5
Output (stdout)
1 0 1
Input (stdin)
7
Output (stdout)
1 1 1
Program:
def binary(n):
   if n > 1:
       binary(n//2)
   print(n % 2,end = ' ')
dec = int(input())
binary(dec)
Q-2: Fibonacci series using recursion
Write a Python Program to find the fibonacci series using recursion.
Input (stdin)
5
Output (stdout)
0
1
1
2
3
Input (stdin)
6
Output (stdout)
0
1
1
2
3
5
 
Program:
def recur_fibo(n): 
   if n <= 1: 
       return n 
   else: 
       return(recur_fibo(n-1) + recur_fibo(n-2)) 
nterms = int(input("")) 
if nterms <= 0: 
   print("Plese enter a positive integer") 
else: 
   for i in range(nterms): 
       print(recur_fibo(i)) 
Q-3: Flatten a Nested List using Recursion
Write a python program to Flatten a Nested List using Recursion.
Input (stdin)

Output (stdout)
Flattened list is: [1, 2, 3, 4]
Program:
def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])
s=[[1,2],[3,4]]
print("Flattened list is:",flatten(s))
Q-4: Sum of digits using recusrion
Write a python program takes a number and finds the sum of the digits of the number recursively.
Input (stdin)
135
Output (stdout)
9
Input (stdin)
5678
Output (stdout)
26
Program:
def sum_of_digit( n ):
    if n == 0:
        return 0
    return (n % 10 + sum_of_digit(int(n / 10)))
num=int(input(""))
result = sum_of_digit(num)
print(result)
Q-5: Reverse a string using recursion
Write a Python Program to reverse a string using recursion.
Input (stdin)
hello world
Output (stdout)
dlrow olleh
Input (stdin)
Hello programmer
Output (stdout)
remmargorp olleH
Program:
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = str(input(""))
print(reverse(a))
String
Q-1 : Replace all Occurrences of ‘a’ with $ in a String
ESome people are playing cricket match. One is wound, so he was taken to hospital. And there is no person to play the match. So one person is to replace instead of him. Help them to replace the person to win the match.(replace all occurrences of ‘a’ with ‘$’ in a string.) Problem Description The program takes a string and replaces all occurrences of ‘a’ with ‘$’. Problem Solution 1. Take a string and store it in a variable. 2. Using the replace function, replace all occurrences of ‘a’ and ‘A’ with ‘$’ and store it back in the variable. 3. Print the modified string. 4. Exit.


Input (stdin)
Apple
Output (stdout)
$pple
 
Program:
str=input()
str=str.replace('A','$')
print(str)
Q-2 : Remove the nth Index Character from a Non-Empty String
There is an interview process going on in a company. In that recruitment 200 people came for an interview. For HR it is very difficult to take an interview for those 200 peoples. So help the HR to disqualify the person who is sufficient for the proper work( remove the nth index character from a non-empty string..) Problem Description The program takes a string and removes the nth index character from the non-empty string. Program Explanation 1. User must enter a string and store it in a variable. 2. User must also enter the index of the character to remove. 3. The string and the index of the character to remove are passed as arguments to the remove function. 4. In the function, the string is split into two halves before the index character and after the index character. 5. The first half and the last half is then merged together using the ‘+’ operator. 6. The modified string is printed.


Input (stdin)
Hello
3
Output (stdout)
Helo
Input (stdin)
welcome
2
Output (stdout)
wecome
 
Program:
def remove(string, n): 
      first = string[:n]  
      last = string[n+1:] 
      return first + last
string=input()
n=int(input())
print(remove(string, n))
Q-3 : String and Replace Every Blank Space with Hyphen
There is a people standing in a row. We have to insert flower in each and every gap between two persons. Help the person to fill the gap between them. Write a Python Program to take a string and replace every blank space with a hyphen. Problem Description The program takes a string and replaces every blank space with a hyphen. Problem Solution 1. Take a string and store it in a variable. 2. Using the replace function, replace all occurrences of ‘ ‘ with ‘-‘ and store it back in the variable. 3. Print the modified string. 4. Exit.


Input (stdin)
hello world
Output (stdout)
hello-world
Input (stdin)
c programming
Output (stdout)
c-programming
 
Program:
str=input()
str=str.replace(' ','-')
print(str)
Q-4 : Remove the Characters of Odd Index Values in a String
Students in a class going to write an exam. In a bench there are 5 members were sitting. Staff wants the students to sit three in bench. So he/she told that odd number people who is sitting in the bench should move out and sit in another bench. Help the staff to find out the odd people out. Problem Description The program takes a string and removes the characters of odd index values in the string. Problem Solution 1. Take a string from the user and store it in a variable. 2. Pass the string as an argument to a function. 3. In the function, initialize a variable to an empty character. 4. Use a for loop to traverse through the string. 5. Use an if statement to check if the index of the string is odd or even. 6. If the index is odd, append the no character to the string. 7. Then print the modified string. 8. Exit.


Input (stdin)
hello
Output (stdout)
hlo
Input (stdin)
welcome
Output (stdout)
wloe
 
Program:
def modify(str):
  final = ""
  for i in range(len(str)):
    if (i % 2) == 0:
      final = final + str[i]
  return final
str = input()
print(modify(str))
Q-5 : Take in Two Strings and Display the Larger String without Using Built-in Functions
Write a Python Program to take in two strings and display the larger string without using built-in functions. Problem Description The program takes in two strings and display the larger string without using built-in function. Problem Solution 1. Take in two strings from the user and store it in separate variables. 2. Initialize the two count variables to zero. 3. Use a for loop to traverse through the characters in the string and increment the count variables each time a character is encountered. 4. Compare the count variables of both the strings. 5. Print the larger string. 6. Exit.


Input (stdin)
Delhi
Bangalore
Output (stdout)
Bangalore
 
Program:
str,str1 = input(),input()
c1,c2 = 0,0
for i in str:
  c1 = c1+1
for j in str1:
  c2 = c2+1
if(c1<c2):
  print(str1)
else:
  print(str)
Q-6 : Calculate the case in the String
There are 50 students in the class. The teacher wants to arrange them in the height order. So help the teacher to find the smallest person and tallest to arrange.(count the number of lowercase letters and uppercase letters in a string.) Problem Description The program takes a string and counts the number of lowercase letters and uppercase letters in the string. Problem Solution 1. Take a string from the user and store it in a variable. 2. Initialize the two count variables to 0. 3. Use a for loop to traverse through the characters in the string and increment the first count variable each time a lowercase character is encountered and increment the second count variable each time a uppercase character is encountered. 4. Print the total count of both the variables. 5. Exit.


Input (stdin)
HeLLo
Output (stdout)
2
3
 
Program:
str = input()
c1,c2 = 0,0
for i in str:
  if i.islower():
    c1 = c1+1
  else:
    c2 = c2+1
print(c1)
print(c2)
Q-7 : Check if a String is a Pangram or Not
Write a Python Program to check if a string is a pangram or not. Problem Description The program takes a string and checks if it is a pangram or not. Problem Solution 1. Take a string from the user and store it in a variable. 2. Pass the string as an argument to a function. 3. In the function, form two sets- one of all lower case letters and one of the letters in the string. 4. Subtract these both sets and check if it is equal to an empty set. 5. Print the final result. 6. Exit.


Input (stdin)
The quick brown fox jumps over the lazy dog.
Output (stdout)
pangram
 
Program:
from string import ascii_lowercase as asc_lower
def check(s):
    return set(asc_lower) - set(s.lower()) == set([])
strng=input()
if(check(strng)==True):
      print("pangram")
else:
      print("Not pangram")
Q-8 : Calculate the Number of Digits and Letters in a String
Write a Python Program to calculate the number of digits and letters in a string. Problem Description The program takes a string and calculates the number of digits and letters in a string. Problem Solution 1. Take a string from the user and store it in a variable. 2. Initialize the two count variables to 0. 3. Use a for loop to traverse through the characters in the string and increment the first count variable each time a digit is encountered and increment the second count variable each time a character is encountered. 4. Print the total count of both the variables. 5. Exit.


Input (stdin)
Hello123
Output (stdout)
3
8
 
Program:
s = input()
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print(d)
print(l+d)
Q-9 : form a new string made of the first 2 characters and last 2 characters from a given string
write a Python Program to form a new string made of the first 2 characters and last 2 characters from a given string. Problem Description The program takes a string and forms a new string made of the first 2 characters and last 2 characters from a given string. Problem Solution 1. Take a string from the user and store it in a variable. 2. Initialize a count variable to 0. 3. Use a for loop to traverse through the characters in the string and increment the count variable each time. 4. Form the new string using string slicing. 5. Print the newly formed string. 6. Exit.


Input (stdin)
Hello World
Output (stdout)
Held
 
Program:
str=input()
c=0
for i in str:
      c=c+1
new=str[0:2]+str[c-2:c]
print(new)
Q-10 : Characters in Ascending order
Write a python code to arrange the characters in ascending order of the given String


Input (stdin)
Top Speed
Output (stdout)
 deeoppst
Input (stdin)
God of War
Output (stdout)
  adfgoorw
 
Program:
str = input()
str2 = ''.join(sorted(str.lower()))
print(str2)
Q-11 : Count number of words
Write a Python program to count number of words in the given sentence.


Input (stdin)
Wildlife traditionally refers to undomesticated animal species, but has come to include all organisms that grow or live wild in an area without being introduced by humans
Output (stdout)
The number of words in string are : 27
 
Program:
s=input()
s=s.split()
print("The number of words in string are :",len(s))
Q-12 : Add substring at specific index
Write a Python program to add substring at specific index in the given string


Input (stdin)
Bond Bond
 James
4
 
Output (stdout)
Bond James Bond
Input (stdin)
Winner Winner Dinner
 Chicken
13
Output (stdout)
Winner Winner Chicken Dinner
 
Program:
s1=input()
s2=input()
indx=int(input())
a=s1[:indx]+s2+s1[indx:]
print(a)
Q-13 : Replace string1 with string 2
Write a Python code to replace the string1 with string 2.
Explanation:
Get two strings. Check whether first character of string2 is present in the string1. If yes, replace the remaining characters in string1 with string2
else concatenate both string.
 
Input (stdin)
My prince
precious
Output (stdout)
My precious
Input (stdin)
Lord Voldemort
 Tyrion
Output (stdout)
Lord Tyrion
 
Program:
s1=input()
s2=input()
indx=s1.find(s2[:1])
print(s1[:indx]+s2)
Q-14 : Highest occurrence of character
Write a Python code to find the highest occurrence of character in the given string. The string is in lower case.
Input (stdin)
iron man
Output (stdout)
n 2
Input (stdin)
avengers endgame
Output (stdout)
e 4
 
Program:
from collections import OrderedDict
string = input()
N= {}
for character in string:
    if character in N:
        N[character] += 1
    else:
        if character ==' ':
            pass
        else:
            N[character] = 1
D=OrderedDict(sorted(N.items()))
M= max(D, key=D.get)
print(M, D[M] )
Q-15 : String Encryption
Write a Java code to encrypt the given string using a key.


Input (stdin)
Game of Thrones
6
Output (stdout)
Mgsk ul Znxutky
Input (stdin)
Jhon Wick
53
Output (stdout)
Kipo Xjdl
 
Program:
str = input()
key = int(input())
temp = ""
for i in range(0,len(str)):
    if str[i]>='A' and str[i]<='Z':
        offset = ord(str[i])-65
        offset = (offset+key) % 26
        ch = chr(offset+ord('A'))
        temp +=ch
    elif str[i]>='a' and str[i]<='z':
        offset = ord(str[i])-97
        offset = (offset+key) % 26
        ch = chr(offset+ord('a'))
        temp +=ch
    else:
         temp+=" "
print(temp)
Q-16 : Run length encoding
Write a Python code that prints the run length encoding of the input string


Input (stdin)
ggggooooottttttt
Output (stdout)
g4o5t7
Input (stdin)
sssttTTaaar
Output (stdout)
s3t2T2a3r1
 
Program:
s1 =input()
n = len(s1)
i = 0
while i < n:
  count = 1
  while (i<n-1 and s1[i]== s1[i + 1]):
    count += 1
    i += 1
  i += 1
  print(s1[i-1]+str(count),end="")
Q-17 : Frequency of character
Write a Python program to find the frequency of character in the given string.


Input (stdin)
execute
Output (stdout)
c 1
e 3
t 1
u 1
x 1
Input (stdin)
Compilation
Output (stdout)
a 1
c 1
i 2
l 1
m 1
n 1
o 2
p 1
t 1
 
Program:
s1=input()
a=list(s1)
s2=set(s1)
s3=sorted(s2)
for letters in s3:
  print(letters,a.count(letters))
Q-18 : Frequency of words
Write a Python program to find the frequency of words in the given string.


Input (stdin)
Hatred was spreading everywhere blood was being spilled everywhere wars were breaking out everywhere
Output (stdout)
Hatred : 1
was : 2
spreading : 1
everywhere : 3
blood : 1
being : 1
spilled : 1
wars : 1
were : 1
breaking : 1
out : 1
Input (stdin)
No heart is so hard as the timid heart
Output (stdout)
No : 1
heart : 2
is : 1
so : 1
hard : 1
as : 1
the : 1
timid : 1
  
Program:
s1=input()
s1=s1.split()
s2=[]
for i in s1:            
  if i not in s2:
    s2.append(i)        
for i in range(len(s2)):
  print(s2[i], ':',s1.count(s2[i]))
Q-19 : Binary String
Write a Python program to check whether the given string is binary string or not.


Input (stdin)
1101010111
Output (stdout)
Binary String
Input (stdin)
1261010
Output (stdout)
Not a Binary String
 
Program:
def check(string) :
    p = set(string)
    s = {'0', '1'}
    if s == p or p == {'0'} or p == {'1'}:
        print("Binary String")
    else :
        print("Not a Binary String")
if __name__ == "__main__" :
    string = input()
    check(string)
Q-20 : accept strings which contains all vowels
Write a Python program to accept strings which contains all vowels.


Input (stdin)
Racecar
Output (stdout)
Not Accepted
Input (stdin)
EDUCATION
Output (stdout)
Accepted
 
 
Program:
s1=input()
s1=s1.lower()
l1=['a','e','i','o','u']
st=set()
for a in s1:
  if a in l1:
    st.add(a)
  else:
    pass
if len(st)==len(l1):
  print("Accepted")
else:
  print("Not Accepted")
Q-21 : Missing alphabets in String
Write a Python code to find the missing alphabets in the given string.


Input (stdin)
The quick brown fox jumps over the dog
Output (stdout)
a,l,y,z,
Input (stdin)
World
Output (stdout)
a,b,c,e,f,g,h,i,j,k,m,n,p,q,s,t,u,v,x,y,z,
 
Program:
MAX_CHAR = 26
def missingChars(Str) :
    present = [False for i in range(MAX_CHAR)]
    for i in range(len(Str)):
        if (Str[i] >= 'a' and Str[i] <= 'z'):
            present[ord(Str[i]) - ord('a')] = True
        elif (Str[i] >= 'A' and Str[i] <= 'Z'):
            present[ord(Str[i]) - ord('A')] = True
    res = ""
    for i in range(MAX_CHAR):
        if (present[i] == False):
            res += chr(i + ord('a'))
    return res
Str = input("")
d =missingChars(Str)
print(','. join(d), end=',' )
Q-22 : Palindrome
Write a Python program to check whether the given string is Palindrome or not.


Input (stdin)
racecar

Output (stdout)
Panlindrome
Input (stdin)
tutor
Output (stdout)
Not Palindrome
 
Program:
def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = input()
ans = isPalindrome(s)
 
if ans:
    print("Panlindrome")
else:
    print("Not Palindrome")
Q-23 : Reverse words
Write a Python program to reverse the words in the given string.


Input (stdin)
valar morghulis
Output (stdout)
morghulis valar
Input (stdin)
Show me the money
Output (stdout)
money the me Show
 
Program:
def rev_sentence(sentence):
 
    # first split the string into words
    words = sentence.split(' ')
 
    # then reverse the split string list and join using space
    reverse_sentence = ' '.join(reversed(words))
 
    # finally return the joined string
    return reverse_sentence 
if __name__ == "__main__":
    a=input()
    print (rev_sentence(a))
Q-24 : Substring is Present in a Given String
Write a Python program to find whether the substring is Present in a Given String


Input (stdin)
With great power comes great responsibility
power
Output (stdout)
YES
Input (stdin)
santa is coming
are
Output (stdout)
NO
 
Program:
def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")
           
# driver code
string = input()
sub_str =input()
check(string, sub_str)
