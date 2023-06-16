class Parking_garage():

    def __init__(self,parkingSpaces):
        self.parkingSpaces = parkingSpaces
        self.tickets = parkingSpaces
        self.currentTicket = 1
        self.ticketStatus = dict()
    
    def print_info(self):
        print(f'{self} parking garage has {self.parkingSpaces} space and {self.tickets} tickets.')

    def takeTicket(self):
        self.parkingSpaces -= 1
        self.tickets -= 1
        print(f"Your ticket number is: {self.currentTicket}")
        self.ticketStatus[self.currentTicket] = False
        self.currentTicket += 1

    def payForParking(self,currentTicket):
        while True:
            ticketNumber = int(input('Please insert your ticket number: '))
            if ticketNumber in self.ticketStatus:
                self.ticketStatus[ticketNumber] = True
                print("Thank you for your payment. You have 15 minuntes to exit")
                
            elif ticketNumber.lower() == "no" or ticketNumber.lower() == "n":
                pass
            else:
                print("That is not a valid response. Please write 'yes' or 'no' to indicate if you'd like to pay for your ticket")

    
    # def payForParking(self):

ChicagoParkingGarage = Parking_garage(200)
ChicagoParkingGarage.print_info()
ChicagoParkingGarage.takeTicket()
ChicagoParkingGarage.print_info()
ChicagoParkingGarage.takeTicket()
print(ChicagoParkingGarage.ticketStatus)