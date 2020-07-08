'''
Logic Pyramid
Identify the logic behind the series

6 28 66 120 190 276....
The numbers in the series should be used to create a Pyramid.

The base of the Pyramid will be the widest and will start converging towards the top where there will only be one element. Each successive layer will have one number less than that on the layer below it. The width of the Pyramid is specified by an input parameter N. In other words there will be N numbers on the bottom layer of the pyramid.

The Pyramid construction rules are as follows:

First number in the series should be at the top of the Pyramid
Last N number of the series should be on the bottom-most layer of the Pyramid, with Nth number being the right-most number of this layer.
Numbers less than 5-digits must be padded with zeroes to maintain the sanctity of a Pyramid when printed. Have a look at the examples below to get a pictorial understanding of what this rule actually means.
Example

If input is 2, output will be

   00006   
00028 00066
If input is 3, output will be

      00006   
   00028 00066   
00120 00190 00276
Formal input and output specifications are stated below

Input Format:
First line of input will contain number k - the number of inputs.
The following k lines contain N that corresponds to the width of the bottom-most layer of each Pyramid

Output Format:
The Pyramid constructed out of numbers in the series as per stated construction rules

Constraints:
0 < N <= 14
'''

k=int(input())
for p in range(k):
    n=int(input())
    x=6
    y=22
    for row in range(1,n+1):
        print((n-row)*'   ',end='')
        for j in range(1,row+1):
            print(format(x,'05'),end=' ')
            x=x+y
            y=y+16
        print()
