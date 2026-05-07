print("NPV AND IRR CALCULATOR")

initial = float(input("enter your initial investment: "))
rate = float(input("enter your rate(%): "))/100
n = int(input("no of years: " ))

cashflows=[] #list to store cash flows
for i in range(n):
    cf = float(input("Cash flow year {}: ".format(i+1)))
    cashflows.append(cf) # add cashflows into list (store npv at each year)

npv=-initial
for j in range (len(cashflows)):
    npv+=cashflows[j]/((1+rate)**(j+1))

print("Your NPV is: ",round(npv,2))

low = 0 #IRR by using binary search
high = 1

for k in range(100):
    mid = (low + high) / 2
    temp = -initial

    for l in range(len(cashflows)):
        temp += cashflows[l] / (1 + mid) ** (l + 1)

    if temp > 0:
        low = mid
    else:
        high = mid

irr = mid * 100
print("IRR =", round(irr, 2), "%")

# Decision 
if npv > 0 and irr > rate * 100:
    print(" Project is acceptable")
else:
    print(" Project is not acceptable")
#Risks
if irr > 25:
    print("Risk Level: High Return (High Risk)")
elif irr > 15:
    print("Risk Level: Medium")
else:
    print("Risk Level: Low")
#graph   
import matplotlib.pyplot as plt

years_list = list(range(1, n+1))
plt.plot(years_list, cashflows)
plt.title("Cash Flow Trend")
plt.xlabel("Years")
plt.ylabel("Cash Flow")
plt.show()