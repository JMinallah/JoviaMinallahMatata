total_bill = float(input("What is the total bill? "))

# validating total bill value to avoid negative calculations and values
if (total_bill >= 0):
    
    number_of_people = int(input("How many people to split the bill? "))
    #validating number of people, ensuring it is greater than 0   
    if(number_of_people > 0):

     #validating the tip value to avoid negative values and displaying custom messages for each scenario       
        tip_percentage = int(input("What percentage tip would you like to give? 10, 15, or 20,...? "))

        if(tip_percentage <= 0):
            
            if(tip_percentage == 0):
                print("OOps, no tip? That's okay, we all have those days! Just remember to tip your server next time! :)")
                tip_amount = 0
                total_bill_with_tip = total_bill + tip_amount
                amount_per_person = total_bill_with_tip / number_of_people
                final_amount = round(amount_per_person, 2)
                
                print(f"Initial Bill: ${total_bill}")
                print(f"Tip percentage: ${tip_percentage}")
                print(f"Tip: ${tip_amount}")
                print(f"Total bill with tip: ${total_bill_with_tip}")
                print(f"Each person pays: ${final_amount}")
            else:
                print(f"Tip percentage cannot be negative. You entered {tip_percentage}, therefore setting it to 0. Otherwise you can repeat the process.")
                tip_percentage = 0
                tip_amount = total_bill * (tip_percentage / 100)
                total_bill_with_tip = total_bill + tip_amount
                amount_per_person = total_bill_with_tip / number_of_people
                final_amount = round(amount_per_person, 2)
                
                print(f"Initial Bill: ${total_bill}")
                print(f"Tip percentage: ${tip_percentage}")
                print(f"Tip: ${tip_amount}")
                print(f"Total bill with tip: ${total_bill_with_tip}")
                print(f"Each person pays: ${final_amount}")
        else:
            tip_amount = total_bill * (tip_percentage / 100)
            total_bill_with_tip = total_bill + tip_amount
            amount_per_person = total_bill_with_tip / number_of_people
            final_amount = round(amount_per_person, 2)
            
            print(f"Initial Bill: ${total_bill}")
            print(f"Tip percentage: {tip_percentage}%")
            print(f"Tip: ${tip_amount}")
            print(f"Total bill with tip: ${total_bill_with_tip}")
            print(f"Each person pays: ${final_amount}")
        
    else:
        print("The number of people cannot be less than 1. Please repeat the process with valid values!")
else:
    print(f"Total bill cannot be less than $0. Recheck and enter the right value!")       

# If the total bill is $0, it means the meal was on the house. In that case, we can skip the tip calculation and just print a message.    
if (total_bill_with_tip == 0):
    print(f"$0? The meal was on the house ):")
    print(f"Hope you enjoyed!")
else:
    print(f"Hope you enjoyed!")
        