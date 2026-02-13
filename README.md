# IT-MLog (CLI + Argument Management)

IT-MLog on Pythonis loodud IT hoolduspäevik, mis võimaldab hallata tehnilisi logisid nii interaktiivse menüü kui ka kiirete käsurea käskude abil.

## Põhifunktsioonid

- **Lühikesed ID-d**: Kirjete haldamine on tehtud lihtsaks tänu numbrilistele ID-dele (1, 2, 3...).
- **Automaatne salvestamine**: Kõik muudatused salvestatakse koheselt `logbook.json` faili.
- **Nutikas tabelivaade**: CLI tabel piirab pikkade kirjelduste kuvamist, et vältida teksti purunemist ekraanil.
- **Argumentide tugi**: Võimalus sooritada tegevusi otse programmi käivitamisel ilma menüüd avamata.
- **Vigade logimine**: Testfailide importimisel tekkivad vead salvestatakse faili `import_errors.log`.

## Käivitamine ja kasutamine

Programmi saab käivitada kolmel viisil:

### 1. Interaktiivne menüü
Tavaline režiim koos selgitava menüüga:
```bash
python main.py
```

### 2. Kiirkäsud (Arguments)
Kasuta otse käsurealt kiireks tegutsemiseks:
- `python main.py list` – kuvab koheselt kõik logid ja sulgub.
- `python main.py add` – avab koheselt uue kirje lisamise dialoogi.

### 3. Graafiline liides (GUI)
Kuigi põhirõhk on suunatud CLI võimekusele, saab graafilise liidese käivitada järgmise käsuga:
```bash
python main.py gui
```

## Failistruktuur

- `main.py` – Programmi sisenemispunkt (argumentide töötlemine).
- `models.py` – `LogEntry` klass ja andmete valideerimine.
- `logic.py` – `LogBook` klass, andmete haldus ja automaatne salvestamine.
- `cli_ui.py` – Kasutajaliides konsooli jaoks (tabeli vormindamine ja pausid).
- `gui_ui.py` – Graafiline kasutajaliides (Tkinter).

