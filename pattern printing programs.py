N = 5

for i in range(1, N + 1):
    print("*" * i)
#output:
*
**
***
****
*****
N = 5

for i in range(N, 0, -1):
    print("*" * i)

#output:
* * * * *
* * * *
* * *
* *
*
N = 5

for i in range(1, N + 1):
    spaces = " " * (N - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
 #output:   
    *
   ***
  *****
 *******
*********
N = 5

for i in range(N, 0, -1):
    spaces = " " * (N - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
#output:
*********
 *******
  *****
   ***
    *
N = 4

# Upper half
for i in range(1, N + 1):
    spaces = " " * (N - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# Lower half
for i in range(N - 1, 0, -1):
    spaces = " " * (N - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
#output:
   *
  ***
 *****
*******
 *****
  ***
   *

N = 5

for i in range(1, N + 1):
    for j in range(i):
        print(i, end=" ")
    print()
#output:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
N = 5

for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#output:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
N = 5

for i in range(1, N + 1):
    # Increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # Decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()
    #output:
1
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
N = 5

for i in range(N):
    letter = chr(65 + i)
    for j in range(i + 1):
        print(letter, end=" ")
    print()
#output:
A
B B
C C C
D D D D
E E E E E
N = 5

for i in range(N):
    for j in range(N):
        if i == 0 or i == N - 1 or j == 0 or j == N - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
#0utput:
* * * * *
*       *
*       *
*       *
* * * * *
N = 4

# Upper half
for i in range(1, N + 1):
    spaces = " " * (N - i)
    
    if i == 1:
        print(spaces + "*")
    else:
        inner_spaces = " " * (2 * i - 3)
        print(spaces + "*" + inner_spaces + "*")

# Lower half
for i in range(N - 1, 0, -1):
    spaces = " " * (N - i)
    
    if i == 1:
        print(spaces + "*")
    else:
        inner_spaces = " " * (2 * i - 3)
        print(spaces + "*" + inner_spaces + "*")
#output:
   *
  * *
 *   *
*     *
 *   *
  * *
   *
N = 5
num = 1

for i in range(1, N + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
#output:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
N = 4

# Upper half
for i in range(1, N + 1):
    print("*" * i + " " * (2 * (N - i)) + "*" * i)

# Lower half
for i in range(N, 0, -1):
    print("*" * i + " " * (2 * (N - i)) + "*" * i)
#output:
*      *
**    **
***  ***
********
********
***  ***
**    **
*      *
