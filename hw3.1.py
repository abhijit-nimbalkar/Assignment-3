#Author Name-Abhijit Nimbalkar and Sriman Kolachalam
#Homework-3

def main():
    call_a_function={1:problem1,2:problem2,3:problem3,4:problem4,5:problem5,6:problem6,7:problem7,8:problem8} #Creating the dict to call functions
    records2=[]
    while True:     #while loop for showing options to users until user ends the program or enter 9 
        try:
            input_value=main_menu_of_homework3()  #calling the function to display menu option
            if input_value in call_a_function:
                records2=call_a_function[input_value](records2) #as per the input, using dict, calling required function
            elif input_value==9:    #ending the program
                return
            else:
                print("Please enter in input from 1 to 9. Otherwise I am not able to understand what you want. The program will again restart.")
        except:
            print("Oops!Either you have not specified the *FILE PATH* or you have entered *WRONG Number*. The program will again restart.")


def main_menu_of_homework3():   #Calling menu function to display menu
    print('\n\nPlease select from Below Menu***STRICTLY EXECUTE IN SEQUENCE***-')
    print("1.Program a","2.Program b","3.Program c",'4.Program d','5.Program e','6.Program f','7.Program g','8.Program h','9.Exit',sep='\n')
    input_value=input("Please enter number from 1 to 9 to run the above designated program?-> ")
    return int(input_value) #returning the input value user has entered

#Problem Statement 1.a
def problem1(records):
    with open('/Users/Deadpool/Desktop/Classes/Python/Assignment 3/expenses.txt') as fin:   #opening the file with 'with open'
        records=[]  #declaring empty list
        data=[]
        for line in fin:
            records.append(line[:-1])   #stripping newline charachter

    for line in records:
        print(line)
    return data

#problem Statement 1.b    
def problem2(records):
    with open('/Users/Deadpool/Desktop/Classes/Python/Assignment 3/expenses.txt') as fin:
        records2=[] #declaring empty record
        for line in fin:
            line=line[:-1]  #stripping newline charachter
            columns=line.split(':') #splitting each items by ':'
            records2.append(columns)    #appending each row to column

    for row in records2:
        print(row)  #displaying each row
    return records2

#problem Statement 1.c
def problem3(records2):
    if records2==[]:#List will be empty if proper sequence is not followed
        print("Oops! Oops! Already told you! Please follow the SEQUENCE!")
        return records2
    r2_copy=records2.copy() #copying the records
    r2_copy.sort()  #sorting the list
    for row in r2_copy:
        print(row)
    print("Comment: This list is sorted on first charachter!!")
    return records2

#problem Statement 1.d
def problem4(records2):
    if records2==[]:#List will be empty if proper sequence is not followed
        print("Oops! Already told you! Please follow the SEQUENCE!")
        return records2
    header=records2[0]
    data=[]
    print(header)
    for row in range(1,len(records2)):
        data.append(records2[row])  #seperating the header and appeding it to the new list of data
    print(header)
    for d in data:
        print(d)
    return {'header':header,'data':data}
        
#problem Statement 1.e
def problem5(header_and_data):
    if header_and_data==[]:#List will be empty if proper sequence is not followed
        print("Oops! Already told you! Please follow the SEQUENCE!")
        return header_and_data
    data=header_and_data['data'].copy()
    for row in data:
        row[0]=float(row[0])    #Converting the amount column into float
    print(header_and_data['header'])
    for row in data:
        print(row)
    return {'header':header_and_data['header'],'data':data}

#problem Statement 1.f
def problem6(header_and_data):  
    if header_and_data==[]:#List will be empty if proper sequence is not followed
        print("Oops! Already told you! Please follow the SEQUENCE!")
        return header_and_data
    data=header_and_data['data'].copy()
    data.sort()     #Sorting the list
    print(header_and_data['header'])
    for row in data:
        print(row)
    return {'header':header_and_data['header'],'data':data}

#problem Statement 1.g
def problem7(header_and_data):
    if header_and_data==[]: #List will be empty if proper sequence is not followed
        print("Oops! Already told you! Please follow the SEQUENCE!")
        return header_and_data
    categories=set()
    item=''
    for row in header_and_data['data']:
        if row[1] not in categories:    #taking only unique categories
            categories.add(row[1])
    print('There are', len(categories), 'expense categories:')
    for c in categories:
        print(c)
    return {'header':header_and_data['header'],'data':header_and_data['data']}

#problem Statement 1.g
def problem8(records2):
    n2s = {"01" : "Jan", "02" : "Feb", "03" : "Mar", "04" : "Apr", "05" : "May", "06" : "Jun",
           "07" : "Jul", "08" : "Aug", "09" : "Sep", "10" : "Oct", "11" : "Nov", "12": "Dec"}
    print("{:<6}{:<6}".format("Key", "Value"))
    for key, value in n2s.items():      #looping through dict
        print("{:<6}{:<6}".format(key, value))
    return records2

    
main()  #calling main() function
