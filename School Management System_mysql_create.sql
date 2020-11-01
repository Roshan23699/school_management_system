CREATE TABLE `student` (
	`Name` varchar(30) NOT NULL,
	`Roll No` INT NOT NULL,
	`division` varchar(1) NOT NULL,
	`Standard` INT NOT NULL,
	`Email` varchar(20) NOT NULL,
	`Mobile` varchar(10) NOT NULL,
	`Address Id` varchar(5) NOT NULL,
	PRIMARY KEY (`Roll No`,`division`,`Standard`)
);

CREATE TABLE `Subject` (
	`Subject Id` varchar(5) NOT NULL,
	`Standard` INT NOT NULL,
	`Type` varchar(10) NOT NULL,
	`Subject Name` varchar(10) NOT NULL,
	PRIMARY KEY (`Subject Id`,`Standard`)
);

CREATE TABLE `Homework` (
	`Assignment No` INT NOT NULL,
	`Subject Id` varchar(5) NOT NULL,
	`Standard` INT NOT NULL,
	`Description` varchar(50) NOT NULL,
	`Last Date` TIMESTAMP NOT NULL,
	PRIMARY KEY (`Assignment No`,`Subject Id`,`Standard`)
);

CREATE TABLE `Teacher` (
	`Name` varchar(20) NOT NULL,
	`Teacher Id` varchar(5) NOT NULL,
	`Salary` INT NOT NULL,
	`Email` varchar(20) NOT NULL,
	PRIMARY KEY (`Teacher Id`)
);

CREATE TABLE `Result` (
	`Roll No` INT NOT NULL,
	`Division` varchar(1) NOT NULL,
	`Standard` INT NOT NULL,
	`Subject Id` varchar(5) NOT NULL,
	`Marks` INT NOT NULL,
	PRIMARY KEY (`Roll No`,`Division`,`Standard`,`Subject Id`)
);

CREATE TABLE `Teaches` (
	`teacher Id` varchar(5) NOT NULL,
	`Subject Id` varchar(5) NOT NULL,
	`Standard` INT NOT NULL,
	`Division` varchar(1) NOT NULL,
	PRIMARY KEY (`teacher Id`,`Subject Id`,`Standard`,`Division`)
);

CREATE TABLE `Login` (
	`Id` varchar(5) NOT NULL,
	`Username` varchar(10) NOT NULL,
	`Password` varchar(10) NOT NULL,
	PRIMARY KEY (`Id`)
);

CREATE TABLE `Role` (
	`Id` varchar(5) NOT NULL,
	`Type` varchar(10) NOT NULL,
	PRIMARY KEY (`Id`)
);

CREATE TABLE `User` (
	`Id` varchar(5) NOT NULL,
	`Username` varchar(10) NOT NULL,
	`Password` varchar(10) NOT NULL,
	`Email` varchar(20) NOT NULL,
	PRIMARY KEY (`Id`)
);

CREATE TABLE `Registration` (
	`Registration Id` varchar(5) NOT NULL,
	`Student Roll No` INT NOT NULL,
	`Division` varchar(1) NOT NULL,
	`Standard` INT NOT NULL,
	PRIMARY KEY (`Student Roll No`,`Division`,`Standard`)
);

CREATE TABLE `Address` (
	`Address Id` varchar(5) NOT NULL,
	`house No/Name` varchar(10) NOT NULL,
	`Area` varchar(10) NOT NULL,
	`Street Name` varchar(10) NOT NULL,
	`City` varchar(10) NOT NULL,
	`District` varchar(10) NOT NULL,
	`State` varchar(10) NOT NULL,
	PRIMARY KEY (`Address Id`)
);

ALTER TABLE `student` ADD CONSTRAINT `student_fk0` FOREIGN KEY (`Address Id`) REFERENCES `Address`(`Address Id`);

ALTER TABLE `Homework` ADD CONSTRAINT `Homework_fk0` FOREIGN KEY (`Subject Id`) REFERENCES `Subject`(`Subject Id`);

ALTER TABLE `Homework` ADD CONSTRAINT `Homework_fk1` FOREIGN KEY (`Standard`) REFERENCES `Subject`(`Standard`);

ALTER TABLE `Result` ADD CONSTRAINT `Result_fk0` FOREIGN KEY (`Roll No`) REFERENCES `student`(`Roll No`);

ALTER TABLE `Result` ADD CONSTRAINT `Result_fk1` FOREIGN KEY (`Division`) REFERENCES `student`(`division`);

ALTER TABLE `Result` ADD CONSTRAINT `Result_fk2` FOREIGN KEY (`Standard`) REFERENCES `student`(`Standard`);

ALTER TABLE `Result` ADD CONSTRAINT `Result_fk3` FOREIGN KEY (`Subject Id`) REFERENCES `Subject`(`Subject Id`);

ALTER TABLE `Teaches` ADD CONSTRAINT `Teaches_fk0` FOREIGN KEY (`teacher Id`) REFERENCES `Teaches`(`teacher Id`);

ALTER TABLE `Teaches` ADD CONSTRAINT `Teaches_fk1` FOREIGN KEY (`Subject Id`) REFERENCES `Subject`(`Subject Id`);

ALTER TABLE `Teaches` ADD CONSTRAINT `Teaches_fk2` FOREIGN KEY (`Standard`) REFERENCES `Subject`(`Standard`);

ALTER TABLE `Login` ADD CONSTRAINT `Login_fk0` FOREIGN KEY (`Id`) REFERENCES `User`(`Id`);

ALTER TABLE `Role` ADD CONSTRAINT `Role_fk0` FOREIGN KEY (`Id`) REFERENCES `User`(`Id`);

ALTER TABLE `Registration` ADD CONSTRAINT `Registration_fk0` FOREIGN KEY (`Student Roll No`) REFERENCES `student`(`Roll No`);

ALTER TABLE `Registration` ADD CONSTRAINT `Registration_fk1` FOREIGN KEY (`Division`) REFERENCES `student`(`division`);

ALTER TABLE `Registration` ADD CONSTRAINT `Registration_fk2` FOREIGN KEY (`Standard`) REFERENCES `student`(`Standard`);

