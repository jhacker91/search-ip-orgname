#Giuseppe Compare
#10-11-2020
import sys
import requests
import time
import chiavi
import argparse

print("****************************")
print("OUTPUT Dettagliato: IP, LOCATION COUNTRY, COUTRYCODE, (AS)AUTONOMOUS-SYSTEM-ASN, AS-NAME, AS-COUNTRYCODE, AS-DESCRIPTION")
print("search-ip-orgname.py [-h] [--ip | --desc] name")
print("(--ip) consente di stampare solo ip mentre (--desc) permette di stampare ip con descrizione")
print("****************************")
#creazione del parser

parser = argparse.ArgumentParser(description='Lista di ip dato un nome di Organizazzione')
parser.add_argument("name", type=str ,help="Organizzazione da ricercare")
group = parser.add_mutually_exclusive_group()
group.add_argument("--ip", help="Stampa solo ip", action="store_true")
group.add_argument("--desc", help="Ip con descrizione", action="store_true")
args = parser.parse_args()

#definizione API di accesso. Il file chiavi contiene UID e SECRET rilasciati dall'account di Censys

API_URL = "https://censys.io/api/v1"
UID = chiavi.UID
SECRET = chiavi.SECRET

#inserire l'organizzazione da ricercare

data= args.name
p=1

#prima richiesta per determinare il numero di pagine di risultati

params = {
    "query":"443.https.tls.certificate.parsed.issuer.organization: " + data,
}

res = requests.post(API_URL + "/search/ipv4", json= params, auth=(UID, SECRET))

if res.status_code != 200:
    print("Errore : "+ str(res.status_code))
    sys.exit(1)

payload = res.json()
pages = payload['metadata']['pages']


#per ogni pagina stampa i risultati

if args.ip:
    while p <= pages:
        time.sleep(0.5)
        params = {
            "query": "443.https.tls.certificate.parsed.issuer.organization: " + data,
            "page": p,
            "fields": ['ip']
        }
        res = requests.post(API_URL + "/search/ipv4", json=params, auth=(UID, SECRET))
        p = p + 1
        n = 0
        payload = res.json()
        print(payload)

if args.desc:
    while p <= pages:

        time.sleep(0.5)
        params = {
            "query": "443.https.tls.certificate.parsed.issuer.organization: " + data,
            "page": p,
            "fields":['ip','autonomous_system.asn','autonomous_system.country_code',
                      'autonomous_system.description','autonomous_system.name',
                      'location.country','location.country_code']
        }
        res = requests.post(API_URL + "/search/ipv4", json=params, auth=(UID, SECRET))
        p = p + 1
        n = 0
        payload = res.json()
        print(payload)
