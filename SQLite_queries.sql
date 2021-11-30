/* Records for SQLite

Create the table: */

`
CREATE TABLE users (
    entry_date varchar (20) NOT NULL,
    user varchar (20) NOT NULL
);
`
    
/* Get the table data with auto increment id feature from SQLite: */ 

`
SELECT
   rowid,
   entry_date,
   user
FROM
   users;
`