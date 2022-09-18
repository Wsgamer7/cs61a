.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = "blue" AND pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = "blue" AND pet = "dog";


CREATE TABLE smallest_int AS
  SELECT time, smallest from students where smallest >2 
        order by smallest limit 20;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color from students as a, students as b 
          where a.time > b.time and a.pet = b.pet and a.song = b.song;


CREATE TABLE sevens AS
  SELECT a.seven from students as a, numbers as b where a.seven = 7 and b.'7' = 'True' and a.time = b.time;

