from tabulate import tabulate

all_data = [["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"],
            [" "," "," "," "," "," ","O"," "," "," " ," " ," " ," " ,"O" ," " ," " ," " ," " ," " ," " ],
            [" "," "," "," "," "," ","O"," "," "," " ," " ," " ," " ,"O" ," " ," " ," " ," " ," " ," " ]
            ]

table1 = tabulate(all_data)
table2 = tabulate(all_data,headers='firstrow')

print(tabulate(all_data,headers='firstrow',tablefmt='fancy_grid'))