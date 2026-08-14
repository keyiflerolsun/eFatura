# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from ..Libs.Oturum import legacy_session
from pathlib       import Path
from shutil        import copyfileobj
from PIL           import Image
from pytesseract   import image_to_string
import tempfile

def e_fatura(vergi_numarasi: str) -> bool:
    """Vergi veya TC Kimlik Numarasından E-Fatura Mükellefiyet Sorgusu"""
    user_agent = (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    while True:
        oturum = legacy_session()
        oturum.headers.update({"User-Agent": user_agent})

        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_captcha:
            captcha_path = Path(temp_captcha.name)
            try:
                captcha_istek = oturum.get(
                    "https://sorgu.efatura.gov.tr/kullanicilar/img.php",
                    stream  = True,
                    timeout = 10,
                )
                copyfileobj(captcha_istek.raw, temp_captcha)
                temp_captcha.flush()

                captcha_metni = image_to_string(Image.open(captcha_path)).strip()
            finally:
                if captcha_path.exists():
                    captcha_path.unlink(missing_ok=True)

        e_fatura_istek = oturum.post(
            url  = "https://sorgu.efatura.gov.tr/kullanicilar/xliste.php",
            data = {
                "search_string" : str(vergi_numarasi),
                "captcha_code"  : str(captcha_metni),
                "submit"        : "Ara",
            },
            timeout=15,
        )

        if "Güvenlik kodu hatalı" in e_fatura_istek.text:
            continue

        return "Mükellef kayıtlıdır" in e_fatura_istek.text
