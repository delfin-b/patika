update employee
set name= 'Merrickson',
	birthday= '2022-08-08',
	email='mr.merrick@sql.com'
where id= 2;

update employee
set name= 'Paulo',
	birthday= '2022-12-01',
	email='p00la@sql.com'
where id= 44;

update employee
set name= 'Abi',
	birthday= '2023-07-17',
	email='abe@sql.com'
where id= 21;

update employee
set name= 'Carylyn',
	birthday= '2022-10-10',
	email='crcrcr@sql.com'
where id= 12;

update employee
set name= 'Kemet',
	birthday= '2022-09-19',
	email='dv-kemet@sql.com'
where id= 20;

delete from employee
where id=13;

delete from employee
where name='Berri';

delete from employee
where id=39;

delete from employee
where name='Skippie';

delete from employee
where id=4;
