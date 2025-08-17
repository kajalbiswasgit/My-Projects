"""January Orders:
{"OD101", "OD102", "OD103", "OD105", "OD108", "OD110"}
February Orders:
{"OD103", "OD104", "OD105", "OD106", "OD108", "OD111"}

Find customers who ordered in both months → (intersection)
Find customers who ordered only in January → (difference)
Find customers who ordered only in February → (difference)
Find all unique orders from both months → (union)
Find orders that are not common between both months"""
January_Orders= {"OD101", "OD102", "OD103", "OD105", "OD108", "OD110"}
February_Orders= {"OD103", "OD104", "OD105", "OD106", "OD108", "OD111"}
unique_orders=January_Orders.union(February_Orders)
cust_for_both_months=January_Orders.intersection(February_Orders)
cust_for_jan=January_Orders.difference(February_Orders)
cust_for_feb=February_Orders.difference(January_Orders)
uncommon_orders=January_Orders.symmetric_difference(February_Orders)
print ("unique_orders:",unique_orders)
print ("both month cust:",cust_for_both_months)
print ("jan cust:",cust_for_jan)
print ("feb cust:",cust_for_feb)
print ("uncommon orders:",uncommon_orders)