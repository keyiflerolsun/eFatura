# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from sys     import argv
from eFatura import e_fatura
from .Libs   import konsol

def basla() -> None:
    """Konsol üzerinden E-Fatura mükellefiyet sorgusu çalıştırır."""
    print()

    if len(argv) != 2:
        konsol.print("[bold yellow2][!] Lütfen Vergi Numarası veya TC Kimlik Numarası Belirtin..[/]")
        konsol.print("\n[turquoise2]Örn.: [pale_green1]eFatura 11111111111[/]\n")
        return

    vergi_numarasi = argv[1].strip()

    with konsol.status(f"[bold yellow]{vergi_numarasi}[/] sorgulanıyor..."):
        sonuc = e_fatura(vergi_numarasi)

    if sonuc:
        konsol.print(f"[green][+] [light_coral]{vergi_numarasi}[/] Numarası E-Fatura Mükellefidir..\n")
    else:
        konsol.print(f"[red][~] [light_coral]{vergi_numarasi}[/] Numarası E-Fatura Mükellefi Değildir..\n")

if __name__ == "__main__":
    basla()
