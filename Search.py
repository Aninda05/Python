def find(name):
    count=0
    for root, dirs, files in os.walk('E:\\'):
        if name in files:
            print(root,name)
            count+=1
    print("We found "+ count+" results")
    print("Finish")
    input()

try:
    s=input("name: ")
    find(s)
except:
    print("Error")
