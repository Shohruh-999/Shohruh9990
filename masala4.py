def func(cars):
    sort = sorted(cars, key=lambda car: car["year"])
    return sort

cars = [
    { "model": "RDX", "year": 2009 },
    { "model": "LS", "year": 2000 },
    { "model": "GLK-Class", "year": 2010 },
    { "model": "Express 1500", "year": 2005 },
    { "model": "LR2", "year": 2008 },
    { "model": "XF", "year": 2012 },
    { "model": "MR2", "year": 2005 },
    { "model": "Malibu", "year": 2007 },
    { "model": "M-Class", "year": 2010 },
    { "model": "Routan", "year": 2011 }
]

n = func(cars)

for i in n:
    print(i)
