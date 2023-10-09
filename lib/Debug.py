#!/usr/bin/env python3

from lib import CONN, CURSOR
from lib.song import Song

if __name__ == "__main__":
    # Create the songs table if it doesn't exist
    Song.create_table()

    # Create and save songs
    hello = Song.create("Hello", "25")
    despacito = Song.create("Despacito", "Vida")

    # Query and print the saved songs
    songs = CURSOR.execute('SELECT * FROM songs')
    for row in songs:
        print(row)
