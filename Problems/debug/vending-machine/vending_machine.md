# Vending Machine

A vending machine is represented as a two-dimensional array of size n x m. Treat this vending machine as a Finite State Machine. Complete the Vending Machine class such that it vends items to a customer taking into account the different states of the machine.

## Class VendingMachine

### Attributes:

- `int itemsId[n][m]`: each element stores the id of the item at the ith row and jth column of the vending machine
- `int itemsCount[n][m]`: each element stores the number of items of itemsId[i][j] available
- `int itemsCost[n][m]`: each element stores the cost per unit of itemsId[i][j]
- `int totalCash`: represents the amount of money that can be used as change
- `VendingMachineState state`: an enum that represents the state of the machine as defined below

### Methods:

- `int selectItem(int i, int j)`: An item is selected at the ith row and jth column of the vending machine. If the item is out of stock, return -1, otherwise, return the id of the number that is selected.
- `int insertMoney(int money)`: A consumer inserted money units into the vending machine. If the money inserted is enough, return the amount to return as change. Otherwise, return -1.

**Note:** Assume that the totalCash is not affected by the amount of money inserted into the machine. The money received by the machine and the totalCash that can be dispensed as change are unrelated.

## Vending Machine States:

- `STAND_BY` : Default state; ready to take orders
- `SELECT_ITEM`: Wait for the consumer to select an item. If the selected item is out of stock, the vending machine goes into the `STAND_BY` state.
- `INSERT_MONEY`: Wait for the consumer to insert money. The machine can come to this state only if an item is already selected. If successful, the item is given money in vending machine is updated. If the request fails, the consumer's money is returned, and items are not changed. In either event, the machine goes to `STAND_BY`.

## Implementation Description

Fix the bugs in the code written below.

## Constraints

- 1 ≤ totalNumberOfRequests ≤ 105
- 1 ≤ n ≤ 103
- 1 ≤ m ≤ 103
- 1 ≤ i ≤ n
- 1 ≤ j ≤ m
- 1 ≤ totalCash ≤ 109
- 1 ≤ money ≤ 109

The first line contains two integers, n, and m, defining the dimensions of the vending machine arrays. Each line i of the next n lines contains m space-separated integers, itemsId[i]. Each line i of the next n lines contains m space-separated integers., itemsCount[i]. Each line i of the next n lines contains m space-separated integers, itemsCost[i]. The next line contains an integer, totalCash. The next line contains an integer, totalNumberOfRequests. Each of the next totalNumberOfRequests lines contains the name of a function to call and its arguments in order.
