-- Database schema and sample data for simple blog using web.py
--
-- create a database using:
--
--    sqlite3 blog.db < schema.sql
--
create table post (
	id integer primary key autoincrement,
	slug text unique,
	title text,
	body text,
	created timestamp default current_timestamp
);

insert into post (slug, title, body) 
	values ('hello-world', "Hello World", "First blog post");
insert into post (slug, title, body) 
	values ('hello-again', "Hello Hello!", "Another blog post");