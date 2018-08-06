from textblob import TextBlob
text=input("Enter your doubt: ")
check=TextBlob(text)
print(check.correct())