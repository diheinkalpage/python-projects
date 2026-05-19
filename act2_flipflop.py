def palind(r):
    e = len(r) -1
    s = 0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True

r = (8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8)
if(palind(r)):
    print("The tuple is a Flip-Flop")
else:
    print("The tuple is not a Flip Flop")
          
