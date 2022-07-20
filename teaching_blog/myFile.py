sales_person_name = input("Enter the names of your sales person?")

dollar_ammount = float( input("Enter the sales of" + " "+ sales_person_name))
while dollar_ammount < 0:
    print("You Enter the wrong ammount")
    dollar_ammount =float(input("Enter the ammount again !"))


print("Salesman                       " + str(sales_person_name))
print("Sales                          "+ str( dollar_ammount))
gross_income = 0
if(dollar_ammount < 30,000):
    gross_income = 300 + 9/100* dollar_ammount
if (dollar_ammount > 30,000 and dollar_ammount < 4000):
    gross_income = 325 + 12/100 * dollar_ammount
if (dollar_ammount > 40,000):
    gross_income = 350 + 14/100*dollar_ammount        
taxes = 0
if(gross_income < 4000):
    taxes = 15/100 * gross_income
if (gross_income > 4000):
    taxes = 20/100 * gross_income        
print ("Gross Income                  "+ str(gross_income))
print("Taxes                          "+ str(taxes))
print("Net Income                          "+ str(gross_income - taxes))
