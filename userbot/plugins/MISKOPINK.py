
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


 
@mafiaopbolte.on(mafiafightbot(pattern="raid|madarchod"))
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
        RAIDHU = ["bhosadi ke aisa thappad marunga tere muh ke dant gad se hoker girenge", "jija se bkchodi krta hai maderchod tamiz sikh lowde", "gand mei tere sua ghusa ke swetter bna dunga", "Jhant khayega mera behn ke lowde", "teri ammy ka asiq hun wo v khufiya asiq ati hai mujhse chummiya lene apne chut pe", "teri ammy ke gand ko mukka marke tod dunga maderchod baap se bakchodi", "bhagg maderchod teri ammy toh nukkad ki randi hai re", "300 rs wali randi ke olad", "teri behn ko utha ke salwar ke sath hi pelunga", "hahahaha gandu tera baal pakad ke diwal se lada lada ke tera seer phod ke teri ammy ka mang bharunga", "teri ammy ka boxda ka bujiya bana dunga", "gandu rand ki paidais jhantu sale", "loda chusega meraa maderchod sale tatti", "teri ammy ke muh pe mut ke bhag jaunga maderchod", "tu mera beta hai mai tera baap hun teri ammy roz chudwati hai mujhse", "baap se batmizi krega behnchod", "chuchi bada ke dudh pee jaunga teri ammy ki", "thuk laga ke pelunga sale maderchod bakchodi kiya toh", "muh pakad ke pattar se lada lada ke maar dalunga teri ammy ko", "baap se aya tha ladne mera beta randi ka bachha sala", "gandu tere ammy ke chut mei ghus ke dipawali manaunga", "diwali ke din jis chunne se ghar pent krte hai usi se tere ammy ki gand lal krke pelunga", "tere bua ke boxde mei lux saboon dal ke chodunga randi ke olad", "LPG mei aag laga ke tere ammy ke boxde mei fenk dunga ayr bhag jaunga andar jaker fatega aur teri ammy ka boxda chithda ud jayega", "teri behn ko date pe lejaunga aur cold drink mei apna moot mila dunga fir pilaunga usko", "teri ammy ko saki saki gaane pe nachwa ke pelunga kacha kach", "tu boxdi ke guh khane wala insan hai teri ammy bhi bade chaw se mera guh khati hai", "aisa chodunga na jhant ke chore teri maa ko "]  
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
        RAIDHU = ["T3R1 4MMY K3 B0XDE M3 MUT DUNG4", "B44P HU T3R4 M4D3RCH0D", "T3R1 B3H3N KO N4CH4 N4CH4 K3 P3LU", "G4NND M3 G0L1 M4RUNG4 T3R1 B3HN K3", "GARAM PANI SE TERI AMMY KI CHUCH1  J4L4 DUNG4", "TERI AMMY K3 G4ND M3 S4NP DALU", "BEHN T3RI R4ND1 AMMY T3R1 NACH4NIYA", "KUHANI M44R K3 TERI AMMY K1 PEETH T0D DUNGA", "SU4RCH0D L0DU AUK44D BANA", "HATH T0D DUNGA T3R1 AMMY KE", "SUN TERI AMMY KA BOXDA MEI MUT KE BHAG JAUNGA AUR TU KUCHH NA KAR PAYEGA MADERCHOD", "BAAP HU TERA LODA PAKAD KE NAMASTE KAR MADERCHOD", "JHANTU GAANDU BAAP SE LADEGA TU AB ITNI AUKAAD HOGYI TERI MADERCHOD", "GAWAR SALE LAGTA HAI BACHPAN MEI TERI AMMY RANDI KHANE MEI CHUDWA KR TUJHE PAIDA KIYA THA ISLIYE ITTA HARAMI PAIDA HUA HAI SALA HAZAR BAAP KI OLAD", "TERI BEHN KA EK EK JHANT NOCH KE USI KE MUH PE LAGA DUNGA AUR MUH MEI LIDA DAL KE AISA PELUNGA AISA PELUNGA KI MUH SE ULTIYA KREGI MADRCHOD", "HAAthI CHALI BAZAR MEI TERI AMMY CHUDI HAZAR MEI", "LODA KE PASENE SALE JHANTU", "HATH DAL KE TERI AMMY KA BOOR FAAD KE BABA RAM RAHIM KA GUFA BANA DUNGA", "DARWAJE KE KUNDI MEI TERI AMMY KA HATH LAGA JE DARWAJA BAND KRDUNGA", "TERI BEHN KA CHOTI APNE LODA SE GANDA KR DUNGA AUR WAHI LODA USKO MUH MEI DAL DUNGA", "Behnch0d baap se mat ulajh gand mei danda dal ke tod dunga", "Jyada bak bak kiya toh muh se l0da dal ke tere gand se fadte huye nikaluga", "Jhant jaisi sakal leke jyada itra mat jhantu", "Aisa pelung Tujhe ki zindagi bhar allah ko boleega ki duniya mei kyu bheja", "mahine mei 12000 tareeke se teri ammy ka ch00t jhadunga", "Study table pe baitha ke kach kach pelunga tere maal ko", "Ek tang se rassi bandh ke nanga  ulta latka dunga madharch0d jyada udd mat", "Thand mei teri ammy ko. Thande paani mei duba duba ke muh mei dunga", "Teri behn ko bolunga ki mere liye paani lao aur jb wo paani lene ke liye jhukegi tbi peeche se utha ke pel dunga", "Pairasuit se girte huye tere muh mei moot dunga behn ke l0nd "]  
        counter = int(cat[0]) 
        for _ in range(counter): 
            reply = random.choice(RAIDHU) 
            username = random.choice(user) 
            caption = f"{username} {reply}" 
            sandy = await event.client.send_message( 
                event.chat_id, caption 
            ) 
            await asyncio.sleep(sleeptimem)