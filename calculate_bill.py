
'''


         CALCULATE_BILL:
         
         
'''



def calculate_bill():
    bill_amount=int(input("enter the bill"))
    if bill_amount < 500:
        discount = 0.05 * bill_amount
    elif bill_amount < 2500:
        discount = 0.10 * bill_amount
    else:
        discount = 0.20 * bill_amount
        
    discounted_bill = bill_amount - discount
    rounded_discounted_bill = round(discounted_bill, 3)
    return rounded_discounted_bill

a=calculate_bill()
print(a)