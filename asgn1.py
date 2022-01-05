#-------HELPERS---------
def read_file(n):
    rec_lst=[]
    with open(n, 'a+') as f:
        f.seek(0)
        for record in f:
            recs = eval(record.strip())
            rec_lst+= [recs]
        return rec_lst
def save_changes(rec_lst, filename):
    with open(filename, 'w+') as f:
        for record in rec_lst:
            f.write(str(record)+ '\n')
def display_stock(n):
    stock=read_file(n)
    for i in range(len(stock)):
        print (stock[i][0],':', stock[i][1])
    return

#-------FOOD-----
def input_stock():
         total_stock=read_file('food.txt')
         item= input('Press \'0\' to make changes to Samosa stock or \'1\' for Roll stock:')
         value= int(input('Enter new value of stock'))
         if item== '0':
              total_stock[0][1]=value
         if item=='1':
              total_stock[1][1]= value
         save_changes(total_stock,'food.txt')
         print('NEW STOCK DETAILS:',display_stock('food.txt'))
         return

def order_process():
    total_stock= read_file('food.txt')
    print(total_stock)
    amount= input('Enter number of samosas and rolls you want to buy respectively:')
    amount=amount.split()
    amount_int=[int(i) for i in amount]

    total_stock[0][1]-=amount_int[0]
    total_stock[1][1]-=amount_int[1]
    save_changes(total_stock, 'food.txt')
    return amount_int

def billing_process(amount_int):
    price_of_samosas= 15
    price_of_rolls= 25
    total_price= (amount_int[0]*price_of_samosas)+(amount_int[1]*price_of_rolls)
    return total_price
while True:
     print ('WELCOME TO MY BAKESHOP:\nMENU:\n1. ORDER PROCESS\n2. STOCK UPDATE\n3. STOCK DETAILS\nPRESS \'e\' TO EXIT')
     option=input('PLEASE SELECT AN OPTION:')
     if option=='e':
         break
     elif option =='1':
         order_details=order_process()
         x=input('would you like to proceed to checkout:')
         print ('Your total amount is:',billing_process(order_details))
     elif option== '2':
         input_stock()
     elif option=='3':
         print ('STOCK DETAILS:', '\n', display_stock('food.txt'))
