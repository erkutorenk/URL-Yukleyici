from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):
    START_TEXT = """Merhaba {},\n
Ben bir URL Yükleyicisiyim!
Bu Botu kullanarak HTTP/HTTPS bağlantılarını yükleyebilirsiniz!"""
    FORMAT_SELECTION = """<b>İstenen formatı seçin:</b> 👇\n<u>belirtilen</u> <i>dosya boyutu yaklaşık olabilir.</i>"""
    SET_CUSTOM_USERNAME_PASSWORD = """\n\nBu videoyu indirmek istiyorsanız, aşağıdaki biçimi sağlayın:
    URL | dosyaadı | kullanıcıadı | parola"""
    DOWNLOAD_START = "<b>Dosya Adı:</b> {}\n\nİndiriliyor.. 📥"
    UPLOAD_START = "Yükleniyor.."
    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🏴‍☠ Kanal', url='https://t.me/torrentler'),
            InlineKeyboardButton('⚙ Ayarlar', callback_data='Settings')
        ], [
            InlineKeyboardButton('❔ Yardım Menüsü', callback_data='help')
        ]]
    )
    RCHD_TG_API_LIMIT = "{} saniye içinde İndirildi.\nAlgılanan Dosya Boyutu: {}\nÜzgünüm. Ancak, TELEGRAM API sınırlamaları nedeniyle 2GB'DEN büyük dosyaları yükleyemiyorum."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "{} saniye içinde İndirildi.\n{} saniye içinde yüklendi."
    SAVED_CUSTOM_THUMB_NAIL = "**✔️ Kapak fotoğrafı kaydedildi.**"
    DEL_ETED_CUSTOM_THUMB_NAIL = "**🗑️ Kapak fotoğrafı başarıyla temizlendi.**"
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "<b>YT-DLP</b>:\n{}"
    SETTINGS = "**Ayarlarlarınızı buradan yapabilirsiniz.**"
    HELP_TEXT = """Nasıl kullanılır? Aşağıdaki adımları izleyin!

1. URL gönderin.
2. Kapak fotoğrafı için fotoğraf gönderin. (İsteğe bağlı)
3. Buton seçin.
Bot cevap vermediyse @thebans ile iletişime geçin"""
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Geri', callback_data='home'),
            InlineKeyboardButton('✖ Kapat', callback_data='close')
        ]]
    )
    UPLOADER = "\n\n© {} tarafından {} kullanılarak yüklendi."
    THUMBNAIL_TEXT = "Thumbnail ayarlamak için bana herhangi bir fotoğraf gönderin."
    IFLONG_FILE_NAME = """Telegram tarafından izin verilen dosya adı sınırı {alimit} karakterdir.\n\nBana verilen dosya adında {num} karakter var.\nLütfen dosya adınızı kısaltın ve tekrar deneyin!"""
