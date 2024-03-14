add_space = {
    'operator': ['(', ')', '/', '*', '-', '+'],
    'operations': ['/', '*', '-', '+'],
    'operations1': ['/', '*', '+']
}
def syntactic(stuff):
    i = 0
    numeric = 0
    temp_sign = '+'
    stack = []
    check = 0
    operator = False
    
    #if stuff[0] == '-':     #This makes the - have precedence
        #temp_sign = '-'
    #    stuff = '-1*' + stuff[1:]
        
    while i < (len(stuff)):
        
        if not (stuff[i].isdigit() or (stuff[i] in add_space['operator'])):
            return "MUST HAVE VALID CHARACTERS"
        if stuff[i].isdigit():  #checks if is integer, if yes it stores it
            check = 1
            numeric = numeric*10 + int(stuff[i])
            
        #need to do recursion for parenthesis
        
        if stuff[i] == '(': 
            if stuff[i+1]==')':
                return "ERROR"    #checks to see if beginning of parenthesis
            check = 1
            smaller_stuff = stuff[i:]   #makes a copy of list from current index
            parenthesis_record = 0  #keeps a record of how many parenthesis it comes across
            smaller_i = 0       #index for the copy
            
            while smaller_i < (len(smaller_stuff)): #Goes through copy
                if smaller_stuff[smaller_i] == '(':     #adds 1 to the record variable
                    parenthesis_record += 1
                
                elif smaller_stuff[smaller_i] == ')':   #Subtracts 1 from record variable
                    parenthesis_record -= 1
                    if parenthesis_record == 0:         #sees if record is 0, meaning it found
                        break                           #as many ( as )
                smaller_i += 1
                
            if parenthesis_record != 0:
                return "ERROR, missing parenthesis"
            
            numeric = syntactic(smaller_stuff[1:smaller_i]) #calls this function again for what was
            i = i + smaller_i                               #inside the parenthesis
            #print("TESTING")
        
        try:
            if stuff[i] in add_space['operations'] or (i+1 == len(stuff)): #checks if current char is / * + -
                #i+1 == len(stuff) is necessary because in a case like 6+7, it will only go inside this if statement
                #when stuff[i] is 7 (last index)
                check = 1
                #print("Inside operations", i)

                
                if temp_sign == '/':
                    operator = True
                    stack[len(stack)-1] /= numeric    #divides back of list by current number
                                                    #Overwrites back of stack because it takes precedence
                elif temp_sign == '*': 
                    operator = True
                    stack[len(stack)-1] *= numeric    #multiplies the back of list by the current number
                                                    #Overwrites back of stack because it takes precedence
                elif temp_sign == '-':
                    operator = True
                    stack.append(numeric * -1)  #multiplies number by -1 and adds to back of list
                elif temp_sign == '+':
                    operator = True
                    stack.append(numeric)   #Puts the number at back of the list
                
                temp_sign = stuff[i]    #Stores the next sign
                numeric = 0     #resets the number stored
            
            if i+1 == len(stuff) and stuff[i] in add_space['operations']:   #Returns an error if last char is an operator
                return "ERROR"
            if stuff[i] in add_space['operations'] and stuff[i+1] in add_space['operations1']:
                return "ERROR"
        except:
            #print("Invalid input")
            return "ERROR"
        
        #if check == 0:
        #    print("Invalid input")
        #    break
        #print(stack, i)
        i+= 1
        
        check = 0
        #else:
        #    print("Not valid symbol", stuff[i])
        #    break
        
    return int(sum(stack))   #adds all numbers in the stack giving the solution

expression = input("Enter the expression\n")

for stuff in add_space['operator']:
    if stuff in expression:
        expression = expression.replace(stuff, " " + stuff + " ")

stuff = expression.replace('  ', ' ')
stuff = stuff.replace(" ", "")

#stuff = list(expression.split(' '))
#stuff[len(stuff)-1] = '$'

print("ANSWER:",syntactic(stuff))