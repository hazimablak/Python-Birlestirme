import json
import os

# Dosya İsimleri
TR_FILE = 'tr.json'
EN_FILE = 'en.json'
AR_FILE = 'ar.json'

def load_json(filename):
    print(f"📂 {filename} okunuyor...")
    if not os.path.exists(filename):
        print(f"❌ HATA: {filename} bulunamadı!")
        return None
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

try:
    # 1. Dosyaları Yükle
    tr_data = load_json(TR_FILE) # Bu bir LİSTE []
    en_data = load_json(EN_FILE) # Bu bir LİSTE []
    ar_data = load_json(AR_FILE) # Bu bir SÖZLÜK {} (Dictionary)

    if not tr_data or not en_data or not ar_data:
        raise Exception("Dosyalardan biri eksik.")

    print("✅ Dosyalar yüklendi. Veri yapıları dönüştürülüp birleştiriliyor...")

    combined_quran = []

    # 2. Ana döngüyü Türkçe/İngilizce listesi üzerinden kuralım
    # Çünkü onlar zaten sıralı ve ID'li.
    
    # Güvenlik önlemi: En kısa listenin uzunluğunu alalım
    limit = min(len(tr_data), len(en_data))

    for i in range(limit):
        tr = tr_data[i]
        en = en_data[i]
        
        # ID, Sure ve Ayet bilgilerini alalım
        # Senin TR dosyanın içinde bu bilgiler sayı (int) olarak var varsayıyoruz.
        sura_no = str(tr['sura']) # Arapça JSON'da anahtarlar string ("1" gibi)
        aya_no = str(tr['aya'])   # Arapça JSON'da anahtarlar string ("1" gibi)
        
        # 3. Arapça Sözlükten (Dictionary) Doğru Ayeti Çekelim
        # Mantık: ar_data["1"]["5"] -> 1. Sure, 5. Ayet metnini getir.
        
        ar_text = "Bulunamadı" # Varsayılan
        
        if sura_no in ar_data:
            if aya_no in ar_data[sura_no]:
                ar_text = ar_data[sura_no][aya_no]
            else:
                print(f"⚠️ Uyarı: Arapça veride Sure {sura_no} Ayet {aya_no} bulunamadı.")
        else:
             print(f"⚠️ Uyarı: Arapça veride Sure {sura_no} bulunamadı.")

        # 4. Birleştirilmiş Objeyi Oluştur
        unified_verse = {
            "id": tr.get('id', i+1),
            "sura": tr['sura'],
            "aya": tr['aya'],
            "text_ar": ar_text,     # Sözlükten çektiğimiz temiz Arapça
            "text_tr": tr['text'],  # Türkçe Meal
            "text_en": en['text']   # İngilizce Meal
        }
        
        combined_quran.append(unified_verse)

    # 5. Kaydet
    output_file = 'quran_unified.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(combined_quran, f, ensure_ascii=False, indent=2)

    print(f"\n🎉 MÜKEMMEL! Toplam {len(combined_quran)} ayet birleştirildi.")
    print(f"📂 Dosya oluşturuldu: {output_file}")
    
except Exception as e:
    print(f"\n❌ BİR HATA OLUŞTU: {e}")
    print("Hata Detayı: Özellikle 'sura' ve 'aya' alanlarının tr.json içinde doğru olduğundan emin ol.")