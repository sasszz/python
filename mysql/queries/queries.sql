-- Forward engineer the dojos_and_ninjas_schema from the previous chapter

-- Create a .txt file where you'll save each of your queries from below

-- Query: Create 3 new dojos

INSERT INTO dojos (name) 
VALUES ('Burbank'), ('San Jose'), ('Online');

-- Query: Delete the 3 dojos you just created

DELETE FROM `dojos_and_ninjas`.`dojos` WHERE (`id` < '3');

-- Query: Create 3 more dojos

INSERT INTO dojos (name) 
VALUES ('Las Vegas'), ('Seattle'), ('Tulsa');

-- Query: Create 3 ninjas that belong to the first dojo

-- Query: Create 3 ninjas that belong to the second dojo

INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
VALUES ('Andy', 'Lim', 25, 5), ('Joe', 'Smith', 22, 5), ('Mary', 'Coder', 35, 5);


-- Query: Create 3 ninjas that belong to the third dojo

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES('Lucie', 'Chevreuil', 25, 3), ('Nisrine', 'Kane', 31, 3), ('Tyler', 'Maxwell', 39, 3)

-- Query: Retrieve all the ninjas from the first dojo
SELECT * FROM ninjas WHERE dojo_id  = 1

-- Query: Retrieve all the ninjas from the last dojo

-- Query: Retrieve the last ninja's dojo

SELECT * FROM dojos WHERE id = (SELECT dojo_id FROM ninjas ORDER BY id DESC LIMIT 1);

-- Submit your .txt file that contains all the queries you ran in the shell

SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id;