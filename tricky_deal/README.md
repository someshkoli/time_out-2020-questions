Problem statement
One of Chef's friends offered him a deal: during D days, they are going to exchange money. For each i (1≤i≤D), on the i-th day, Chef's friend would give Chef A rupees, while Chef would give his friend 2i−1 rupees (1 rupee on day 1, 2 rupees on day 2, 4 rupees on day 3

, and so on). Chef's profit from the deal is the total number of rupees he received from his friend minus the total number of rupees he gave his friend.

Chef decided to ask for your advice before accepting the deal. You want to help him by telling him two numbers D1
and D2, where D1 is the maximum value of D such that Chef should accept the deal, i.e. his profit from the deal is positive if D=D1, and D2 is the value of D that leads to the maximum possible profit for Chef. If there are multiple values of D that lead to the maximum profit, D2

is the smallest of these values.
Input

    The first line of the input contains a single integer T

denoting the number of test cases. The description of T
test cases follows.
The first and only line of each test case contains a single integer A

    .

Output

For each test case, print a single line containing two space-separated integers D1
and D2

.
Constraints

    1≤T≤100,000

5≤A≤109

Subtasks

Subtask #1 (100 points): original constraints
Example Input

4
5
8
9
1000000000

Example Output

4 3
5 3
5 4
35 30
