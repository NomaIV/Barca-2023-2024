# Barca-2023-2024
Database program that manages FC Barcelona players minutes played in La Liga for the 2023/2024 season.
Users can enter, update, delete and search player information in a SQLite database.

Player data can also be visualised in a bar graph using Matplotlib. The bar graph will show the number of minutes played by each player. 

## Technoilogies Used
- SQL
- SQLite
- Python
- VSCode
- Matplotlib ( for visualisation)

## Repository
[Link to repository](https://github.com/NomaIV/Barca-2023-2024.git)

## Features
- Add new playes to database
- Update player information
- Delete player information
- Search the database to find a specific player's information
- Visualise player data in a bar graph

## Prerequisites
Before you begin, ensure you have the following installed:
- VSCode
- SQLite
- Python

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/NomaIV/Barca-2023-2024.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Barca 2023:2024
   ```
3. Create and activate virtual environment (optional):
   ``` sh
   python3 -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```
4. Install required dependencies:
   ```sh
   pip3 install -r requirements.txt
   ```

## Usage
1. Setup the Database
   - Ensure SQLite is installed and available in your PATH.
   - The database will be created and populated with the initial data when you run the main script.

2. Running the Program:
   - To start the program, run the main script:
     ```sh
     python3 main.py
     ```
   - Follow the on-screen prompts to add, update, delete, or search for players in the database.

  3. Using the Program:
     - Add New Players:
       - Select option 1.
       - Enter the required information: player name, position, number of appearances, and minutes played.
     - Update Players Information:
       - Select option 2.
       - Enter the player name, new number of appearances, and new minutes played.
     - Delete Players Information:
       - Select option 3.
       - Enter the name of the player to delete.
     - Search for Players Information:
       - Select option 4.
       - Enter the name of the player to search for.

  4. Exiting the program:
     - Select option 0 to exit the program.
    
## Visualisation
To visualise the player data using Matplotlib and Pandas you can use the `visual.py` script:
```sh
python3 visual.py
```
This script will create a bar chart showing the minutes played by each player.

## Project Structure
- `main.py`: The main script to run the program.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.
- `visual.py`: Script for creating bar graph of player data.
  
## License
This project is licensed under MIT License



       
      



