from aiogram import types

kirish1 = [
    [types.KeyboardButton(text="Golds"), types.KeyboardButton(text="Trends")]
]

kirish1_set = types.ReplyKeyboardMarkup(keyboard=kirish1, resize_keyboard=True)

########################################################################################################################

golds = [
    [types.KeyboardButton(text="Xitoy"), types.KeyboardButton(text="Avstraliya")],
    [types.KeyboardButton(text="Yaponiya"), types.KeyboardButton(text="Janubiy Koreya")],
    [types.KeyboardButton(text="Qo'shma Shtatlar"), types.KeyboardButton(text="Venesuella")],
]

golds_set = types.ReplyKeyboardMarkup(keyboard=golds, resize_keyboard=True)
