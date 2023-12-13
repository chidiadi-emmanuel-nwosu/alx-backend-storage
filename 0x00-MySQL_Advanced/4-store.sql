-- creates a trigger that decreases the quantity
-- of an item after adding a new order.
DELIMETER //
CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
    BEGIN
        UPDATE items
        SET quantity = quantity - NEW.number
        WHERE name = NEW.item_name;
    END //
DELIMETER ;
