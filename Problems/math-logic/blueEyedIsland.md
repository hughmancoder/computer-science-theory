# Blue eyed island

## Inital workthrough

Example Case: 3bl,4br,10bl,5g

Person A commands every person with blue eyes to assemble in a group in which case if everyone in that group who has blue eyes is present they all can leave withing 1 day.

If person A has blue eyes than person B who does not have blue eyes commands everyone who has blue eyes to assemble in a group (person A) who will leave on the subsequent evening.

Hence this solutino will take at most two evenings to progress or optimally one evening

## Solution

Case of 1 Blue-Eyed Person: If there is only one person with blue eyes, they will see that no one else has blue eyes. Since they know at least one person has blue eyes, they must conclude that it's them. They will leave on the first evening.

Case of 2 Blue-Eyed People: If there are two people with blue eyes, each will see exactly one person with blue eyes. If there was only one blue-eyed person, that person would leave on the first evening (as per the first case). When this doesn't happen, each of the two realizes that there must be another person with blue eyes and that this person can only be themselves. Therefore, both leave on the second evening.

Case of 3 Blue-Eyed People: Each of the three sees two others with blue eyes. They wait to see if those two leave on the second evening (as they would in the two-person case). When they don't, each realizes there must be three blue-eyed people, including themselves. So, all three leave on the third evening.

General Case: This pattern continues for any number of blue-eyed people. If there are
�
n people with blue eyes, each will see
�
−
1
n−1 people with blue eyes and will wait
�
−
1
n−1 days to see if those
�
−
1
n−1 people leave. When they don't, each realizes there must be
�
n blue-eyed people. So, all
�
n blue-eyed people will leave on the
�
nth evening.
