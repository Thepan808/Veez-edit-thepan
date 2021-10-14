# (C) 2021 VeezMusic-Project

from handlers.play import cb_admin_check
from helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Bem vindo [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Sou um bot de música onde toco em voice chats!**

💡 **Bom, para querer saber dos comandos do bot segue nessa etapa apertando » 📚 Botões de comandos!**

❔ **Primeiramente, para começar a saber os comandos aperte em comandos básicos » ❓ Botão Básico da Guia!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Para me adicionar em seu grupo ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Guia básica", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Comandos", callback_data="cbcmds"),
                    InlineKeyboardButton("😎 Criador", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Grupo oficial", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Canal Oficial", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌐 Canal de músicas", url="https://t.me/GR4V3_S4D_CRAZZY"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Olá** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

» **pressione o botão dos comandos para verificar!**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 Comandos Básicos", callback_data="cbbasic"),
                    InlineKeyboardButton("📕 Comandos avançados", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("📘 Comandos de admin", callback_data="cbadmin"),
                    InlineKeyboardButton("📗 Comandos de Sudos users", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("📙 Comandos do Criador", callback_data="cbowner")],
                [InlineKeyboardButton("🔙 Para voltar", callback_data="cbguide")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Comandos básicos**

🎧 [ Para grupos ]

/play (nome da música) - Toca música via youtube
/ytp (Nome da música) - Toca a música diretamente via youtube Music
/stream (Marque o áudio ou música file) - Para tocar músicas file
/song (Nome da música) - Para baixar uma música via youtube
/search (Nome do vídeo) - Pesquisar um video via youtube em detalhes
/vsong (Nome do vídeo) - Baixar um video via youtube em detalhes
/lyric - (Nome da música) baixar a lyrics (Letra da música) 

🎧 [ Para tocar no canal ]

/cplay - Marque a música para tocar no chat do canal
/cplayer - Ver um painel de músicas sendo tocadas e ainda que vai ser reproduzidas
/cpause - Pausar a música 
/cresume - Reproduzir uma música que foi pausada
/cskip - Pular para próxima música 
/cend - Encerrar a transmissão de música 
/refresh - Atualizar os admins
/ubjoinc - Convidar o assistant para entrar no canal

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Comandos avançados**

/start (Em grupo) - Para ver o Alive status do bot
/reload - Atualizar a lista dos admin
/ping - Checar o ping do bot
/uptime - Checar o uptime do bot
/id - Ver o id do grupo, marcando você para ver o seu id

⚡ __Powered por {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Para voltar", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Para comandos dos admins**

/player - Para ver o status (quando estiver reproduzindo algo) 
/pause - Pausar a música 
/resume - Resumir a música 
/skip - Pular a música 
/end - Parar de transmitir o som
/join - Convidar o userbot ao grupo
/leave - Faz que o Userbot saia do grupo
/auth - Autorizar o meliante à usar o bot
/deauth - Não autorizar o meliante à usar o bot
/control - Abrir o painel do bot
/delcmd (on ou off) - Ative / Desative del cmd, futuro... 
/musicplayer (on ou off) - Ative / ou Desative music player em seu grupo

⚡ __Powered por {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Comandos para os Sudo users**

/leaveall - Faz o userbot sair de todos os grupos
/stats - Ver a estatística do bot
/rmd - Remover todos os downloads file
/eval (Nada de útil) - executar o code
/sh (Nada útil) - run code

⚡ __Powered por {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Para comandos do pae (CRIADOR)**

/stats - Ver a estática do bot
/broadcast (Marque a mensagem) - Enviar uma mensagem em todos os grupo via bot
/block (user id - duração - reação - Bloqueia o meliante pra não usar o bot
/unblock (user id - reação) - Desbloqueia o fdp pra usar o bot
/blocklist - Ver a lista de todos os bloqueados KKKK

📝 Um aviso: Nem pense em fazer gracinha fazendo flood, só você fazendo isso em 10 segundos, você irá ser banido de todos os grupos e block no bot permamente.

⚡ __Powered por {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ Como usar o bot:

1.) Primeiramente, me adicione no seu grupinho.
2.) Me dê admin, que seja completo sem aquela merda de opção anônima.
3.) Adicione o @{ASSISTANT_NAME} para seu grupo ou use /join para convidar, caso não consiga me chame no pv.
4.) Última etapa, ative o chat de voz e ponhe o cabaré pra rolar.

⚡ __Powered por {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("📚 Lista de comandos", callback_data="cbhelp")],
                [InlineKeyboardButton("🗑 Fechar", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**💡 Controle menu do bot:**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⏸ pause", callback_data="cbpause"),
                    InlineKeyboardButton("▶️ resume", callback_data="cbresume"),
                ],
                [
                    InlineKeyboardButton("⏩ skip", callback_data="cbskip"),
                    InlineKeyboardButton("⏹ stop", callback_data="cbend"),
                ],
                [InlineKeyboardButton("⛔ anti cmd", callback_data="cbdelcmds")],
                [InlineKeyboardButton("🗑 Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""📚 **Uma informação futuramente:**
        
**💡 Feature:** Deletar excetos comandos que seja de spam!

❔ Usando:**

 1️⃣ Para ativar:
     » `/delcmd on`
    
 2️⃣ Para desativar:
     » `/delcmd off`
      
⚡ __Powered por {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbback")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello fiatin glingo** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

» **press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 Basic Cmd", callback_data="cblocal"),
                    InlineKeyboardButton("📕 Advanced Cmd", callback_data="cbadven"),
                ],
                [
                    InlineKeyboardButton("📘 Admin Cmd", callback_data="cblamp"),
                    InlineKeyboardButton("📗 Sudo Cmd", callback_data="cblab"),
                ],
                [InlineKeyboardButton("📙 Owner Cmd", callback_data="cbmoon")],
                [InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /join to invite her.
4.) turn on the voice chat first before start to play music.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblocal"))
async def cblocal(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the basic commands**

🎧 [ GROUP VC CMD ]

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/vsong (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper

🎧 [ CHANNEL VC CMD ]

/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/refresh - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadven"))
async def cbadven(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the advanced commands**

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/ping - check the bot ping status
/uptime - check the bot uptime status
/id - show the group/user id & other

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblamp"))
async def cblamp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the admin commands**

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/join - invite userbot join to your group
/leave - order the userbot to leave your group
/auth - authorized user for using music bot
/deauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/musicplayer (on / off) - disable / enable music player in your group

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblab"))
async def cblab(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the sudo commands**

/leaveall - order the assistant to leave from all group
/stats - show the bot statistic
/rmd - remove all downloaded files
/eval (query) - execute code
/sh (query) - run code

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmoon"))
async def cbmoon(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the owner commands**

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

📝 note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )
