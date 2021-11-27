import numpy as np

arr0 = np.zeros((5,5))

#print(f'the original array is \n {arr0}')
def checkPlayerMove():
    # user input for the coordinate to be placed at
    quit = False
    # Checking the user input for a valid input 
    while not quit:
            tempInd = input("enter the index to place the peice at: ").split(" ")
            try:
                index_X = int(tempInd[0])
                index_Y = int(tempInd[1])
                if(index_X > arr0.shape[0] or index_Y > arr0.shape[1]):
                    temp = 1
                    raise Exception
                quit= True
            except:
                if(temp != 1):
                    print("Please enter a number value")
                else:
                    print(f'Please enter numbers between {arr0.shape[0]} and {arr0.shape[1]}')
                    
                    
# To take a transpose of the array across the secondary diagonal
def SecTrans(arr):
    tempMat = np.matrix(arr0)
    tempMat[0:,0:] = tempMat[0:,0:][::-1].transpose()[::-1]
    tempArr = np.array(tempMat)
    return tempArr

# to poulate the matrix with a moves 
def Pop0(arr0,index_X,index_Y):
    for i in range(arr0.shape[0]):
      if(i == index_X and arr0[index_X][i] != 0):
        arr0[index_X][i] += arr0[index_X][i]
      elif(i == index_X and arr0[index_X][i] == 0):
        arr0[index_X][i] = 2
      else:
        arr0[index_X][i] = 2
    for j in range(arr0.shape[1]):
      if(j == index_Y and arr0[j][index_Y] != 0):
        arr0[j][index_Y] += arr0[j][index_Y]
      elif(j == index_Y and arr0[j][index_Y] == 0):
        arr0[j][index_Y] = 2
      else:
        arr0[j][index_Y] = 2 
    print(f'The new array is \n {arr0}')
    #return arr0

# Still Working on this function sooner than later threading will also be introduced
# To make things run a bit faster 
# But for now ignore this function completely
def Pop1(arr0,index_X,index_Y):
    pass



# driver Code
player = 1
index_X,index_Y = 1,1
arr0[index_X,index_Y] = player
Pop0(arr0,index_X,index_Y)
index_X,index_Y = 2,2
arr0[index_X,index_Y] = player
Pop0(arr0,index_X,index_Y)
