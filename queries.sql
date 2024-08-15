CREATE DATABASE expense_tracker;
USE expense_tracker;
CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
);
CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL,
    category_id INT,
    description VARCHAR(255),
    date DATE NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Insert some categories
INSERT INTO categories (name) VALUES ('Food');
INSERT INTO categories (name) VALUES ('Transportation');
INSERT INTO categories (name) VALUES ('Entertainment');
INSERT INTO categories (name) VALUES ('Health');
INSERT INTO categories (name) VALUES ('Others');
