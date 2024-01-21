# PiHoleV5 to Telegram

## Juste un simple bot Telegram pour Pi-Hole

Site officiel de Pi-hole : https://pi-hole.net/

Créer un bot telegram depuis [BotFather](t.me/botfather). (Si vous n'êtes pas familier avec les bots Telegram et le t'chat, lisez la [documentation](https://core.telegram.org/bots)).

###### Télécharger juste ces fichiers :
`pihole2telegram.py`
`config.py`
`keyboard.py`
`parse.py`

Ou cloner ce repository :
```bash
git clone https://github.com/FleuryK/piholev5-to-telegram.git
```

###### Installer les packages requis :

```bash
pip3 install -r requirements.txt
```
ou
```bash
pip3 install python_telegram_bot
pip3 install request
```

### Utilisation

Insérer TOUTES vos données dans `config.py`

Exemple :

```python
# Token du Bot Telegram
TELEGRAM_BOT_TOKEN = "XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# ID de l'utilisateur avec tous les accès
TELEGRAM_USER_ID = ["XXXXXXXXX"]

# Adresse Web de l'API du Pi-Hole
ADRESSE_API_PIHOLE = "https://adresse.du.pi.hole/admin/api.php"

# Token d'API du Pi-Hole. Cela se trouve dans "Settings" puis l'onglet "API" et
# cliquer sur le bouton "Show API" puis sur "Oui"
TOKEN_API_PIHOLE = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Nombre d'entrées à retourner pour affichage
ENTREE_PIHOLE = "10"
```

Executer : pihole2telegram.py

#### Bot testé sur :
- Debian 11
- Pi-Hole v5.17.3
- AdminLTE v5.21
- FTL v5.24