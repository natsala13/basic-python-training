stam = [1,"hello",3.14,True,"bye"]
stam1 = stam[::2]
for element in stam1:
    print(element)
stam_new = stam + stam1
for element in stam_new:
    print(element)
