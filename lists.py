countries = ['Ghana', "United States", "Canada", "Bahamas", "Ukraine", "Tunisia"]

countries.sort()
counted = countries.count("United States")
append_new = countries.append("Nigeria")
countries.remove("Ghana")
popped = countries.pop(-2)
countries.clear()
print(countries, counted, append_new, popped)
