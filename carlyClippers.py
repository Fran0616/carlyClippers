hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
#prices and cuts
for i in prices:
  total_price = total_price + i # sum of the prices goes in the total_price variable
average_price = total_price/len(prices)# average prices
print("Average Haircut Price:", average_price)

new_prices = [x - 5 for x in prices]
print(new_prices)
#Revenue 
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue:",total_revenue )
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(prices)) if prices[i] < 30 ]
print(cuts_under_30)
