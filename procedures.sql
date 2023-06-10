DELIMITER //

-- Procedure to insert a new item into the table and return its id.
CREATE PROCEDURE InsertNewItem(IN name VARCHAR(100), IN description VARCHAR(255), IN price DECIMAL(10,2))
BEGIN
   INSERT INTO Items (name, description, price) VALUES (name, description, price);
   SELECT LAST_INSERT_ID() as 'new_item_id';
END//

-- Procedure to return all items details.
CREATE PROCEDURE GetAllItems()
BEGIN
   SELECT id, name, description, price, created_at FROM Items;
END//

-- Procedure to update the item price with matching id and return the updated price.
CREATE PROCEDURE UpdateItemPrice(IN item_id INT, IN new_price DECIMAL(10,2))
BEGIN
   UPDATE Items SET price = new_price WHERE id = item_id;
   SELECT price FROM Items WHERE id = item_id;
END//

-- Procedure to delete the item with the matching id.
CREATE PROCEDURE DeleteItem(IN item_id INT)
BEGIN
   DELETE FROM Items WHERE id = item_id;
END//

-- Procedure to insert a new employee into the table and return its id.
CREATE PROCEDURE InsertNewEmployee(IN name VARCHAR(100), IN position VARCHAR(100), IN hourly_wage DECIMAL(10,2))
BEGIN
   INSERT INTO Employees (name, position, hourly_wage) VALUES (name, position, hourly_wage);
   SELECT LAST_INSERT_ID() as 'new_employee_id';
END//

-- Procedure to return an employee details with the provided id.
CREATE PROCEDURE GetEmployeeDetails(IN employee_id INT)
BEGIN
   SELECT name, position, hired_at, hourly_wage FROM Employees WHERE id = employee_id;
END//

-- Procedure to update the employee's hourly wage with the provided id and return the updated wage.
CREATE PROCEDURE UpdateEmployeeWage(IN employee_id INT, IN new_wage DECIMAL(10,2))
BEGIN
   UPDATE Employees SET hourly_wage = new_wage WHERE id = employee_id;
   SELECT hourly_wage FROM Employees WHERE id = employee_id;
END//

-- Procedure to delete the employee with the provided id.
CREATE PROCEDURE DeleteEmployee(IN employee_id INT)
BEGIN
   DELETE FROM Employees WHERE id = employee_id;
END//

DELIMITER ;
