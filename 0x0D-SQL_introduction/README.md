#0x0D. SQL - Introduction
##0. List databases
Write a script that lists all databases of your MySQL server.

guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x0D-SQL_introduction
File: 0-list_databases.sql
