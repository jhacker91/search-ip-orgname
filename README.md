# search-ip-orgname
Search ip ( or ip with detailed info) from organization name

# before start

Add information in "chiavi.py". All you need to do is to go on Censys to take UID and SECRET key of your API.
IF YOU DON'T WRITE YOUR API IN "CHIAVI.PY" THE SCRIPT DON'T WORK


# usage

search-ip-orgname.py --ip example.com

The script return all the ip in json format. If you want to save in a file you can add ">"
(search-ip-orgname.py --ip example.com > file.txt)

search-ip-orgname.py --desc example.com

The script return all the ip whit detail in json format. If you want to save in a file you can add ">"
(search-ip-orgname.py --desc example.com > file.txt)

