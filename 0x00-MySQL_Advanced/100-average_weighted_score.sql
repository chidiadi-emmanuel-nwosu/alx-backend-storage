-- script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN in_user_id INT)
BEGIN
    DECLARE weighted_average_score FLOAT;

    SELECT SUM(p.weight * score) / SUM(p.weight) INTO weighted_average_score
    FROM corrections c JOIN projects p ON c.project_id = p.id
    WHERE user_id = in_user_id;

    UPDATE users
    SET average_score = weighted_average_score
    WHERE id = in_user_id;
END //
DELIMITER ;
