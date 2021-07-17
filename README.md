# tip-calculator-start
Tip-Calculator
You are out with your friends at a restaurant. Had an amazing dinner. Now it is time to bring out your debit/credit cards to pay for the sumptious meal. You want to split 
the total but it is too late and you don't want to use your head to do the math. Just to help in such a situation, it is great to have an application that does the Math for you.
This project is a tip-calculator and it will calculate how much each person has to pay including the tip. So there you go!

My main TakeAway:
1. How to round numbers in Python?

final_amount = round(amount,2)
This one however can fall flat if the amount is 7.50 as it might output simply 7.5. 

2. In such cases, we can use the format of .2f that helps display 2 digits after the decimal point and it will not discriminate against 0's. 7.50 will be the output. 
final_amount = "{:.2f}".format(amount)
