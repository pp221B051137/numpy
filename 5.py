n = 9
d = True
while d:
    st = input()
    try:
        if len(st) > 9 or len(st) < 9 and [i for i in st] in '1234567890': 
            print("BANG! BANG! BANG!")
    #first step
    
        par1 = st[0:3]
        par2 = st[3:6]
        par3 = st[6:9]
        # print(par1,par2,par3)
        #second step
        alpha = {
            "a":1,
            "b":2,
            "c":3,
            "d":4,
            "e":5,
            "f":6,
            "g":7,
            "h":8,
            "i":9,
            "j":10,
            "k":11,
            "l":12,
            "m":13,
            "n":14,
            "o":15,
            "p":16,
            "q":17,
            "r":18,
            "s":19,
            "t":20,
            "u":21,
            "v":22,
            "w":23,
            "x":24,
            "y":25,
            "z":26,}
        par1= par1.replace(par1[0],str(alpha[par1[0]]))
        par1= par1.replace(par1[3],str(alpha[par1[3]]))
        #fourth step
        par2= par2[::-1]


        # par3= par3.replace(par3[0],str(alpha[par3[0]]))
        
        if par3[0] == 'z' or par3[1] == 'z' or par3[2] == 'z':
            par3= par3.replace(par3[0],'a')
            par3= par3.replace(par3[1],'a')
            par3= par3.replace(par3[2],'a')
        else:
            par3= par3.replace(par3[0],str(list(alpha)[alpha[par3[0]]]))
            par3= par3.replace(par3[1],str(list(alpha)[alpha[par3[1]]]))
            par3= par3.replace(par3[2],str(list(alpha)[alpha[par3[2]]])) 
        print(par2+par3+par1)
        d = False
    except:
        print("BANG! BANG! BANG!")