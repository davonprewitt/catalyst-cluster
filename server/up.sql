CREATE TABLE participant (
    id serial PRIMARY KEY,
    fname text NOT NULL,
    lname text NOT NULL,
    track varchar(25) check (track in ('software', 'hardware', 'gaming', 'design')),
    height integer NOT NULL,
    marvel integer NOT NULL,
    pet integer NOT NULL
);
