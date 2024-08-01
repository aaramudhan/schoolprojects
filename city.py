print("CITY LIST")
cityList=["Tokyo","New Dehli","Chennai","Paris","Hanoi"]
print("#"*60)
# to store the commands, first time, it is empty
uCommand= " "
while uCommand != "x":
    print("use  t  to traverse; a  to append; d to delete element;  p to print;  x to exit ")

    uCommand = input("enter a command: ")
    print("#"*60)

    if uCommand == "t" :
      cityCount= len(cityList)
      for i in range(cityCount):
        print(i,cityList[i])
        print("-"*60)

    if uCommand == "a" :
       aCity = input("enter a city: ")
       cityList.append(aCity)
       print("#"*60)
    if uCommand == "p":
       print(f"City List {cityList}")
       print("#"*60)
    
    if uCommand == "d":
       maxNum= len(cityList)-1
       print(f"index numbers go from 0 to {maxNum}")
       delIndex=int(input("choose number: "))
       
       
       if delIndex <= maxNum:
          del[cityList[delIndex]]
          print("#"*60)
       else:
          print(f"out of bounds error, use numbers 0 to {maxNum}")
          print("#"*60)
       
       

