class Flight():
    def __init__(self,max):
        self.max = max
        self.passenger = []

    def add_passenger(self,name):
        if not self.open_seat():
            return False
        self.passenger.append(name)
        return True


    def open_seat(self):
        return self.max - len(self.passenger)

UA888 = Flight(2)
people = ["Amy","Oscar","Peter"]
for i in people:
    success = UA888.add_passenger(i)
    if success:
        print(f"We added {i} to the flight")
    else:
        print(f"There's no longer seat open for {i}")