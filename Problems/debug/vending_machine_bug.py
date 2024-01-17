#!/bin/python3

import math
import os
import random
import re
import sys

class VendingMachineStates:
    STAND_BY = "STAND_BY"
    SELECTED_ITEM = "SELECTED_ITEM"
    INSERT_MONEY = "INSERT_MONEY"

    def __init__(self):
        self.valid_from_states = { 
            VendingMachineStates.STAND_BY: [VendingMachineStates.SELECTED_ITEM, VendingMachineStates.INSERT_MONEY],
            VendingMachineStates.SELECTED_ITEM: [VendingMachineStates.STAND_BY],
            VendingMachineStates.INSERT_MONEY: [VendingMachineStates.SELECTED_ITEM] 
        }

    def can_change_vending_machine_state(self, from_state, to_state):
        return from_state in self.valid_from_states[to_state]


class VendingMachine:
    def __init__(self, total_cash, items_number, items_count, items_cost):
        self.items_number = items_number
        self.items_count = items_count
        self.items_cost = items_cost
        self.total_cash = total_cash

        self.selected_index = [-1, -1]
        self.state = VendingMachineStates.STAND_BY

    def reset_vending_machine(self):
        self.selected_index = [-1, -1]
        self.state = VendingMachineStates.STAND_BY

    def select_item(self, i, j):
        i -= 1
        j -= 1

        if not VendingMachineStates().can_change_vending_machine_state(self.state, VendingMachineStates.SELECTED_ITEM):
            self.reset_vending_machine()
            return -1

        self.state = VendingMachineStates.INSERT_MONEY

        if i >= len(self.items_number) or j >= len(self.items_number) or i < 0 or j < 0:
            self.reset_vending_machine()
            return -1

        if self.items_count[i][j] < 0:
            self.reset_vending_machine()
            return -1

        self.selected_index = [i, j]
        return self.items_number[i][j]

    def insert_money(self, money):
        if not VendingMachineStates().can_change_vending_machine_state(self.state, VendingMachineStates.STAND_BY):
            # print("here", self.state, money)
            self.reset_vending_machine()
            return -1

        cost_of_selected_item = self.items_cost[self.selected_index[0]][self.selected_index[1]]
        change = money - cost_of_selected_item
        if change < 0 or change > self.total_cash:
            self.reset_vending_machine()
            return -1

        self.total_cash -= cost_of_selected_item
        self.items_count[self.selected_index[0]][self.selected_index[1]] -= 1
        self.state = VendingMachineStates.STAND_BY
        return change

def read(N, M, arr):
    for i in range(N):
        inp = input().strip().split(" ")
        for j in range(M):
            arr[i][j] = int(inp[j])


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N, M = map(int, input().rstrip().split())

    item_id = [[0 for _ in range(M)] for _ in range(N)]
    items_count = [[0 for _ in range(M)] for _ in range(N)]
    items_cost = [[0 for _ in range(M)] for _ in range(N)]

    read(N, M, item_id)
    read(N, M, items_count)
    read(N, M, items_cost)

    total_cash = int(input().strip())
    total_number_of_requests = int(input().strip())

    vending_machine = VendingMachine(total_cash, item_id, items_count, items_cost)

    for request_number in range(1, total_number_of_requests + 1):
        inp = input().strip().split(" ")
        command = inp[0]
        if command == "selectItem":
            i, j = int(inp[1]), int(inp[2])
            res = vending_machine.select_item(i, j)
            fptr.write(str(res) + ' ' + str(vending_machine.state) + '\n')

            print(res, vending_machine.state)
        elif command == "insertMoney":
            money = int(inp[1])
            res = vending_machine.insert_money(money)
            fptr.write(str(res) + ' ' + str(vending_machine.state) + '\n')
    
    fptr.close()


if __name__ == "__main__":
    main()