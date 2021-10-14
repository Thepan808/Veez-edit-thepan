from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from handlers import __version__
from helpers.decorators import sudo_users_only
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""➜ **Bem vindo(a) {message.from_user.mention} !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Permite que você toque música em grupos através dos novos bate-papos de voz do Telegram!**

💡 **Descubra todos os comandos do Bot e como eles funcionam clicando no » 🗂 Comandos!**

❔ **Para saber como usar este bot, clique no » ❓ Botão Básico Guia!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Me adicione em seu grupo ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Guia Básico", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("🗂 Comandos", callback_data="cbcmds"),
                    InlineKeyboardButton("🤔 Criador", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Grupo oficial", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Canal oficial", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "💬 Canal oficial de música", url="https://t.me/GR4V3_S4D_CRAZZY"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🧐 Grupo", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "📣 Canal", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**Olá admiro, membro em comum {message.from_user.mention}, O {BOT_NAME}**\n\n✨ Bot está funcionando perfeitamente\n😎 Meu criador: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ Bot na versão: `v{__version__}`\n⚙️ Pyrogram versão: `{pyrover}`\n⚙️ Python versão: `{__python_version__}`\n⚙️ Uptime Status: `{uptime}`\n\n**Obrigado por me adicionar, para tocar músicas em seu grupo, no chat de voz** 🙃❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Olá** {message.from_user.mention()}!

» **aperte-se no botão abaixo para ler a explicação e ver a lista de comandos disponíveis !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="❓ Guia Básica", callback_data="cbguide")]]
        ),
    )


@Client.on_message(
    command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ **Olá {message.from_user.mention}!**

» **Através deste painel menu você poderá apertar um dos botões abaixo para ler a explicação de cada comando do bot**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🗂️ Comandos básico", callback_data="cbbasic"),
                    InlineKeyboardButton("📕 Comandos avançados", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("📘 Comandos dos admins", callback_data="cbadmin"),
                    InlineKeyboardButton("📗 Comandos dos Sudo users", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("📙 Comandos do criador", callback_data="cbowner")],
            ]
        ),
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🤺 `PONG FELA DA POTA!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 Status do bot:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **Tempo de duração online:** `{START_TIME_ISO}`"
    )
