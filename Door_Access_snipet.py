open = '\nACCESS GRANTED'
dont_open = '\nACCESS DENIED'
code = '142857'

def access_granted():
    if passcode == code:
        return(f"{open}\nWelcome Home!")
    

def access_denied():
    if passcode != code:
        return(f"Invalid Entry!\n{dont_open}")
    

def granted_or_denied():
   
    if code == passcode:
        return access_granted()
    else: 
        return access_denied()


print("Notice!!!\nThis Door is Under 24/7 CCTV Suveilance!!!\n")
passcode = input("ENTER A PASS PHRASE\n: ")

access = granted_or_denied()
print(access)