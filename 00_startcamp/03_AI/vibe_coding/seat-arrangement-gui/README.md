# Seat Arrangement GUI Application

This project is a Python GUI application designed to help users arrange seats for students in a classroom setting. The application allows users to input the number of rows and columns for seating, select a student list file, and compare the number of students with the total available seats. The interface features a cute design with a sky-blue background and rounded fonts.

## Features

- User-friendly interface for inputting seating arrangements.
- Ability to load student names from a text file.
- Visual comparison of the number of students to the total seats.
- Cute icons and a pleasant design to enhance user experience.

## Project Structure

```
seat-arrangement-gui
├── src
│   ├── main.py          # Entry point of the application
│   ├── gui.py           # GUI layout and design
│   ├── seat_logic.py    # Logic for seating arrangement
│   └── assets
│       └── icons        # Directory for icon files
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

## Requirements

To run this application, you need to install the following dependencies:

- Tkinter (or any other GUI library you choose)
- Additional libraries as specified in `requirements.txt`

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd seat-arrangement-gui
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To start the application, run the following command:

```
python src/main.py
```

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and suggestions are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.