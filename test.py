import json
import os

def dosya_kontrol(dosya_adi):
    print(f"\n--- {dosya_adi} Kontrol Ediliyor ---")
    
    # 1. Dosya var mı?
    if not os.path.exists(dosya_adi):
        print(f"❌ HATA: '{dosya_adi}' klasörde bulunamadı!")
        return

    # 2. Dosya okunabiliyor mu?
    try:
        with open(dosya_adi, 'r', encoding='utf-8') as f:
            icerik = f.read().strip() # Boşlukları temizle
            
        print(f"📄 Karakter Sayısı: {len(icerik)}")
        if len(icerik) > 20:
            print(f"👀 Başlangıç: {icerik[:20]}...")
        else:
            print(f"👀 İçerik: {icerik}")

        if not icerik:
            print("❌ HATA: Dosya tamamen BOŞ!")
            return

        # 3. JSON geçerli mi?
        json.loads(icerik)
        print("✅ BAŞARILI: Bu dosya sağlam.")
        
    except json.JSONDecodeError as e:
        print(f"❌ JSON FORMAT HATASI: {e}")
        print("💡 İPUCU: Dosyanın en başında [ ve sonunda ] olduğundan ve çift tırnak kullandığından emin ol.")
    except Exception as e:
        print(f"❌ GENEL HATA: {e}")

# Sırayla kontrol et
dosya_kontrol('tr.json')
dosya_kontrol('en.json')