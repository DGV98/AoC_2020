import sys
import os
ACCUM = 0

class Command(object):
    def __init__(self, command, arg):
        self.command = command
        self.arg = arg
        self.touched = False
        self.last_changed = False
        self.already_changed = False

    def print_self(self):
        print(self.command + " " + str(self.arg))
        print("I was changed:", self.already_changed)
    
    def execute(self):
        global ACCUM
        self.touched = True
        if self.command == "acc":
            ACCUM += self.arg
            return 1
        elif self.command == "nop":
            return 1
        else:
            return self.arg

def main():
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print("File %s is not correct", filepath)
        sys.exit()
    commands = parse_file(filepath)
    # execute_commands_part_1(commands)
    print(run_no_inifinite(commands))

    # print(ACCUM)
    
def parse_file(filepath):
    commands = []
    with open(filepath) as f:
        for line in f:
            command = line.split(" ")
            if command[1][0] == "-":
                arg = -1 * int(command[1][1:])
            else:
                arg = int(command[1][1:])
            commands.append(Command(command[0], arg))
    return commands

def execute_commands_part_1(commands):
    i = 0
    while i < len(commands):
        command = commands[i]
        # command.print_self()
        if command.touched:
            break
        i += command.execute()
    return

def run_no_inifinite(commands):
    accum = 0
    i = 0
    while i < len(commands):
        command = commands[i]
        # command.print_self()
        # print(i)
        if command.touched:
            break
        i += command.execute()
    if i == len(commands)-1:
        return accum
    else:
        change_command(commands)
        return run_no_inifinite(commands)
        
def change_command(commands):
    for i in commands:
        i.print_self()
        if i.last_changed:
            # command.print_self()
            if i.command == "nop":
                i.command = "jmp"
            else:
                i.command = "nop"
            i.last_changed = False
            i.already_changed = True
            continue
        if i.command == "nop" and not i.already_changed:
            i.command = "jmp"
            i.last_changed = True
        elif i.command == "jmp" and not i.already_changed:
            i.command = "nop"
            i.last_changed = True
        return

if __name__ == "__main__":
    main()
