grade=[55, 70, 65, 40, 90, 85, 50, 77]
filters= [i for i in grade if i > 60]
def percent(a):
    return round(a*(105/100),2)
applies=[percent(i) for i in filters]
print("Grades after filtering and applying bonus: ", applies)
