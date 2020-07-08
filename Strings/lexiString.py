'''
Lexi String
Little Jill jumbled up the order of the letters in our dictionary. Now, Jack uses this list to find the smallest lexicographical string that can be made out of this new order. Can you help him?

You are given a string P that denotes the new order of letters in the English dictionary.

You need to print the smallest lexicographic string made by rearranging all the letters of the given string S.

Constraints
1 <= T <= 1000
Length (P) = 26
1 <= length (S) <= 100
All characters in the string S, P are in lowercase

Input Format
The first line contains number of test cases T
The second line has the string P
The third line has the string S
Output
Print a single string in a new line for every test case giving the result
Example Input
2
polikujmnhytgbvfredcxswqaz
abcd
qwryupcsfoghjkldezxvbintma
ativedoc
Output
bdca
codevita
Explanation
The transformed smallest lexicographical strings are in order they would be if order of letters are changed to string P

'''

t=int(input())
for i in range(t):
    p=input().strip()
    s=input().strip()
    q=''
    for i in p:
        if i in s:
            q=q+i*s.count(i)
    print(q)
