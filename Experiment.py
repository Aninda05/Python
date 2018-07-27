print('Please create a username and password')
print('USERNAME:')
createun=input()
print('PASSWORD')
createps=input()
f=open('Test.txt','w+')
f.write(createun)
f.write(createps)
f.close()
print('Thanks for signing up please login to continue')
print('USERNAME:')
loginun=input()
f1=open('Test.txt','r')
check1=f1.readlines()
print(check1)
if check1==loginun:
    print('PASSWORD:')
    loginps=input()
    if createps==loginps:
        print('Login Successfull!')
    else:
        print('Password Incorrect')
else:
    print('Login Failed')