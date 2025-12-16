russian = {
    "start": lambda name, keys: f"привет {name}\n\n/vpn - получить ключ\n/donate - для донатов\n/api - примеры использования API\n/check [ключ] - проверить статус ключа\n/instruction - инструкция для подключения VPN\n\nвсего бот выдал <code>{keys}</code> ключей",
    "generation": "генерация ключа...",
    "key": lambda config_url, date, traffic: f"<b>твой ключ:</b>\n<code>{config_url}</code>\n\n<b>действителен до:</b> {date}\n<b>трафик:</b> {traffic} ГБ",
    "error": lambda error_msg: f"ошибка: <code>{error_msg}</code>",
    "any_message": "используй следующие команды:\n\n/vpn - получить ключ\n/donate - для донатов\n/api - примеры использования API\n/check [ключ] - проверить статус ключа\n/instruction - инструкция для подключения VPN",
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
    "inline_check_error_description": "не удалось проверить ключ",
    "instruction": lambda name: f"{name}, выбери свою платформу:",
    "android": "переходим в play market и скачиваем клиент hiddify\n\nпосле запуска клиента нажимаем на "+" в правом верхнем углу\n\nдобавляем ссылку которую вы получили от бота, жмем кнопку подключения",
    "ios": "переходим в app store и скачиваем клиент v2ray\n\nпосле запуска клиента нажимаем на "+" в правом верхнем углу\n\nдобавляем ссылку которую вы получили от бота, жмем кнопку подключения",
    "windows": "переходим на github и скачиваем клиент hiddify\n\nпосле установки открываем файл, в открывшемся клиенте нажимаем на "+" в правом верхнем углу\n\nдобавляем ссылку которую вы получили от бота, жмем кнопку подключения",
    "macos": "переходим в app store и скачиваем клиент streisand\n\nпосле запуска клиента нажимаем на "+" в правом верхнем углу\n\nдобавляем ссылку которую вы получили от бота, жмем кнопку подключения",
    "linux": "переходим на github и скачиваем клиент happ\n\nпосле установки открываем файл, в открывшемся клиенте нажимаем на "+" в правом верхнем углу\n\nдобавляем ссылку которую вы получили от бота, жмем кнопку подключения",
}

english = {
    "start": lambda name, keys: f"hi {name}\n\n/vpn - get a key\n/donate - for donations\n/api - examples of use API\n/check [key] - check key status\n/instruction - connection instructions\n\nin total the bot issued <code>{keys}</code> keys",
    "generation": "generating a key...",
    "key": lambda config_url, date, traffic: f"<b>your key:</b>\n<code>{config_url}</code>\n\n<b>valid until:</b> {date}\n<b>traffic:</b> {traffic} GB",
    "error": lambda error_msg: f"error: <code>{error_msg}</code>",
    "any_message": "use the following commands:\n\n/vpn - get a key\n/donate - for donations\n/api - examples of use API\n/check [key] - check key status\n/instruction - connection instructions",
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
    "check": lambda traffic, left, expires: f"<b>used:</b> {traffic} GB\n<b>left:</b> {left} GB\n<b>valid until:</b> {expires}",
    "checking": "checking key...",
    "inline_check_title": "VPN key check",
    "inline_check_description": "click to check key status",
    "inline_check_error_description": "failed to check key",
    "instruction": lambda name: f"{name}, select your platform:",
    "android": "go to play market and download hiddify client\n\nafter launching the client, click on "+" in the top right corner\n\nadd the link you received from the bot, click the connect button",
    "ios": "go to app store and download v2ray client\n\nafter launching the client, click on "+" in the top right corner\n\nadd the link you received from the bot, click the connect button",
    "windows": "go to github and download hiddify client\n\nafter installation, open the file, in the opened client click on "+" in the top right corner\n\nadd the link you received from the bot, click the connect button",
    "macos": "go to app store and download streisand client\n\nafter launching the client, click on "+" in the top right corner\n\nadd the link you received from the bot, click the connect button",
    "linux": "go to github and download happ client\n\nafter installation, open the file, in the opened client click on "+" in the top right corner\n\nadd the link you received from the bot, click the connect button",
}

uzbek = {
    "start": lambda name, keys: f"salom {name}\n\n/vpn - kalit olish\n/donate - xayriya uchun\n/api - API dan foydalanish misollari\n/check [kalit] - kalit holatini tekshirish\n/instruction - ulanish bo'yicha ko'rsatma\n\njami bot <code>{keys}</code> ta kalit berdi",
    "generation": "kalit yaratilmoqda...",
    "key": lambda config_url, date, traffic: f"<b>sizning kalitingiz:</b>\n<code>{config_url}</code>\n\n<b>amal qilish muddati:</b> {date}\n<b>trafik:</b> {traffic} GB",
    "error": lambda error_msg: f"xato: <code>{error_msg}</code>",
    "any_message": "quyidagi buyruqlardan foydalaning:\n\n/vpn - kalit olish\n/donate - xayriya uchun\n/api - API dan foydalanish misollari\n/check [kalit] - kalit holatini tekshirish\n/instruction - ulanish bo'yicha ko'rsatma",
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
    "check": lambda traffic, left, expires: f"<b>ishlatilgan:</b> {traffic} GB\n<b>qolgan:</b> {left} GB\n<b>amal qilish muddati:</b> {expires}",
    "checking": "kalit tekshirilmoqda...",
    "inline_check_title": "VPN kalitni tekshirish",
    "inline_check_description": "kalit holatini bilish uchun bosing",
    "inline_check_error_description": "kalitni tekshirib bo'lmadi",
    "instruction": lambda name: f"{name}, platformangizni tanlang:",
    "android": "play market-ga o'ting va hiddify mijozini yuklab oling\n\nmijozni ishga tushirgandan so'ng, yuqori o'ng burchakdagi "+" tugmasini bosing\n\nbotdan olgan havolangizni qo'shing, ulanish tugmasini bosing",
    "ios": "app store-ga o'ting va v2ray mijozini yuklab oling\n\nmijozni ishga tushirgandan so'ng, yuqori o'ng burchakdagi "+" tugmasini bosing\n\nbotdan olgan havolangizni qo'shing, ulanish tugmasini bosing",
    "windows": "github-ga o'ting va hiddify mijozini yuklab oling\n\no'rnatishdan so'ng, faylni oching, ochilgan mijozda yuqori o'ng burchakdagi "+" tugmasini bosing\n\nbotdan olgan havolangizni qo'shing, ulanish tugmasini bosing",
    "macos": "app store-ga o'ting va streisand mijozini yuklab oling\n\nmijozni ishga tushirgandan so'ng, yuqori o'ng burchakdagi "+" tugmasini bosing\n\nbotdan olgan havolangizni qo'shing, ulanish tugmasini bosing",
    "linux": "github-ga o'ting va happ mijozini yuklab oling\n\no'rnatishdan so'ng, faylni oching, ochilgan mijozda yuqori o'ng burchakdagi "+" tugmasini bosing\n\nbotdan olgan havolangizni qo'shing, ulanish tugmasini bosing",
}

ukrainian = {
    "start": lambda name, keys: f"привіт {name}\n\n/vpn - отримати ключ\n/donate - для донатів\n/api - приклади використання API\n/check [ключ] - перевірити статус ключа\n/instruction - інструкція для підключення VPN\n\nвсього бот видав <code>{keys}</code> ключів",
    "generation": "генерація ключа...",
    "key": lambda config_url, date, traffic: f"<b>твій ключ:</b>\n<code>{config_url}</code>\n\n<b>дійсний до:</b> {date}\n<b>трафік:</b> {traffic} ГБ",
    "error": lambda error_msg: f"помилка: <code>{error_msg}</code>",
    "any_message": "використовуй наступні команди:\n\n/vpn - отримати ключ\n/donate - для донатів\n/api - приклади використання API\n/check [ключ] - перевірити статус ключа\n/instruction - інструкція для підключення VPN",
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
    "check": lambda traffic, left, expires: f"<b>використано:</b> {traffic} ГБ\n<b>залишилося:</b> {left} ГБ\n<b>дійсний до:</b> {expires}",
    "checking": "перевірка ключа...",
    "inline_check_title": "перевірка VPN ключа",
    "inline_check_description": "натисніть щоб дізнатися статус ключа",
    "inline_check_error_description": "не вдалося перевірити ключ",
    "instruction": lambda name: f"{name}, вибери свою платформу:",
    "android": "переходимо в play market і завантажуємо клієнт hiddify\n\nпісля запуску клієнта натискаємо на "+" у правому верхньому куті\n\nдодаємо посилання яке ви отримали від бота, натискаємо кнопку підключення",
    "ios": "переходимо в app store і завантажуємо клієнт v2ray\n\nпісля запуску клієнта натискаємо на "+" у правому верхньому куті\n\nдодаємо посилання яке ви отримали від бота, натискаємо кнопку підключення",
    "windows": "переходимо на github і завантажуємо клієнт hiddify\n\nпісля встановлення відкриваємо файл, у відкритому клієнті натискаємо на "+" у правому верхньому куті\n\nдодаємо посилання яке ви отримали від бота, натискаємо кнопку підключення",
    "macos": "переходимо в app store і завантажуємо клієнт streisand\n\nпісля запуску клієнта натискаємо на "+" у правому верхньому куті\n\nдодаємо посилання яке ви отримали від бота, натискаємо кнопку підключення",
    "linux": "переходимо на github і завантажуємо клієнт happ\n\nпісля встановлення відкриваємо файл, у відкритому клієнті натискаємо на "+" у правому верхньому куті\n\nдодаємо посилання яке ви отримали від бота, натискаємо кнопку підключення",
}

spanish = {
    "start": lambda name, keys: f"hola {name}\n\n/vpn - obtener una clave\n/donate - para donaciones\n/api - ejemplos de uso de API\n/check [clave] - verificar estado de clave\n/instruction - instrucción para conectar VPN\n\nen total el bot ha emitido <code>{keys}</code> claves",
    "generation": "generando clave...",
    "key": lambda config_url, date, traffic: f"<b>tu clave:</b>\n<code>{config_url}</code>\n\n<b>válida hasta:</b> {date}\n<b>tráfico:</b> {traffic} GB",
    "error": lambda error_msg: f"error: <code>{error_msg}</code>",
    "any_message": "usa los siguientes comandos:\n\n/vpn - obtener una clave\n/donate - para donaciones\n/api - ejemplos de uso de API\n/check [clave] - verificar estado de clave\n/instruction - instrucción para conectar VPN",
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
    "check": lambda traffic, left, expires: f"<b>usado:</b> {traffic} GB\n<b>restante:</b> {left} GB\n<b>válido hasta:</b> {expires}",
    "checking": "verificando clave...",
    "inline_check_title": "verificación de clave VPN",
    "inline_check_description": "haz clic para verificar el estado de la clave",
    "inline_check_error_description": "no se pudo verificar la clave",
    "instruction": lambda name: f"{name}, selecciona tu plataforma:",
    "android": "ve a play market y descarga el cliente hiddify\n\ndespués de iniciar el cliente, haz clic en "+" en la esquina superior derecha\n\nagrega el enlace que recibiste del bot, haz clic en el botón de conexión",
    "ios": "ve a app store y descarga el cliente v2ray\n\ndespués de iniciar el cliente, haz clic en "+" en la esquina superior derecha\n\nagrega el enlace que recibiste del bot, haz clic en el botón de conexión",
    "windows": "ve a github y descarga el cliente hiddify\n\ndespués de la instalación, abre el archivo, en el cliente abierto haz clic en "+" en la esquina superior derecha\n\nagrega el enlace que recibiste del bot, haz clic en el botón de conexión",
    "macos": "ve a app store y descarga el cliente streisand\n\ndespués de iniciar el cliente, haz clic en "+" en la esquina superior derecha\n\nagrega el enlace que recibiste del bot, haz clic en el botón de conexión",
    "linux": "ve a github y descarga el cliente happ\n\ndespués de la instalación, abre el archivo, en el cliente abierto haz clic en "+" en la esquina superior derecha\n\nagrega el enlace que recibiste del bot, haz clic en el botón de conexión",
}

arabic = {
    "start": lambda name, keys: f"مرحباً {name}\n\n/vpn - احصل على مفتاح\n/donate - للتبرعات\n/api - أمثلة استخدام API\n/check [مفتاح] - التحقق من حالة المفتاح\n/instruction - تعليمات الاتصال بـ VPN\n\nإجمالاً أصدر البوت <code>{keys}</code> مفتاح",
    "generation": "جاري إنشاء المفتاح...",
    "key": lambda config_url, date, traffic: f"<b>مفتاحك:</b>\n<code>{config_url}</code>\n\n<b>صالح حتى:</b> {date}\n<b>الحركة المرورية:</b> {traffic} جيجابايت",
    "error": lambda error_msg: f"خطأ: <code>{error_msg}</code>",
    "any_message": "استخدم الأوامر التالية:\n\n/vpn - احصل على مفتاح\n/donate - للتبرعات\n/api - أمثلة استخدام API\n/check [مفتاح] - التحقق من حالة المفتاح\n/instruction - تعليمات الاتصال بـ VPN",
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
    "check": lambda traffic, left, expires: f"<b>المستخدم:</b> {traffic} جيجابايت\n<b>المتبقي:</b> {left} جيجابايت\n<b>صالح حتى:</b> {expires}",
    "checking": "جاري التحقق من المفتاح...",
    "inline_check_title": "فحص مفتاح VPN",
    "inline_check_description": "انقر للتحقق من حالة المفتاح",
    "inline_check_error_description": "فشل في التحقق من المفتاح",
    "instruction": lambda name: f"{name}، اختر منصتك:",
    "android": "اذهب إلى play market وقم بتنزيل عميل hiddify\n\nبعد تشغيل العميل، انقر على "+" في الزاوية اليمنى العليا\n\nأضف الرابط الذي تلقته من البوت، انقر على زر الاتصال",
    "ios": "اذهب إلى app store وقم بتنزيل عميل v2ray\n\nبعد تشغيل العميل، انقر على "+" في الزاوية اليمنى العليا\n\nأضف الرابط الذي تلقته من البوت، انقر على زر الاتصال",
    "windows": "اذهب إلى github وقم بتنزيل عميل hiddify\n\nبعد التثبيت، افتح الملف، في العميل المفتوح انقر على "+" في الزاوية اليمنى العليا\n\nأضف الرابط الذي تلقته من البوت، انقر على زر الاتصال",
    "macos": "اذهب إلى app store وقم بتنزيل عميل streisand\n\nبعد تشغيل العميل، انقر على "+" في الزاوية اليمنى العليا\n\nأضف الرابط الذي تلقته من البوت، انقر على زر الاتصال",
    "linux": "اذهب إلى github وقم بتنزيل عميل happ\n\nبعد التثبيت، افتح الملف، في العميل المفتوح انقر على "+" في الزاوية اليمنى العليا\n\nأضف الرابط الذي تلقته من البوت، انقر على زر الاتصال",
}

chinese = {
    "start": lambda name, keys: f"你好 {name}\n\n/vpn - 获取密钥\n/donate - 捐赠\n/api - API使用示例\n/check [密钥] - 检查密钥状态\n/instruction - VPN连接说明\n\n机器人已累计发放 <code>{keys}</code> 个密钥",
    "generation": "正在生成密钥...",
    "key": lambda config_url, date, traffic: f"<b>你的密钥:</b>\n<code>{config_url}</code>\n\n<b>有效期至:</b> {date}\n<b>流量:</b> {traffic} GB",
    "error": lambda error_msg: f"错误: <code>{error_msg}</code>",
    "any_message": "使用以下命令:\n\n/vpn - 获取密钥\n/donate - 捐赠\n/api - API使用示例\n/check [密钥] - 检查密钥状态\n/instruction - VPN连接说明",
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
    "check": lambda traffic, left, expires: f"<b>已使用:</b> {traffic} GB\n<b>剩余:</b> {left} GB\n<b>有效期至:</b> {expires}",
    "checking": "正在检查密钥...",
    "inline_check_title": "VPN密钥检查",
    "inline_check_description": "点击查看密钥状态",
    "inline_check_error_description": "检查密钥失败",
    "instruction": lambda name: f"{name}，选择你的平台:",
    "android": "前往play市场下载hiddify客户端\n\n启动客户端后，点击右上角的"+"\n\n添加从机器人收到的链接，点击连接按钮",
    "ios": "前往app store下载v2ray客户端\n\n启动客户端后，点击右上角的"+"\n\n添加从机器人收到的链接，点击连接按钮",
    "windows": "前往github下载hiddify客户端\n\n安装后打开文件，在打开的客户端中点击右上角的"+"\n\n添加从机器人收到的链接，点击连接按钮",
    "macos": "前往app store下载streisand客户端\n\n启动客户端后，点击右上角的"+"\n\n添加从机器人收到的链接，点击连接按钮",
    "linux": "前往github下载happ客户端\n\n安装后打开文件，在打开的客户端中点击右上角的"+"\n\n添加从机器人收到的链接，点击连接按钮",
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