class script(object):
    START_TXT = """<b>ʜᴇʟʟᴏ {},
ᴍy ɴᴀᴍᴇ ɪꜱ <a href=https://t.me/{}>{}</a>, ɪ ᴄᴀɴ ᴩʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇꜱ , ᴊᴜꜱᴛ ᴀᴅᴅ  ᴍᴇ ᴛᴏ yᴏᴜʀ  ɢʀᴏᴜᴩ ᴀɴᴅ ꜱᴇᴇ ᴍy ᴍᴀɢɪᴄ😇</b>"""
    HELP_TXT = """<b>ʜᴇy  {}
ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʜᴇʟᴩ ꜰᴏʀ ᴍy ᴄᴏᴍᴍᴀɴᴅꜱ.</b>"""
    ABOUT_TXT = """<b>🥱 ᴍy ɴᴀᴍᴇ : {}</b>
<b><b>🕵‍♂ ᴅᴇᴠᴇʟᴏᴩᴇʀ : <a href=https://t.me/MichaelAnjoottiTG><b>🇮🇳 𝐌𝐢𝐜𝐡𝐚𝐞𝐥 𝐀𝐧𝐣𝐨𝐨𝐭𝐭𝐢 𝐓𝐆</a></b>
📚 ʟɪʙʀᴀʀy : 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</b>
🖥 ʟᴀɴɢᴜᴀɢᴇ : 𝙿𝚈𝚃𝙷𝙾𝙽 3
🎪 ᴅᴀᴛᴀʙᴀꜱᴇ : 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
🔋 ꜱᴇʀᴠᴇʀ : ᴄᴏɴᴛᴀʙᴏ </b>"""
    SOURCE_TXT = """<b>NOTE:</b>
<b>𝖳𝗁𝗂𝗌 𝖡𝗈𝗍 𝖶𝖺𝗌 𝖬𝖺𝗄𝖾𝖽 𝖳𝖺𝗄𝗂𝗇𝗀 𝖲𝗈𝗆𝖺𝗇𝗒 𝖱𝖾𝗉𝗈𝗌 𝖮𝖿 𝖮𝗍𝗁𝖾𝗋 𝖪𝗂𝗇𝖽 𝖡𝗈𝗍𝗌
𝖲𝖮𝖴𝖱𝖢𝖤 𝖢𝖮𝖣𝖤 ~ 𝖭𝖮𝖳 𝖠𝖵𝖠𝖨𝖫𝖠𝖡𝖫𝖤 𝖱𝖨𝖦𝖧𝖳 𝖭𝖮𝖶
𝖮𝖳𝖧𝖤𝖱 𝖪𝖨𝖭𝖣 𝖡𝖮𝖳𝖲:
𝖠𝖴𝖳𝖮 𝖥𝖨𝖫𝖳𝖤𝖱 : <a href=https://github.com/EvamariaTG/EvaMaria>𝖤𝗏𝖺 𝖬𝖺𝗋𝗂𝖺</a>
𝖲𝖮𝖭𝖦 :  <a href=https://github.com/AsmSafone/RadioPlayerV2>𝖠𝗌𝗆𝖲𝖺𝖿𝗈𝗇𝖾</a>
𝖥𝖨𝖫𝖳𝖤𝖱 : <a href=https://github.com/TroJanzHEX/Unlimited-Filter-Bot>𝖴𝗇𝗅𝗂𝗆𝗂𝗍𝖾𝖽 𝖥𝗂𝗅𝗍𝖾𝗋 𝖡𝗈𝗍</a></b>"""
    MANUELFILTER_TXT = """<b>Help: Filters</b>

<b>Filter is the feature were users can set automated replies for a particular keyword and Bee Pathu will respond whenever a keyword is found the message

<b>NOTE:</b>
<b>1. BeePathu should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.</b>

<b>Commands and Usage:</b>
<b>• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code></b>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

<b>- BeePathu Supports both url and alert inline buttons.</b>

<b>NOTE:</b>
<b>1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bee Pathu supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format</b>

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
<b>1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db.</b>"""
    CONNECTION_TXT = """Help: <b>Connections</b>

<b>- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.</b>

<b>NOTE:</b>
<b>1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM</b>

<b>Commands and Usage:</b>
<b>• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code></b>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
<b>these are the extra features of Bee Pathu</b>

<b>Commands and Usage:</b>
<b>• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code></b>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
<b>This module only works for my admins</b>

<b>Commands and Usage:</b>
<b>• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code></b>"""
    STATUS_TXT = """<b>ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ ➪: <code>{}</code></b>
<b>ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ ➪: <code>{}</code>
ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ ➪: <code>{}</code>
ᴜꜱᴇᴅ ꜱᴛᴏʀᴀɢᴇ ➪: <code>{}</code> 𝙼𝚒𝙱
ꜰʀᴇᴇ ꜱᴛᴏʀᴀɢᴇ ➪ <code>{}</code> 𝙼𝚒𝙱</b>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
