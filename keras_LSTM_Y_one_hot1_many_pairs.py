import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from golden_readin_1y import *
from keras.preprocessing import sequence
from keras.preprocessing.text import one_hot


output = open("testing_accuracies.txt","w")
class_number = 12

for i in range(1,class_number+1):
    for j in range(i+1,class_number+1):
        
        X_train, Y_train, X_test, Y_test = readin_data(i,j)
        Y_train = np.reshape(Y_train,(1,Y_train.shape[0]))
        Y_test = np.reshape(Y_test,(1,Y_test.shape[0]))

        cls = j+1
        Y_train=np.int_(Y_train)
        Y_test=np.int_(Y_test)

        Y_train_new = convert_to_one_hot(Y_train, cls)
        Y_train_new=np.reshape(Y_train_new.T,(X_train.shape[0],1,cls))

        Y_test_new = convert_to_one_hot(Y_test, cls)
        Y_test_new=np.reshape(Y_test_new.T,(X_test.shape[0],1,cls))

        model = Sequential()
        model.add(LSTM(50,input_shape=(1,X_train.shape[2]),return_sequences=True))#(100,26)=(X.shape[1],X.shape[2])
        model.add(Dense(cls))
        #model.compile(optimizer='adam', loss='binary_crossentropy')
        model.compile(optimizer='adam', loss='mean_squared_error')
        print(model.summary())
        model.fit(X_train, Y_train_new, epochs=5, verbose=2)

        train_pred = model.predict(X_train)
        test_pred = model.predict(X_test)

        Y_train_new=np.reshape(Y_train_new,(Y_train_new.shape[0],cls))
        Y_test_new=np.reshape(Y_test_new,(Y_test_new.shape[0],cls))

        train_pred = np.reshape(train_pred,(Y_train_new.shape[0],cls))
        train_pred_2=np.zeros_like(train_pred)
        train_pred_2[np.arange(len(train_pred_2)),train_pred.argmax(1)]=1
        train_pred=train_pred_2

        test_pred = np.reshape(test_pred,(Y_test_new.shape[0],cls))
        test_pred_2=np.zeros_like(test_pred)
        test_pred_2[np.arange(len(test_pred_2)),test_pred.argmax(1)]=1
        test_pred=test_pred_2


        cor =0;
        count = 0;
        for k in range(train_pred.shape[0]):
            count+=1;
            if np.all(train_pred[k]==Y_train_new[k]):
                cor+=1;
        print("class"+str(i)+" and "+str(j)+":train accuracy: "+str(cor/count),file=output);
        print("class"+str(i)+" and "+str(j)+":train accuracy: "+str(cor/count));
        #print("train accuracy: "+str(cor/count))

        cor =0;
        count = 0;
        for k in range(test_pred.shape[0]):
            count+=1;
            if np.all(test_pred[k]==Y_test_new[k]):
                cor+=1;
        print("class"+str(i)+" and "+str(j)+":test accuracy: "+str(cor/count),file=output);
        print("class"+str(i)+" and "+str(j)+":test accuracy: "+str(cor/count));
        #print("test accuracy: "+str(cor/count))

output.close()

