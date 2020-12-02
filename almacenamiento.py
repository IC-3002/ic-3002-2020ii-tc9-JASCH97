def maximizar(As,D):
    M = []
    Suma = 0
    As = sorted(As,key=lambda archivo:archivo[1])
    #print(As)

    for i in range(len(As)):
        if(Suma + As[i][1] > D):
            return M
        
        if(Suma + As[i][1] == D):
            M = M + [As[i]]
            return M
        
        else:
            Suma = Suma + As[i][1]
            M = M + [As[i]]

        
#print(maximizarAux([("qwe",3),("asd",5),("as",9),("s",8),("c",10),("k",1)],18,[],0))
