import logging
from Buttonk import *
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from aiogram.types import CallbackQuery
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Tilni tanlang/Choose language",reply_markup = boshminu1)
            # Ingliz tili uchun kodlar
@dp.callback_query_handler(text = "registration")
async def menu_tanlash(call:CallbackQuery):
    await call.answer("You are registered", cache_time=60, show_alert=True)
@dp.callback_query_handler(text = "eng")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>👋 Hello!</b>"
     f"\n\n We are glad to see you among our observers!"
     f"\n\n The Young Managers Program is a special project organized in collaboration with the"
     f" Five Initiative Project and representatives of MBM IT Company!"     
     f"\n\n Through this program personnel management skills system will be formed in the international arena.",parse_mode = 'HTML',reply_markup = eng1)
@dp.callback_query_handler(text = "project")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"About the project",reply_markup = project1)
    await call.message.delete()
@dp.callback_query_handler(text = "aim_project")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"🔰 <b>What is the main purpose of the Young Managers Program?</b>"
        f"\n\n Project is designed to provide theoretical training in project management to young"
        f" people from aged 17 to 25, to share practical work experience with young people, and to"
        f" establish a community between people with different ideas and worldviews.",parse_mode = 'HTML',reply_markup = aim_project1)
    await call.message.delete()
@dp.callback_query_handler(text = "task_project")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>🔰 What are the objectives of project?</b>"
        f"\n\n• Training of specialists with international qualifications in the"
        f" field of management and creation of a potential human resources system"
        f" for entities and objects in the public and private sectors;"
        f"• Providing high-paid jobs to increase the knowledge and skills of youth;" 
        f"• To form a process of communication between the older and younger generations, to put an end to the 'cliff'"
        f" between them, to help them to ensure their interaction;",parse_mode = 'HTML',reply_markup = task_project1)
    await call.message.delete()
@dp.callback_query_handler(text = "the_order")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"🔰 <b>How long will the project last and what is the procedure?</b>"
    f"\n\n📝 Procedure for the Young Managers Program:"
    f"\n\nThe project will last for 10 weeks: practical and theoretical lessons will be conducted."
    f"\n\n📋 From August 25 to September 10, the process of registration and selection of candidates" 
    f"for participation in the project will be organized:"
    f"\n• Round 1 qualifiers: September 13 will be announced. (100 participants);"
    f"\n• Qualifying Round 2: September 15-16;"
    f"\n• Answers: to be announced on September 18 (50 participants)."
    f"\n\n💡 Out of the candidates, 50 young people who are strong, fluent in English, have their own ambitions"
    f" and have big goals for the future will be selected.",parse_mode = 'HTML',reply_markup = the_order1)
    await call.message.delete()
@dp.callback_query_handler(text = "requirements")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"🔰 <b>What are the requirements for candidates to participate?</b>"
     f"\n\n— Office work in English, Russian, Uzbek: fluent speaking and writing skills;"
     f"\n— Knowledge of IT and media;" 
     f"\n— 17-25 years old;"
     f"\n— Resident of Tashkent city and region.",parse_mode = 'HTML',reply_markup = requirements1)
    await call.message.delete()
@dp.callback_query_handler(text = "send")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>Hello!</b>"
    f"\n\nYou can send your questions to @Sherbek_Saydullayev. We will reply you soon."
    f"\n\nThank you for your attention.",parse_mode = 'HTML',reply_markup = send1)
    await call.message.delete()
        #Ingliz tili uchun ortdagi
@dp.callback_query_handler(text = "back")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>👋 Hello!</b>"
     f"\n\n We are glad to see you among our observers!"
     f"\n\n The Young Managers Program is a special project organized in collaboration with the"
     f" Five Initiative Project and representatives of MBM IT Company!"     
     f"\n\n Through this program personnel management skills system will be formed in the international arena.",parse_mode = 'HTML',reply_markup = eng1)
    await call.message.delete()
@dp.callback_query_handler(text = "project back")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"About the project",reply_markup = project1)
    await call.message.delete()

            # Uzbek tili uchun kodlar
@dp.callback_query_handler(text = "uz")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>👋Assalom aleykum!</b>\n\nSizni kuzatuvchilarimiz safida ko'rganimizdan mamnunmiz!"
                        f"\n\nYosh menejerlar dasturi Besh tashabbus loyihasi hamda MBM IT kompaniyasi vakillari hamkorligida tashkil etilgan maxsus dastur hisoblanadi!"
                        f"\n\nUshbu loyiha orqali xalqaro doirada boshqaruv qobiliyatiga ega kadrlar tizimi shakllantiriladi.",parse_mode='HTML',reply_markup = uz1)
@dp.callback_query_handler(text = "ruyxat")
async def menu_tanlash(call:CallbackQuery):
    await call.answer("Siz Ro'yxatga olindingiz", cache_time=60, show_alert=True)

@dp.callback_query_handler(text = "loyiha")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer("Loyiha hqaida",reply_markup = loyiha1)
    await call.message.delete()
@dp.callback_query_handler(text = "yollash")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer("Assalomu alaykum!"
        f"\n\nSavollaringizni @Sherbek_Saydullayev ga yo'llashingiz mumkin. Sizga tez orada javob beramiz!"
        f"\n\nE'tiboringiz uchun rahmat.",reply_markup = yollash1)
    await call.message.delete()
@dp.callback_query_handler(text = "loyiha_maqsadi")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"🔰 <b>Yosh Menejerlar dasturi nima maqsadda tashkil etilmoqda?</b>"
        f"\n\nMazkur loyiha 17 yoshdan 25 yoshgacha bo'lgan yoshlar qatlamini loyihalar" 
        f" boshqaruvi bo'yicha nazariy jihatdan o'qitish, amaliy jihatdan yoshlarga ish tajribasini ulashish,"
        f" turli fikr va dunyoqarashga ega shaxslar orasida muloqot almashinuvini yo'lga qo'yish maqsadida"
        f" tashkil etilgan.",parse_mode = 'HTML',reply_markup = loyiha_maqsadi1)
    await call.message.delete()
@dp.callback_query_handler(text = "loyiha_vazifalari")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"🔰 <b>Loyihaning vazifalari nimalardan iborat?</b>"
        f"\n\n• Boshqaruv sohasida malakaga ega, xalqaro doirada faoliyat yurita oladigan mutaxassislar tayyorlab,"
        f" davlat va nodavlat sektoridagi subyekt/obyektlar uchun salohiyatli kadrlar tizimini yaratib berish;"
        f"\n\n• Yoshlarning bilim va ko'nikmasini oshirib, yuqori daromad keltiradigan ish bilan ta'minlash;"
        f"\n\n• Kattalar va yoshlar orasida kommunikatsiya jarayonini shakllantirib, o'rtadagi "
        f"'jarlik'ka ma'lum ma'noda chek qo'yish, ularning o'zaro hamkorligini ta'minlashga "
        f"ko'maklashish.",parse_mode = 'HTML',reply_markup = loyiha_vazifalari1)
    await call.message.delete()
@dp.callback_query_handler(text = "utkazilishi_tartibi")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"🔰 <b>Loyiha qancha vaqt davom etadi va o'tkazilish tartibi qanday?</b>"
        f"\n\n📝Yosh menejerlar dasturining o’tkazilish tartibi:"
        f"\nLoyiha 10 hafta davomida bo'lib o'tadi: amaliy va nazariy darslar olib boriladi."
        f"\n\n📋 Avgust oyining 25-sanasidan boshlab 10-Sentabr kuniga qadar loyihada ishtirok "
        f"etishga nomzod shaxslarni ro'yxatdan o'tkazish va saralash jarayoni tashkil etiladi:"
        f"\n\n• 1-bosqichi saralashdan o’tganlar: 13 Sentabr e’lon qilinadi. (100 ta ishtirokchi);"
        f"\n• 2-saralash bosqichi: 15-16 Sentabr kuni bo’lib o’tadi;"
        f"\n• Javoblar: 18 Sentabr kuni e’lon qilinadi (50 ta ishtirokchi)."
        f"\n\n💡 Nomzodlar ichidan 50 nafar kuchga to'la, ingliz tilini yaxshi biluvchi, o'z ambitsiyalariga"
        f" ega va kelajakda katta maqsadlari bor yoshlar tanlab olinadi.",parse_mode = 'HTML',reply_markup = utkazilishi_tartibi1)
    await call.message.delete()
@dp.callback_query_handler(text = "talablar")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer("🔰 <b>Loyihada qatnashish uchun nomzodlarga qanday talablar qo'yiladi?</b>"
     f"\n\n— ingliz, rus, o'zbek tilida ish yuritish: erkin so'zlashish va yoza olish;"
     f"\n— IT texnologiyalari hamda mediasavodxonlik bo'yicha bilimga egalik;"
     f"\n— 17-25 yosh orasida bo'lish;"
     f"\n— Toshkent shahri va viloyati hududida istiqomat qilish.",parse_mode = 'HTML',reply_markup = talablar1)
    await call.message.delete() 
            # Orqaga tugmalari
@dp.callback_query_handler(text = "ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer(f"<b>👋Assalom aleykum!</b>\n\nSizni kuzatuvchilarimiz safida ko'rganimizdan mamnunmiz!"
                        f"\n\nYosh menejerlar dasturi Besh tashabbus loyihasi hamda MBM IT kompaniyasi vakillari hamkorligida tashkil etilgan maxsus dastur hisoblanadi!"
                        f"\n\nUshbu loyiha orqali xalqaro doirada boshqaruv qobiliyatiga ega kadrlar tizimi shakllantiriladi.",parse_mode='HTML',reply_markup = uz1)
    await message.delete()
@dp.callback_query_handler(text = "loyiha1 ortga")
async def menu_tanlash(call:CallbackQuery):
    await call.message.answer("Loyiha hqaida",reply_markup = loyiha1)
    await message.delete()

if __name__ == '__main__':
     executor.start_polling(dp, skip_updates=True)
