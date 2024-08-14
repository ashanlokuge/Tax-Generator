import math

print("tax generator")
monthly_income=int(input("enter your monthly income"))
annual_income= monthly_income*12
print(annual_income)
tax_income=annual_income-1200000
print(tax_income)

remian= math.floor(tax_income/500000)
mod= tax_income%500000
print(remian)
print(mod)
if (remian==0):
    tax_fee= mod*0.06/12
    print(tax_fee)

elif (remian==1):
    tax1=(500000*0.006/12)+(mod*0.12/12)
    print(tax1)

elif(remian==2):
    tax_fee=500000*0.06/12+5000000*0.12/12+mod*0.18/12
    print(tax_fee)

elif(remian==3):
    tax_fee = 500000 * 0.06 / 12 + 5000000 * 0.12 / 12 + 500000 * 0.18 / 12+mod*0.24/12
    print(tax_fee)

elif(remian==4):
    tax_fee = 500000 * 0.06 / 12 + 5000000 * 0.12 / 12 + 500000 * 0.18 / 12+500000*0.24/12+mod*0.3/12
    print(tax_fee)

elif(remian==5):
    tax_fee = 500000 * 0.06 / 12 + 5000000 * 0.12 / 12 + 500000 * 0.18 / 12 + 500000 * 0.24 / 12 + 500000* 0.3 / 12+mod*0.36/12
    print(tax_fee)

else:
    tax_fee = 500000 * 0.06 / 12 + 500000 * 0.12 / 12 + 500000 * 0.18 / 12 + 500000 * 0.24 / 12 + 500000 * 0.3 / 12 + (tax_income-2500000)* 0.36 / 12
    print(tax_fee)

#this is tax generator