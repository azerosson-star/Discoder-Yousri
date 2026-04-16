drop table if exists Station
create table if not exists Station

create table Station (
id_Station INT AUTO_INCREMENT PRIMARY KEY,
nom_station VARCHAR(100) NOT NULL,
altitude INT NOT NULL

)

drop table if exists Hotels
create table if not exists Hotels

create table Hotels (
id_Hotels INT AUTO_INCREMENT PRIMARY KEY,
id_Station INT NOT NULL,
nom_hotel varchar(100) not null,
categorie_hotel int not null,
adreese_hotel varchar (200) not null,
ville_hotel varchar (100) not null

CONSTRAINT `fk_hotels_station`
    foreign key (`id_Station`)
    References `Station`(`id_Station`)
    ON DELETE RESTRICT ON UPDATE CASCADE);

drop table if exists Chambres
create table if not exists Chambres
CREATE TABLE Chambres (
id_Chambres INT AUTO_INCREMENT PRIMARY KEY,
id_Hotel INT NOT NULL,
numero_chambre INT NOT NULL,
type_chambre INT NOT NULL,
capacite_chambre INT NOT NULL

CONSTRAINT `fk_hotels_chambres`
    foreign key (`id_Hotel`)
    References `Hotel`(`id_Hotel`)
    ON DELETE RESTRICT ON UPDATE CASCADE);
drop table if exists Reservation
create table if not exists Reservation
CREATE TABLE Reservation (
id_Reservation INT AUTO_INCREMENT PRIMARY KEY,
id_Chambres INT NOT NULL,
id_Client INT NOT NULL,

 date_reserv DATE NOT NULL,
 date_debut DATE NOT NULL,
 date_fin DATE NOT NULL,
 prix_sejour INT NOT NULL

CONSTRAINT `fk_reservation_chambres`
    foreign key (`id_reservation`)
    References `Reservation`(`id_Reservation`)
    ON DELETE RESTRICT ON UPDATE CASCADE);
CONSTRAINT `fk_reservation_clients`
    foreign key (`id_Client`)
    References `Client`(`id_Client`)
    ON DELETE RESTRICT ON UPDATE CASCADE);
)
drop table if exists Client
create table if not exists Client
CREATE TABLE Client (
id_Reservation INT AUTO_INCREMENT PRIMARY KEY,
nom_client text,
prenom_client text,
adresse_client text,
ville_client text
)

