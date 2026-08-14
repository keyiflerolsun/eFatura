# <a href="#"><img width="32" src="https://raw.githubusercontent.com/keyiflerolsun/eFatura/main/Shared/org.kekikakademi.eFatura.svg"></a> eFatura

[![Boyut](https://img.shields.io/github/repo-size/keyiflerolsun/eFatura?logo=git&logoColor=white&label=Boyut)](#)
[![Görüntülenme](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/keyiflerolsun/eFatura&title=Görüntülenme)](#)
<a href="https://KekikAkademi.org/Kahve" target="_blank"><img src="https://img.shields.io/badge/☕️-Kahve Ismarla-ffdd00" title="☕️ Kahve Ismarla" style="padding-left:5px;"></a>

[![GitHub](https://img.shields.io/github/v/release/keyiflerolsun/eFatura?logo=github&label=GitHub)](https://github.com/keyiflerolsun/eFatura/releases)
[![Fonksiyon Testleri ve PyPI Yükle](https://img.shields.io/github/actions/workflow/status/keyiflerolsun/eFatura/PyPI.yml?label=PyPI%20Y%C3%BCkleyici&logo=github)](https://github.com/keyiflerolsun/eFatura/actions/workflows/PyPI.yml)
[![Flatpak Yükleyici](https://img.shields.io/github/actions/workflow/status/keyiflerolsun/eFatura/flatpakYukle.yml?label=Flatpak%20Y%C3%BCkleyici&logo=github)](https://github.com/keyiflerolsun/eFatura/actions/workflows/flatpakYukle.yml)

[![FlatHub](https://img.shields.io/flathub/v/org.kekikakademi.eFatura?logo=flathub&logoColor=white&label=FlatHub)](https://flathub.org/tr/apps/org.kekikakademi.eFatura)
[![FlatHub - Yüklenme](https://img.shields.io/flathub/downloads/org.kekikakademi.eFatura?logo=flathub&logoColor=white&label=Yüklenme)](https://flathub.org/tr/apps/org.kekikakademi.eFatura)

[![PyPI](https://img.shields.io/pypi/v/eFatura?logo=pypi&logoColor=white&label=PyPI)](https://pypi.org/project/eFatura)
[![PyPI - Yüklenme](https://img.shields.io/pypi/dm/eFatura?logo=pypi&logoColor=white&label=Yüklenme)](https://pypi.org/project/eFatura)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/eFatura?logo=pypi&logoColor=white&label=Wheel)](https://pypi.org/project/eFatura)

[![Python Version](https://img.shields.io/pypi/pyversions/eFatura?logo=python&logoColor=white&label=Python)](#)
[![Lisans](https://img.shields.io/pypi/l/eFatura?logo=gnu&logoColor=white&label=Lisans)](#)
[![Durum](https://img.shields.io/pypi/status/eFatura?logo=windowsterminal&logoColor=white&label=Durum)](#)

*Vergi veya TC Kimlik Numarasından E-Fatura Mükellefiyet Sorgusu*

[![eFatura](https://raw.githubusercontent.com/keyiflerolsun/eFatura/main/.github/icons/SS.png)](#)

[![ForTheBadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](https://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/keyiflerolsun/)

## 🚀 Kurulum

### <a href="#"><img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/eFatura/main/.github/icons/pypi.svg"></a> PyPI (Lib - CLI - UI)

```bash
# Yüklemek
pip install eFatura

# Güncellemek
pip install -U eFatura
```

### <a href="#"><img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/eFatura/main/.github/icons/flathub.svg"></a> FlatHub (UI)

```bash
# Yüklemek
flatpak install flathub org.kekikakademi.eFatura

# Çalıştırmak
flatpak run org.kekikakademi.eFatura
```

## 📝 Kullanım

### <a href="#"><img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/eFatura/main/.github/icons/python.svg"></a> Lib

```python
from eFatura import e_fatura

print(e_fatura("11111111111")) # Vergi Numarası veya TC Kimlik Numarası

>> True | False
```

### <a href="#"><img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/eFatura/main/.github/icons/iterm2.svg"></a> CLI

```bash
eFatura 11111111111

# » [~] 11111111111 Numarası E-Fatura Mükellefi Değildir..
```

### <img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/eFatura/main/.github/icons/freedesktop.svg"> UI

```bash
eFaturaGUI

# veya

flatpak run org.kekikakademi.eFatura
```

---

<details>
    <summary style="font-weight: bold; font-size: 20px">
      <a href="#"><img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/eFatura/main/.github/icons/buddy.svg"></a> <b>Kendiniz Paketlemek İsterseniz</b>
      <i>(genişletmek için tıklayın!)</i>
    </summary>
    <br/>

### <a href="#"><img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/eFatura/main/.github/icons/python.svg"></a> Python

```bash
# Depoyu Çek
https://github.com/keyiflerolsun/eFatura.git
cd eFatura

# Paketi Yükle
pip install .

# Artıkları Temizle
rm -rf build *.egg-info

# Çalıştır
eFatura     # CLI
eFaturaGUI  # GUI

# Paketi Kaldır
pip uninstall eFatura
```

### <a href="#"><img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/eFatura/main/.github/icons/flatpak.svg"></a> FlatPak

```bash
# Depoyu Çek
git clone https://github.com/keyiflerolsun/eFatura.git
cd eFatura

# Gerekli Dosyaları Al
mv Shared/*.yml . && mv Shared/SRC .

# Gerekli Ortamları Kur
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak remote-add --if-not-exists flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo
flatpak update && flatpak upgrade
flatpak install flathub org.gnome.{Platform,Sdk}//50

# Paketle
flatpak-builder --user --install --force-clean build-dir org.kekikakademi.eFatura.yml

# Artıkları Temizle
rm -rf .flatpak* .vscode build-dir && find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

# Çalıştır
flatpak run org.kekikakademi.eFatura

# Paketi Kaldır
flatpak uninstall org.kekikakademi.eFatura
```

</details>

---

## 📝 Proje Sahibi

- ✅ **[kmprens/CheckEinvoice](https://github.com/kmprens/CheckEinvoice)**

## 🌐 Telif Hakkı ve Lisans

* *Copyright (C) 2023 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/keyiflerolsun/eFatura/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## ♻️ İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@keyiflerolsun](https://t.me/KekikKahve)

## 💸 Bağış Yap

**[☕️ Kahve Ismarla](https://KekikAkademi.org/Kahve)**

***

> **[@KekikAkademi](https://t.me/KekikAkademi)** *için yazılmıştır..*