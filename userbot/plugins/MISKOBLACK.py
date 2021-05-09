
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


 
@mafiaopbolte.on(mafiafightbot(pattern="raid|loda"))
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
        RAIDHU = ["Teri behn ki ch00t mei charger dalke charge krdunga fir pelunga kacha kach", "teri ammy ki ch00t mei dumbble leke ghus jaunga aur workout krunga", "sale corona ke lockdown mei paida hua juja behn ka loda", "teri ammy ke ch00t mei pullup krunga", "teri nani ki ch00t mei ghus ke quarantine mei baith jaunga gand ke guh bhosadi ke", "chai ka glass fenk ke marunga teri ammy ka gand fut jayega", "teri ammy atma nirbhar ni mere l0nd pe nirbhar hai behnch0d", "gandu behnch0d sale bhosadi ke lanth g4nd ki paidais behnch0d", "jhingoor ki aulaad hai tu", "Teri ammy ko wheel wali kursi pe baitha ke ch0dunga kacha kach", "landbhature ki aulaad sale", "teri ammy ke b00r ka baal se tera gala daba ke maar dalunga", "tiktok ke chuchidhari betich0d", "nipple nikal ke teri ammy ka peechwade pe laga dunga", "tatti khor hai tu sale apni tatti chatne wala suar hai tu", "chachundar sale badbudaar prani behnch0d", "g@nd mei teri belan dal ke faad dunga usme se khun hi khun niklega lawde", "insta pe live ch0dunga tere nani ko patak patak ke", "chakke ki nasal behnch0d gandmari ke pille", "Teri ammy ke bh0xde mei lucents ki book daal ke ch0dunga", "teri behn ki ch00t madharch0d tere ammy ke ch00t mei 303 se gusa ke goli marunga", "tere ammy ke g0nd mei guldasta ghusa ke ch00t marunga", "teri ammy ko mai tb se ch0dra hun jb mai class 12 mei tha m4dharch0d", "g4ndu bsd k baap se ladega tu tere bahin ke b00r mei fadi hui dahi dal ke chatunga", "takiya se muh daba ke pelunga teri behn ko taki koi sun ke pelne na ajaye ni toh teri behn ko g4ng b4ng krna pad jayega", "sale sadi hui ch00t ke jh4nt ke dheel", "suna hai tu bahut bada mafia hai , lagta hai teri ammy meri r4khail thi", "sale haiwan se chud1 hui auraat ke aulaad", "teri ammy ke ch00t pe sanitizer laga ke ch0dunga "]  
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
        RAIDHU = ["Teri ammy ke boxde mei covid 19 ka virus", "corona ke mariz banke pelunga tere ammy ko aur apne sath uper v leke jaunga waha v ch0dunga kacha kach", "mere moot se banta hai covid 19 ka ilaj lejake apne saare gharwalon ko pila sab swasth ragenge", "sale bhadwech0de r4ndi ke r4ndpane se nikle aulaad", "chal na chhinal ki aulaad tere muh mei nirma powder dalke moot dunga", "sale gandu ki eklauti aulaad gand ke paseene se uge huye beej", "teri ammy ko dis tv ke chhatri pe baitha ke pelunga", "pure lockdown mei teri ammy ko ch0da tha", "tere ammy ke bhoxd3 mei lockdown krwa dunga jhant ke kide", "sale jhadi hui choot ke safed gandagi", "memech0du bh0sadi ke r@nd ki paidais", "teri ammy ke bh0sade mei dslr dal ke photo khechunga kutiya ku aulaad saale", "muh se hagne wala prani hai tu jh@nt ke baal saale", "teri g@nd mei jalta hua kerosin dal dunga behnk3lod3", "gaadi ke neeche teri behn ki ungliyon ko rakh ke uper se caar chala dunga", "l@nd se shower lene wali r@nd ki aulaad hai tu", "teri ammy ek baar pakdi gyi thi r@ndi khane mei", "call girls hai n teri behn mai roz baat krta hun usse nokia 3310 se", "chrome khol aur apni ammy ka naam dal p0rnhub pe pehli video usi ki hai dekh", "emojichoda bsd ka l@nd piyega tu mera ab", "sun bey bulbul ki aulaad gand maar ke chhura bhonk dunga teri gand mei", "tu hai ek number ka jhantu aur teri gand hai mastani maar maar ke bana dunga teri ammy ko apna deewani", "teri ammy ke gand mei JNU ka sara sperm dal dunga soch kitne bachhe nikalenge tarah tarah ke", "jamiya university ke students se bhi chudwati hai teri ammy kya ghuma ghuma ke gand leti hai teri ammy re", "sale aisa thappad marunga na ki teri ammy ko gand ki nase fat jayengi", "akansha ki film mei jaise chudai hoti hai waise hi chodunga teri ammy ko", "board ke exam mei baitha ke chodunga kacha kach kach", "chal na chutiye teri behn ka yaar hun mai jija ji bol bhi de ab", "sale super man ki tarah hawa mei udke chodunga teri ammy ko", "spider man ki tarah latak ke bhi pelunga aur usi tarah chumma bhi lunga teri behn ko "]  
        counter = int(cat[0]) 
        for _ in range(counter): 
            reply = random.choice(RAIDHU) 
            username = random.choice(user) 
            caption = f"{username} {reply}" 
            sandy = await event.client.send_message( 
                event.chat_id, caption 
            ) 
            await asyncio.sleep(sleeptimem)
