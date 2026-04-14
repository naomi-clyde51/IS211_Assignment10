-- Artists table
CREATE TABLE Artists (
  artist_id INTEGER PRIMARY KEY,
  artist_name TEXT NOT NULL -- name not allowed to be NULL
);

-- Albums table
CREATE TABLE Albums (
  album_id INTEGER PRIMARY KEY,
  album_name TEXT NOT NULL, -- name not allowed to be NULL
  artist_id INTEGER,
  FOREIGN KEY (artist_id) REFERENCES Artists(artist_id)
);

-- Songs table
CREATE TABLE Songs (
  song_id INTEGER PRIMARY KEY,
  song_name TEXT NOT NULL, -- name not allowed to be NULL
  album_id INTEGER,
  track_number INTEGER,
  duration_seconds INTEGER,
  FOREIGN KEY (album_id) REFERENCES Artists(album_id)
);
