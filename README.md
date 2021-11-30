# Flask SQLite full-stack-Python template

## About

A web app in Flask that allows via web form to enter a username.<br> 
The backend saves it with the date of the day and an auto-incrementing ID and saves it to a local SQLite DB.

### Records for SQLite

Create the table:<br>

CREATE TABLE users (<br>
    entry_date varchar (20) NOT NULL,<br>
    user varchar (20) NOT NULL<br>
);<br>

    
Get the table data with auto increment id feature from SQLite:<br>

SELECT<br>
   rowid,<br>
   entry_date,<br>
   user<br>
FROM<br>
   users;<br>

