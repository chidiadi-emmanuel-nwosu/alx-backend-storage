-- script that creates users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE KEY NOT NULL,
    name VARCHAR(255)
);
