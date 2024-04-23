SELECT name from songs where artist_id =
(SELECT id from artists WHERE name = 'Post Malone');
