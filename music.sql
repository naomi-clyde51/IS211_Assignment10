-- Artists table
CREATE TABLE Artists (
  artist_id INTEGER PRIMARY KEY,
  artist_name TEXT NOT NULL -- name not allowed to be NULL
);

-- Albums table
CREATE TABLE Albums (
  album_id INTEGER PRIMARY KEY,
  album_name TEXT NOT NULL, -- name not allowed to be NULL
  artist_id INTEGER, -- artist id is whole number
  FOREIGN KEY (artist_id) REFERENCES Artists(artist_id) -- linking artist_id in current table with album_id in Artists table
);

-- Songs table
CREATE TABLE Songs (
  song_id INTEGER PRIMARY KEY,
  song_name TEXT NOT NULL, -- name not allowed to be NULL
  album_id INTEGER, -- the associated album this song appears on
  track_number INTEGER, -- track number of the song
  duration_seconds INTEGER, -- how long the song is (in seconds)
  FOREIGN KEY (album_id) REFERENCES Artists(album_id) -- linking album_id in current table with album_id in Artists table
);
