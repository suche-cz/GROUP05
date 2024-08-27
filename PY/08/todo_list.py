# todo_list.py

# add Uklidit
# remove Uklidit
# clear
# print
# exit

task_list = []


while True:
    command = input('Zadej příkaz: ')

    if command == 'exit':
        break

    elif command == 'clear':
        task_list.clear()

    elif command == 'print':
        print('-----------------------------')
        index = 0
        for item in task_list:
            index += 1
            print(index, item)
        print('-----------------------------')

    elif command.startswith('add '):
        task_list.append(command[4:])
    
    elif command.startswith('remove '):
        if command[7:] in task_list:
            task_list.remove(command[7:])





"""
todo: ukládát úkoly do souboru
"""

