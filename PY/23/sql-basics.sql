-- SQL = Structured Query Language
-- CRUD Operace
-- C - create - SQL INSERT
-- R - retreive (read) - SQL SELECT
-- U - update - SQL UPDATE
-- D - delete - SQL DELETE

select * from users
limit 100 -- TOP 100

SELECT id, name, work_position_id FROM users
-- WHERE work_position_id = 1 AND (work_position_id = 2 OR id = 1)
ORDER BY id DESC
LIMIT 2

select * from users where id = 1
-- UPDATE users SET name = 'Leo++', work_position_id = 2 WHERE id = 1

-- UPDATE users SET
-- name = name || '..' -- concat(text1, text2...)
-- WHERE work_position_id != 2


-- DELETE from users where id = 4
select * from users

INSERT INTO users (name, work_position_id)
VALUES ('Jakob', 3), ('Lena', 1), ('Nina', 2)

select * from users where name like '%a%'


-- CRUD - samostaná práce
-- 1. vložte nový záznam do tabulky users (INSERT)
--  name='Galgot', work_position_id=3

-- 2. select všechny users, kteří mají work_position_id=3 (SELECT)

-- 3. delete users kde jméno je 'Jakob' (DELETE)

-- 4. update work_position_id=1 kde name='Galgot' (UPDATE)
-- s.ganbaatar@seznam.cz
