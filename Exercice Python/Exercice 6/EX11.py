tab1=[4,8,7,12]
tab2=[3,6]
nombredetour=len(tab1)
tabcopie2=tab2[0]
tabcopie1=tab2[1]
tab3=[tabcopie1]*nombredetour
tab4=[tabcopie2]*nombredetour
tab7=[]


for i in range(nombredetour):
     tab5=(tab1[i]*tab3[i])
     tab6=(tab1[i]*tab4[i])
for i in range(nombredetour):
     tab7=tab5+tab6*nombredetour



    
print(tab7)