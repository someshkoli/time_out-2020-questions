Problem Statement

It is 2042 and we are surrounded by cyborgs everywhere. Geneo is one such cyborg with a human body and an electronic brain. To monitor skills and health of Geneo he is posed with questions everyday. On one fine day Geneo was asked the following question.

You are given a string S of size N containing letters a to z. You are allowed to remove a character from the string and exchange it for a number signifying its position. i.e a -> 1, b -> 2, c -> 3, ... z -> 26. After some number of these operations you arrive at a final array A.

Power P of any such array is defined as:
count of letters - count of numbers + (sum of numbers/K)
where K is a given integer and '/' denotes float division.

Geneo has to find maximum possible power Pmax of such an array.
You want to test if Geneo is right. For this you have to generate correct answers for the question.
Input section

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.

The first line of each test case contains a two space separated integers N and K.

The second line of each test case contains the string S of size N.
Output Section

For each test case, output a single line containing two space seperated integers a and b such that a / b = Pmax - the maximum possible power achievable after transformation and gcd(a,b) = 1.
Input constraints

    1 ≤ T ≤ 100
    1 ≤ N ≤ 1000
    1 ≤ K ≤ 1000

Sample Input

2
10 6
abcdefghij
10 1
qwertyuiop

Sample Output

10 1
159 1

Explanation

For the first test case, if we replace no character, we get an array comprising of letters only. This gives us the maximum power 10.

For the second test case, we get maximum power when we replace all the characters by respective numbers.