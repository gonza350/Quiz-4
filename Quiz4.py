def scalarvecmulti(scalar,vector):
    """
    The function scalarvecmulti(scalar,vector) does the following
    1: A for loop is implemented.
    2: the for loop checks  to see if the elements are integers floating point numbers and complex numbers.
       if the elements are not integers floating point numbers and complex numbers the function returns invalid input.
       if it is true the loop continues and defines a a variable as an empty list
    3: another loop is implemented that multiplies the elements of the vector by the scalar.
    4: The elements are then appended to the enpty list and returned. 
    """
    for i in range(len(vector)):
       inputstatus = True
    for i in range(len(vector)):
        if ((type(vector[i]) != int) and (type(vector[i]) != float) and (type(vector[i]) != complex)):
            inputstatus = False
            print("Invalid Input")
        if inputstatus == True:
            scalaranswer=[]
            for i in range(len(vector)):
                scalaranswer1=scalar*vector[i]
                scalaranswer.append(scalaranswer1)
        return scalaranswer

def dot(vector01,vector02):
    """
    The function dot(vector1,vector2) does the following.
    1: A for loop is implementedthat sets a variable as True
    2: another for loop is implemented that checks to see if the elemtns in vector are int float and complex.
    3: if they are not the function prints Invalid input
    4: if they are true a variable is set that checks to see the length of vector one and vector two.
    5: if it is not true the function prints out invalid input.
    6: a for loop is implemented that multiplies the elemnts of vector 1 by vector 2 and returns the answer. 
    """
    for i in range(len(vector01)):
       inputstatus = True
    for i in range(len(vector01)):
        if ((type(vector01[i]) != int) and (type(vector01[i]) != float) and (type(vector01[i]) != complex)):
            inputstatus = False
            print("Invalid Input")
        if inputstatus == True:
            isvalid=len(vector01)==len(vector02)
            if isvalid is False:
                print("Invalid Input")
                return None
            answer=0
            for i in range(len(vector01)):
                answer+= vector01[i]*vector02[i]
        return answer
 
def vecsubtract(vector01,vector02):
    """
    The function vecsubtract(vector01,vector02) does the following.
    1: The function inplements a for loop
    2: in the for loop the function checks to see if the elemtns in the vector are int floats or complex numbers
    3: if it is false the function prints out invalid input
    4: if its true 
    5: The function checks to see if vector01 or vector 02 is a list
       if its not a list the function prints out Invalid Input and returns
       None.
    6: The function sets a variable titled isvalid and states that
       the length of vector01 is equal to vector02. If the lenghts are not
       equal the function prints Invalid Input and returns None.
    7: The function sets a variable titled answer as an empty list.
    8: the function then goes through a for loop and goes through the numbers
       in the entire length of vector01, it then sets a variable titled
       addedanswer and in the variable addedanswer subtracts the elements in
       vector02 from the elements in vector01
       the results from addedanswer are then appended to the emptylist in the
       variable answer and returns the updated list in the variable answer. 
    """
    for i in range(len(vector01)):
        inputstatus = True
        for i in range(len(vector01)):
            if ((type(vector01[i]) != int) and (type(vector01[i]) != float) and (type(vector01[i]) != complex)):
                inputstatus = False
                print("Invalid Input")
            if inputstatus == True:
                if type(vector01) != list or type(vector02) != list:
                    print("Invalid Input")
                    return None
                isvalid=len(vector01)==len(vector02)
                if isvalid is False:
                    print("Invalid Input")
                    return None
                answer=[]
                for i in range(len(vector01)):
                    addedanswer = vector01[i]-vector02[i]
                    answer.append(addedanswer)
                return answer 

def twonorm(vector):
    """
    The function does the following.
    1: a variable titled imputstatus is set to the boolean True
    2: The function checks to see if the elemetns in the function
       are integers booleans and floating point numbers
    3: if the inputs are true a variable titled result is set
       to 0
    4: A for loop is implemented and a variable titled result is set
       in the variable the loop adds the variable result and squares teh elements
       in the vector and teh outside function result takes the square root of the
       squares and returns the result. 
    """
    for i in range(len(vector)):
       inputstatus = True
    for i in range(len(vector)):
        if ((type(vector[i]) != int) and (type(vector[i]) != float) and (type(vector[i]) != complex)):
            inputstatus = False
            print("Invalid Input")
        if inputstatus == True:
            result = 0
            for i in range(len(vector)):
                result = result + (vector[i]**2)
            result = result**(1/2)
        return result 

def normalized(vector):
    """
    The function does the following.
    1: A for loop is implemented.
    2: the loop checks teh elements of the vector for int float and complex numbers.
    3: if its false the function prints out invalid input
    4: if its true the function divides the elements in the vector by the function twonorm defined earlier.
    5: The function then returns the results
    """
    result_normalized=[]
    for i in range(len(vector)):
        inputstatus = True
    for i in range(len(vector)):
        if (type(vector[i]) != int and type(vector[i]) != float and type(vector[i]) != complex):
            inputstatus = False
            print("Invalid Input")
        if inputstatus == True:
            for i in range(len(vector)):
                normalization = vector[i]/twonorm(vector)
                result_normalized.append(normalization)
        return result_normalized
    

def QR(A):
    """
    The function AR(A) does the following
    1: a variable m is set to the len of A from the first index
    2: a variable n is set for the entire lenth of A
    3: a variable v is set to A
    4: a variable R is set that multiplies the elements of n by zero
    5: a varia Q is set that multiplies the elements of m by zero.
       that creates a zero matrix
    6: A for loop is implemented that does the following
        1: the twonorm defined earlier is calculated throughout A
        2: the normalized vector is computed using the normalized function defined earlier.
    7: A for loop is implemented.
       1: The dot product is aquired
       2: the vectors are multiplied by a scalar.
       3: The vectors are subtracted from each other.
    8 we return the results. 
    """
    m = len(A[0])
    n= len(A)
    v = A
    R = [[0]*n for i in range(n)]
    Q = [[0]*m for i in range(n)]
    for i in range(n):
        R[i][i]= twonorm(v[i])
        Q[i] = normalized(v[i])
        for j in range(i+1, n):
            R[j][i] = dot(Q[i],v[j])
            temp = scalarvecmulti(R[j][i],Q[i])
            v[j] = vecsubtract(v[j],temp)
    return [Q,R]
"""
A is a representation of a matrix
the print function prints the results from matrix A 
"""
A = [[1,0,1],
     [2,1,0],
     [1,1,1]]

print(QR(A))      




    
    




































    
        
    
    
    

    
    
    
    
    



    

    
    












        

    

    

    
                                      
                                     
            
            
            
        
        

        
        
                
                   
               



    
    
    
