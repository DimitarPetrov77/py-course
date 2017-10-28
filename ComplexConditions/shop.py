product = input().lower()
town = input().lower()
quantity = float(input())
price = 0

if town == 'Sofia':
    if product == "coffee":
        price = 0.50 * quantity
    elif product == "water":
        price == 0.80 *quantity
    elif product == "beer":
        price = 1.20 * quantity
    elif product == "sweets":
        price = 1.45 * quantity
    elif product == "peanuts":
        price = 1.60 * quantity


#print(2%f. % price)