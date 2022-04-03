
create role tourism_dev with login password 'tourism_dev' createdb ;
grant all privileges on database "Tourist2" to tourism_dev;
ALTER DATABASE "Tourist2" OWNER TO tourism_dev;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO tourism_dev;

