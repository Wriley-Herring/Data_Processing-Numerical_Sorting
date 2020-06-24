'''
Created on Jun 18, 2020

@author: wrileyherring
'''


def sortA(filename):
    
    #open input file
    file = open(filename,'r')
    
    #read in file
    lines = file.readlines()
    
    #set maximum size
    k = lines.pop(0)
    
    #initialize numbers list
    numbers = []
    
    #fill numbers list with values and remove line spacing
    for line in lines:
        line = line.rstrip()
        numbers.append(line)
    
    #join into master string     
    numbers = " ".join(numbers)
    
    #split string into list of numbers
    numbers = numbers.split(" ")
    
    #convert strings to int
    numbers = list(map(int,numbers))
    
    #initialize array of zeros
    A = [0]* int(k)
    
    #set markers where of what numbers are contained in list
    for num in numbers:
        
        A[num] = A[num] + 1
    
    #initialize sorted list 
    sortedList =[]
   
    
    i = 1 
    #parse through array
    for index in range(int(k)):
        
        
        if A[index] != 0:
            
            #if array doesn't contain zero add it too the sorted list
            for j in range(A[index]):
                
                #if sorted 10 elements add a line space
                if i % 10 == 0:
                    sortedList.append(str(index))
                    sortedList.append('\n')
                    i+=1
                else:
                    sortedList.append(str(index))
                    i+=1

        else:
            pass
    
    #join sorted list into string 
    sortedList = " ".join(sortedList)
    
    #create output file
    outFile = filename.replace("in","out")
    outFile = outFile.replace(".txt","a.txt")
    
    #write sorted list to output file
    out = open(outFile,"w+")
    out.write(sortedList)
          
          
def sortB(filename):
    
    #open input file
    file = open(filename,'r')
    
    #read in file
    lines = file.readlines()
    
    #initialize numbers list
    numbers = []
    
    #remove k value
    lines.pop(0)
    
    #fill numbers list with values and remove line spacing
    for line in lines:
        line = line.rstrip()
        numbers.append(line)
    
    #join into master string     
    numbers = " ".join(numbers)
    
    #split string into list of numbers
    numbers = numbers.split(" ")
    
    #convert strings to int
    numbers = list(map(int,numbers))
    
    #set length of array
    arrayLength = len(numbers)
    
    #traverse array element by element
    for i in range(arrayLength - 1):
        
        #move through elements for every element
        for j in range(arrayLength -i -1):
            
            #if element is found to be greater than thr next
            #swap the elements
            if numbers[j] > numbers[j+1]:
                
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    
    #convert list of ints back to strings
    numbers = list(map(str,numbers))
    
    #join sorted list into string 
    sortedList = " ".join(numbers)
    
    #create output file
    outFile = filename.replace("in","out")
    outFile = outFile.replace(".txt","b.txt")
    
    #write sorted list to output file
    out = open(outFile,"w+")
    out.write(sortedList)
                       
        
if __name__ == '__main__':
    
    #sort in10.txt with sortA
    sortA("in10.txt")
    
    #sort in100.txt with sortA
    sortA("in100.txt")
    
    #sort in10.txt with sortB
    sortB("in10.txt")
    
    #sort in100.txt with sortB
    sortB("in100.txt")
    