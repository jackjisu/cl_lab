class Restaurant:
    def __init__(self, menu, label):
        self.menu = menu
        self.label = label
    
    def __str__(self):
        return f"label: {self.label} | menu: {self.menu}"
    
    def write(self, new_file):
        with open(new_file, 'a') as f:
            f.write(f"{self.label} {str(self.menu)}\n")
    
restaurants = []
file = "/Users/jackbyun/Documents/cl_lab/restaurants/menu_train.txt"

with open(file, 'r') as f:
    for line in f:
        line_split = line.split(maxsplit=1) # split only at first space
        label = line_split[0]
        menu = line_split[1:]
        doc = Restaurant(menu, label)
        restaurants.append(doc)

#print(restaurants[0])

for restaurant in restaurants:
    restaurant.write('/Users/jackbyun/Documents/cl_lab/restaurants/test_write2.txt')

