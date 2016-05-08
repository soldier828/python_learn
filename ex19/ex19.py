def cheese_and_crackers(cheese_cout, boxs_of_crackers):
	print "You have %d cheeses!" % cheese_cout
	print "You have %d boxs of crackers!" % boxs_of_crackers
	print "Man that's enough for party!"
	print "Get a blanket. \n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Or, we can use variables from out script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 10000)

print "And we can just input"
a = int(raw_input("chees>: "))
b = int(raw_input("crackers>: "))
cheese_and_crackers(a, b)

