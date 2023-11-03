#From HTB academy
for char in '%20' '%0a' '%00' '%0d0a' '/' '.\\' '.' '…' ':'; do
    for ext in '.php' '.phps'; do
        echo "blah$char$ext.jpg" >> wordlist.txt
        echo "blah$ext$char.jpg" >> wordlist.txt
        echo "blah.jpg$char$ext" >> wordlist.txt
        echo "blah.jpg$ext$char" >> wordlist.txt
    done
done
