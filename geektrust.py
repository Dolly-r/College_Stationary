from sys import argv

def main():
    # Sample code to read inputs from the file
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    sum=0
    clothing=0
    stationary=0
    discount=0
    count=0
    for line in lines:
        item=line
        if(item=="PRINT_BILL"):
            if(sum>3000):
                sum=sum-(sum*0.05)
                discount=discount+(sum*0.05)
            print("TOTAL_DISCOUNT ","%.2f" % discount)
            sum=sum+(sum*0.1)
            print("TOTAL_AMOUNT_TO_PAY ", "%.2f" % sum)
            count=0
            break

        item=list(item.split(" "))
        # print(item)
        count=int(item[2])
        if(item[1]=="TSHIRT"):
            if(count>2):
                print("ERROR_QUANTITY_EXCEEDED")
            else:
                sum=sum+1000*count
                sum=sum-100*count
                discount=discount+100*count
                clothing=clothing+count
                print("ITEM_ADDED")
        elif(item[1]=="JACKET"):
            if(count>2):
                print("ERROR_QUANTITY_EXCEEDED")
            else:
                sum=sum+2000*count
                sum=sum-100*count
                discount=discount+100*count
                clothing=clothing+count
                print("ITEM_ADDED")
        elif(item[1]=="CAP"):
            if(count>2):
                print("ERROR_QUANTITY_EXCEEDED")
            else:
                sum=sum+500*count
                if(sum>1000):
                    sum=sum-100*count
                    discount=discount+100*count
                clothing=clothing+count
                print("ITEM_ADDED")
        elif(item[1]=="PENS"):
            if(count>3):
                print("ERROR_QUANTITY_EXCEEDED")
            else:
                sum=sum+300*count
                if(sum>1000):
                    sum=sum-30*count
                    discount=discount+30*count
                stationary=stationary+count
                print("ITEM_ADDED")
        elif(item[1]=="NOTEBOOK"):
            if(count>3):
                print("ERROR_QUANTITY_EXCEEDED")
            else:
                sum=sum+200*count
                if(sum>1000):
                    sum=sum-40*count
                    discount=discount+40*count
                stationary=stationary+count
                print("ITEM_ADDED")
        elif(item[1]=="MARKERS"):
            if(count>3):
                print("ERROR_QUANTITY_EXCEEDED")
            else:
                sum=sum+500*count
                if(sum>1000):
                    sum=sum-25*count
                    discount+25*count
                stationary=stationary+count
            print("ITEM_ADDED")
    
if __name__ == "__main__":
    main()