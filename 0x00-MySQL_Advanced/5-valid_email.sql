-- script that creates a trigger that resets the attribute
-- valid_email only when the email has been changed.
DELIMITER //
CREATE TRIGGER reset_valid_email
AFTER UPDATE ON user
FOR EACH ROW
    BEGIN
        IF OLD.email <> NEW.email
            SET quantity = quantity - NEW.number;
        END IF
    END //
DELIMITER ;
