#********************************************************************
#
#  Developer:         <Brandon>
#
#  Program #:         9
#
#  File Name:         Program9.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          <July 10, 2019>
#
#  Instructor:        Sajjad Mohsin 
#
#  Chapter:           <Chapter #5, 6, and 7>
#
#  Description:
#     This program reads the contents of a file, displays the total,
#     maximum value, minimum value, and average, and associates those values,
#     with a dictionary of the months of the year.
#
#********************************************************************
def main():
    developerInfo()
    #call developerInfo()
    rainfall = open_file()
    #sets rainfall = function open_file()
    open_file()
    #call open_file()
    totalRainfall(rainfall)
    #call totalRainfall(rainfall)
    get_average_and_total(rainfall)
    #call get_average_and_total(rainfall)
    get_max_and_min(rainfall)
    #call get_max_and_min(rainfall)
    #end of main() function
def open_file():
    
    inFile = open('program9.txt', 'r')#opens the .txt file in read
    rainfall = inFile.readlines()# sets rainfall to read lines in file
    inFile.close()#closes the file
    index = 0 #accumulator end point
    while index < len(rainfall):# While there are more records
        rainfall[index] = float(rainfall[index])
        #reads rainfall into an index and makes the values float type
        index += 1 # accumulates the index until the value reaches the length
                #of rainfall.
    #returns rainfall
    return rainfall 
    #end of function open_file()
def totalRainfall(rainfall):
    
    #sets the accumulator end point for TotalRainfall and x
    TotalRainfall = 0
    x = 0
    while x < len(rainfall): #iterates until x is equal to the length of rainfall
        rainfall[x] = float(rainfall[x])#turns each value in rainfall into a float
        TotalRainfall = TotalRainfall + rainfall[x]#accumulates for total
        x = x + 1#accumulates to the length of rainfall
        float(TotalRainfall)
    #returns TotalRainfall
    return TotalRainfall
    #end of function totalRainfall(rainfall)
def get_average_and_total(TotalRainfall):
    #sets the value for numberMonths to 12
    numberMonths = 12
    #sets the end point for running total 
    total = 0.00
    #sets the start value of 'i' for each iteration
    i = 0.00
    #for each value in TotalRainfall, turns the value into a float
    #and accumulates the total as a running total
    for i in TotalRainfall:
        float(i)
        total+=i
    #prints the total
    print('The total rainfall is {:.02f}.'.format(total))
    
    #average is equal to the total of TotalRainfall divided by the number
    #of months in a year.
    average =  total / numberMonths
    
    #prints the average
    print('The average rainfall is {:.02f}.'.format(average))
    
    #end of function get_average_and_total(TotalRainfall)
def get_max_and_min(TotalRainfall):
    #creates a list for months
    months = ['January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November',
            'December']
    #creates a dictionary to associate months and TotalRainfall
    valueTable={}
    #Sets the start value for an accumulator to end the loop
    y = 0
    for x in TotalRainfall:
        valueTable[x] = months[y]
        y = y + 1
        #creates an accumulator
    #Gets the min and max TotalRainfall from valueTable
    maxRainfall = max(valueTable)
    minRainfall = min(valueTable)
    #prints the minRainfall and maxRainfall followed by the associated value in
    #the dictionary
    print('The maximum rainfall was {:.02f} in {}.'.format(maxRainfall, valueTable[maxRainfall]))
    print('The minimum rainfall was {:.02f} in {}.'.format(minRainfall, valueTable[minRainfall]))
    #end of function get_max_and_mind(TotalRainfall)
def developerInfo():

    print('Name: Brandon')
    print('Course: Programming Fundamentals I')
    print('Program: 9')
    print()

    # End of the developerInfo function
# Call the main function.
main()

#End of Program 9
