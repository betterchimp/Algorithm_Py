def main():
    A, B= input().split()
    A = int(A)
    B = int(B)
    
    if B > 44 : 
        print("%d %d" % (A, B-45))
    else :
        if A == 0 :
            print(("%d %d" % (23, 60-(45-B))))
        else :
            print(("%d %d" % (A-1, 60-(45-B))))
        
main()