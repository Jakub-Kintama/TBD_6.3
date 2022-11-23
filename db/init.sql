create table Car
(
    id      serial primary key,
    model   varchar(255),
    year    integer,
    details text
);

insert into Car (model, "year", details)
values ('mondeo', 2010, 'details'),
       ('golf 5', 2009, 'details'),
       ('mx-5 miata', 2000, 'details');