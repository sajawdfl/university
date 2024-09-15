def national_card(char):
    n = []
    k=10
    
    if all(c == char[0] for c in char):
        return False
        
    for i in char:
        n.append(int(i) * k)
        k-=1
    mod = sum(n)%11
    if mod ==1:
        checkdigit=mod
    elif mod > 1:
        checkdigit=11 - mod
        
    return char+""+str(checkdigit)  