import random

for i in range(1,13):
    for j in range(i+1,13):
        input_name = "class"+str(i)+"_"+str(j)+".txt"
        ff = open(input_name,"r")
        data = ff.read().split("\n")
        random.shuffle(data)

        train_data = data[:9000]
        test_data = data[9000:]

        train_name = "class"+str(i)+"_"+str(j)+"_train.txt"
        test_name = "class"+str(i)+"_"+str(j)+"_test.txt"
        train = open(train_name,"w")
        test = open(test_name,"w")

        for it in train_data:
            print(it,file=train)
        for it in test_data:
            print(it,file=test)

        ff.close()
        train.close()
        test.close()


