import random



def round_one():
    counter = 0
    while counter < 11:
        number = random.randint(1, 10000)
        print(number)
        position = int(input("Choose position: "))
        
        if position < 0 or position > 10:
            print("Error")
            return
        selected_positions = []
        selected_positions.append(position)
        i = []
        list = []
        list.insert(position, number)
        return list, selected_positions

def round_two():
    counter = 0
    while counter < 10:
        number = random.randint(1,10000)
        print(number)
        position = int(input("Choose position"))
        if position in selected_positions:
            print("Error")
            return
        if position < 0 or position > 10:
            print("Error")
            return
        list.insert(position, number)