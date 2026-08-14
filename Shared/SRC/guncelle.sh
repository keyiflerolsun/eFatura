#!/usr/bin/env bash
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.
# pyproject.toml bağımlılıklarından Shared/SRC/python3-requirements.yaml dosyasını dinamik günceller.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

echo "Flatpak Python bağımlılıkları pyproject.toml dosyasından güncelleniyor..."

# ! --runtime olmadan generator, host Python'unun (uv) wheel tag'lerini kullanır;
# ! GNOME Sdk runtime'ının Python sürümüyle uyuşmayabilir ve sdist derlemesine düşer.
# ! Bu yüzden flatpak + org.gnome.Sdk//50 kurulu olmalı (bkz: flatpakDepsGuncelle.yml).
# ! --prefer-wheels olmadan generator platform-specific paketler için (pillow gibi)
# ! wheel indirmiş olsa bile çıktıya sdist yazar; wheel isteyen paketler tek tek
# ! bu listeye eklenmeli.
uv run --with requirements-parser --with pyyaml \
  https://raw.githubusercontent.com/flatpak/flatpak-builder-tools/master/pip/flatpak-pip-generator.py \
  --pyproject-file "$PROJECT_ROOT/pyproject.toml" \
  --runtime org.gnome.Sdk//50 \
  --prefer-wheels pillow \
  --yaml --checker-data \
  --ignore-pkg pygobject \
  -o "$SCRIPT_DIR/python3-requirements.yaml"

echo "Güncelleme tamamlandı: Shared/SRC/python3-requirements.yaml"
