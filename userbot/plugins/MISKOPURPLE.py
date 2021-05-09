
import os 
 
from telethon.errors.rpcerrorlist import UsernameOccupiedError 
from telethon.tl import functions 
from telethon.tl.functions.account import UpdateUsernameRequest 
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest 
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest 
from telethon.tl.types import Channel, Chat, InputPhoto, User 
from telethon.tl.functions.channels import JoinChannelRequest 
from telethon.tl.functions.channels import LeaveChannelRequest 
import asyncio 
import base64 
import random 
from telethon.tl import functions, types 
from telethon.tl.functions.messages import GetStickerSetRequest 
from telethon.tl.functions.messages import ImportChatInviteRequest as Get 
from userbot.utils import admin_cmd as mafiafightbot
from userbot import bot as mafiaopbolte


 
@mafiaopbolte.on(mafiafightbot(pattern="raid|harami"))
async def _(event): 
    if event.fwd_from: 
        return 
    if event.reply_to_msg_id: 
        r_msg = await event.get_reply_message() 
        if r_msg.from_id is None and not event.is_private: 
            await edit_delete(event, "`Well that's an anonymous admin !`") 
            return None 
        user = await event.client.get_entity(r_msg.sender_id) 
        username = (f"@{user.username}") 
        await edit_or_reply(event, f"{username}") 
        RAIDHU = ["Teri behn ke boor mei nariyal ka ped", "Teri ammy ko golamber mei ghuma ghuma ke chodu", "Jhant ke kide gandu ki paidais sale rand ki olad", "BHU university mei nanga krke pelunga teri behn ko", "Road pe jalne wali light jalwa ke chudwati hai teri ammy bina condom ke", "Ek kapde pe muth marunga fir uss kapde ko teri ammy ke muh mei thus ke apna bada wala lund dalunga taki jb chillaye toh awaje na nikle aur padosi na jag jaye", "Tere ammy ke boxde mei notepad dal ke boxda faad dunga", "Poncha lagwaunga teri ammy se apne pure ghar mei aur jb mn tb pelunga", "Rangoli bnwate time bhi pelunga pura rangoli bigad jayega", "narangi colour se rang dunga teri ammy ka choot behn ke lode", "Teri ammy ke boxer mei hayabusa leke ghus jaunga", "Teri behn ke bhosade mei taddy dal dunga", "Charger ki aulaad behnchod sale gandu", "Teri ammy ke boxde mei mic dal ke chodunga dhak dhak ki awaj record hogi Fir wo sound tere whatsapp pe bhejunga", "Bokachoda bhaisa choda bhosadi ke lanth sale", "Teri gf ke bhosade mei parda tangne wala danda dal dunga sali orgasm se pagl ho jayegi", "Teri behn ko jeans pehna ke chodunga  aur uski jeans ke chain mei uski chut laga ke band krdunga ah ah chillayegi", "Sale bawasir wale gand ki paidais bhosadi ke", "Teri behn ki gand mei gilahri dal ke chhor dunga aur wo sb andar jake kategi teri behn ki gand ko jb subeh hagne baithegi toh khun billega aur mari hui gilahri", "Teri behn mujhse chudwati hai belt dilwaya tha n usko usi din usne bola paisa nahi hai lekin badle mei aap meri chhoti si chut pe sakte hai", "Gand mei teri ammy ke bajaj ka bullet dalunga", "sabji lane wale jholi mei teri ammy ki chuchi kat ke le ke bhag jaunga", "tere ammy ki ungaliyan tod ke tere baap ke gand mei dal dunga", "sehnaz ki chuchi tere behn jaisi hai badi badi bigg boss wali", "tere ammy ke chut pe chini dal ke chatunga", "deepawali mei lagane wali electric battiyan tere behn ke chuchi se latka dunga aur fir chodunga kach kach", "tere ammy ke chut pe nariyal phodunga", "bawasir ke time paida hua tha tu betichod", "margo saboon laga ke chodunga teri ammy ko taki muth ki mehek na aye", "ghadi ke kante tere behn ke chuchi mei gada ke dudh nikal lunga sara aur pichka dunga "]  
        input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2) 
        sleeptimet = sleeptimem = float(input_str[0]) 
        cat = input_str[1:] 
        await event.delete() 
        counter = int(cat[0]) 
        for _ in range(counter): 
            reply = random.choice(RAIDHU) 
            caption = f"{username} {reply}" 
            sandy = await event.client.send_message( 
                event.chat_id, caption 
            ) 
            await asyncio.sleep(sleeptimem) 
    else: 
        input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 3) 
        sleeptimet = sleeptimem = float(input_str[0]) 
        cat = input_str[1:] 
        user = input_str[2:] 
        await event.delete()
        RAIDHU = ["MADARCHOD TERI MAA KI CHUT ME GHUTKA KHAAKE THOOK DUNGA 🤣🤣", "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA", "TERI VAHEEN NHI HAI KYA? 9 MAHINE RUK SAGI VAHEEN DETA HU 🤣🤣🤩", "TERI MAA K BHOSDE ME AEROPLANEPARK KARKE UDAAN BHAR DUGA ✈️🛫", "TERI MAA KI CHUT ME SUTLI BOMB FOD DUNGA TERI MAA KI JHAATE JAL KE KHAAK HO JAYEGI💣", "TERI MAAKI CHUT ME SCOOTER DAAL DUGA👅", "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA", "TERE BEHEN K CHUT ME CHAKU DAAL KAR CHUT KA KHOON KAR DUGA", "TERI MAA KI CHUT KAKTE 🤱 GALI KE KUTTO 🦮 ME BAAT DUNGA PHIR 🍞 BREAD KI TARH KHAYENGE WO TERI MAA KI CHUT", "DUDH HILAAUNGA TERI VAHEEN KE UPR NICHE 🆙🆒😙", "TERI MAA KI CHUT ME ✋ HATTH DALKE 👶 BACCHE NIKAL DUNGA 😍", "TERI BEHN KI CHUT ME KELE KE CHILKE 🍌🍌😍", "TERI BHEN KI CHUT ME USERBOT LAGAAUNGA SASTE SPAM KE CHODE" , "TERI VAHEEN DHANDHE VAALI 😋😛", "TERI MAA KE BHOSDE ME AC LAGA DUNGA SAARI GARMI NIKAL JAAYEGI", "TERI VAHEEN KO HORLICKS PEELAUNGA MADARCHOD😚", "TERI MAA KI GAAND ME SARIYA DAAL DUNGA MADARCHOD USI SARIYE PR TANG KE BACHE PAIDA HONGE 😱😱", "TERI MAA KO KOLKATA VAALE JITU BHAIYA KA LUND MUBARAK 🤩🤩", "TERI MUMMY KI FANTASY HU LAWDE, TU APNI BHEN KO SMBHAAL 😈😈", "TERA PEHLA BAAP HU MADARCHOD ", "TERI VAHEEN KE BHOSDE ME XVIDEOS.COM CHALA KE MUTH MAARUNGA 🤡😹", "TERI MAA KA GROUP VAALON SAATH MILKE GANG BANG KRUNGA🙌🏻☠️ ", "TERI ITEM KI GAAND ME LUND DAALKE,TERE JAISA EK OR NIKAAL DUNGA MADARCHOD🤘🏻🙌🏻☠️ ", "AUKAAT ME REH VRNA GAAND ME DANDA DAAL KE MUH SE NIKAAL DUNGA SHARIR BHI DANDE JESA DIKHEGA 🙄🤭🤭", "TERI MUMMY KE SAATH LUDO KHELTE KHELTE USKE MUH ME APNA LODA DE DUNGA☝🏻☝🏻😬", "TERI MAA KI CHOOT ME SUAR KA BOOSDA DAAL DIAAA MAINE", "TERI BHEN KI GAND MAAR KAR ZINDAGI ANDHER KAR DUNGA", "TERI MAA KI CHOOT ME LODA DAAL KAR MOOT DOONGA TO TERI MAA KE MUH SE PANI NILEGA", "TERI BUA MERI SETTING HAI BHAVE", "TERI MAAA KI CHOOOT ME GANJAA DAAL KAR FOOK DUNGA RANDI KE BACCE", "TERI MAA KA AASHIQ HU TERI MAAA KO BACHPAN ME PREGNENT KARDIA THAA ISLIYE TERI MAA JAWAAN HAI BACCHE", "TERI BHEN KI CHOOT ME CORONA VIRUS DAAL DUNGAA", "TERI BHEN KAA BOOSDA FAAD DUNGAA RANDI KE BACCHE", "TERI MAA KI GAND ME AAG LAGAA DUNGAA", "TERI BHEN KO CHOOOD CHOOD KAR MAAR DUNGAAA", "TERI BHEN KO MERE LAUDE PAR BITHAA DE BACCHE", "TERI BHEN KI CHOOT BHOOT TIGHT HAI MERA LAND MUD JATA HAI DALTE WAQT", "TERI MAA KI GAND ME BOMB DAL KAR UDAA DUNGAA TERI MAA KI GAND", "TERI MAA KI RASEELI CHOOT ME MERA MOTA LAMBA LODA", "TERI VAHEEN KO APNE LUND PR ITNA JHULAAUNGA KI JHULTE JHULTE HI BACHA PAIDA KR DEGI👀👯 "]  
        counter = int(cat[0]) 
        for _ in range(counter): 
            reply = random.choice(RAIDHU) 
            username = random.choice(user) 
            caption = f"{username} {reply}" 
            sandy = await event.client.send_message( 
                event.chat_id, caption 
            ) 
            await asyncio.sleep(sleeptimem)
