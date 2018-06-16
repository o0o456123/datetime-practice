from datetime import datetime
from datetime import timedelta



def testfu(x,y,z):

    zowoday = datetime(year=x,month=y,day=z)

    now = datetime.today()
    endday= zowoday + timedelta(days = 365)
    talwoday = (endday-now).days
    if talwoday<=0:
        print("退伍了")
    else:
        print ("剩下",talwoday,"天")


testfu(int(input('西元年ex2018')),int(input('幾月ex06')),int(input('幾日ex08')))