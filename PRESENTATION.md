# Sunum İçeriği Taslağı (15 Sayfa)

Bu dosya, proje sunumu için hazırlanmış metinleri ve görsel önerilerini içerir. Powerpoint veya PDF sunumu hazırlarken bu metinleri kopyalayıp kullanabilirsiniz.

---

### Sayfa 1: Kapak
**Başlık:** Python ile Yılan Oyunu Geliştirme: Veri Yapıları Uygulaması
**Alt Başlık:** Linked List Implementasyonu ve Oyun Algoritmaları
**Görsel:** Oyunun başlangıç ekranından renkli bir ekran görüntüsü, ortada "Snake Game" yazısı.

---

### Sayfa 2: Projenin Amacı
**Metin:**
Bu projenin temel amacı, teorik olarak öğrenilen **Veri Yapıları (Data Structures)** konusunu, eğlenceli ve interaktif bir uygulama olan Yılan Oyunu (Snake Game) üzerinde hayata geçirmektir. Özellikle **Bağlı Liste (Linked List)** yapısının dinamik bellek yönetimi üzerindeki avantajlarını göstermek hedeflenmiştir.

**Görsel:** Bir yanda teorik Linked List şeması (Node -> Node -> Node), diğer yanda yılanın kıvrımlı görüntüsü.

---

### Sayfa 3: Kullanılan Teknolojiler
**Metin:**
- **Dil:** Python 3.11 (Okunabilirlik ve hızlı prototipleme için)
- **Kütüphane:** Pygame (Oyun döngüsü, grafik çizimi ve giriş kontrolü için)
- **Veri Kaydı:** JSON (Yüksek skorları kalıcı olarak tutmak için)

**Görsel:** Python ve Pygame logolarının yan yana durduğu bir görsel.

---

### Sayfa 4: Oyun Mimarisi (Genel Bakış)
**Metin:**
Proje modüler bir yapıda tasarlanmıştır:
1. **main.py:** Oyunun ana döngüsü ve giriş noktası.
2. **game_logic.py:** Oyun kuralları (yem yeme, çarpışma, seviye).
3. **snake_ll.py:** Yılanın veri yapısı (Linked List).
4. **utils.py:** Renkler ve sabit ayarlar.

**Görsel:** Dosyaların birbirine oklarla bağlandığı basit bir akış diyagramı.

---

### Sayfa 5: Neden Linked List?
**Metin:**
Yılan oyunu doğası gereği bir "Kuyruk" (Queue) yapısına benzer.
- **Problem:** Dizi (Array) kullansaydık, yılan hareket ettiğinde tüm gövde parçalarını dizide kaydırmamız gerekirdi. Bu işlem maliyetlidir.
- **Çözüm:** Linked List ile sadece **Başa Ekle (Head Insertion)** ve **Sondan Sil (Tail Deletion)** işlemleri yaparız. Ara elemanlara dokunmayız.

**Görsel:** Array vs Linked List karşılaştırma tablosu (Hız/Performans odaklı).

---

### Sayfa 6: Node (Düğüm) Yapısı
**Metin:**
Her bir yılan parçası bir `Node` objesidir.
```python
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
```
Her düğüm, kendi koordinatını ve kendinden sonraki parçanın adresini tutar.

**Görsel:** `snake_ll.py` dosyasındaki `Node` sınıfının ekran görüntüsü.

---

### Sayfa 7: Hareket Algoritması (Move)
**Metin:**
Yılanın hareketi bir illüzyondur. Gövde komple hareket etmez:
1. Gidilen yönde yeni bir kafa (Node) oluşturulur.
2. Bu yeni kafa, listenin başına eklenir.
3. Listenin en sonundaki kuyruk (Tail) silinir.
Sonuç: Yılan bir kare ilerlemiş gibi görünür.

**Görsel:** Hareket mantığını gösteren adım adım şematik çizim (Before Move -> After Move).

---

### Sayfa 8: Büyüme Mantığı (Grow)
**Metin:**
Yılan yem yediğinde boyunun uzaması gerekir.
- Normal harekette kuyruk silinirken, yem yendiği turda **kuyruk silinmez**.
- Böylece başa bir eleman eklenmiş olur, kuyruk aynı kalır ve toplam uzunluk +1 artar.

**Görsel:** Yılanın elmayı yediği an ve boyunun uzadığını gösteren oyun içi ekran görüntüsü.

---

### Sayfa 9: Yem Oluşturma (Spawn Food)
**Metin:**
Yem, ekranda rastgele bir koordinatta oluşturulur.
**Önemli Detay:** Yem oluşturulurken, koordinatın yılanın gövdesi üzerine gelip gelmediği kontrol edilir. Eğer çakışma varsa, boş bir yer bulunana kadar tekrar rastgele koordinat seçilir.

**Görsel:** `spawn_food` fonksiyonunun kod bloğu görüntüsü.

---

### Sayfa 10: Çarpışma Kontrolü (Collision)
**Metin:**
Oyunun bitme koşulları:
1. **Duvar:** Yılanın başı ekran sınırlarının dışına çıkarsa.
2. **Kendisi:** Yılanın başı, gövdesindeki herhangi bir Node ile aynı koordinata gelirse.
Bu kontroller her karede (frame) yapılır.

**Görsel:** Oyunun "Game Over" ekranının görüntüsü.

---

### Sayfa 11: Seviye ve Hız Sistemi
**Metin:**
Oyunun zorluğunu artırmak için seviye sistemi eklendi.
- Başlangıç hızı: 5 FPS.
- Her **50 puanda** bir seviye atlanır.
- Her seviye atlayışında oyun hızı artar, böylece refleks gereksinimi yükselir.

**Görsel:** Ekranın sol üst köşesindeki "Level: 3" ve "Score: 120" yazılarının olduğu bir kesit.

---

### Sayfa 12: High Score (JSON Yönetimi)
**Metin:**
Oyuncunun motivasyonunu artırmak için en yüksek skor kaydedilir.
- Oyun açıldığında `high_score.json` dosyası okunur.
- Oyun bittiğinde, eğer yeni skor eskiden büyükse JSON dosyası güncellenir.
Bu sayede oyunu kapatıp açsanız bile rekorunuz kaybolmaz.

**Görsel:** `load_high_score` ve `save_high_score` fonksiyon kodları ve oluşturulan `.json` dosya içeriği.

---

### Sayfa 13: Görsel Tasarım ve Animasyon
**Metin:**
Google Snake oyunundan esinlenildi.
- **Damalı Zemin:** Gözü yormayan açık ve koyu yeşil tonlar.
- **Yılan:** Gövde ve baş için farklı renkler, yön belirten göz çizimleri.
- **Smoothness:** Pygame'in sağladığı akıcı çizim yetenekleri kullanıldı.

**Görsel:** Oyun çalışırken çekilmiş, yılanın kıvrıldığı estetik bir ekran görüntüsü.

---

### Sayfa 14: Karşılaşılan Zorluklar ve Çözümler
**Metin:**
- **Zorluk:** Yılanın kendi içine girmesi (Örn: Yukarı giderken aşağı basılması).
- **Çözüm:** Klavye girdileri işlenirken mevcut yönün zıttına izin verilmedi.
- **Zorluk:** Hızlı tuş basımlarında yılanın yön şaşırması.
- **Çözüm:** Input buffer mantığı veya anlık yön kontrolü ile çözüldü.

**Görsel:** Yılanın "U" dönüşü yaptığı bir anın çizimi.

---

### Sayfa 15: Sonuç ve Gelecek Geliştirmeler
**Metin:**
Bu proje ile Linked List yapısının oyun geliştirmede ne kadar efektif kullanılabileceği gösterildi.
**Gelecek Planları:**
- Ses efektleri eklenmesi.
- Engel bloklarının eklenmesi.
- İki kişilik oyun modu.

**Görsel:** "Teşekkürler" yazısı ve GitHub repo linki (varsayalım) olan kapanış slaytı.
