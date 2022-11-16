-- whose age is between 20 and 25
DELIMITER //
CREATE PROCEDURE GetCitizen1(IN gender varchar(1))
BEGIN
	SELECT * from citizen where citizen.gender = gender ;
END //

DELIMITER ;



    UNION  
    select * from citizen where gender = "F";