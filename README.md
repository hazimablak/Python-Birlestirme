# 📖 Quran Unified JSON Merger

A lightweight Python script that merges **Arabic, Turkish, and English Quran JSON files** into a single unified dataset.

---

## ✨ Features

- Combines 3 different JSON sources
- Supports:
  - 🇸🇦 Arabic text
  - 🇹🇷 Turkish translation
  - 🇬🇧 English translation
- Automatic verse matching by `sura` and `aya`
- Error & missing verse warnings
- Clean formatted output JSON

---

<details>
<summary>🇹🇷 Türkçe Açıklama</summary>

Bu proje, Kur’an-ı Kerim verilerini farklı dillerden tek bir JSON dosyasında birleştirir.

### Özellikler

- Arapça, Türkçe ve İngilizce verileri birleştirir
- Sure ve ayet numarasına göre eşleştirme yapar
- Eksik veriler için uyarı verir
- Düzenli ve okunabilir çıktı oluşturur

### Çıktı Örneği

```json
{
  "id": 1,
  "sura": 1,
  "aya": 1,
  "text_ar": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
  "text_tr": "Rahmân ve Rahîm olan Allah’ın adıyla.",
  "text_en": "In the name of Allah, the Entirely Merciful, the Especially Merciful."
}
```

</details>

---

## 🚀 Usage

```bash
python main.py
```

---

## 📂 Required Files

- `tr.json`
- `en.json`
- `ar.json`

---

## 📦 Output

```bash
quran_unified.json
```

---

## 🛠️ Technologies

- Python
- JSON
- File Processing

---

⭐ Feel free to fork and improve the project.
