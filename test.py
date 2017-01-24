import geocoder

g = geocoder.google(input("Maps search: "))

print("g.housenumber:")
print(g.housenumber)

print("\n g.postal")
print(g.postal)

print("\ng.street")
print(g.street)

print("\ng.street_long")
print(g.street_long)

print("\ng.latlng")
print(g.latlng)

print("\ng.city")
print(g.city)

print("\ng.state")
print(g.state)

print("\ng.state_long")
print(g.state_long)

print("\ng.country")
print(g.country)

print("\ng.country_long")
print(g.country_long)

print(g)