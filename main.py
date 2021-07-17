#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the Tip Calculator!")
bill_amount = float(input("how much is the bill? "))
num_people = int(input("how many people? "))
tip_amount = int(input("how much is the tip?(in %) "))
split_bill = (bill_amount/num_people)*((tip_amount/100)+1)
final_amount = round(split_bill,2)
final_amount = "{:.2f}".format(split_bill)
print(f"Each person has to pay {final_amount}")