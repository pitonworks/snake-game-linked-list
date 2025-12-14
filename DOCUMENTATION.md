# Python Snake Game with Linked List - Proje Dokümantasyonu

Bu proje, Python programlama dili ve Pygame kütüphanesi kullanılarak geliştirilmiş klasik bir Yılan (Snake) oyunudur. Projenin ana amacı, **Linked List (Bağlı Liste)** veri yapısının gerçek bir uygulama üzerinde nasıl kullanıldığını göstermektir.

## Kurulum ve Çalıştırma

1. Python'un yüklü olduğundan emin olun.
2. Gerekli kütüphaneyi yükleyin:
   ```bash
   pip install pygame
   ```
3. Oyunu başlatın:
   ```bash
   python main.py
   ```

## Proje Yapısı

### 1. `snake_ll.py` (Linked List Implementasyonu)
Yılanın gövdesi, dinamik bir veri yapısı olan **Singly Linked List** ile temsil edilmiştir.
- **Node Sınıfı:** Her bir yılan parçasını (koordinatlarını) ve bir sonraki parçayı (`next`) tutar.
- **SnakeLinkedList Sınıfı:**
    - `head`: Yılanın başı (hareket yönüne göre yeni node eklenen yer).
    - `tail`: Yılanın kuyruğu (her adımda silinen yer).
    - `move()`: Başa yeni bir düğüm ekler (Head Insertion) ve eğer yem yenmediyse kuyruğu siler (Tail Deletion). Bu işlem **O(1)** karmaşıklığında yapılmaya çalışılır (kuyruk pointer'ı tutarak).
    - `grow()`: Yılanın büyümesini sağlar (kuyruk silme işlemini bir adım atlar).

### 2. `game_logic.py` (Oyun Mantığı)
Oyunun kuralları burada işlenir.
- **Game Sınıfı:**
    - `spawn_food()`: Yılanın üzerine gelmeyecek şekilde rastgele yem oluşturur.
    - `check_collisions()`: Duvarlara veya yılanın kendisine çarpıp çarpmadığını kontrol eder.
    - `update()`: Oyun döngüsünün mantıksal güncelleme adımıdır.
    - **Seviye Sistemi:** Her 50 puanda bir seviye artar ve oyun hızı (`FPS`) yükselir.
    - **High Score:** `high_score.json` dosyasında en yüksek skor saklanır.

### 3. `utils.py` (Sabitler)
Oyunun renkleri, ekran boyutları ve yön vektörleri gibi sabit değerler burada tutulur. Bu sayede tasarım değişiklikleri tek bir dosyadan yönetilebilir.

## Algoritma Detayları

### Neden Linked List?
Yılan oyunu, veri yapısı derslerinde **Queue (Kuyruk)** veya **Linked List** mantığını anlatmak için mükemmel bir örnektir.
- Yılan hareket ettiğinde, aslında baş tarafına yeni bir kare eklenir ve kuyruk tarafından bir kare silinir.
- Array (Dizi) kullansaydık, her adımda tüm elemanları kaydırmak (shifting) gerekebilirdi, bu da performans kaybı yaratırdı.
- Linked List ile eleman ekleme ve çıkarma işlemleri pointer değişimi ile hızlıca yapılır.

### Animasyon ve Görsellik
Pygame'in çizim kütüphanesi kullanılarak grid tabanlı ancak göze hoş gelen bir tasarım yapılmıştır.
- **Renkler:** Google'ın Snake oyunundan esinlenilen yumuşak ve canlı renkler kullanılmıştır.
- **Gözler:** Yılanın hangi yöne gittiğini belli eden gözler eklenmiştir.

## Geliştirici Notları
Öğrenci projesi olduğu için kodlar modüler ve okunabilir tutulmuştur. Her fonksiyonun üzerinde ne işe yaradığına dair açıklama satırları (docstring) bulunmaktadır.
