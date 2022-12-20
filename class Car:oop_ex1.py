class Car:
    
    color = "black"
    
    def __init__(self, brand, year) -> None:
        #pass
        self.brand = brand
        self.year = year
    
    def show_brand(self):
        return self.brand
        
    def show_year(self):
        return self.year
        
c1 = Car(brand="ford", year="2012")

brand = c1.show_brand()
year = c1.show_year()
color = c1.color

print(brand)
print(year)
print(color)


    