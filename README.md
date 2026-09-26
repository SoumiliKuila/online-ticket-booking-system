🎬 Online Ticket Booking System

A simple Python-based Online Ticket Booking System that allows users to view available movies, book tickets, check booking history, and store booking details in a text file.

📌 Project Overview

This project is a command-line based movie ticket booking system developed using Python.

Users can:

- View available movies
- Check ticket prices and available seats
- Book tickets
- Enter customer details
- Calculate the total ticket amount
- Confirm or cancel a booking
- View booking history
- Store confirmed booking details permanently in a text file

✨ Features

🎥 Movie Display

Displays:

- Movie ID
- Movie name
- Ticket price
- Available seats

🎟️ Ticket Booking

Users can select a movie and enter the number of tickets they want to book.

The system validates:

- Movie selection
- Number of tickets
- Available seats

💰 Automatic Bill Calculation

The total amount is calculated automatically:

Total Amount = Number of Tickets × Ticket Price

👤 Customer Details

The system collects:

- Customer name
- Phone number
- Selected movie
- Number of tickets
- Total amount

📋 Booking History

Users can view all bookings made during the current program session.

💾 File Storage

Confirmed bookings are also stored in:

ticket_booking.txt

This allows booking information to be saved even after the program closes.

🛠️ Technologies Used

- Python
- Python Dictionaries
- Python Lists
- Functions
- Loops
- Conditional Statements
- File Handling
- User Input and Validation

🎬 Movies Included

The current system contains the following movies:

Movie| Price
Avengers: Welcome to The Jungle| ₹350
Jungle Cruise| ₹300
Spider-Man: No Way Home| ₹400
Toy Story 4| ₹250

The movie prices and available seats can be modified directly in the "movies" dictionary.

🔄 How the System Works

Start
  ↓
Display Main Menu
  ↓
Book Ticket / View Booking History / Exit
  ↓
Select Movie
  ↓
Enter Number of Tickets
  ↓
Check Seat Availability
  ↓
Calculate Total Amount
  ↓
Confirm Booking
  ↓
Update Available Seats
  ↓
Save Booking Details
  ↓
Display Success Message

📂 Project Structure

online-ticket-booking-system/
│
├── Online_Ticket_Booking.py
├── README.md
└── ticket_booking.txt

«"ticket_booking.txt" is created automatically when a booking is successfully made.»

▶️ How to Run

1. Install Python

Make sure Python is installed on your computer.

2. Clone the Repository

git clone https://github.com/SoumiliKuila/online-ticket-booking-system.git

3. Open the Project Folder

cd online-ticket-booking-system

4. Run the Program

python Online_Ticket_Booking.py

🖥️ Main Menu

When the program starts, users see:

==== ONLINE TICKET BOOKING ====

1. Book Ticket
2. View Booking History
3. Exit

📚 Concepts Demonstrated

This project demonstrates practical use of:

- Dictionaries
- Lists
- Functions
- "if-elif-else"
- "while" loops
- "for" loops
- User input
- Input validation
- File handling
- String formatting
- Data updating
- Program entry point using "if __name__ == "__main__""

🚀 Future Improvements

Some possible improvements for future versions are:

- Add a graphical user interface (GUI)
- Add a database such as MySQL
- Add login and registration
- Add movie show timings
- Add theatre selection
- Add online payment integration
- Add ticket cancellation
- Generate digital/printable tickets

👩‍💻 Author

Soumili Kuila

BCA Student | Aspiring Data Analyst / Data Science Professional

GitHub:
https://github.com/SoumiliKuila

LinkedIn:
https://www.linkedin.com/in/soumili-kuila-7a553a374/
