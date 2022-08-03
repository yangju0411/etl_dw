CREATE TABLE contents (
	contents_key serial PRIMARY KEY,
	path	varchar(65532)	unique NOT NULL
);

CREATE TABLE visit (
	client_key int NOT NULL,
	contents_key int NOT NULL,
	time_key char(14) NOT NULL,
	os_key	int	NOT NULL,
	browser_key	int	NOT NULL,
	method	VARCHAR(255)	NULL,
	status	int	NULL,
	size int null
);

CREATE TABLE time (
	time_key	char(14)	NOT NULL,
    date date null,
	day	int	NULL,
	weekday	int	NULL,
	month	int	NULL,
	year	int	NULL,
	hour	int	NULL,
	minute	int	NULL,
	second	int	NULL
);

CREATE TABLE client (
	client_key	serial	NOT NULL,
	host	VARCHAR(255)	unique not null
);

CREATE TABLE os (
	os_key	serial	NOT NULL,
	name	VARCHAR(255)	unique not NULL
);

CREATE TABLE browser (
	browser_key	serial	NOT NULL,
	name	VARCHAR(255)	unique not NULL
);

ALTER TABLE contents ADD CONSTRAINT PK_CONTENTS PRIMARY KEY (
	contents_key
);

ALTER TABLE visit ADD CONSTRAINT PK_VISIT PRIMARY KEY (
	client_key,
	contents_key,
	time_key,
	os_key,
	browser_key
);

ALTER TABLE time ADD CONSTRAINT PK_TIME PRIMARY KEY (
	time_key
);

ALTER TABLE client ADD CONSTRAINT PK_client PRIMARY KEY (
	client_key
);

ALTER TABLE os ADD CONSTRAINT PK_OS PRIMARY KEY (
	os_key
);

ALTER TABLE browser ADD CONSTRAINT PK_BROWSER PRIMARY KEY (
	browser_key
);

ALTER TABLE visit ADD CONSTRAINT FK_client_TO_Visit_1 FOREIGN KEY (
	client_key
)
REFERENCES client (
	client_key
);

ALTER TABLE visit ADD CONSTRAINT FK_Contents_TO_Visit_1 FOREIGN KEY (
	contents_key
)
REFERENCES contents (
	contents_key
);

ALTER TABLE visit ADD CONSTRAINT FK_Time_TO_Visit_1 FOREIGN KEY (
	time_key
)
REFERENCES time (
	time_key
);

ALTER TABLE visit ADD CONSTRAINT FK_Os_TO_Visit_1 FOREIGN KEY (
	os_key
)
REFERENCES os (
	os_key
);

ALTER TABLE visit ADD CONSTRAINT FK_Browser_TO_Visit_1 FOREIGN KEY (
	browser_key
)
REFERENCES browser (
	browser_key
);