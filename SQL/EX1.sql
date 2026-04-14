SELECT * FROM `clients`
SELECT `nomClient` FROM `clients`;
SELECT DISTINCT`dateCommande` FROM `commandes`;
SELECT * FROM clients where prenomClient = 'sophie';
SELECT idArticle,idCommande FROM `commandes` where idClient in (2);
SELECT * FROM clients WHERE REGEXP_LIKE(nomClient, '[A-Z]','c'); "case-sensitive"
SELECT CONCAT(UPPER(SUBSTRING(nomClient, 1, 1)), LOWER(SUBSTRING(nomClient, 2))) AS nomFormate FROM clients;
SELECT nomClient FROM clients WHERE CHAR_LENGTH(nomClient) = 5;
SELECT nomClient FROM clients WHERE nomClient LIKE 't%' OR nomClient LIKE '__l%';
SELECT idClient, idCommande, dateCommande, DATE_ADD(dateCommande, INTERVAL 15 DAY) AS datePaiementAttendue FROM commandes;
SELECT NOW() AS dateHeureActuelles;
SELECT nomClient, prenomClient, TIMESTAMPDIFF(YEAR, dateEntreeClient, CURDATE()) AS ancienneteEnAnnees FROM clients;
SELECT MAX(quantiteCommande) AS quantiteMax FROM commandes;
SELECT SUM(quantiteCommande) AS quantiteTotale FROM commandes WHERE idClient = 1;
SELECT AVG(quantiteCommande) AS quantiteMoyenne FROM commandes WHERE idClient = 2;
SELECT * FROM clients ORDER BY nomClient ASC;
SELECT * FROM articles ORDER BY prixArticle DESC;