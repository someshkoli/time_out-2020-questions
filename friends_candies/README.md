Problem Statement
Hasan is preparing a party for his M friends (numbered 1 through M). He bought N baskets of candies (numbered 1 through N); for each valid i, the i-th basket contains ai

candies.

Each friend should get at most one candy. For each valid i
, the i-th friend would like to get a candy either from one of the first Li baskets or one of the last Ri baskets, i.e. a from basket b (1≤b≤N) such that b≤Li or b≥N+1−Ri

.

Hasan loves his friends, so he wants as many of them as possible to get the candies they want. If he distributes the candies optimally, what is the maximum number of his friends who will get the candies they want?
Input

    The first line of the input contains a single integer T

denoting the number of test cases. The description of T
test cases follows.
The first line of each test case contains two space-separated integers N
and M
.
The second line contains N
space-separated integers a1,a2,…,aN
.
M
lines follow. For each i (1≤i≤M), the i-th of these lines contains two space-separated integers Li and Ri

    .

Output

    For each test case, print a single line containing one integer — the maximum number of Hasan's friends who can get the candies they want.
Constraints

    1≤T≤103

1≤N,M≤106
0≤ai≤106
for each valid i
0≤Li,Ri≤N
for each valid i
0≤Li+Ri≤N
for each valid i
the sum of N
over all test cases does not exceed 106
the sum of M
over all test cases does not exceed 106

Example Input

2
3 3
1 1 1
0 2
1 1
0 2
3 3
1 1 1
1 1
1 1
1 1

Example Output

3
2

Explanation

Example case 1: We can give a candy from basket 1
to the 2-nd friend, a candy from basket 2 to the 1-st friend and a candy from basket 3 to the 3-rd friend.