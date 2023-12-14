-- script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for all student.
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN in_user_id INT)
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE in_user_id INT;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    user_loop: LOOP
        FETCH cur INTO in_user_id;
        IF done THEN
            LEAVE user_loop;
        END IF;

        DECLARE weighted_average_score FLOAT;

        SELECT SUM(p.weight * score) / SUM(p.weight) INTO weighted_average_score
        FROM corrections c JOIN projects p ON c.project_id = p.id
        WHERE user_id = in_user_id;

        UPDATE users
        SET average_score = weighted_average_score
        WHERE id = in_user_id;

    END LOOP user_loop;

    CLOSE cur;

END //
DELIMITER ;
