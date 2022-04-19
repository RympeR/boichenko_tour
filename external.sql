
REVOKE CREATE ON SCHEMA public FROM public;
REVOKE ALL ON DATABASE "Tourism2" FROM public;

CREATE USER tourism_guest WITH LOGIN PASSWORD 'tourism_guest';
CREATE USER tourism_client WITH LOGIN PASSWORD 'tourism_client';

create role tourism_dev with login password 'tourism_dev' createdb ;
grant all privileges on database "Tourism2" to tourism_dev;
ALTER DATABASE "Tourism2" OWNER TO tourism_dev;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO tourism_dev;

CREATE ROLE tourism_director with login password 'tourism_director' createdb ;
grant all privileges on database "Tourist2" to tourism_director;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO tourism_director;

CREATE ROLE tourism_manager with login password 'tourism_manager' ;
CREATE ROLE tourism_manager with login password 'tourism_manager' ;
GRANT SELECT, REFERENCES ON ALL TABLES IN SCHEMA public TO tourism_manager;

GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE "tourism_users"
TO tourism_guest;

GRANT SELECT, REFERENCES ON ALL TABLES IN SCHEMA public TO tourism_client;

REVOKE SELECT ON TABLE
	public.tourism_users
	FROM tourism_client;

GRANT INSERT, UPDATE  ON TABLE
    public.tourism_roomorders,
    public.tourism_tourorders,
    public.tourism_transferorders
 TO tourism_manager;

GRANT INSERT  ON TABLE
    public.tourism_roomorders,
    public.tourism_tourorders,
    public.tourism_transferorders
 TO tourism_client;


GRANT CONNECT ON DATABASE "Tourism2" to tourism_manager;
GRANT CONNECT ON DATABASE "Tourism2" to tourism_director;
GRANT CONNECT ON DATABASE "Tourism2" to tourism_dev;
GRANT CONNECT ON DATABASE "Tourism2" to tourism_client;
GRANT CONNECT ON DATABASE "Tourism2" to tourism_guest;



CREATE OR REPLACE FUNCTION verify_free_places() RETURNS TRIGGER AS $$
DECLARE
    amount int;
    places int;
BEGIN

    SELECT DISTINCT count(*) into places from tourism_rooms where id=New.room;
    SELECT DISTINCT count(*) into amount from tourism_roomorders
        join tourism_rooms on tourism_roomorders.room = tourism_rooms.id
        where 
            NEW.enddate > now()::date and room=NEW.room;


    IF amount > places  THEN
        RAISE NOTICE 'Amount of places is less than amount of orders';
        RETURN OLD;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


DROP TRIGGER IF EXISTS verify_free_places_trigger ON tourism_roomorders;
CREATE TRIGGER verify_free_places_trigger BEFORE INSERT ON tourism_roomorders
    FOR EACH ROW EXECUTE PROCEDURE verify_free_places();


CREATE OR REPLACE FUNCTION verify_free_places_tourorders() RETURNS TRIGGER AS $$
DECLARE
    amount int;
    places int;
BEGIN

    SELECT DISTINCT count(*) into places from tourism_tours where id=New.tour;
    SELECT DISTINCT count(*) into amount from tourism_tourorders
        join tourism_tours on tourism_tours.id = tourism_tourorders.tour
        where 
            NEW.enddate > now()::date and tour=NEW.tour;


    IF amount > places  THEN
        RAISE NOTICE 'Amount of places is less than amount of orders';
        RETURN OLD;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


DROP TRIGGER IF EXISTS verify_free_places_tourorders_trigger ON tourism_tourorders;
CREATE TRIGGER verify_free_places_tourorders_trigger BEFORE INSERT ON tourism_tourorders
    FOR EACH ROW EXECUTE PROCEDURE verify_free_places_tourorders();


CREATE OR REPLACE FUNCTION verify_free_places_transferorders() RETURNS TRIGGER AS $$
DECLARE
    amount int;
    places int;
BEGIN

    SELECT DISTINCT count(*) into places from tourism_trasnfers where id=New.transfer;
    SELECT DISTINCT count(*) into amount from tourism_transferorders
        join tourism_trasnfers on tourism_trasnfers.id = tourism_transferorders.transfer
        where 
            NEW.enddate > now()::date and tourism_transferorders.transfer=NEW.transfer;


    IF amount > places  THEN
        RAISE NOTICE 'Amount of places is less than amount of orders';
        RETURN OLD;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


DROP TRIGGER IF EXISTS verify_free_places_transferorders_trigger ON tourism_transferorders;
CREATE TRIGGER verify_free_places_transferorders_trigger BEFORE INSERT ON tourism_transferorders
    FOR EACH ROW EXECUTE PROCEDURE verify_free_places_transferorders();
