-- Create database

create table detection (
    id INTEGER primary key AUTOINCREMENT,
    original_image text,
    processed_image text,
    error text
);