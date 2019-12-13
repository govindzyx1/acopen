from bankFun import *
yes="Y"
while yes=="Y":
    m=showOption()
    if m==1:
        deposite()
    elif m==2:
        withdraw()
    elif m==3:
        checkBal()
    elif m==4:
        show()
    else:
        openAc()
