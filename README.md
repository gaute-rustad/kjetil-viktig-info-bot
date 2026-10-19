# Kjetil "Viktig Info" Discord-bot ⏳

Denne boten overvåker meldinger fra Kjetil. Hver gang han skriver en melding som inneholder `"Viktig info"` (uavhengig av store/små bokstaver), svarer boten med et varsel og en **levende nedtelling** på 10 minutter. Når de 10 minuttene har gått, slettes varselet automatisk og erstattes med en melding om at det nå er lov å svare.

## Oppsett

1. **Installer pakkene:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Konfigurer `.env`:**
   Åpne filen `.env` og fyll inn:
   - `DISCORD_TOKEN`: Bot-tokenet ditt fra [Discord Developer Portal](https://discord.com/developers/applications) (husk å skru på **Message Content Intent** under *Bot*-fanen!).
   - `KJETIL_USER_ID`: Bruker-ID-en til Kjetil (høyreklikk på Kjetil i Discord med *Utviklermodus* på -> *Kopier bruker-ID*).

3. **Start boten:**
   ```bash
   python bot.py
   ```
