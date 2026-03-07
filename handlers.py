from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, Location
import keyboards as kb

router = Router()

ADMIN_ID = 7143007426

def monitor_activity(func):
    async def wrapper(message: Message, *args, **kwargs):
        # Foydalanuvchi ma'lumotlari
        user_info = f"👤 <b>Foydalanuvchi:</b> {message.from_user.full_name} (@{message.from_user.username})\n"
        user_info += f"🆔 <b>ID:</b> {message.from_user.id}\n"
        user_info += f"💬 <b>Xabar:</b> {message.text}\n"
        
        # Adminga xabar yuborish (Xatoni oldini olish uchun try-except ishlatamiz)
        try:
            await message.bot.send_message(ADMIN_ID, f"🔔 <b>Yangi faollik:</b>\n\n{user_info}", parse_mode="HTML")
        except Exception as e:
            print(f"Monitoring error: {e}")
            
        return await func(message, *args, **kwargs)
    return wrapper

@router.message(CommandStart())
@monitor_activity
async def cmd_start(message: Message):
    await message.answer(
        "Assalomu alaykum! 👋\n\n"
        "Di Travel botiga xush kelibsiz ✈️\n"
        "Biz sizga Umra, Haj va dunyo bo'ylab sayohatlar haqida ma'lumot beramiz.",
        reply_markup=kb.get_main_menu()
    )

@router.message(F.text == "Umra Paketlar 🕋")
@monitor_activity
async def umra_info(message: Message):
    text = (
        "🕋 <b>UMRA PAKETLARI</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"

        "🌙 <b>Tejamkor — Econom</b>\n"
        "💵 <b>950$</b> dan\n"
        "Hamyonbop va sifatli sayohat imkoniyati.\n"
        "▫️ 3⭐ Mehmonxona\n"
        "▫️ Transport\n"
        "▫️ Viza ko'magi\n"
        "▫️ Gid xizmati\n\n"

        "⭐ <b>Ommabop — Standart</b>\n"
        "💵 <b>1000$</b> dan\n"
        "Sifat va qulaylik uyg'unligi, eng ommabop.\n"
        "▫️ 4⭐ Mehmonxona\n"
        "▫️ Transport\n"
        "▫️ Viza ko'magi\n"
        "▫️ Ellikboshi\n\n"

        "✨ <b>Yaxshilangan — Standart Plus</b>\n"
        "💵 <b>1100$</b> dan\n"
        "Qo'shimcha qulayliklar va markazga yaqin.\n"
        "▫️ 4⭐ Premium Mehmonxona\n"
        "▫️ Maxsus Transport\n"
        "▫️ Viza ko'magi\n"
        "▫️ Gid xizmati\n\n"

        "💎 <b>Qulay — Comfort</b>\n"
        "💵 <b>1200$</b> dan\n"
        "Maksimal darajadagi eksklyuziv xizmatlar.\n"
        "▫️ 5⭐ Mehmonxona\n"
        "▫️ VIP Transport\n"
        "▫️ Viza ko'magi\n"
        "▫️ Shaxsiy yordamchi\n\n"

        "━━━━━━━━━━━━━━━━━━━━\n"
        "🎯 <b>Sizga mos maxsus paket kerakmi?</b>"
    )
    await message.answer(text, parse_mode="HTML", reply_markup=kb.get_umra_menu())


@router.message(F.text == "Ziyoratgohlar 🕌")
@monitor_activity
async def ziyorat_info(message: Message):
    text = (
        "Biz quyidagi ziyorat safarlarini taklif qilamiz:\n\n"
        "📍 Mahalliy ziyoratlar (O'zbekiston bo'ylab muqaddas qadamjolar)\n"
        "📍 Umra safarlari\n"
        "📍 Ziyorat turlari haqida batafsil ma'lumot\n\n"
        "Kerakli bo'limni tanlang yoki operator bilan bog'lanish uchun yozib qoldiring. "
        "Sizga yordam berishdan mamnunmiz!"
    )
    await message.answer(text, reply_markup=kb.get_ziyorat_menu())

@router.message(F.text == "Mahalliy Ziyoratlar 🕌")
@monitor_activity
async def mahalliy_ziyoratlar(message: Message):
    text = (
        "Siz <b>Mahalliy ziyoratlar</b> bo'limini tanladingiz\n\n"
        "Biz quyidagi ziyorat va sayohat yo'nalishlari bo'yicha ma'lumot taqdim etamiz:\n\n"
        "🕌 Samarqand ziyoratlari (muqaddas maqbaralar)\n"
        "🕌 Buxoro ziyoratlari (tarixiy qadamjolar)\n"
        "🕌 Toshkent ziyoratgohlari\n"
        "🕌 Boshqa viloyatlardagi ziyorat safarlari\n"
        "🕋 Umra safarlari\n"
        "🌍 Boshqa davlatlarga ziyorat va sayohatlar\n\n"
        "ℹ️ Ushbu bot faqat umumiy ma'lumot beradi.\n"
        "📅 Safar sanalarini bilish uchun Mijozlarga xizmat ko'rsatish xodimlariga murojaat qiling.\n"
        "💰 Narxlar haqida ma'lumot olish uchun qo'ng'iroq qiling.\n"
        "🚌 Transport va xizmatlar haqida batafsil ma'lumot beriladi.\n\n"
        "📞 <a href=\"tel:+998883339099\">+998 88 333 90 99</a>"
    )
    await message.answer(text, parse_mode="HTML", reply_markup=kb.get_ziyorat_menu())

@router.message(F.text == "Umra Safarlari 🕋")
@monitor_activity
async def umra_safarlari(message: Message):
    await message.answer(
        "🕋 Umra safarlarimiz haqida batafsil ma'lumot olish uchun:\n\n"
        "📞 <a href=\"tel:+998883339099\">+998 88 333 90 99</a>\n\n"
        "👉 Yoki <b>Umra Paketlar 🕋</b> bo'limini ko'ring.",
        parse_mode="HTML",
        reply_markup=kb.get_ziyorat_menu()
    )

@router.message(F.text == "Ziyorat turlari ℹ️")
@monitor_activity
async def ziyorat_turlari(message: Message):
    await message.answer(
        "ℹ️ <b>Ziyorat turlari haqida batafsil ma'lumot:</b>\n\n"
        "Bizning agentligimiz quyidagi tur turlarini taklif etadi:\n"
        "🕌 Mahalliy ziyorat turlari\n"
        "🕋 Umra turlari\n"
        "🌍 Xalqaro ziyorat turlari\n\n"
        "Batafsil ma'lumot uchun:\n"
        "📞 <a href=\"tel:+998883339099\">+998 88 333 90 99</a>",
        parse_mode="HTML",
        reply_markup=kb.get_ziyorat_menu()
    )

@router.message(F.text == "🔙 Orqaga")
@monitor_activity
async def orqaga_main(message: Message):
    await message.answer("Asosiy menyu:", reply_markup=kb.get_main_menu())

@router.message(F.text == "⬅️ Foydali Ma'lumotlar")
@monitor_activity
async def orqaga_to_info(message: Message):
    await message.answer("Foydali ma'lumotlar bo'limi:", reply_markup=kb.get_info_menu())

@router.message(F.text == "Foydali Ma'lumotlar 💡")
@monitor_activity
async def info_main(message: Message):
    text = (
        "<b>Ma'lumotlar markaziga xush kelibsiz!</b> 💡\n\n"
        "Sayohat davomida sizga asqotadigan eng kerakli ma'lumotlarni shu bo'limdan topishingiz mumkin.\n\n"
        "Marhamat, o'zingizni qiziqtirgan mavzuni tanlang:"
    )
    await message.answer(text, parse_mode="HTML", reply_markup=kb.get_info_menu())

@router.message(F.text == "Sayohatga tayyorgarlik 🎒")
@monitor_activity
async def preparation_tips(message: Message):
    text = (
        "🎒 <b>Sayohatga tayyorgarlik bo'yicha tavsiyalar:</b>\n\n"
        "▫️ <b>Hujjatlar:</b> Xalqaro pasport, viza va safar chiptalarini tekshiring.\n"
        "▫️ <b>Kiyim:</b> Safar davomida havo haroratiga mos va qulay kiyimlar oling. Ziyorat uchun qulay poyabzal juda muhim.\n"
        "▫️ <b>Dori-darmonlar:</b> Shaxsiy dori-darmonlaringiz va birinchi yordam to'plamini (og'riq qoldiruvchi, oshqozon uchun dori va h.k.) unutmang.\n"
        "▫️ <b>Gigiyena:</b> Shaxsiy gigiyena vositalari, nam salfetkalar va dezinfeksiyalovchi vositalarni oling.\n\n"
        "💡 <i>Maslahat: Safarga chiqishdan oldin telefoningiz xalqaro aloqa (roaming) xizmatiga ulanganligini tekshiring.</i>"
    )
    await message.answer(text, parse_mode="HTML")

@router.message(F.text == "Viza masalalari 🛂")
@monitor_activity
async def visa_info(message: Message):
    text = (
        "🛂 <b>Viza haqida umumiy ma'lumot:</b>\n\n"
        "▫️ <b>Umra vizasi:</b> Faqat Umra amallarini bajarish uchun mo'ljallangan.\n"
        "▫️ <b>Turistik viza:</b> Saudiya Arabistoniga sayohat qilish va Umra amalini bajarish imkoniyatini beradi.\n\n"
        "<b>Kerakli hujjatlar:</b>\n"
        "1. Xalqaro pasport (kamida 6 oy amal qilish muddati bilan).\n"
        "2. 3.5x4.5 o'lchamdagi oq fondagi rasm.\n\n"
        "⚠️ <i>Viza rasmiylashtirish vaqti va narxi tanlangan paketga qarab farq qilishi mumkin.</i>"
    )
    await message.answer(text, parse_mode="HTML")

@router.message(F.text == "Tez-tez so'raladigan savollar ❓")
@monitor_activity
async def faq_info(message: Message):
    text = (
        "❓ <b>Ko'p so'raladigan savollar:</b>\n\n"
        "<b>S: Safar necha kun davom etadi?</b>\n"
        "J: Odatda guruhli turlarimiz 10, 14 yoki 15 kunlik muddatni o'z ichiga oladi.\n\n"
        "<b>S: Paketga ovqatlanish kiritilganmi?</b>\n"
        "J: Ha, tarifga qarab kuniga 2 yoki 3 mahal issiq ovqat taqdim etiladi.\n\n"
        "<b>S: Gid (yo'lboshchi) xizmati bormi?</b>\n"
        "J: Albatta, tajribali Ellikboshi va gidlarimiz sizga barcha amallarni bajarishda hamrohlik qilishadi.\n\n"
        "<b>S: Bolalar bilan borish mumkinmi?</b>\n"
        "J: Ha, bolalar uchun maxsus chegirmalar va qulayliklar mavjud."
    )
    await message.answer(text, parse_mode="HTML")

@router.message(F.text == "Ziyorat Odoblari & Duolar 📖")
@monitor_activity
async def religious_info_main(message: Message):
    text = (
        "📖 <b>Ziyorat Odoblari va Duolar</b>\n\n"
        "Umra va Haj amallarini bajarishda sizga kerak bo'ladigan eng muhim duolar va odoblar to'plami.\n\n"
        "Marhamat, kerakli bo'limni tanlang:"
    )
    await message.answer(text, parse_mode="HTML", reply_markup=kb.get_religious_menu())

@router.message(F.text == "Ehrom kiyish tartibi 🕋")
@monitor_activity
async def ehrom_info(message: Message):
    text = (
        "🕋 <b>Ehrom kiyish va niyat qilish:</b>\n\n"
        "1. <b>Ehromdan oldin:</b> Tirnoqlarni olish, ortiqcha tuklardan tozalanish va g'usl qilish (imkon bo'lmasa tahorat).\n"
        "2. <b>Kiyish:</b> Erkaklar ikki bo'lak oq matoga o'ranadilar. Ayollar esa odatiy, shar'an ruxsat etilgan yopiq kiyim kiyadilar.\n"
        "3. <b>Namoz:</b> Ehrom kiygandan so'ng, ikki rakat ehrom namozini o'qish (agar karohiyat vaqti bo'lmasa).\n"
        "4. <b>Niyat:</b>\n"
        "اللَّهُمَّ إِنِّي أُرِيدُ الْعُمْرَةَ فَيَسِّرْهَا لِي وَتَقَبَّلْهَا مِنِّي\n"
        "(Allohumma inniy uriydu-l-umrota fa yassirha liy wa taqobbalha minniy)\n"
        "Tarjimasi: Allohim, men Umra qilishni iroda qildim, uni menga oson qil va mendan qabul et.\n\n"
        "5. <b>Talbiya:</b>\n"
        "لَبَّيْكَ اللَّهُمَّ لَبَّيْكَ، لَبَّيْكَ لَا شَرِيكَ لَكَ لَبَّيْكَ، إِنَّ الْحَمْدَ وَالنِّعْمَةَ لَكَ وَالْمُلْكَ، لَا شَرِيكَ لَكَ\n"
        "(Labbaykallohumma labbayk, labbayka laa shariyka laka labbayk. Inna-l-hamda wa-n-ni'mata laka wa-l-mulk, laa shariyka lak)\n"
        "Tarjimasi: Labbayka Allohim, Labbayka. Labbayka, Sening sheriging yo'qdir, Labbayka. Albatta, hamd, ne'mat va mulk Senikidir. Sening sheriging yo'qdir."
    )
    await message.answer(text, parse_mode="HTML")

@router.message(F.text == "Safar duolari ✈️")
@monitor_activity
async def travel_duas(message: Message):
    text = (
        "✈️ <b>Safar davomidagi duolar:</b>\n\n"
        "🏠 <b>Uydan chiqayotganda:</b>\n"
        "بِسْمِ اللهِ تَوَكَّلْتُ عَلَى اللهِ، وَلَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللهِ\n"
        "(Bismillahi tavakkaltu 'alalloh, va laa havla va laa quvvata illa billah)\n"
        "Tarjimasi: Allohning nomi bilan, Allohga tavakkal qildim. Kuch va quvvat faqat Alloh bilandir.\n\n"
        "🚀 <b>Samolyotga (ulovga) minganda:</b>\n"
        "سُبْحَانَ الَّذِي سَخَّرَ لَنَا هَذَا وَمَا كُنَّا لَهُ مُقْرِنِينَ وَإِنَّا إِلَى رَبِّنَا لَمُنْقَلِبُونَ\n"
        "(Subhanallaziy sakh-khoro lana haza va ma kunna lahu muqriniyn, va inna ila Robbina lamunqolibun)\n"
        "Tarjimasi: Bizga buni bo'ysundirib qo'ygan Zot pokdir, biz bunga qodir emas edik. Albatta, biz Robbimizga qaytguvchilarmiz.\n\n"
        "🚩 <b>Miyqotga yetganda:</b>\n"
        "Ehromga kirish va niyat qilish vaqti kelganini bildiradi. Bu yerda Talbiya aytish ko'paytiriladi."
    )
    await message.answer(text, parse_mode="HTML")

@router.message(F.text == "Tavof va Sa'y duolari 🤲")
@monitor_activity
async def thawaf_duas(message: Message):
    text = (
        "🤲 <b>Tavof va Sa'y amallari duolari:</b>\n\n"
        "🔄 <b>Tavof boshlanganda:</b> Har galt 'Hajarul Asvad' burchagiga kelganda: 'Bismillah, Allohu Akbar' deb qo'l ko'tariladi.\n"
        "🟢 <b>Ruknul Yamoniy va Hajarul Asvad orasida:</b>\n"
        "رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الْآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ\n"
        "(Robbana atina fid-dunya hasanatan va fil-axiroti hasanatan va qina 'azaban-nar)\n"
        "Tarjimasi: Robbimiz, bizga dunyoda ham yaxshilik bergin, oxiratda ham yaxshilik bergin va bizni do'zax azobidan saqlagin.\n\n"
        "🏃‍♂️ <b>Sa'y (Safa va Marva) amali:</b>\n"
        "Safa tepaligida turib Qiblaga yuzlanib:\n"
        "لَا إِلَهَ إِلَّا اللهُ وَحْدَهُ لَا شَرِيكَ لَهُ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ\n"
        "(La ilaha illallohu vahdahu la shariyka lah, lahul mulku va lahul hamdu va huva 'ala kulli shay'in qodiyr)\n"
        "Tarjimasi: Yolg'iz Allohdan o'zga iloh yo'q, Uning sherigi ham yo'q. Mulk ham, hamd ham Unikidir va U har narsaga qodirdir."
    )
    await message.answer(text, parse_mode="HTML")

@router.message(F.text == "Madina ziyorati odoblari 🕌")
@monitor_activity
async def madinah_tips(message: Message):
    text = (
        "🕌 <b>Madinai Munavvara ziyorati:</b>\n\n"
        "▫️ <b>Salovot:</b> Payg'ambarimiz (s.a.v)ga imkon qadar ko'p salovot aytish:\n"
        "اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ\n"
        "(Allohumma solli 'ala Muhammadiv-va 'ala ali Muhammad)\n"
        "Tarjimasi: Allohim, Muhammadga va Muhammadning oilasiga salovat yo'lla.\n\n"
        "▫️ <b>Masjidun Nabaviy:</b> Ushbu masjidda o'qilgan bir rakat namoz boshqa joydagi mingta namozdan afzaldir.\n"
        "▫️ <b>Ravza:</b> 'Menining uyim va minbarim orasi jannat bog'laridan bir bog'dir' - deyilgan joyda duo qilishga harakat qiling.\n"
        "▫️ <b>Odob:</b> Payg'ambarimiz (s.a.v) huzurlarida ovozni baland qilmaslik va kamoli ehtirom bilan turish."
    )
    await message.answer(text, parse_mode="HTML")

@router.message(F.text == "Biz Haqimizda ✈️")
@monitor_activity
async def about_us(message: Message):
    text = (
        "✈️ <b>Di Travel haqida</b>\n\n"
        "Di Travel — zamonaviy sayohat agentligi bo'lib, sizga qulay, ishonchli va sifatli turistik xizmatlarni taqdim etadi. "
        "Biz mijozlarga yuqori darajadagi xizmat ko'rsatish va unutilmas safar tashkil qilishni maqsad qilganmiz.\n\n"
        "🌍 <b>Bizning xizmatlarimiz:</b>\n\n"
        "🕋 Umra safari — to'liq xizmatlar (viza, mehmonxona, transport, yo'lboshchi)\n"
        "🕌 Haj safari — professional tashkil etilgan safar xizmatlari\n"
        "✈️ Aviabiletlar — arzon va qulay aviachiptalar\n"
        "🏝 Turistik paketlar — dunyo bo'ylab dam olish sayohatlari\n"
        "🏨 Mehmonxona bron qilish xizmati\n"
        "🧾 Viza xizmatlari\n"
        "👨‍💼 Professional konsultatsiya va yordam\n\n"
        "⭐ <b>Nega aynan Di Travel?</b>\n"
        "✔ Ishonchli va sifatli xizmat\n"
        "✔ Qulay narxlar\n"
        "✔ Tajribali mutaxassislar\n"
        "✔ 9:00 dan 20:00 gacha yordam\n"
        "✔ Mijozlar ishonchi va qulaylik birinchi o'rinda\n\n"
        "🎯 Bizning maqsadimiz — sizning sayohatingizni xavfsiz, qulay va unutilmas qilish.\n\n"
        "🌐 <b>Rasmiy sayt:</b>\nwww.ditravel.uz"
    )
    await message.answer(text, parse_mode="HTML")

@router.message(F.text == "Bog'lanish 📞")
@monitor_activity
async def contact_info(message: Message):
    text = (
        "📞 <b>Bog'lanish</b>\n\n"
        "Biz bilan quyidagi usullar orqali bog'lanishingiz mumkin:\n\n"
        "☎️ Telefon: <a href=\"tel:+998982228899\">+998 98 222 88 99</a>  <a href=\"tel:+998883339099\">+998 88 333 90 99</a>\n"
        "📱 Telegram: https://t.me/di_traveluz\n"
        "📧 Email: <a href=\"mailto:info@ditravel.uz\">info@ditravel.uz</a>\n"
        "📍 Manzil: Toshkent shahri Chilonzor tumani Muqimiy ko'chasi 142/2\n\n"
        "🕒 Ish vaqti: Dushanba – Shanba, 09:00 – 20:00\n\n"
        "💬 Savollaringiz bo'lsa yozib qoldiring yoki qo'ng'iroq qiling. "
        "Mijozlarga xizmat ko'rsatish xodimlari sizga yordam beradi."
    )
    await message.answer(text, parse_mode="HTML", disable_web_page_preview=True)
    
    # Ofis joylashuvi koordinatalari
    latitude = 41.293436
    longitude = 69.221912
    await message.answer_location(latitude=latitude, longitude=longitude)

@router.callback_query(F.data.startswith("umra_"))
async def umra_packages(callback: CallbackQuery):
    pkg = callback.data.split("_")[1]
    info = {
        "premium": "Premium Paket: 5 darajali mehmonxona, VIP transport va kengaytirilgan xizmatlar.",
        "standart": "Standart Paket: 4 darajali mehmonxona, qulay transport va barcha zarur xizmatlar.",
        "ekonom": "Ekonom Paket: Hamyonbop narxda sifatli ziyorat."
    }
    await callback.message.answer(info.get(pkg, "Paket haqida ma'lumot topilmadi."))
    await callback.answer()
