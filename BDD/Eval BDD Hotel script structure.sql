/* Création d'une base de données de gestions des hôtels dans une station balnéaire */
/* Créé le 29/09/2017 */

/* D'abord je crée la base de données */

CREATE DATABASE IF NOT EXISTS gestion_hotels DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
use gestion_hotels;

/* Ensuite je crée mes tables via le script généré par JMerise */

#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: Stations
#------------------------------------------------------------

CREATE TABLE IF NOT EXISTS Stations(
        idStation       int (11) Auto_increment  NOT NULL ,
        nomStation      Varchar (25) NOT NULL ,
        altitudeStation Int NOT NULL ,
        PRIMARY KEY (idStation )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Hotels
#------------------------------------------------------------

CREATE TABLE IF NOT EXISTS Hotels(
        idHotel        int (11) Auto_increment  NOT NULL ,
        nomHotel       Varchar (25) NOT NULL ,
        categorieHotel Int NOT NULL ,
        adresseHotel   Varchar (25) NOT NULL ,
        villeHotel     Varchar (25) NOT NULL ,
        idStation      Int NOT NULL ,
        PRIMARY KEY (idHotel )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Chambres
#------------------------------------------------------------

CREATE TABLE IF NOT EXISTS Chambres(
		IdChambre		Int NOT NULL ,
        numChambre      Int NOT NULL ,
        typeChambre     Int NOT NULL ,
        capaciteChambre Int NOT NULL ,
        idHotel         Int NOT NULL ,
        PRIMARY KEY (IdChambre )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Clients
#------------------------------------------------------------

CREATE TABLE IF NOT EXISTS Clients(
        idClient      int (11) Auto_increment  NOT NULL ,
        nomClient     Varchar (25) NOT NULL ,
        prenomClient  Varchar (25) NOT NULL ,
        adresseClient Varchar (250) NOT NULL ,
        villeClient   Varchar (25) NOT NULL ,
        PRIMARY KEY (idClient )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Réservations
#------------------------------------------------------------

CREATE TABLE IF NOT EXISTS Reservations(
		idReservation int (11) Auto_increment NOT NULL ,
        dateReservationSejour Date NOT NULL ,
        dateDebutSejour       Date NOT NULL ,
        dateFinSejour         Date NOT NULL ,
        prixSejour            Int NOT NULL ,
        arrhesSejour          Int NOT NULL ,
        idClient              Int NOT NULL ,
        IdChambre            Int NOT NULL ,
        PRIMARY KEY (idReservation )
)ENGINE=InnoDB;

ALTER TABLE Hotels ADD CONSTRAINT FK_Hotels_idStation FOREIGN KEY (idStation) REFERENCES Stations(idStation);
ALTER TABLE Chambres ADD CONSTRAINT FK_Chambres_idHotel FOREIGN KEY (idHotel) REFERENCES Hotels(idHotel);
ALTER TABLE Reservations ADD CONSTRAINT FK_reservation_idClient FOREIGN KEY (idClient) REFERENCES Clients(idClient);
ALTER TABLE Reservations ADD CONSTRAINT FK_reservation_IdChambre FOREIGN KEY (IdChambre) REFERENCES Chambres(IdChambre);


