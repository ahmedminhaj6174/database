INSERT INTO LAS_PAL.Physician(physicianID,name,position,ssn)
VALUES ('327386387','Dustin Squires','Resident','2158014'),
        ('264309669','Marlie Oneil','Psychiatrist','6426584'),
         ('360883210','Simeon Fowler','Senior','6478535'),
         ('594033452', 'Elsie Mae Douglas','Intern','2401218'),
         ('458952198','Bill Clinton', 'Chief of Medicine','1513896');



INSERT INTO LAS_PAL.Department(deptID,name,headID)
VALUES ('591082441','General Medicine','458952198'),
		('155201147','Surgery','360883210'),
		('608518898','Psychiatry','264309669');
        



INSERT INTO LAS_PAL.Procedure(procID,name, cost)
VALUES ('553369161','Inguinal hernia repair','5000'),
		('898549894','Partial colectomy','7500'),
		('500882132','Cesarean section','10000'),
		('598455190','Appendectomy','14000'),
		('106223531','Coronary artery bypass','15000');



INSERT INTO LAS_PAL.Nurse(nurseID,name,position,ssn)
VALUES ('241946979','Kitty Spencer','Nurse','1264530'),
        ('899004305','Evelyn Goff','Head Nurse','2939497'),
         ('962051891','Samuel Flores','Head Nurse','2982500'),
         ('286537267', 'Alice Herbert','Nurse','1180177'),
         ('833273127','Hajrah Maynard', 'Nurse','6033063');


INSERT INTO LAS_PAL.Medication(medID,name)
VALUES ('778403277','Azithromycin'),
		('315504360','Xanax '),
		('490752859','Hydrochlorothiazide'),
		('125544328','Doxycycline'),
		('710705701','Loratadine');


INSERT INTO LAS_PAL.Room(roomID,roomType)
VALUES ('382967810','Single'),
		('208919412','Double'),
		('347138212','Single'),
		('337270421','Single'),
		('217968759','Double');



INSERT INTO LAS_PAL.AffiliatedWith(physicianID, departmentID)
VALUES ('327386387','591082441'),
		('264309669','608518898'),
		('360883210','155201147'),
		('594033452','155201147'),
		('458952198','591082441');


INSERT INTO LAS_PAL.Patient(patientID,ssn,name,address,dob,phone, 
insuranceNumber,primaryPhysID)
VALUES ('782731294','9274193','Awais Prince','2 Towers Dr','1994-05-26','430-989-1188','17996','594033452'),
('654671730','5521511','Khadija Lake','8824 Sunland Rd','1986-11-17','210-515-8993','55033','264309669'),
('547500389','3676212','Zishan Simmons','944 Wyatt Dr','1972-07-18','832-758-2118','82204','458952198'),
('463919139', '3903822','Sapphire Maguire','9535 Acer Ave','1994-06-24', '210-434-2106','10768','327386387'),
('102338851','5958539','Giovanni Pugh', '9012 Mettler Dr
','1991-02-21','361-703-4332','78523','360883210');



INSERT INTO LAS_PAL.Prescribes(physicianID, patientID, medicationID, 
prescribedDate, dose)
VALUES ('360883210', '102338851','490752859','2021-05-04','3/day'),
('594033452', '782731294','125544328','2022-01-11','2/day'),
('264309669', '654671730','778403277','2022-01-18','5/day'),
('327386387', '463919139','710705701','2022-05-02','6/day'),
('458952198', '547500389','315504360', '2022-07-20','3/day');



INSERT INTO LAS_PAL.Stay(stayID, patientID, roomID, 
startDate, endDate)
VALUES ('538897638','547500389','347138212','2021-05-06', '2021-05-22'),
('484315300','463919139','382967810','2022-01-12', '2022-01-17'),
('822648980','102338851','337270421','2022-01-19', '2022-01-30'),
('685674538', '782731294','217968759','2022-05-05', '2022-05-09'),
('903357112','654671730','208919412', '2022-07-21', '2022-07-26');



INSERT INTO LAS_PAL.Undergoes(patientID, procedureID, 
stayID, procDate, physicianID, nurseID)
VALUES ('782731294', '500882132', '685674538','2022-05-06', '594033452', '241946979'),
		('654671730', '598455190', '903357112', '2022-07-23', '264309669', '899004305'),
		('547500389', '106223531', '538897638', '2021-05-06', '458952198', '833273127'),
		('463919139', '553369161', '484315300', '2022-01-14','327386387', '286537267'),
		('102338851', '898549894', '822648980', '2022-01-21', '360883210', '962051891');



INSERT INTO LAS_PAL.OnCall(nurseID, startDate, endDate)
VALUES ('241946979', '2022-05-05', '2022-05-09'),
        ('899004305', '2022-07-21', '2022-07-26'),
         ('962051891', '2022-01-19', '2022-01-30'),
         ('286537267', '2022-01-12', '2022-01-17'),
         ('833273127', '2021-05-06', '2021-05-22');


INSERT INTO LAS_PAL.Appointment(appID, patientID, nurseID, physicianID, 
startDateTime, endDateTime)
VALUES ('250869095', '782731294', '241946979', '594033452', '2022-05-04 11:00', '2022-05-04 12:00'),
('180995558', '654671730', '899004305', '264309669', '2022-07-19 13:00', '2022-07-19 13:30'),
('142488219', '547500389', '833273127', '458952198', '2022-01-18 10:00', '2022-01-18 10:45'),
('136646594', '463919139', '286537267', '327386387','2022-01-10 14:00', '2022-01-10 15:00'),
('774820429', '102338851', '962051891', '360883210', '2021-05-06 15:00', '2021-05-06 16:00');





