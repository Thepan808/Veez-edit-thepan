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
    await query.message.reply_to_message.delete()

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
        f"""✨ **Olá** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

» **Aperte-se no botão de ver os comandos, primeramente em Básico de Guia !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 Comandos Básicos", callback_data="cblocal"),
                    InlineKeyboardButton("📕 Comandos Avançados", callback_data="cbadven"),
                ],
                [
                    InlineKeyboardButton("📘 Comandos dos Admins", callback_data="cblamp"),
                    InlineKeyboardButton("📗 Comandos dos Sudos", callback_data="cblab"),
                ],
                [InlineKeyboardButton("📙 Comandos do Pae(CRIADOR)", callback_data="cbmoon")],
                [InlineKeyboardButton("🔙 Voltar", callback_data="cbstart")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ COMO USAR O BOT:

1.) Primeiro, adicione o bot no grupo ou chame o criador pra por.
2.) Dê adm completo pra o bot ( Necessário...) Não precisa por em modo Anonymous.
3.) Adicione o @{ASSISTANT_NAME} Em seu grupo ou /join pra convidar.
4.) Agora só ativar o chat e pôr o cabaré pra dançar.

⚡ __Powered por {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Voltar", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblocal"))
async def cblocal(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Comandos Básicos**

🎧 [ GROUP VC CMD ]

/play (Nome da música) - Para tocar a música via youtube
/ytp (Nome da música) - Para tocar a música direto via youtube 
/stream (Marque a música/áudio file) - Toque a música usando audio file mp3
/playlist - Para ver a faixas de músicas que irão ser reproduzidas
/song (Nome da música) - Para baixar a música via youtube
/search (Nome do vídeo) - Para pesquisar videos via youtube em detalhes
/vsong (Nome do vídeo - Para baixar um vídeo via youtube
/lyric - (Nome da música para baixar a letra dela. 

🎧 [ Comandos pra canais (Nem é útil bastante) ]

/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/refresh - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel

⚡ __Powered por {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Voltar", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadven"))
async def cbadven(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Comandos Avançados**

/start (Em grupo) - Alive Status do bot
/reload - Atualizar a lista dos admins
/ping - check ping status
/uptime - check o bot uptime status
/id - check/user id de grupo, seu id e etc.

⚡ __Powered por {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Voltar", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblamp"))
async def cblamp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Comandos de admins**

/player - Abrir o Player e ver qual está tocando
/pause - Pause a música
/resume - Resume a música
/skip - Pular a música
/end - Parar a música
/join - Convidar o userbot para o seu grupo
/leave - Retirar o userbot do grupo
/auth - Autoriza pra usar o bot
/deauth - Não autoriza pra não usar o bot
/control - Abrir o panel da call(Reproduções)
/delcmd (on | off) - Ative / Desative del cmd 
/musicplayer (on / off) - Ative / Desatice music player pra tocar ou não tocar nada no grupo

⚡ __Powered por {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Voltar", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblab"))
async def cblab(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Comandos Sudos**

/leaveall - Userbot sairá de todos os grupo
/stats - Ver a estática
/rmd - remove downloads das músicas que foram baixada
/eval (Ignore) - execute code
/sh (Ignore) - run code

⚡ __Powered por {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Voltar", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmoon"))
async def cbmoon(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Comandos do Pae**

/stats - Ver a estática
/broadcast - Mandar um recado pra todos via bot
/block (user id - duração - reação - block no usuário pra não usar o bot
/unblock (user id - reason) - desblock no usuário pra usar novamente o bot 
/blocklist - Lista de pessoas bloqueadas

📝 Nota: Nem tente fazer gracinha, fazendo flood e tal não irá passar menos de 1 min, que irá ser banido do bot e dos grupos que estiver :) espero que não seja demente.

⚡ __Powered por {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Voltar", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cmdhome"))
async def cmdhome(_, query: CallbackQuery):

    bttn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Command Syntax", callback_data="cmdsyntax")
            ],[
                InlineKeyboardButton("🗑 Fechar", callback_data="close")
            ]
        ]
    )

    nofound = "😕 **não consigo encontrar a vossa música que você pediu**\n\n» **por favor, forneça o nome correto da música ou inclua o nome do artista também**"

    await query.edit_message_text(nofound, reply_markup=bttn)


@Client.on_callback_query(filters.regex("cmdsyntax"))
async def cmdsyntax(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Command Syntax** to play music on **Voice Chat:**

• `/play (query)` - para tocar música via youtube
• `/ytp (query)` - para tocar música diretamente via youtube

⚡ __Carregado pelo {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Para voltar", callback_data="cmdhome")]]
        ),
    )
