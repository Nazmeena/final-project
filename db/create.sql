CREATE TABLE IF NOT EXISTS classes (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(30) 
);
CREATE TABLE IF NOT EXISTS students (
        id INT PRIMARY KEY AUTO_INCREMENT, 
        name VARCHAR(30),
        position VARCHAR(30),
        fk_classid INT, 
        FOREIGN KEY (fk_classid) REFERENCES classes(id)
);
