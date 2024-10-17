SELECT
	users.id,
	users.name,
	work_positions.name
FROM users
INNER JOIN work_positions ON users.work_position_id = work_positions.id
-- ORDER by ...
WHERE work_positions.name = 'manager'



-- delete from users where name like '0%'