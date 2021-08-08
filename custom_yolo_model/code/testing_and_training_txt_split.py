import os

direction= os.getcwd()

print(direction)

file_test=open("testing.txt","a+",encoding="utf-8")

file_train=open("training.txt","a+",encoding="utf-8")



count=1



while (count<=320):



    file_train.write(r"cotton_data\cotton_img\{}.frame.jpg".format(count)+"\n")

    count+=1

    print(count)

    if count==320:

        while (count<=399):

             file_test.write(r"cotton_data\cotton_img\{}.frame.jpg".format(count)+"\n")

             count+=1