# Vending Machine

A vending machine is represented as a two-dimensional array of size n x m. Treat this vending machine as a Finite State Machine. Complete the Vending Machine class such that it vends Items to a customer taking into account the different states of the machine.

**Class VendingMachine** has the following attributes:

- `int itemsId[n][m]`: Each element stores the id of the item at the row and column of the vending machine.
- `int itemsCount[n][m]`: Each element stores the number of items of `itemsId[i][j]` available.
- `int itemsCost[n][m]`: Each element stores the cost per unit of `itemsId[i][j]`.
- `int totalCash`: Represents the amount of money that can be used as change.
- `VendingMachineState state`: An enum that represents the state of the machine as defined below.

**Class VendingMachine** has the following methods:

- `int selectItem(int i, int j)`: An item is selected at the i-th row and j-th column of the vending machine. If the item is out of stock, return -1, otherwise, return the id of the number that is selected.
- `int insertMoney(int money)`: A consumer inserted money units into the vending machine. If the money inserted is enough, return the amount to return as change. Otherwise, return -1.

**Note**: Assume that the `totalCash` is not affected by the amount of money inserted into the machine. The money received by the machine and the `totalCash` that can be dispensed as change are unrelated.

The different states of the vending machine are:

- `SELECT_ITEM`: Wait for the consumer to select an item. If the selected item is out of stock, the vending machine goes into the `STAND_BY` state.
- `INSERT_MONEY`: Wait for the consumer to insert money. The machine can come to this state only if an item is already selected. If successful, the item is given, money in vending machine is updated. If the request fails, the consumer's money is returned, and items are not changed. In either event, the machine goes to `STAND_BY`.

**Implementation Description**: Fix the bugs in the code written below.
