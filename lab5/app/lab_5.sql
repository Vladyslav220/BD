USE parkingdb;

DELIMITER //

-- Тригер для заборони видалення в таблиці parking
CREATE TRIGGER prevent_delete_on_parking
BEFORE DELETE ON parking
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Deletion is not allowed on parking table.';
END //

DELIMITER ;



USE parkingdb;

DELIMITER //

-- Тригер для заборони модифікації в таблиці reservation
CREATE TRIGGER prevent_modification_on_reservation
BEFORE UPDATE ON reservation
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Modifications are not allowed on reservation table.';
END //

-- Тригер для заборони видалення в таблиці reservation
CREATE TRIGGER prevent_delete_on_reservation
BEFORE DELETE ON reservation
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Deletion is not allowed on reservation table.';
END //

DELIMITER ;




USE parkingdc;

DELIMITER //

-- Тригер для заборони вставки значень, які закінчуються двома нулями
CREATE TRIGGER prevent_double_zero_insert_on_parking
BEFORE INSERT ON parking_spot
FOR EACH ROW
BEGIN

    IF RIGHT(NEW.spot_number, 2) = '00' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Values in column_name cannot end with two zeros.';
    END IF;
END //

DELIMITER ;
