# Hotel Booking App

## Prerequisites
- Python 3.x
- MySQL Server
- `mysql-connector-python` library (Install using `pip install mysql-connector-python`)

## Getting Started
1. Ensure you have Python and MySQL installed on your system.
2. Install the `mysql-connector-python` library using `pip`.
3. Update the database connection details (`host`, `username`, `password`, `database`) in the script with your own RDS details.

## Usage
1. Run the script (`hotel_booking.py`).
2. Upon running, the application will prompt whether to register or login.
3. If registering, provide necessary details (email, name, password).
4. Upon successful registration or login, the user can proceed to book a hotel.
5. Enter the city name, booking dates, number of rooms, and guests.
6. The application will display available rooms in the specified city along with pricing.
7. Select a hotel for booking and confirm.
8. A booking receipt will be displayed with the total cost.
9. Option to book another ticket or go back to the booking page will be provided.

## Database Schema
- The script assumes the following database schema:
  - `hotelinfor` database with tables `hotelinfor` for user information and `hotel_info` for hotel details.

## Notes
- Ensure that the MySQL server is running and accessible.
- Make sure to handle sensitive information securely, especially when deploying in production environments.

## Disclaimer
This script is provided as a basic demonstration and may require additional features, error handling, and security enhancements for production use.