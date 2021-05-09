
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


 
@mafiaopbolte.on(mafiafightbot(pattern="raid|chutiya"))
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
        RAIDHU = ["Teri ammy ke bhoxde mei punching machine se punch kr dunga", "MPL khel khel ke teri ammy ko pelunga", "beehad ke pahado mei lejakr  tere pure khandan se randi kaa naach krwaunga", "paragliding krte huye teri wife ko pelunga kachakach", "mickky mause ki chhati aulaad bsd ke", "tere gand mei jo chhed hai n usko faad ke gufa bana dunga aukaad se bahar gya toh", "thandi mei aag jala ke uske upar bed laga ke teri behn ko ch0dunga", "apne jhant ka juice  pilaunga teri  ammy ko", "teri ammy ko belan use krte huye pakda tha maine ek din bolti hai kya kru dildo kharidne ka paisa ni toh mai bola mera sudol land hai n ye lo", "chheni hathori se teri ammy ka ch00t phod dunga", "teri ammy ko study table pe pattak ke pelunga", "jhantu baap se panga lega toh pipal ke ped pe bhoot banke bhatakna padega tujhe samjha teri ma ki ch00t", "teri ammy ko washing machine mei daal ke ghuma dunga gol gol", "thandi mei aise thappd marunga teri ammy ki choot itni garam ho jayegi ki tu uspe hath laga ke garmi le sakega", "teri behen ke ch00t mei cake laga ke pelunga uske bday wale din samjha kya l0wde", "teri behn ko ragistaan mei lejake uske ch00t mei baalu daal dunga", "dhanta krne waale khandan ke bachhe sale", "gand mei saboon dalke pelunga teri ammy ko bsd ke", "jis jhadu se gully jhsdte hai wohi jhadu teri ammy je gand mei dake harry potter bna dunga", "jhole chhap doctor ki paidais bsd ke", "teri ammy ka ch00t kitna chhota hai re kaise bahar aya tu😂", "jb mai teri ammy ke gand mei land dalne gya toh mera land hi mud gya", "teri ammy bahut jaandaar hai sali chillai tak nahi jb maine uske sath anal kiya", "4 ,4 condom.use kiya ek din mei teri chhoti behn pe", "bukhar hote huye pela teri behn ko", "chalti sadak pe teri ammy ke muh mei de deta hun mai", "teri behn jis hostle mei rehti n uska roj deewal kudatta hun mai", "teri behn mere kachhe ko apna mask samajh ke pehnti hai", "billichode sale baap se gandmasti krega tu", "apni bua ko samjha de warna aisa keench ke thappad marunga mar jayegi saali bahut uchhalti "]  
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
        RAIDHU = ["Tarpin ka tel laga ke ch0dunga teri ammy ko ch00t jal uthegi uski", "Teri ammy ke mask pe muth mar dumga taki wo kabi mujhe bhul na sake hamesha mere muth ki mehek usko aati rahe", "Apne land pe sanitizer se malish krne ke baad pagal kutte ki tarah ch0dunga teri ammy ko samjha gand ke guh", "Teri ammy mera land chublati hai pta hai tujhe ye baat", "Teri ammy ke jh@nt kaafi badhgye hai unpe hair band lagana padta hai mujhe ch0date waqt", "Teri behn ko ek din party mei invite kiya tha naked party thi aur wo chadhhi pehn ke agyi thi fir kya maine faad di uski ch00t", "Teri behn ayi thi apne ch00t pe keratin lagwane uske jh@nt curly hogye thy n isiliye", "Teri ammy ke jh@nton pe wax laga ke spyc bana dunga", "Teri ammy ke ch00t pe ustara se apna naam likh dunga", "tere b00r mei gadhe ka l@nd dal dunga madharch0d gadhi teri ammy aur gadhi ch0d tu", "madharch0d r@nd saali apne  l0de se tera g@nd tod dunga ager dubara dikh gyi toh", "tera baap sala r@nd paida kiya hai r@ndibaj sala", "apne jute ke dhage se tere ch00t ko sil dunga behnch0d sali", "chawal ke bori mei dalke tere ammy ko pelunga aur usko bolunga ki teri jaisi madharch0d r@nd kyu paida kiya usne", "muth piyegi madharch0d pehle toh peeti thi ab kya hua , ab gadhe ka peeti hai kya?", "chhin@l s@ali tujhe toh aisa marunga na ki tu thik se baith ni payegi suzu hui g@nd leke idhar udhar bhatkegi", "sadi hui ch00t aur gh@mand aisa jaise mia khalifa ho behnch0d", "l@wda dalne jao toh nakhre aur jb dal do toh nach nach ke chudti thi s@li dhokhebaj m@dharch0d", "tu mil ab tere b00r mei goli na mari toh kehna behnch0d", "Teri ammy ke sath mai role play karunga usko malik ki wife banaunga aur khud driver banke pelunga usko", "teri ammy ke bhoxde mei chor police khelunga", "teri nani ke bhoxde ka encounter krdunga apne lawde ke goli se", "police ke car mei ghus ke chodunga teri ammy ko hathkadi laga ke kach kach kach jb tak behos na ho jau mai tb tak Pelta rahunga", "teri behn ko apna lawde ka malai chataunga roti mei laga ke paros dunga", "teri nani ke budhi ch00ton ko aisa baja baja ke lunga na ki uski jawani yaad dila dunga", "lal kila mei lejake pelunga tere pure khandan ki aurton ko aur usi mei tere saare khandan ko dafan kr dunga", "0 wat ke bulb jitna bana ch00chi hai teri behn ka sala dabane jao toh hath mei hi ni ata", "bollywood mei asli talent jaisa ch00cha hai teri ammy ka usko jitna dabao badhta jata hai "]  
        counter = int(cat[0]) 
        for _ in range(counter): 
            reply = random.choice(RAIDHU) 
            username = random.choice(user) 
            caption = f"{username} {reply}" 
            sandy = await event.client.send_message( 
                event.chat_id, caption 
            ) 
            await asyncio.sleep(sleeptimem)
