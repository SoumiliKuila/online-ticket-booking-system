# Online Ticket Booking System
# Movies data
# Movie is a dictionary with movie id as key and another dictionary as value containing movie name, price, and available seats.
movies = {
    1: {"name": "Avengers: Welcome to The Jungle", "price": 350, "seats": 10},
    2: {"name": "Jungle Cruise", "price": 300, "seats": 8},
    3: {"name": "Spider-Man: No Way Home", "price": 400, "seats": 12},
    4: {"name": "Toy Story 4", "price": 250, "seats": 6},
}


# this is an empty list to store booked tickets. Each ticket is a dictionary containing customer name, phone number, movie name, number of tickets, and total amount.
#whenever a customer successfully books tickets , their booking information is added to this list.
booked_tickets = []


# This function display al the available movies
def display_movies():
    print("\nAvailable Movies:")
    for movie_id, movie in movies.items():# it goes through each movie in the movies dictionary and prints the movie id, name, price, and available seats.
        print(f"{movie_id}. {movie['name']} - Rs.{movie['price']} | Seats left: {movie['seats']}")


def book_ticket():# This is the main booking function
    print("\n=== Book Your Ticket ===")
    customer_name = input("Enter your name: ")#get customer information
    customer_phone = input("Enter your phone number: ")

    display_movies()# this call display movies function
    movie_id = int(input("Select a movie number: "))# the user enter the movie

    if movie_id not in movies:# if the user enter a movie id that is not in the movies dictionary, it will print an error message and return from the function.
        print("Invalid movie selection.")
        return

    selected_movie = movies[movie_id]# it select the movie
    ticket_qty = int(input("Enter number of tickets: "))

    if ticket_qty <= 0:# checking ticket quality
        print("Number of tickets must be greater than 0.")
        return

    if ticket_qty > selected_movie["seats"]:# checking if the requested number of tickets is greater than the available seats for the selected movie. If it is, it will print an error message and return from the function.
        print("Sorry! Not enough seats available.")
        return

    total_bill = ticket_qty * selected_movie["price"]# calculate the total bill by multiplying the number of tickets by the price of the selected movie.

    # display booking summary and ask for confirmation
    print(f"\nMovie: {selected_movie['name']}")
    print(f"Tickets: {ticket_qty}")
    print(f"Total Amount: Rs.{total_bill}")

    confirm = input("Confirm booking? (Y/N): ").strip().lower()# confirm booking

    if confirm == 'y':
        selected_movie["seats"] -= ticket_qty

        # create book records , it contain the customer booking details such as name, phone number, movie name, number of tickets, and total amount. This booking record is then appended to the booked_tickets list.
        booking = {
            "customer_name": customer_name,
            "phone": customer_phone,
            "movie": selected_movie["name"],
            "tickets": ticket_qty,
            "total": total_bill,
        }
        booked_tickets.append(booking)# adds the booking record to a text file named "ticket_booking.txt" in append mode. Each booking is written as a new line in the file, containing the customer's name, phone number, selected movie, number of tickets, and total amount.

        with open("ticket_booking.txt", "a") as file:# this saves the booking parmanently in a text file
            file.write(f"Name: {customer_name}, Phone: {customer_phone}, Movie: {selected_movie['name']}, Tickets: {ticket_qty}, Total: Rs.{total_bill}\n")

        print("\nTicket booked successfully!")
        print("Thank you for booking with us.")
    else:
        print("Booking cancelled.")


def view_bookings():# This function displays the booking history by iterating through the booked_tickets list and printing each booking's details. If there are no bookings, it informs the user that no tickets have been booked yet.
    if not booked_tickets:
        print("No tickets booked yet.")
        return

    print("\n=== Booking History ===")
    for index, ticket in enumerate(booked_tickets, start=1):# loops through all booking
        print(f"{index}. {ticket['customer_name']} | {ticket['movie']} | {ticket['tickets']} ticket(s) | Rs.{ticket['total']}")


def main():#main menu
    while True:
        print("\n==== ONLINE TICKET BOOKING ====")
        print("1. Book Ticket")
        print("2. View Booking History")
        print("3. Exit")

        choice = input("Enter your choice: In 1 2 And 3 ")

        if choice == "1":
            book_ticket()
        elif choice == "2":
            view_bookings()
        elif choice == "3":
            print("Thanks for using the booking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":# run the main() function when this file is executed directly. It serves as the entry point of the program, allowing users to interact with the online ticket booking system through a command-line interface.
    main()
