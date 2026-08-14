# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from gi import require_version

require_version("Gtk", "4.0")
require_version("Adw", "1")

from gi.repository import Adw, Gtk, GLib, Gdk
from eFatura       import e_fatura
from pathlib       import Path
import threading
import sys

class KekikGUIWindow(Adw.ApplicationWindow):
    def __init__(self, application: Adw.Application):
        super().__init__(
            application    = application,
            title          = "eFatura",
            default_width  = 420,
            default_height = 520,
            resizable      = True,
        )

        # HeaderBar Setup
        self.header_bar = Adw.HeaderBar()
        title_widget    = Adw.WindowTitle(
            title    = "eFatura",
            subtitle = "Mükellefiyet Sorgu Aracı",
        )
        self.header_bar.set_title_widget(title_widget)

        self.hakkinda_butonu = Gtk.Button.new_from_icon_name("help-about-symbolic")
        self.hakkinda_butonu.set_tooltip_text("Hakkında")
        self.hakkinda_butonu.connect("clicked", self.hakkinda_ac)
        self.header_bar.pack_end(self.hakkinda_butonu)

        # Main Layout Structure
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        main_box.append(self.header_bar)

        clamp       = Adw.Clamp(maximum_size=420)
        content_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        content_box.set_margin_start(20)
        content_box.set_margin_end(20)
        content_box.set_margin_top(20)
        content_box.set_margin_bottom(20)
        clamp.set_child(content_box)
        main_box.append(clamp)

        self.set_content(main_box)

        # Hero Header Banner
        hero_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        hero_box.set_halign(Gtk.Align.CENTER)
        hero_box.set_margin_bottom(8)

        hero_icon = Gtk.Image.new_from_icon_name("document-properties-symbolic")
        hero_icon.set_pixel_size(48)
        hero_icon.add_css_class("accent")
        hero_box.append(hero_icon)

        hero_title = Gtk.Label(label="E-Fatura Sorgulama")
        hero_title.add_css_class("title-2")
        hero_box.append(hero_title)

        hero_subtitle = Gtk.Label(
            label="Vergi veya TC Kimlik Numarası ile mükellefiyet durumunu sorgulayın."
        )
        hero_subtitle.add_css_class("caption")
        hero_subtitle.add_css_class("dim-label")
        hero_subtitle.set_wrap(True)
        hero_subtitle.set_justify(Gtk.Justification.CENTER)
        hero_box.append(hero_subtitle)

        content_box.append(hero_box)

        # Input Card Group (Adw.PreferencesGroup)
        input_group    = Adw.PreferencesGroup()
        self.arama_row = Adw.EntryRow(title="Vergi / TC Kimlik No")
        self.arama_row.connect("entry-activated", self.ara_butonuna_tiklandiginda)
        input_group.add(self.arama_row)
        content_box.append(input_group)

        # Action Button
        self.ara_butonu = Gtk.Button(label="Mükellefiyet Sorgula")
        self.ara_butonu.add_css_class("suggested-action")
        self.ara_butonu.add_css_class("pill")
        self.ara_butonu.connect("clicked", self.ara_butonuna_tiklandiginda)
        content_box.append(self.ara_butonu)

        # Result / Status Group (Adw.PreferencesGroup & Adw.ActionRow)
        self.sonuc_group = Adw.PreferencesGroup(title="Sorgu Sonucu")

        self.sonuc_row = Adw.ActionRow(
            title    = "Henüz Sorgulama Yapılmadı",
            subtitle = "Yukarıdaki alana numara girip sorgulama yapabilirsiniz.",
        )
        self.sonuc_icon = Gtk.Image.new_from_icon_name("info-symbolic")
        self.sonuc_row.add_prefix(self.sonuc_icon)

        self.spinner = Gtk.Spinner()
        self.spinner.set_visible(False)
        self.sonuc_row.add_suffix(self.spinner)

        self.sonuc_group.add(self.sonuc_row)
        content_box.append(self.sonuc_group)

    def ara_butonuna_tiklandiginda(self, widget):
        sorgu = self.arama_row.get_text().strip()
        if not sorgu:
            self.sonuc_row.set_title("Eksik Bilgi")
            self.sonuc_row.set_subtitle("Lütfen geçerli bir Vergi veya TC Kimlik Numarası girin.")
            self.sonuc_icon.set_from_icon_name("dialog-warning-symbolic")
            return

        # Loading State
        self.arama_row.set_sensitive(False)
        self.ara_butonu.set_sensitive(False)
        self.spinner.set_visible(True)
        self.spinner.start()

        self.sonuc_row.set_title(f"{sorgu} Sorgulanıyor...")
        self.sonuc_row.set_subtitle("Gelir İdaresi Başkanlığı sistemlerinden sorgu yapılıyor.")
        self.sonuc_icon.set_from_icon_name("network-transmit-receive-symbolic")

        threading.Thread(target=self._sorgula_arkaplanda, args=(sorgu,), daemon=True).start()

    def _sorgula_arkaplanda(self, sorgu: str):
        """GTK ana thread'ini bloklamadan arka planda sorgu çalıştırır."""
        try:
            sonuc = e_fatura(sorgu)
        except Exception:
            sonuc = None

        GLib.idle_add(self._sorgu_tamamlandi, sorgu, sonuc)

    def _sorgu_tamamlandi(self, sorgu: str, sonuc: bool | None):
        # Reset Loading State
        self.spinner.stop()
        self.spinner.set_visible(False)
        self.arama_row.set_sensitive(True)
        self.ara_butonu.set_sensitive(True)

        if sonuc is True:
            self.sonuc_row.set_title("E-Fatura Mükellefidir")
            self.sonuc_row.set_subtitle(f"{sorgu} numaralı mükellef E-Fatura sistemine kayıtlıdır.")
            self.sonuc_icon.set_from_icon_name("emblem-ok-symbolic")
        elif sonuc is False:
            self.sonuc_row.set_title("E-Fatura Mükellefi Değildir")
            self.sonuc_row.set_subtitle(f"{sorgu} numaralı kayıt E-Fatura mükellefleri arasında bulunamadı.")
            self.sonuc_icon.set_from_icon_name("dialog-error-symbolic")
        else:
            self.sonuc_row.set_title("Sorgulama Hatası")
            self.sonuc_row.set_subtitle(f"{sorgu} sorgulanırken bir ağ veya sunucu hatası oluştu.")
            self.sonuc_icon.set_from_icon_name("dialog-warning-symbolic")

        return GLib.SOURCE_REMOVE

    def hakkinda_ac(self, widget):
        dialog = Adw.AboutDialog(
            application_name = "eFatura Sorgu",
            developer_name   = "keyiflerolsun",
            version          = "1.1.8",
            comments         = "Vergi veya TC Kimlik Numarasından E-Fatura Mükellefiyet Sorgusu",
            website          = "https://keyiflerolsun.dev/Kahve",
            copyright        = "Copyright © 2023-2026 keyiflerolsun",
            license_type     = Gtk.License.GPL_3_0,
            developers       = ["keyiflerolsun"],
        )
        dialog.add_credit_section("Özel Teşekkürler", ["@KekikAkademi", "@KekikKahve"])
        dialog.present(self)

class KekikGUI(Adw.Application):
    def __init__(self):
        super().__init__(
            application_id = "org.kekikakademi.eFatura",
            flags          = 0,
        )
        Adw.StyleManager.get_default().set_color_scheme(Adw.ColorScheme.PREFER_DARK)

        # pip/uvx gibi izole venv'lere kurulunca ikon sys.prefix/share/icons
        # altına gidiyor ama bu, GTK'nın varsayılan icon theme arama
        # yollarında (XDG_DATA_DIRS) değil; burada elle ekliyoruz.
        icon_dir = Path(sys.prefix) / "share" / "icons"
        if icon_dir.is_dir():
            display = Gdk.Display.get_default()
            if display:
                Gtk.IconTheme.get_for_display(display).add_search_path(str(icon_dir))

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = KekikGUIWindow(application=self)
        win.present()

    def goster(self):
        self.run(None)
