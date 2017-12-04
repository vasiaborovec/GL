Select * from Users
where date_of_block = DATEADD(year, -1, getdate())
and date_of_attempt => DATEADD(month, -1, getdate());
