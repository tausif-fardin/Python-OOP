def addnumber(a, b, c=1):
    return a + b + c


print(addnumber(8, 9))
print(addnumber(8, 9, 10))


class Bangladesh:
    def capital_city(self):
        print("Dhaka is the capital city of Bangladesh.")

    def language(self):
        print("Language is Bangla.")


class UK:
    def capital_city(self):
        print("London is the capital city of UK.")

    def language(self):
        print("Language is English.")


var1 = Bangladesh()
var1.capital_city()
var1.language()

var2 = UK()
var2.capital_city()
var2.language()


for Country in (var1, var2):
    Country.capital_city()
    Country.language()
