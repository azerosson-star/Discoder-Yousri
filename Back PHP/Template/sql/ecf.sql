CREATE DATABASE ECF;
USE ECF;
DROP TABLE IF EXISTS `voiture`;
CREATE TABLE IF NOT EXISTS `voiture` (
  `idVoiture` int NOT NULL AUTO_INCREMENT,
  `Marque` varchar(50) NOT NULL,
  `Modele` varchar(50) NOT NULL,
  `NbKilometres` int NOT NULL,
  PRIMARY KEY (`idVoiture`)
) ENGINE=INNODB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `voiture` (`idVoiture`, `Marque`, `Modele`, `NbKilometres`) VALUES
(1, 'Audi', 'A4', 2002),
(3, 'Renault', 'R5', 1000),
(4, 'Renault', 'R5 Electrique', 250);
