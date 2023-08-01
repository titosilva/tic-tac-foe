from collections import defaultdict
from sys import argv, stdin, stdout
from typing import DefaultDict
import re
import readchar

class BFState:
    cells: DefaultDict[int, int]
    pointer: int

    def __init__(self) -> None:
        self.cells = defaultdict(lambda: 0)
        self.pointer = 0

    @property
    def curr_cell(self):
        return self.cells[self.pointer]
    
    @curr_cell.setter
    def curr_cell(self, value: int):
        self.cells[self.pointer] = value 

    def move_right(self):
        self.pointer += 1

    def move_left(self):
        self.pointer -= 1

    def increment(self):
        self.cells[self.pointer] += 1

    def decrement(self):
        self.cells[self.pointer] -= 1

def read_code() -> str:
    with open(argv[1], 'r') as f:
        lines = f.readlines()

        code = ''
        for line in lines:
            code += line

        return re.sub(r'[^\+\-\>\<\[\]\,\.]+', '', code)

bf_chars = [
    '>', '<',
    '[', ']',
    '+', '-',
    '.', ',',
]

if __name__ == "__main__":
    code = read_code()
    state = BFState()
    ins_pointer = -1

    while True:
        ins_pointer += 1
        if ins_pointer >= len(code) or ins_pointer < 0:
            print('\n<<< Finished >>>')
            break

        c = code[ins_pointer]

        if c not in bf_chars:
            continue

        if c == '>':
            state.move_right()
            continue

        if c == '<':
            state.move_left()
            continue

        if c == '+':
            state.increment()
            continue

        if c == '-':
            state.decrement()
            continue

        if c == '[':
            if state.curr_cell == 0:
                count = 0
                while True:
                    while (c := code[ins_pointer]) != ']':
                        if c == '[':
                            count += 1
                        ins_pointer += 1
                    
                    count -= 1
                    if count == 0:
                        break
                    else:
                        ins_pointer -= 1
            
            continue

        if c == ']':
            if state.curr_cell != 0:
                count = 0
                while True:
                    while (c := code[ins_pointer]) != '[':
                        if c == ']':
                            count += 1
                        ins_pointer -= 1
                    
                    count -= 1
                    if count == 0:
                        break
                    else:
                        ins_pointer -= 1
            
            continue

        if c == '.':
            print(chr(state.curr_cell), end = '')
            stdout.flush()
            continue

        if c == ',':
            char = readchar.readkey()
            print(char, end = '')
            stdout.flush()
            state.curr_cell = ord(char)
            continue
