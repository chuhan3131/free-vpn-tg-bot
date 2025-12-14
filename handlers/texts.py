russian = {
    "start": lambda name, keys: f"привет {name}\n\n/vpn - получить ключ\n/donate - для донатов\n/api - примеры использования API\n\nвсего бот выдал <code>{keys}</code> ключей",
    "generation": "генерация ключа...",
    "key": lambda config_url, date, traffic: f"<b>твой ключ:</b>\n<code>{config_url}</code>\n\n<b>действителен до:</b> {date}\n<b>трафик:</b> {traffic} ГБ",
    "error": lambda error_msg: f"ошибка: <code>{error_msg}</code>",
    "any_message": "используй следующие команды:\n\n/vpn - получить ключ\n/donate - для донатов\n/api - примеры использования API",
    "donate": "поддержать проект",
    "api_intro": "бот использует публичный API для предоставления VPN конфигов, который может прекратить работу в любой момент :)",
    "api_examples": "примеры использования:",
    "api_response": "ответ от сервера:",
    "key_generated": "ключ сгенерирован!",
    "inline_get_title": "получить бесплатный VPN!",
    "inline_get_description": "нажмите чтобы сгенерировать VPN конфигурацию",
    "inline_error_title": "ошибка",
    "inline_get_error_description": "не удалось сгенерировать VPN",
    "check_error": "пожалуйста, укажите ключ после команды\n\nпример:\n<code>/check https://vpn-telegram.com/config/...</code>",
    "check": lambda traffic, left, expires: f"<b>использовано:</b> {traffic} ГБ\n<b>осталось:</b> {left} ГБ\n<b>действителен до:</b> {expires}",
    "checking": "проверка ключа...",
    "inline_check_title": "проверка VPN ключа",
    "inline_check_description": "нажмите чтобы узнать статус ключа",
    "inline_check_error_description": "не удалось проверить ключ"
}

english = {
    "start": lambda name, keys: f"hi {name}\n\n/vpn - get a key\n/donate - for donations\n/api - examples of use API\n\nin total the bot issued <code>{keys}</code> keys",
    "generation": "generating a key...",
    "key": lambda config_url, date, traffic: f"<b>your key:</b>\n<code>{config_url}</code>\n\n<b>valid until:</b> {date}\n<b>traffic:</b> {traffic} GB",
    "error": lambda error_msg: f"error: <code>{error_msg}</code>",
    "any_message": "use the following commands:\n\n/vpn - get a key\n/donate - for donations\n/api - examples of use API",
    "donate": "support the project",
    "api_intro": "the bot uses a public API to provide VPN configs, which can stop at any time :)",
    "api_examples": "examples of use:",
    "api_response": "response from the server:",
    "key_generated": "key generated!",
    "inline_get_title": "get free vpn!",
    "inline_get_description": "click to generate VPN configuration",
    "inline_error_title": "error",
    "inline_get_error_description": "failed to generate VPN",
    "check_error": "please specify the key after the command\n\nexample:\n<code>/check https://vpn-telegram.com/config/...</code>",
    "check": lambda traffic, left, expires: f"used: {traffic} GB (left {left})\nvalid until: {expires}",
    "checking": "checking key...",
    "inline_check_title": "VPN key check",
    "inline_check_description": "click to check key status",
    "inline_check_error_description": "failed to check key"
}

uzbek = {
    "start": lambda name, keys: f"salom {name}\n\n/vpn - kalit olish\n/donate - xayriya uchun\n/api - API dan foydalanish misollari\n\njami bot <code>{keys}</code> ta kalit berdi",
    "generation": "kalit yaratilmoqda...",
    "key": lambda config_url, date, traffic: f"<b>sizning kalitingiz:</b>\n<code>{config_url}</code>\n\n<b>amal qilish muddati:</b> {date}\n<b>trafik:</b> {traffic} GB",
    "error": lambda error_msg: f"xato: <code>{error_msg}</code>",
    "any_message": "quyidagi buyruqlardan foydalaning:\n\n/vpn - kalit olish\n/donate - xayriya uchun\n/api - API dan foydalanish misollari",
    "donate": "loyihani qo'llab-quvvatlash",
    "api_intro": "bot VPN konfiguratsiyalarni taqdim etish uchun ochiq API dan foydalanadi, u har qanday vaqtda to'xtashi mumkin :)",
    "api_examples": "foydalanish misollari:",
    "api_response": "serverdan javob:",
    "key_generated": "kalit yaratildi!",
    "inline_get_title": "bepul VPN oling!",
    "inline_get_description": "VPN konfiguratsiyasini yaratish uchun bosing",
    "inline_error_title": "xato",
    "inline_get_error_description": "VPN yaratish muvaffaqiyatsiz",
    "check_error": "iltimos, buyruqdan keyin kalitni belgilang\n\nmisol:\n<code>/check https://vpn-telegram.com/config/...</code>",
    "check": lambda traffic, left, expires: f"ishlatilgan: {traffic} GB (qolgan {left})\namal qilish muddati: {expires}",
    "checking": "kalit tekshirilmoqda...",
    "inline_check_title": "VPN kalitni tekshirish",
    "inline_check_description": "kalit holatini bilish uchun bosing",
    "inline_check_error_description": "kalitni tekshirib bo'lmadi"
}

ukrainian = {
    "start": lambda name, keys: f"привіт {name}\n\n/vpn - отримати ключ\n/donate - для донатів\n/api - приклади використання API\n\nвсього бот видав <code>{keys}</code> ключів",
    "generation": "генерація ключа...",
    "key": lambda config_url, date, traffic: f"<b>твій ключ:</b>\n<code>{config_url}</code>\n\n<b>дійсний до:</b> {date}\n<b>трафік:</b> {traffic} ГБ",
    "error": lambda error_msg: f"помилка: <code>{error_msg}</code>",
    "any_message": "використовуй наступні команди:\n\n/vpn - отримати ключ\n/donate - для донатів\n/api - приклади використання API",
    "donate": "підтримати проект",
    "api_intro": "бот використовує публічний API для надання VPN конфігів, який може припинити роботу в будь-який момент :)",
    "api_examples": "приклади використання:",
    "api_response": "відповідь від сервера:",
    "key_generated": "ключ згенеровано!",
    "inline_get_title": "отримати безкоштовний VPN!",
    "inline_get_description": "натисніть щоб згенерувати VPN конфігурацію",
    "inline_error_title": "помилка",
    "inline_get_error_description": "не вдалося згенерувати VPN",
    "check_error": "будь ласка, вкажіть ключ після команди\n\nприклад:\n<code>/check https://vpn-telegram.com/config/...</code>",
    "check": lambda traffic, left, expires: f"використано: {traffic} ГБ (залишилося {left})\nдійсний до: {expires}",
    "checking": "перевірка ключа...",
    "inline_check_title": "перевірка VPN ключа",
    "inline_check_description": "натисніть щоб дізнатися статус ключа",
    "inline_check_error_description": "не вдалося перевірити ключ"
}

spanish = {
    "start": lambda name, keys: f"hola {name}\n\n/vpn - obtener una clave\n/donate - para donaciones\n/api - ejemplos de uso de API\n\nen total el bot ha emitido <code>{keys}</code> claves",
    "generation": "generando clave...",
    "key": lambda config_url, date, traffic: f"<b>tu clave:</b>\n<code>{config_url}</code>\n\n<b>válida hasta:</b> {date}\n<b>tráfico:</b> {traffic} GB",
    "error": lambda error_msg: f"error: <code>{error_msg}</code>",
    "any_message": "usa los siguientes comandos:\n\n/vpn - obtener una clave\n/donate - para donaciones\n/api - ejemplos de uso de API",
    "donate": "apoyar el proyecto",
    "api_intro": "el bot utiliza una API pública para proporcionar configuraciones VPN, que puede dejar de funcionar en cualquier momento :)",
    "api_examples": "ejemplos de uso:",
    "api_response": "respuesta del servidor:",
    "key_generated": "¡clave generada!",
    "inline_get_title": "¡obtener VPN gratis!",
    "inline_get_description": "haz clic para generar la configuración VPN",
    "inline_error_title": "error",
    "inline_get_error_description": "no se pudo generar VPN",
    "check_error": "por favor especifique la clave después del comando\n\nejemplo:\n<code>/check https://vpn-telegram.com/config/...</code>",
    "check": lambda traffic, left, expires: f"usado: {traffic} GB (quedan {left})\nválido hasta: {expires}",
    "checking": "verificando clave...",
    "inline_check_title": "verificación de clave VPN",
    "inline_check_description": "haz clic para verificar el estado de la clave",
    "inline_check_error_description": "no se pudo verificar la clave"
}

arabic = {
    "start": lambda name, keys: f"مرحباً {name}\n\n/vpn - احصل على مفتاح\n/donate - للتبرعات\n/api - أمثلة استخدام API\n\nإجمالاً أصدر البوت <code>{keys}</code> مفتاح",
    "generation": "جاري إنشاء المفتاح...",
    "key": lambda config_url, date, traffic: f"<b>مفتاحك:</b>\n<code>{config_url}</code>\n\n<b>صالح حتى:</b> {date}\n<b>الحركة المرورية:</b> {traffic} جيجابايت",
    "error": lambda error_msg: f"خطأ: <code>{error_msg}</code>",
    "any_message": "استخدم الأوامر التالية:\n\n/vpn - احصل على مفتاح\n/donate - للتبرعات\n/api - أمثلة استخدام API",
    "donate": "دعم المشروع",
    "api_intro": "يستخدم البوت واجهة برمجة تطبيقات عامة لتوفير تكوينات VPN، والتي قد تتوقف في أي وقت :)",
    "api_examples": "أمثلة الاستخدام:",
    "api_response": "الرد من الخادم:",
    "key_generated": "تم إنشاء المفتاح!",
    "inline_get_title": "احصل على VPN مجاني!",
    "inline_get_description": "انقر لإنشاء تكوين VPN",
    "inline_error_title": "خطأ",
    "inline_get_error_description": "فشل في إنشاء VPN",
    "check_error": "الرجاء تحديد المفتاح بعد الأمر\n\nمثال:\n<code>/check https://vpn-telegram.com/config/...</code>",
    "check": lambda traffic, left, expires: f"المستخدم: {traffic} جيجابايت (المتبقي {left})\nصالح حتى: {expires}",
    "checking": "جاري التحقق من المفتاح...",
    "inline_check_title": "فحص مفتاح VPN",
    "inline_check_description": "انقر للتحقق من حالة المفتاح",
    "inline_check_error_description": "فشل في التحقق من المفتاح"
}

chinese = {
    "start": lambda name, keys: f"你好 {name}\n\n/vpn - 获取密钥\n/donate - 捐赠\n/api - API使用示例\n\n机器人已累计发放 <code>{keys}</code> 个密钥",
    "generation": "正在生成密钥...",
    "key": lambda config_url, date, traffic: f"<b>你的密钥:</b>\n<code>{config_url}</code>\n\n<b>有效期至:</b> {date}\n<b>流量:</b> {traffic} GB",
    "error": lambda error_msg: f"错误: <code>{error_msg}</code>",
    "any_message": "使用以下命令:\n\n/vpn - 获取密钥\n/donate - 捐赠\n/api - API使用示例",
    "donate": "支持项目",
    "api_intro": "机器人使用公共API提供VPN配置，该API可能随时停止工作 :)",
    "api_examples": "使用示例:",
    "api_response": "服务器响应:",
    "key_generated": "密钥已生成!",
    "inline_get_title": "获取免费VPN!",
    "inline_get_description": "点击生成VPN配置",
    "inline_error_title": "错误",
    "inline_get_error_description": "生成VPN失败",
    "check_error": "请在命令后指定密钥\n\n示例:\n<code>/check https://vpn-telegram.com/config/...</code>",
    "check": lambda traffic, left, expires: f"已使用: {traffic} GB (剩余 {left})\n有效期至: {expires}",
    "checking": "正在检查密钥...",
    "inline_check_title": "VPN密钥检查",
    "inline_check_description": "点击查看密钥状态",
    "inline_check_error_description": "检查密钥失败"
}


def get_text(lang_code: str = None, text_key: str = "generation", **kwargs) -> str:

    languages = {
        "ru": russian,
        "en": english,
        "uz": uzbek,
        "uk": ukrainian,
        "es": spanish,
        "ar": arabic,
        "zh": chinese,
    }

    if not lang_code:
        selected_lang = english
    else:
        lang = lang_code.lower()
        selected_lang = english

        for prefix, lang_dict in languages.items():
            if lang.startswith(prefix):
                selected_lang = lang_dict
                break

    if text_key in selected_lang:
        text_func = selected_lang[text_key]

        if callable(text_func):
            return text_func(**kwargs)
        return text_func

    if text_key in english:
        text_func = english[text_key]
        if callable(text_func):
            return text_func(**kwargs)
        return text_func

    return f"[text not found: {text_key}]"