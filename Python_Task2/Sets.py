# Declaration of 3 sets
Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
WorkingDays = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
Dates = {21, 22, 17}

# print the elements in set days
print('Days:', Days)
print('Working Days:', WorkingDays)
print("Dates:", Dates)

# adding element in the set
Days.add("Sunday")
print("Days:", Days)

# remove the specified element from set
Days.discard("Wednesday")
print("Days:", Days)

# union of set working days and dates
print("union of set working days and dates", WorkingDays.union(Dates))

# intersection of set days and working days
print("intersection of set working days and days", WorkingDays.intersection(Dates))

# checking set days and dates are disjoint or not
print("Is set days and dates are disjoint:", Days.isdisjoint(Dates))

# difference between days and working days
print("difference between days and working days:", Days.difference(WorkingDays))
