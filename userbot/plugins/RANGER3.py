
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
        RAIDHU = ["Teri behn ke boor mei nariyal ka ped", "Teri ammy ko golamber mei ghuma ghuma ke chodu", "Jhant ke kide gandu ki paidais sale rand ki olad", "BHU university mei nanga krke pelunga teri behn ko", "Road pe jalne wali light jalwa ke chudwati hai teri ammy bina condom ke", "Ek kapde pe muth marunga fir uss kapde ko teri ammy ke muh mei thus ke apna bada wala lund dalunga taki jb chillaye toh awaje na nikle aur padosi na jag jaye*, "Tere ammy ke boxde mei notepad dal ke boxda faad dunga", "Poncha lagwaunga teri ammy se apne pure ghar mei aur jb mn tb pelunga", "Rangoli bnwate time bhi pelunga pura rangoli bigad jayega", "narangi colour se rang dunga teri ammy ka choot behn ke lode", "Teri ammy ke boxer mei hayabusa leke ghus jaunga", "Teri behn ke bhosade mei taddy dal dunga", "Charger ki aulaad behnchod sale gandu", "Teri ammy ke boxde mei mic dal ke chodunga dhak dhak ki awaj record hogi
Fir wo sound tere whatsapp pe bhejunga", "Bokachoda bhaisa choda bhosadi ke lanth sale", "Teri gf ke bhosade mei parda tangne wala danda dal dunga sali orgasm se pagl ho jayegi", "Teri behn ko jeans pehna ke chodunga  aur uski jeans ke chain mei uski chut laga ke band krdunga ah ah chillayegi", "Sale bawasir wale gand ki paidais bhosadi ke", "Teri behn ki gand mei gilahri dal ke chhor dunga aur wo sb andar jake kategi teri behn ki gand ko jb subeh hagne baithegi toh khun billega aur mari hui gilahri", "Teri behn mujhse chudwati hai belt dilwaya tha n usko usi din usne bola paisa nahi hai lekin badle mei aap meri chhoti si chut pe sakte hai", "Gand mei teri ammy ke bajaj ka bullet dalunga", "sabji lane wale jholi mei teri ammy ki chuchi kat ke le ke bhag jaunga", "tere ammy ki ungaliyan tod ke tere baap ke gand mei dal dunga", "sehnaz ki chuchi tere behn jaisi hai badi badi bigg boss wali", "tere ammy ke chut pe chini dal ke chatunga", "deepawali mei lagane wali electric battiyan tere behn ke chuchi se latka dunga aur fir chodunga kach kach", "tere ammy ke chut pe nariyal phodunga", "bawasir ke time paida hua tha tu betichod", "margo saboon laga ke chodunga teri ammy ko taki muth ki mehek na aye", "ghadi ke kante tere behn ke chuchi mei gada ke dudh nikal lunga sara aur pichka dunga "]  
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
        RAIDHU = ["Tere ammy ko pornstar bana dunga betichod", "chuchhi ko pagal kutte se katwaubga tere behn ki", "parda laga ke chodunga tere ammy ke chut pe", "tere ammy ka chut kat kat ke bag mei bharke ghar lekar chala jaunga fir chodunga", "straighner se tere ammy ki jhantein straigh kr dunga fir chodunga", "muh mei canvas ka ball dal ke gand mei lund lagaunga tere wife ki", "khud hi jeans pehnaunga tere ammy ko aur khud hi fadunga fir chodunga  pura mood bana ke", "ager chodate waqt teri ammy chillai ni na toh sua bhonkunga uske chutad pe", "tere ammy ka yovan mei badh la dunga mai bete", "kabootar ka dana tere ammy ke gand mei dalunga fir kabootar usko usi mei se nikal ke khayenge", "Teri ammy ke bhosade mei jalta hua suraj dal dunga madharchod", "Behn ke chut mei teri lED bulb fit krdunga", "Ett fenk ke marunga betichod tere baap ka seer phod dunga aur gand tod dunga", "Arz kiya hai, Chut hota hai kala kala, Choot hota hai kala kala, Mai tera jija tu mera sala", "Teri ammy ke boor mei jio ka tower lagawunga taki mere phone ka network hamesa bana rahe", "Sale kabootar ki gand chatne wale lodu ki olad", "Gilahri choda betichod jhant ke baal teri ammy ko gilahri ne choda hai betichod", "Teri ammy ke bhosde mei kali wali pani ki tanki dal dunga 5000liter wali", "Sale chudi hui rand ke chhati olad betichod gandu ki paidais", "Teri ammy ke boor mei gehu dalunga aur gand mei se ata nikalunga fir usi ka roti bana ke tere ko khilaunga", "Tere ammy ke boxde pe ring guard laga ke pelunga", "Tere behn ki gand mei haldi ram ki namkin dal dunga bsd ke", "Sale nasedi ki aulad haram ke pille jhantu", "tere ammy ke boxde mei markar laga ke hilight krdunga", "Itni majboot tarike se pelunga na ki khoon bach bach krke bahar ayega tere pure khandan ke bund se", "whatsapp pe chudi hui randi ki olad bsd ke", "teri ammy x video pe upload krti hai na apna video wo mask pehn kar maine usko uski chuchi se pehchana", "gandeli road ke chhinar ke chhati olad gand marunga tera mai ab", "galat panga le raha hai tu bete abhi bhi wqt hai apni ammy ko sarso ke tel ke sath bhej mere paas sayad maaf krdu tujhe", "tere ammy ke boxde mei tajmahal bana dunga sale chhinala krne wale aurat ke bachhe "]  
        counter = int(cat[0]) 
        for _ in range(counter): 
            reply = random.choice(RAIDHU) 
            username = random.choice(user) 
            caption = f"{username} {reply}" 
            sandy = await event.client.send_message( 
                event.chat_id, caption 
            ) 
            await asyncio.sleep(sleeptimem)
