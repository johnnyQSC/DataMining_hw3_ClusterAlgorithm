import openpyxl,string
f = open(r'C:/Users/ASUS/Desktop/datamining_hw3/automobile.txt','r+')
excel = openpyxl.load_workbook(r'C:/Users/ASUS/Desktop/datamining_hw3/automobile.xlsx')
sheet = excel.worksheets

line=f.readline()
while line:
        list=[]
        list=line.split(sep=',')
        for i in range(0,len(list)):
            list[i]=list[i].strip('\n')
        sheet[0].append(list)
        line=f.readline()
excel.save(r'C:/Users/ASUS/Desktop/datamining_hw3/automobile.xlsx')