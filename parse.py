import requests
import config

url = config.ADRESSE_API_PIHOLE
token_api_pihole = config.TOKEN_API_PIHOLE
entries = config.ENTREE_PIHOLE

num1 = '={0}'.format(entries)
bold = '*'


def genstats():
	r = requests.get(url + '?summary&auth=' + token_api_pihole).json()
	domains_blocked = r['domains_being_blocked']
	dns_queries = r['dns_queries_today']
	ads_blocked = r['ads_blocked_today']
	ads_percentage = r['ads_percentage_today']
	message = str(bold + "🌍 Requêtes : " + bold + str(dns_queries) + "\n" +
				  bold + "✋ Pubs bloqués : " + bold + str(ads_blocked) + "\n" +
				  bold + "📊 Pourcentage des pubs : " + bold + str(ads_percentage) + "%" + "\n" +
				  bold + "🌐 Total domaines : " + bold + str(domains_blocked))
	return message

def top_it(tops, *args):
	r = requests.get(url + '?' + tops + num1 + '&auth=' + token_api_pihole).json()
	if tops == "topItems":
		for y in args[:1]:
			if y == 1:
				try:
					top_queries = r['top_queries']
					str1 = ""
					for x, value in top_queries.items():
						str1 += str("" if str1 == "" else "") + str(x) + " : " + str(value) + '\n'
					message = str(bold + "🌍 Top requêtes :" + bold + "\n" + str1)
					return message
				except AttributeError:
					message = str(bold + "🌍 Top requêtes :" + bold + "\n" + "Vide")
					return message
			elif y == 2:
				try:
					top_ads = r['top_ads']
					str1 = ""
					for x, value in top_ads.items():
						str1 += str("" if str1 == "" else "") + str(x) + " : " + str(value) + '\n'
					message = str(bold + "⛔ Top pubs :" + bold + "\n" + str1)
					return message
				except AttributeError:
					message = str(bold + "⛔ Top pubs :" + bold + "\n" + "Vide")
					return message
	else:
		try:
			top_sources = r['top_sources']
			str1 = ""
			for x, value in top_sources.items():
				str1 += str("" if str1 == "" else "") + str(x) + " : " + str(value) + '\n'
			message = str(bold + "👤 Top clients :" + bold + "\n" + str1)
			return message
		except AttributeError:
			message = str(bold + "👤 Top clients :" + bold + "\n" + "Vide")
			return message

def check_status(status):
	if status == 'status':
		r = requests.get(url + '?' + status + '&auth=' + token_api_pihole).json()
		cstatus = r['status']
		if cstatus == 'enabled':
			message = str(str(cstatus) + " ✅")
		else:
			message = str(str(cstatus) + " ❌")
	else:
		r = requests.get(url + '?' + status + '&auth=' + token_api_pihole).json()
		if status == 'enable':
			cstatus = r['status']
			message = str(str(cstatus) + " ✅")
		else:
			cstatus = r['status']
			message = str(str(cstatus) + " ❌")
	return message


# TODO Tempoary disable pihole : 30sec, 1m, 5m, 30m.