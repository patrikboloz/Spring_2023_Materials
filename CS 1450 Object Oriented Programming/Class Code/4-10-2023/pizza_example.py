def orderPizza(size, style='regular', topping=None):
	# Do some calculations based on the size and style
	#Check if a topping was specified

	PRICE_OF_TOPPING = 1.50 #price of any topping

	if size == 'small':
		price = 10.00
	elif size == 'medium':
		price = 14.00
	else: #large
		price = 18.00

	if style == 'deepdish':
		price = price + 2.00 #charge extra for deepdish

	line = 'You have ordered a ' + size + ' ' + style + ' pizza with '
	if topping is None:
		print(line + 'no topping')
	else:
		print(line + topping)
		price = price + PRICE_OF_TOPPING

	print('The price is $', price)
	print()


orderPizza('large')

orderPizza('large', style = 'deepdish')

orderPizza('small', style = 'deepdish', topping = 'pepperoni')

orderPizza('small', topping = 'pepperoni', style = 'deepdish')

