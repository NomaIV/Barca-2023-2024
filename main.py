import sqlite3

db =sqlite3.connect('barca2024')
cursor = db.cursor()

# Create the table "barca2024"
cursor.execute('''
    CREATE TABLE if NOT EXISTS barca2024 (
        Player_Name TEXT PRIMARY KEY,
        Player_Position TEXT,
        Number_of_Appearances INTEGER,
        Minutes_Played INTEGER
    )
''')
db.commit()

# Define barca2024 data
barca2024_data = [
    ('Marc-André ter Stegen', 'Goal keeper', 28, 2520),
    ('Iñaki Peña', 'Goal Keeper', 10, 900),
    ('Ronald Araujo', 'Defender',25, 1997),
    ('Jules Koundé','Defender', 35, 2901),
    ('Alejandro Balde', 'Defender', 18, 1381),
    ('Andreas Christensen', 'Defender', 30, 1993),
    ('Pau Cubarsí','Defender', 19, 1562),
    ('João Cancelo', 'Defender', 32, 2510),
    ('Eric García', 'Defender', 2, 57),
    ('Héctor Fort', 'Defender', 7, 321),
    ('Iñigo Martínez', 'Defender', 20, 1297),
    ('Marcos Alonso', 'Defender', 5, 252),
    ('Gavi', 'Medfield', 12, 945),
    ('Pedri', 'Medfield', 24, 1489),
    ('Frenkie de Jong', 'Medfield', 20, 1637),
    ('Fermín López', 'Medfield', 31, 1460 )
]

# Insert barca2024 data
cursor.executemany('''
    INSERT OR REPLACE INTO barca2024 (Player_Name, Player_Position, Number_of_Appearances, Minutes_Played) VALUES  (?, ?, ?, ?)
''', barca2024_data)

while True:
    print('\nMain Menu: ')
    print('1. Enter player information')
    print('2. Update player information')
    print('3. Delete player information')
    print('4. Search player information')
    print('0. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        #Enter player information
        Player_Name = input('Enter player name:')
        Player_Position = input('Enter player position:')
        Number_of_Appearances = int(input('Enter number of appearances:'))
        Minutes_Played = int(input('Enter number of minutes played:'))

        try:
            cursor.execute('''
                INSERT INTO barca2024 (Player_Name, Player_Position, Number_of_Appearances, Minutes_Played) VALUES (?, ?, ?, ?)
                ''', (Player_Name, Player_Position, Number_of_Appearances, Minutes_Played))
            print(f'Player information for {Player_Name} successfully added.')
        except sqlite3.IntegrityError:
            print(f'Error: Player with the name {Player_Name} already exists.')


    elif choice == '2':
        # Update player information
        Player_Name = input('Enter player name:')
        New_Number_of_Appearances = int(input('Enter new number of appearances:'))
        New_Minutes_Played = int(input('Enter new number of minutes played:'))

        cursor.execute('''
            UPDATE barca2024 SET Number_of_Appearances = ?, Minutes_Played = ? WHERE Player_Name = ?
                       ''', (New_Number_of_Appearances, New_Minutes_Played, Player_Name))
        print(f'Number of appearances and minutes played for {Player_Name} has been updated')

    elif choice =='3':
        # Delete player information
        player_name_to_delete = input('Enter player name to delete:')

        cursor.execute('''DELETE FROM barca2024 WHERE Player_Name = ?
                       ''', (player_name_to_delete,))
        print(f'Player information for {player_name_to_delete} deleted successfully.')

    elif choice == '4':
        # Search player information 
        Player_Name = input('Enter player name to search for:')

        cursor.execute(''' SELECT * FROM barca2024 WHERE Player_Name = ?
                       ''', (Player_Name,))
        
        barca_players = cursor.fetchall()
        if barca_players:
            for player in barca_players:
                print(player)
        else:
            print(f'No player information found for player name: {Player_Name}')
        
    elif choice == '0':
        # Exit
        break
    else:
        print('Invalid choice. Please try again.')

db.commit()
db.close()

