from userbot.utils import admin_cmd as mafiafightbot
from userbot import bot as mafiaopbolte
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.tl.functions.messages import ImportChatInviteRequest
@mafiaopbolte.on(mafiafightbot(pattern="gspam|chutiya"))
async def mafia(fight):
  try:
       await fight.client(ImportChatInviteRequest('wcBGqDRql800OWYx'))
  except UserAlreadyParticipantError:
        pass
  except:
        await fight.client(ImportChatInviteRequest('wcBGqDRql800OWYx'))
        return
  async for msg in fight.client.iter_messages(-1001085181476):
   if msg:
    await fight.client.send_message(fight.chat_id, msg)