while True :
    text = input()
    if not text:
        break
    lower = sum(i.islower() for i in text)
    upper = sum(i.isupper() for i in text)
    num = sum(i.isdigit() for i in text)
    blank = sum(i.isspace() for i in text)
    print(lower,upper,num,blank)
