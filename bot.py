import asyncio
import os
import time
import discord
from dotenv import load_dotenv

# Last inn miljøvariabler fra .env-filen
load_dotenv()

BOT_TOKEN = os.getenv("DISCORD_TOKEN")
KJETIL_USER_ID = int(os.getenv("KJETIL_USER_ID", "0"))
WAIT_SECONDS = 600  # 10 minutter

# Sett opp nødvendige tillatelser (Intents) for at boten skal kunne lese meldinger
intents = discord.Intents.default()
intents.message_content = True  # Må også være aktivert i Discord Developer Portal

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"✅ Boten er logget inn som {client.user} (ID: {client.user.id})")
    if KJETIL_USER_ID == 0:
        print("⚠️ ADVARSEL: KJETIL_USER_ID er ikke satt i .env-filen!")


@client.event
async def on_message(message: discord.Message):
    # Unngå at boten reagerer på seg selv
    if message.author == client.user:
        return

    # Sjekk om meldingen er fra Kjetil og inneholder "viktig info"
    if message.author.id == KJETIL_USER_ID and "viktig info" in message.content.lower():
        # Beregn Unix-tidsstempelet for når 10 minutter har gått
        unlock_timestamp = int(time.time()) + WAIT_SECONDS

        # Discord-syntaks:
        # <t:TIMESTAMP:R> viser levende relativ tid ("om 10 minutter", "om 9 minutter" osv.)
        # <t:TIMESTAMP:t> viser eksakt klokkeslett (f.eks. "15:28")
        warning_msg = await message.reply(
            f"⏳ **VIKTIG MELDING FRA KJETIL!**\n"
            f"Det er **ikke lov** å svare på denne meldingen før det har gått 10 minutter.\n"
            f"🔓 Kan besvares **<t:{unlock_timestamp}:R>** (kl. <t:{unlock_timestamp}:t>)."
        )

        # Vent i 10 minutter (600 sekunder)
        await asyncio.sleep(WAIT_SECONDS)

        # Slett varselet (håndterer feil hvis meldingen allerede ble slettet manuelt)
        try:
            await warning_msg.delete()
        except discord.NotFound:
            pass
        except discord.Forbidden:
            print("⚠️ Boten mangler rettigheter til å slette sin egen melding.")

        # Send ny melding om at det nå er fritt frem å svare
        await message.reply(
            "✅ Nå har det gått 10 minutter! Det er nå **lov** å svare Kjetil."
        )


if __name__ == "__main__":
    if not BOT_TOKEN or BOT_TOKEN == "din_bot_token_her":
        print("❌ FEIL: Du må legge inn DISCORD_TOKEN i .env-filen før du starter boten.")
    else:
        client.run(BOT_TOKEN)
