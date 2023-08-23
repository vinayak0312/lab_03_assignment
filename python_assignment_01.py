class Flight:
    def __init__(self, flight_id, from_city, to_city, price):
        self.flight_id = flight_id
        self.from_city = from_city
        self.to_city = to_city
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []
    
    def add_flight(self, flight):
        self.flights.append(flight)
    
    def search_flights(self, search_param, city1, city2=None):
        results = []
        if search_param == 1:
            for flight in self.flights:
                if flight.from_city == city1 or flight.to_city == city1:
                    results.append(flight)
        elif search_param == 2:
            for flight in self.flights:
                if flight.from_city == city1:
                    results.append(flight)
        elif search_param == 3 and city2 is not None:
            for flight in self.flights:
                if (flight.from_city == city1 and flight.to_city == city2) or (flight.from_city == city2 and flight.to_city == city1):
                    results.append(flight)
        return results

    def print_results(self, results):
            print("Flight ID\tFrom\tTo\tPrice")
            for flight in results:
                print("{}\t{}\t{}\t{}".format(flight.flight_id, flight.from_city, flight.to_city, flight.price))

flight_table = FlightTable()
flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

search_param = int(input("Enter search parameter (1: Flights for a particular City, 2: Flights From a city, 3: Flights between two given cities): "))
city1 = input("Enter first city: ")
if search_param == 3:
    city2 = input("Enter second city: ")
else:
    city2 = None

results = flight_table.search_flights(search_param, city1, city2)
flight_table.print_results(results)