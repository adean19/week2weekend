class Parking_garage():

    # The entire code was written by both Nick and Renat; we switched up driving and navigating
    # throughout our Friday coding session.

    def __init__(self,parkingSpaces):
        self.parkingSpaces = parkingSpaces
        self.tickets = parkingSpaces
        self.currentTicket = 1
        self.paidTickets = 0
        self.ticketPrice = 15
        self.ticketStatus = dict()
    
    def print_info(self):
        print(f"{self} parking garage has {self.parkingSpaces} space and {self.tickets} tickets.")

    def takeTicket(self):
        self.parkingSpaces -= 1
        self.tickets -= 1
        print(f"Your ticket number is: {self.currentTicket}. Please remember your ticket number!")
        self.ticketStatus[self.currentTicket] = False
        self.currentTicket += 1

    def payForParking(self):
        while True:
            ticketNumber = input('Please insert your ticket number: ')
            if ticketNumber.isdigit() == True and int(ticketNumber) in self.ticketStatus:
                self.ticketStatus[int(ticketNumber)] = True
                self.paidTickets += 1
                print("Thank you for your payment. You have 15 minutes to exit.")
                break
            elif ticketNumber.isdigit() == True and int(ticketNumber) not in self.ticketStatus:
                print("We can't locate that ticket in our database. Please try again.")
            else:
                print("That is not a valid response. Please provide your ticket number as a numeral.")
    
    def leaveGarage(self):
        while True:
            ticketNumber = input("You are trying to leave the garage. Please input your ticket number: ")
            if ticketNumber.isdigit() == True and int(ticketNumber) in self.ticketStatus and self.ticketStatus[int(ticketNumber)] == True:
                print("Thank You! Have a nice day.")
                self.parkingSpaces += 1
                self.tickets +=1
                del self.ticketStatus[int(ticketNumber)]
                break
            
            elif ticketNumber.isdigit() == True and int(ticketNumber) in self.ticketStatus:
                print("Your ticket has not been paid. Please pay your ticket.")
                while True:
                    pay_ticket = input("Would you like to pay for your ticket? (Yes/No): ")
                    if pay_ticket.lower() == "yes" or pay_ticket.lower() == "y":
                        self.paidTickets += 1
                        print("Thank you for your payment. You have 15 minutes to exit.")
                        return
                    elif pay_ticket.lower() == "no" or pay_ticket.lower() == "n":
                        print("You will need to pay for your ticket before you can leave the garage.")
                    else:
                        print("That is not a valid response. Please provide your ticket number as a numeral.")

            elif ticketNumber.isdigit() == True and int(ticketNumber) not in self.ticketStatus:
                print("We can't locate that ticket in our database. Please try again.")
            
            else:
                print("That is not a valid response. Please provide your ticket number as a numeral.")

    def main(self):
        print(f"Welcome to {self} parking garage!")
        while True:
            enter = input("Would you like to enter? (Yes/No): ")

            if enter.lower() == "yes" or enter.lower() == "y":
                self.takeTicket()
                payleave = input("What would you like to do? (Pay/Leave): ")

                while True:
                    if payleave.lower() == "pay" or payleave.lower() == "p":
                        self.payForParking()
                        self.leaveGarage()
                        break
                    elif payleave.lower() == "leave" or payleave.lower() == "l":
                        self.leaveGarage()
                        break
                    else:
                        print("That does not seem to be a valid response. Please indicate if you'd like to pay for your parking ticket or leave the garage.")
                
            elif enter.lower() == "no" or enter.lower() == "n":
                print(f"Thank you for considering the {self} parking garage. Have a wonderful day!")
                break
            
            else:
                print("That does not seem to be a valid response. Please indicate with a 'Yes' or a 'No' if you'd like to enter the garage.")
    
    def admin(self):
        print(f"Welcome to the admin page of the {self} parking garage.")
        print(f"Here are the garage metrics for today:\n\tNumber of tickets issued: {self.currentTicket - 1}\n\tNumber of tickets paid: {self.paidTickets}\n\tTotal income: ${(self.paidTickets*self.ticketPrice)}")

ChicagoParkingGarage = Parking_garage(200)
ChicagoParkingGarage.main()
ChicagoParkingGarage.admin()