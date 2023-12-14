-- script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all student.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE in_user_id INT;
    DECLARE weighted_average_score FLOAT;
    
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    user_loop: LOOP
        FETCH cur INTO in_user_id;
        IF done THEN
            LEAVE user_loop;
        END IF;

        SET weighted_average_score = (
            SELECT SUM(c.score * p.weight) / SUM(p.weight)
            FROM corrections c
            JOIN projects p ON c.project_id = p.id
            WHERE c.user_id = in_user_id
        );

        UPDATE users
        SET average_score = weighted_average_score
        WHERE id = in_user_id;

    END LOOP user_loop;

    CLOSE cur;
END //
DELIMITER ;
