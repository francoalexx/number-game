import random
global list
global selected_positions
list = [None, None, None, None, None, None, None, None, None, None]
selected_positions = []
generated_nums = []


def round_one():
    global list
    global selected_positions
    global generated_nums
    global position
    global number

    number = random.randint(1, 10000)
    generated_nums.append(number)               # generate number and append to list 
    print(number)
    
    position = (int(input("Choose position: ")) - 1 )
    if position < 0 or position > 10:                       # user selects position, check if position is within 1-10
        print("Error")
        return
    
    selected_positions.append(position)         # if posisiton is available, append to selected_positions to keep track of taken slots 

    list[position] = number              # repalce None with number in list 
    print(list)
    return list

def round_two():
    counter = 0                         # counter allows the function to run only 9 times 
    while counter < 9:
        number = random.randint(1,10000)            # generate numeber and append to generated_nums 
        generated_nums.append(number)
        #print(selected_positions)
        print("Number: " + str(number)) 
        position = (int(input("Choose position: ")) - 1)        #user selects positiion 
        
        if position in selected_positions:  # checking if position is available
            print("Errooooor")
            return
        if position < 0 or position > 11:    # checking if position is within 1-10 
            print("Error")
            return
        selected_positions.append(position)         # if passes both test, append to selected_posiitons 

#####################################

        def compare_values_upward():  # goal is to compare the values of the recently generated number to the numbers down the list to list[0] 
            n = 1                                                           # if the number just generated is smaller than any value below, there is error 
            comp_value = list[position - n]  # number higher on the list compared to current position 
            #print('comp value: ' + str(comp_value ))
            while (position - n) > -1: 
                if comp_value != None:              # check if comp_value is not None bc if it is it cannot be compared 
                    while (position - n) > -1:      # makes sure the index of list[] does not get below 0 
                        if number < comp_value:
                            print("Erro, upward comp")      # check if new number is larger than values higher on the list 
                            quit()
                        else:
                            n += 1    # allows the function to keep searching higher up the list 
                else:
                    n += 1
        
        def compare_values_downward():          # same thing as last function just goes in the opposite direction 
            n = 1
            comp_value = list[position + n]
            while (position + n) < 10:          # makes sure list[] does not get above 9
                if comp_value != None:
                    if number > comp_value:
                        print("Error, downward comp ")
                        quit()
                    else:
                        n += 1
                else:
                    n += 1


        #def compare():
        #    z = 0
         #   none_check = list[position - z]
            #while (position - z) > -1:
          #      if none_check != None:
           #         compare_values_upward()
                             

###################################



        if 0 in selected_positions:       # only runs if #1 exists 

            if position == 0:
                if list[1] != None:             # compares #1 to #2 only in #2 exists, if #2 is smaller than #1 there is an error 
                    if number > list[1]:
                        print("Number too small")
                        return
            if position == 0:
                for i in generated_nums:            # compares #1 to all previous numbers and makes sure they are all larger 
                    if i < number:
                        print("Error, smaller than #1")
                        return  
                    else:
                        list[position] = number         # if pass tests, reraplce None in position with number 
                        print(list)
                        continue
            else:
                if number < list[0]:                        # if #1 is taken on previous round, it compares new number to #1 to make sure it is larger 
                    print("Error, smaller than #111")
                    return
            

        
        if 9 in selected_positions:  #only runs if #10 exists 

            if position == 9:
                if list[8] != None:
                    if number < list[8]:        # compares #9 to #10 only if #9 exists, if #9 is larger, error 
                        print("Number too big")
                        return
            if position == 9:
                for i in generated_nums:
                    if i > number:                          # compares all generated numbers to #10 to make sure they are smaller 
                        print("Error, bigger than #10")
                        return
                    else:
                        list[position] = number         # if passes test, add to list 
                        print(list)
                        continue
            else:
                if number > list[9]:
                    print("Error, bigger than list[9] ")      # if #10 is taken from previous round, compares new number ot #10 to ensure it is smaller 
                    return
                

        
        if position != 0: 
                                          # runs if posiiton is not #1 
            if list[position - 1] != None:              # checks to see if value above new number exists to it can be compared, I only want to compare values immediately next to new number
                print("ran upward comp")                # if can be compared, run the function
                compare_values_upward()
            else:
                pass
        if position != 9:
            if list[position + 1] != None:          # same as above just the other side of the list, and compares values going down the list to #10 
                print("ran downward comp")
                compare_values_downward()
            else:
                pass


                    




        








        list[position] = number
        print(list)











        counter += 1

#def compare_values_upward():
    n = 1
    comp_value = list[position - n]
    while comp_value > -1:
        if number < list[comp_value]:
            print("Erro, upward comp")
            quit()
        else:
            n += 1

#def compare_values_downward():
    n = 1
    comp_value = list[position + n]
    while comp_value < 10:
        if number < list[comp_value]:
            print("Error, downward comp ")
            quit()
        else:
            n += 1





round_one()
round_two()