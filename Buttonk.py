from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton
boshminu1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text = "🇺🇿 O'zbekcha",callback_data = "uz"),
		InlineKeyboardButton(text = "🇬🇪 English",callback_data = 'eng')
		],
	],
)
eng1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text = "📒 About the project",callback_data = "project"),
		InlineKeyboardButton(text = "📋 Registration",callback_data = 'registration')
		],
		[
		InlineKeyboardButton(text = "📝 Send questions",callback_data = "send")
		],
	],
)
project1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text = "Aim of the project",callback_data = "aim_project"),
		InlineKeyboardButton(text = "Project task",callback_data = 'task_project')
		],
		[
		InlineKeyboardButton(text = "The order prpcess",callback_data = "the_order"),
		InlineKeyboardButton(text = "Requirements",callback_data = 'requirements')
		],
		[
		InlineKeyboardButton(text = "Back",callback_data = "back")
		],
	],
)
aim_project1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text = "Back",callback_data = "project back")
		],
	],
)
task_project1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text = "Back",callback_data = "project back")
		],
	],
)
the_order1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text = "Back",callback_data = "project back")
		],
	],
)
requirements1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text = "Back",callback_data = "project back")
		],
	],
)			
	
send1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text = "Back",callback_data = "back")
		],
	],
)	



			#Uzbek tili uchun buttonlar
uz1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text = "📒 Loyiha haqida",callback_data = "loyiha"),
		InlineKeyboardButton(text = "📋 Ro'yxatdan o'tish",callback_data = 'ruyxat')
		],
		[
		InlineKeyboardButton(text = "📝 Savollar yo'llash",callback_data = "yollash")
		],
	],
)
loyiha1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text = "Loyiha maqsadi",callback_data = "loyiha_maqsadi"),
		InlineKeyboardButton(text = "Loyiha vazifalari",callback_data = 'loyiha_vazifalari')
		],
		[
		InlineKeyboardButton(text = "O'tkazilishi tartibi",callback_data = "utkazilishi_tartibi"),
		InlineKeyboardButton(text = "Talablar",callback_data = 'talablar')
		],
		[
		InlineKeyboardButton(text = "Orqaga",callback_data = "ortga")
		],
	],
)
loyiha_maqsadi1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text = "Orqaga",callback_data = "loyiha1 ortga")
		],
	],
)

loyiha_vazifalari1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text = "Orqaga",callback_data = "loyiha1 ortga")
		],
	],
)
utkazilishi_tartibi1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text = "Orqaga",callback_data = "loyiha1 ortga")
		],
	],
)
talablar1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text = "Orqaga",callback_data = "loyiha1 ortga")
		],
	],
)

yollash1 = InlineKeyboardMarkup(
	inline_keyboard = [
		[
		InlineKeyboardButton(text = "Orqaga",callback_data = "ortga")
		],
	],
)
