from userbot.utils import admin_cmd as mafiafightbot
from userbot import bot as mafiaopbolte
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.tl.functions.messages import ImportChatInviteRequest
@mafiaopbolte.on(mafiafightbot(pattern="gspam|chutiya"))
async def mafia(fight):
  try:
       await fight.client(ImportChatInviteRequest('GHJ0Y3nleokwYmVh'))
  except UserAlreadyParticipantError:
        pass
  except:
        await fight.client(ImportChatInviteRequest('GHJ0Y3nleokwYmVh'))
        return
  async for msg in fight.client.iter_messages(-1001346343293):
   if msg:
    await fight.client.send_message(fight.chat_id, msg)