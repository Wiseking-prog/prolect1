
# # # #add two number
# # # # num_1 = 1000
# # # # num_2 = 1000

# # # # result = num_1 - num_2



# # # # print(f"if you subtrat 1000 from 1000 it will give you {result}")

# # # # result =num_1 - num_2

# # # # print(result)


# # # # account_balance = 50000

# # # # withdraw = 50000

# # # # balance = account_balance - withdraw

# # # # if balance == 0:
# # # #     print("no money in the bank")

# # # # else:
# # # #     print("you guide")




# # # # age = 40

# # # # if age < 17:
# # # #     print("cannot enter uni")
# # # # elif age <= 30:
# # # #     print ("welcome to the bachelors degree")
# # # # else:
# # # #     print("okay we will move you to the masters degree")
# # # # price = 90000

if price < 65000:
    print("sell order")
else:
    print("buy order")



# # # name = "joseph"
# # # income_1 = 50000
# # # expenses_2 = 8585

# # # balance = income_1 - expenses_2

# # # if balance > (income_1 * 0.5):
# # #     print(f"{name} great job you are saving well")
    

# # # elif balance >= (income_1 * 0.20) and balance <= (income_1 * 0.50):
# # #     print(f"{name} not bad but try to cut some cost")

# # # else:
# # #     print(f"waring:{name} you are spending too much")

# # # name = "david"
# # # income_1 = 50000
# # # expenses_2 = 8585

# # # balance = income_1 - expenses_2

# # # if balance > (income_1 * 0.5):
# # #     print(f"{name} great job you are saving well")
    

# # # elif balance >= (income_1 * 0.20) and balance <= (income_1 * 0.50):
# # #     print(f"{name} not bad but try to cut some cost")

# # # else:
# # #     print(f"waring:{name} you are spending too much")

# # # print(balance)
# # # 


# # # def add_num(num1,num2):
# #     # result = num1 + num2

# #     # return result




# def check_spend(customer_name:str,income:int,expense:int):
#     balance = income - expense

#     if balance > (income * 0.5):
#         return f"{customer_name} great job you are saving well"
    

#     elif balance >= (income * 0.20) and balance <= (income * 0.50):
#         return f"{customer_name} not bad but try to cut some cost"

#     else:
#         return f"waring:{customer_name} you are spending too much"


# get_spend_data1 = check_spend("Joseph",40000,30000)
# get_spend_data2 = check_spend("david",70000,30000)

# print(get_spend_data1)
# print(get_spend_data2)



# def check_blood_pressuer(systolic:int,diastolic:int):

#     if systolic >= 140 or diastolic >= 90:
#         return "see a doctor"

#     else:
#         return "you are ok"


# print(check_blood_pressuer(150, 95))



def can_enter_uni (age:int):
    
    if age <= 15:
        return "you can not enter uni"
    else:
        return "you can enter uni"


# print(can_enter_uni(19))


# def crypto_price (order:int):
#     if order < 5000:
#         return " sell order trigger"
#     else:
#         return "buy order trigger"

# print(crypto_price(4900))



# def check_bp(systolic, diastolic):
#     if systolic >= 140 or diastolic >= 90:
#         return "see a doctor"
#         else:
#             return "you are fine"
# print(check_bp(150, 95))


# def can_enter_uni(age):
#     if age >= 16:
#         return "you can enter uni"
#     else:
#         return "you can not enter uni"

# print(can_enter_uni(18))

# def crypto_price (order):
#     if order < 5000
#        return sell order trigger
#     else:
#         return buy order trigger
# print(crypto_price(4900))

# coins =["btc","eth","sol","bnb"]

# coins.append("bol")

# print(coins)