# IT-MLog (CLI + GUI)

See projekt on loodud Pythoni õppeaine raames. Rakendus võimaldab hallata IT-tööde ja hoolduste logisid (nt arvuti parandamine, tarkvara paigaldus jne).

## Funktsionaalsus

- **Logikirjete haldamine**: Lisamine, kuvamine, staatuse muutmine (OPEN/DONE) ja kustutamine.
- **Andmete valideerimine**: Pealkiri peab olema vähemalt 4 ja kirjeldus vähemalt 10 tähemärki pikk.
- **Andmete salvestamine**: Kõik andmed salvestatakse automaatselt JSON-faili (`logbook.json`).
- **Otsing ja filtreerimine**: Võimalus leida kirjeid märksõna või staatuse järgi.
- **Kaks kasutajaliidest**: 
  - Konsooliliides (CLI) kiireks tööks.
  - Graafiline liides (GUI) Tkinteriga mugavaks kasutamiseks.
- **Importimise test**: Vigaste andmetega failide importimise tugi koos vigade logimisega (`import_errors.log`).

## Failistruktuur

- `main.py` – Rakenduse käivitusfail (valik CLI ja GUI vahel).
- `models.py` – Andmemudel (`LogEntry` klass) ja valideerimise loogika.
- `logic.py` – Äriloogika (`LogBook` klass), andmete töötlemine ja JSON-i haldus.
- `cli_ui.py` – Konsoolipõhine kasutajaliides.
- `gui_ui.py` – Graafiline kasutajaliides (Tkinter).

## Kasutamine

Programmi käivitamiseks sisestage terminalis:

```bash
python main.py
```

Pärast käivitamist saate valida, kas soovite kasutada konsooli- või graafilist liidest.

## Nõuded süsteemile

- Python 3.x
- Tkinter teek (tavaliselt Pythoniga kaasas)

