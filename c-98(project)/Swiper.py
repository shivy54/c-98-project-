
file1 = input("File 1 ")
file2 = input("File 2 ")

def swipeFile (file1,file2) :
    
    with open(file1, 'r') as data1:
        data_a = data1.read()

    with open(file2, 'r') as data2:
        data_b = data2.read()

    with open(file1,'w') as data1:
        data1.write(data_b)

    with open(file2,'w') as data2:
        data2.write(data_a)
    print("")
    print("Files swapped :)")

swipeFile(file1,file2)