print('welcome to Windows, Please create a username and password')
print('USERNAME:')
createun=input()
print('PASSWORD')
createps=input()
print('Thanks for signing up please login to continue')
print('USERNAME:')
loginun=input()
if createun==loginun:
    print('PASSWORD:')
    loginps=input()
    if createps==loginps:
        print('Login Successfull!')
    else:
        print('Password Incorrect')
else:
    print('Login Failed')