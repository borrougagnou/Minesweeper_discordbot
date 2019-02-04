#!/usr/bin/env python3

#"""A command line version of Minesweeper"""
#""" MIT LICENCE """
# from anon and borrougagnou

import random
from sys import argv
from enum import Enum

class Emoji(Enum):
    white_large_square = 0
    #zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    boom = 9


def creategrid(gridsize, nbmines):
    emptygrid = [['0' for i in range(gridsize)] for i in range(gridsize)]

    mines = getmines(emptygrid, (0,0), nbmines)
    for i, j in mines:
        emptygrid[i][j] = 'X'

    grid = getnumbers(emptygrid)

    return (grid, mines)


def showgrid(grid):
    # Print left row numbers
    for idx, i in enumerate(grid):
        #row = ':'
        row = '||:'
        for j in i:
            #row = row + (Emoji(9).name if j is 'X' else Emoji(int(j)).name) + '::'
            row = row + (Emoji(9).name if j is 'X' else Emoji(int(j)).name) + ':||||:'
        #print(row[0:-1])
        print(row[0:-3])


def getrandomcell(grid):
    gridsize = len(grid)

    a = random.randint(0, gridsize - 1)
    b = random.randint(0, gridsize - 1)

    return (a, b)


def getneighbors(grid, rowno, colno):
    gridsize = len(grid)
    neighbors = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            elif -1 < (rowno + i) < gridsize and -1 < (colno + j) < gridsize:
                neighbors.append((rowno + i, colno + j))

    return neighbors


def getmines(grid, start, numberofmines):
    mines = []
    neighbors = getneighbors(grid, *start)

    for i in range(numberofmines):
        cell = getrandomcell(grid)
        while cell == start or cell in mines or cell in neighbors:
            cell = getrandomcell(grid)
        mines.append(cell)

    return mines


def getnumbers(grid):
    for rowno, row in enumerate(grid):
        for colno, cell in enumerate(row):
            if cell != 'X':
                # Gets the values of the neighbors
                values = [grid[r][c] for r, c in getneighbors(grid,
                                                              rowno, colno)]

                # Counts how many are mines
                grid[rowno][colno] = str(values.count('X'))

    return grid


def main():
    gridsize = 10
    nbmines = 15

    if len(argv) > 1:
        if argv[1].isdigit():
            nbmines = int(argv[1])
            if nbmines < 5 or nbmines > 96:
                print("it's not a number between 5 and 96")
                return
        elif "undefined" not in argv[1]:
            print("it's not a number between 5 et 96")
            return

    grid = []
    grid, mines = creategrid(gridsize, nbmines)
    print('.')
    showgrid(grid)
    return

main()
