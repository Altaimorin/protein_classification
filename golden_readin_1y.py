import numpy as np

def convert_to_one_hot(Y, C):
    Y = np.eye(C)[Y.reshape(-1)].T
    return Y

def readin_data(i,j):
    X_train = []
    Y_train = []
    f_train = open("new_class"+str(i)+"_"+str(j)+"_train.txt","r")
    lines = f_train.readlines()
    count = 0
    print("start training!")
    for line in lines:
        lst = line.split()[:-1] # list of string
        print(count)
        #lst = [np.fromstring(i,'u1') - ord('0') for i in lst ]
        lst = list(map(float,lst))
        lst = np.array(lst)
        
        X_train.append(lst)
        Y_train.append(np.array(line.split()[-1]))
        count+=1
    X_train = np.array(X_train)
    X_train = np.reshape(X_train,(X_train.shape[0],1,X_train.shape[1]))
    #X_train = X_train.astype(float)
    Y_train = np.array(Y_train)
    #Y_train = Y_train.astype(float)


    print("start testing")
    X_test = []
    Y_test = []
    f_test = open("new_class"+str(i)+"_"+str(j)+"_test.txt","r")
    #lines = f_train.readlines()
    lines = f_test.readlines()
    count = 0
    for line in lines:
        if line.split()[-1].isdigit()==False:
            continue
        lst = line.split()[:-1] # list of string
        print(count)
        #lst = [np.fromstring(i,'u1') - ord('0') for i in lst ]
        lst = list(map(float,lst))
        
        lst = np.array(lst)
        #b_lst = np.array(np.fromstring(lst[:],'u1')-ord('0'))
        #X_test.append(b_lst)
        X_test.append(lst)
        Y_test.append(np.array(line.split()[-1]))
        count+=1
    X_test = np.array(X_test)
    X_test = np.reshape(X_test,(X_test.shape[0],1,X_test.shape[1]))
    #X_test = X_test.astype(float)
    Y_test = np.array(Y_test)
    #Y_test = Y_test.astype(float)


    return X_train, Y_train, X_test, Y_test


