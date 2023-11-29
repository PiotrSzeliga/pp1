countries = [
    {"name":"Poland", "population":38000000},
    {"name":"Germany", "population":83000000},
    {"name":"UK", "population":67000000},
    {"name":"France", "population":64000000},
    {"name":"Austria", "population":9000000},
    {"name":"Lichtenstein", "population":36000},
]
counter = 0 
while counter < len(countries):
    print(f"{countries[counter]['name']} {countries[counter]['population']}")
    counter += 1
