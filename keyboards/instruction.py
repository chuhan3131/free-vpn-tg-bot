from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

instruction_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="android", callback_data="android_kb"),
            InlineKeyboardButton(text="ios", callback_data="ios_kb"),
        ],
        [
            InlineKeyboardButton(text="windows", callback_data="windows_kb"),
            InlineKeyboardButton(text="macos", callback_data="macos_kb"),
        ],
        [
            InlineKeyboardButton(text="◀️", callback_data="main_menu"),
            InlineKeyboardButton(text="linux", callback_data="linux_kb"),
        ],
    ]
)


android_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️", callback_data="instruction_kb"),
            InlineKeyboardButton(
                text="Google Play",
                url="https://play.google.com/store/apps/details?id=app.hiddify.com",
            ),
        ]
    ]
)


ios_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️", callback_data="instruction_kb"),
            InlineKeyboardButton(
                text="app store",
                url="https://apps.apple.com/ru/app/v2raytun/id6476628951",
            ),
        ]
    ]
)


windows_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️", callback_data="instruction_kb"),
            InlineKeyboardButton(
                text="github",
                url="https://github.com/hiddify/hiddify-next/releases/latest/download/Hiddify-Windows-Setup-x64.exe",
            ),
        ]
    ]
)


macos_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️", callback_data="instruction_kb"),
            InlineKeyboardButton(
                text="app store",
                url="https://apps.apple.com/ru/app/v2raytun/id6476628951",
            ),
        ]
    ]
)


linux_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️", callback_data="instruction_kb"),
            InlineKeyboardButton(
                text="github", url="https://github.com/Happ-proxy/happ-desktop/releases"
            ),
        ]
    ]
)
