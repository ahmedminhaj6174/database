CREATE DATABASE LAS_PAL;

CREATE TABLE LAS_PAL.Physician(
	physicianID INT NOT NULL,
    name VARCHAR(40) NOT NULL,
    position VARCHAR(40) NOT NULL, 
    ssn INT NOT NULL UNIQUE,
    PRIMARY KEY (physicianID),
    CONSTRAINT CHK_position CHECK (position IN('Intern', 'Surgeon', 'Senior', 
    'Chief of Medicine', 
    'Resident', 'Psychiatrist')));



CREATE TABLE LAS_PAL.Procedure(
 	procID INT NOT NULL,
    name VARCHAR(40) NOT NULL,
    cost REAL NOT NULL,
    PRIMARY KEY (procID)
);

CREATE TABLE LAS_PAL.Nurse(
	nurseID INT NOT NULL,
    name VARCHAR(40) NOT NULL,
    position VARCHAR(40) NOT NULL, 
    ssn INT NOT NULL UNIQUE,
    PRIMARY KEY (nurseID),
	CONSTRAINT CHK_nurse_position CHECK (position IN('Head Nurse','Nurse'))
);


CREATE TABLE LAS_PAL.Medication(
	medID INT NOT NULL,
    name VARCHAR(40) NOT NULL,
    PRIMARY KEY (medID)
);

CREATE TABLE LAS_PAL.Room(
	roomID INT NOT NULL,
    roomType VARCHAR(40) NOT NULL,
    PRIMARY KEY (roomID),
    CONSTRAINT CHK_roomType CHECK (roomType IN('Single','Double'))
);


CREATE TABLE LAS_PAL.Department(
	deptID INT NOT NULL, 
    name VARCHAR(40) NOT NULL, 
    headID INT NOT NULL UNIQUE,
    PRIMARY KEY (deptID),
	FOREIGN KEY (headID) REFERENCES Physician(physicianID), 
    CONSTRAINT CHK_dept_name CHECK (name IN('General Medicine','Surgery', 
    'Psychiatry'))
 );


CREATE TABLE LAS_PAL.AffiliatedWith(
	physicianID INT NOT NULL,
    departmentID INT NOT NULL,
    PRIMARY KEY (physicianID, departmentID),
	FOREIGN KEY (physicianID) REFERENCES Physician(physicianID),
	FOREIGN KEY (departmentID) REFERENCES Department(deptID)
    );
    
   CREATE TABLE LAS_PAL.Patient(
	patientID INT NOT NULL, 
    ssn INT NOT NULL UNIQUE, name VARCHAR(40) NOT NULL, address VARCHAR(100) NOT NULL, 
    dob DATE NOT NULL, phone VARCHAR(16) NOT NULL, 
    insuranceNumber INT NOT NULL UNIQUE, primaryPhysID INT NOT NULL UNIQUE,
    PRIMARY KEY (patientID),
	FOREIGN KEY (primaryPhysID) REFERENCES Physician(physicianID)
    );


    
    CREATE TABLE LAS_PAL.Prescribes(
	physicianID INT NOT NULL, patientID INT NOT NULL, medicationID INT NOT NULL, 
    prescribedDate DATE NOT NULL, dose VARCHAR(40) NOT NULL,
    PRIMARY KEY (physicianID, patientID, medicationID, prescribedDate),
	FOREIGN KEY (physicianID) REFERENCES Physician(physicianID),
	FOREIGN KEY (patientID) REFERENCES Patient(patientID),
	FOREIGN KEY (medicationID) REFERENCES Medication(medID) 
    );


    
CREATE TABLE LAS_PAL.Stay(
	stayID INT NOT NULL, patientID INT UNIQUE NOT NULL, 
    roomID INT NOT NULL, startDate DATE NOT NULL, endDate DATE NOT NULL,
    PRIMARY KEY (stayID),
	FOREIGN KEY (patientID) REFERENCES Patient(patientID),
	FOREIGN KEY (roomID) REFERENCES Room(roomID)
    );


    
   CREATE TABLE LAS_PAL.Undergoes(
	patientID INT NOT NULL, procedureID INT NOT NULL, stayID INT NOT NULL, 
    procDate date NOT NULL, physicianID INT UNIQUE NOT NULL, nurseID INT UNIQUE NOT NULL,
    PRIMARY KEY (patientID, procedureID, stayID, procDate),
	FOREIGN KEY (patientID) REFERENCES Patient(patientID),
	FOREIGN KEY (procedureID) REFERENCES `Procedure`(procID),
	FOREIGN KEY (stayID) REFERENCES Stay(stayID),
	FOREIGN KEY (physicianID) REFERENCES Physician(physicianID),
	FOREIGN KEY (nurseID) REFERENCES Nurse(nurseID)
    );


    
CREATE TABLE LAS_PAL.OnCall(
	nurseID INT NOT NULL, startDate DATE NOT NULL, endDate DATE NOT NULL,
    PRIMARY KEY (nurseID, startDate, endDate),
	FOREIGN KEY (nurseID) REFERENCES Nurse(nurseID)
    );

    
    
   CREATE TABLE LAS_PAL.Appointment(
	appID INT NOT NULL, patientID INT NOT NULL UNIQUE, nurseID INT NOT NULL UNIQUE, 
    physicianID INT NOT NULL UNIQUE, startDateTime DATETIME NOT NULL, 
    endDateTime DATETIME NOT NULL,
    PRIMARY KEY (appID),
	FOREIGN KEY (patientID) REFERENCES Patient(patientID),
	FOREIGN KEY (nurseID) REFERENCES Nurse(nurseID),
	FOREIGN KEY (physicianID) REFERENCES Physician(physicianID)
    );


