# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from .GUI import KekikGUI

def basla() -> None:
    """eFatura GTK 4 + Libadwaita grafik arayüz uygulamasını başlatır."""
    arayuz = KekikGUI()
    arayuz.goster()

if __name__ == "__main__":
    basla()
