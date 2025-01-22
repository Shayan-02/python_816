create table tblstudent(
	s_id int identity(6, 6),
	s_name nvarchar(255) not null,
	s_pid char(10),
	major nvarchar(10),
	field nvarchar(20),
	s_tel char(20)
	primary key(s_id, s_pid)
);

create table tblteacher(
	t_id int identity(4, 4),
	t_name nvarchar(255) not null,
	t_pid char(10),
	courses nvarchar(20),
	t_tel char(20)
	primary key(t_id, t_pid, courses)
);

create table tblcourse(
	c_id int identity(3, 6),
	c_name nvarchar(255) not null,
	c_num int,
	c_vahed int,
	c_type nvarchar(10)
	primary key(c_id, c_name)
);