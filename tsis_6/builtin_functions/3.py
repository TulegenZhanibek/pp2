def polindrom(text):
    
    if(text == text[::-1]):
        return True
    else :
        return False
    
text = input()
print(polindrom(text))