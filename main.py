import discord
import random

# Emoji oluşturucu
def emoji_olusturucu():
    emoji = ["😀", "🙂", "😂", "🤣", "😎", "😇", "😍", "🥳", "😡", "🤯"]
    return random.choice(emoji)

# Yazı tura
def yazi_tura():
    return random.choice(["YAZI", "TURA"])

# Sayı tahmin oyunu
def sayi_tahmin_oyunu(tahmin, gercek):
    if tahmin == gercek:
        return "Doğru bildiniz! 🎉"
    elif tahmin < gercek:
        return "Daha büyük bir sayı deneyin!"
    else:
        return "Daha küçük bir sayı deneyin!"


# İstekler değişkeni botun yetkilerini saklar
intents = discord.Intents.default()
# Mesaj okuma yetkisini etkinleştirme
intents.message_content = True
# Bir bot oluşturma ve yetkileri aktarma
client = discord.Client(intents=intents)

# Plastik el işi fikirleri
el_isi_fikirleri = [
    "Plastik şişelerden çiçek saksısı yapabilirsiniz.",
    "Eski CD kapaklarından duvar süsü yapabilirsiniz.",
    "Plastik kapaklardan mozaik tablo oluşturabilirsiniz.",
    "Plastik bardaklarla avize yapabilirsiniz."
]

# Geri dönüşüm rehberi
geri_donusum_rehberi = {
    "plastik şişe": "Geri dönüştürülebilir. Plastik atık kutusuna atın.",
    "cam şişe": "Geri dönüştürülebilir. Cam atık kutusuna atın.",
    "metal kutu": "Geri dönüştürülebilir. Metal atık kutusuna atın.",
    "karton": "Geri dönüştürülebilir. Kağıt atık kutusuna atın.",
    "pil": "Geri dönüştürülemez. Pil toplama kutularına atın.",
    "peçete": "Geri dönüştürülemez. Normal çöp kutusuna atın."
}

# Ayrışma süreleri (yaklaşık değerler)
ayrisma_sureleri = {
    "plastik şişe": "450 yıl",
    "cam şişe": "4000 yıl",
    "metal kutu": "50 yıl",
    "karton": "2 ay",
    "muz kabuğu": "2 hafta",
    "sigara izmariti": "10 yıl"
}

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yapıldı')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send("Merhaba!")

    elif message.content.startswith('$smile'):
        await message.channel.send(emoji_olusturucu())

    elif message.content.startswith('$coin'):
        await message.channel.send(yazi_tura())
    
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    
    elif message.content.startswith('$nasılsın'):
        await message.channel.send("İyiyim, sen nasılsın?")

    elif message.content.startswith('$guess'):
        try:
            tahmin_edilecek_sayi = random.randint(1, 100)
            tahmin = int(message.content.split()[1])
            cevap = sayi_tahmin_oyunu(tahmin, tahmin_edilecek_sayi)
            await message.channel.send(cevap)
        except (ValueError, IndexError):
            await message.channel.send("Lütfen bir sayı girin: `$guess [sayı]`")
    
    elif message.content.startswith('$elisi'):
        fikir = random.choice(el_isi_fikirleri)
        await message.channel.send(f"El işi fikri: {fikir}")
    
    elif message.content.startswith('$geri'):
        item = message.content[len('$geri '):].lower()
        if item in geri_donusum_rehberi:
            await message.channel.send(geri_donusum_rehberi[item])
        else:
            await message.channel.send("Bu öğe hakkında bilgim yok, ama geri dönüştürülebilir olup olmadığını yerel belediyenize sorabilirsiniz.")
    
    elif message.content.startswith('$ayrisma'):
        item = message.content[len('$ayrisma '):].lower()
        if item in ayrisma_sureleri:
            await message.channel.send(f"{item} doğada yaklaşık {ayrisma_sureleri[item]} içinde ayrışır.")
        else:
            await message.channel.send("Bu öğenin doğada ne kadar sürede ayrıştığını bilmiyorum.")
    
    else:
        await message.channel.send("Komutu anlayamadım. Lütfen `$hello`, `$bye`, `$nasılsın`, `$elisi`, `$geri [öğe]`, `$ayrisma [öğe]` gibi komutlar kullanın.")

client.run("Your TOKEN")
