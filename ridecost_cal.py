travelling_km=float(input("ENTER travelling (km):"))
vehicle_fuel_avg=float(input("ENTER VEHICLE FUEL AVERAGE:"))
diesel_cost=float(input("ENTER diesel cost:"))

fuel_consumption = (travelling_km /vehicle_fuel_avg)
cost_per_day =(diesel_cost * fuel_consumption)

print(cost_per_day)