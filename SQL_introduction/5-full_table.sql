SELECT
    TABLE_NAME AS 'Table',
    CREATE_TIME AS 'Create Table'
FROM
    information_schema.tables
WHERE
    table_schema = 'hbtn_0c_0' AND
    table_name = 'first_table';
