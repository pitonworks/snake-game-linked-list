from utils import *

class Node:
    """
    Linked List için Düğüm (Node) sınıfı.
    Yılanın her bir karesini temsil eder.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None

class SnakeLinkedList:
    """
    Yılanın gövdesini tutan Linked List yapısı.
    Baş (Head) ve Kuyruk (Tail) pointerları ile verimli ekleme/silme yapar.
    """
    def __init__(self):
        # Yılanın başlangıç konumu (Ekranın ortası)
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        
        # Başlangıçta 3 birim uzunluğunda olsun
        self.head = Node(start_x, start_y)
        node2 = Node(start_x, start_y + 1) # Aşağı doğru uzansın (test için)
        node3 = Node(start_x, start_y + 2)
        
        self.head.next = node2
        node2.next = node3
        
        self.tail = node3 # Kuyruğu takip et
        
        self.direction = UP # Başlangıç yönü (Yukarı gitsin)
        self.grow_pending = False # Yem yenince büyüme işareti

    def move(self):
        """
        Yılanı mevcut yönüne göre hareket ettirir.
        Linked List Mantığı:
        1. Başın önüne yeni bir Node ekle (yeni koordinatta).
        2. Eğer büyüme (grow_pending) yoksa, kuyruğu sil.
        """
        # Yeni başın koordinatlarını hesapla
        new_x = self.head.x + self.direction[0]
        new_y = self.head.y + self.direction[1]
        
        # Yeni node oluştur
        new_head = Node(new_x, new_y)
        
        # Yeni node'u başa ekle (Head Insertion)
        new_head.next = self.head
        self.head = new_head
        
        # Eğer büyüme beklenmiyorsa kuyruğu sil (Delete Last Node)
        if not self.grow_pending:
            self.delete_tail()
        else:
            self.grow_pending = False # Büyüme gerçekleşti, işareti kaldır

    def delete_tail(self):
        """
        Listenin son elemanını (kuyruğu) siler.
        Singly Linked List olduğu için kuyruktan bir öncekini bulmamız lazım.
        Ancak performansı artırmak için kuyruğu 'tail' pointer ile tutuyoruz,
        fakat silme işlemi için yine de sondan bir öncekine (traverse) ihtiyacımız var.
        Performans notu: Yılan çok uzun değilse O(N) sorun olmaz.
        """
        if self.head is None or self.head.next is None:
            return # Liste boş veya tek elemanlıysa (oyun bitmiştir muhtemelen)

        current = self.head
        while current.next.next is not None:
            current = current.next
        
        # current şu an sondan bir önceki node
        current.next = None
        self.tail = current

    def grow(self):
        """
        Yılanın büyümesini tetikler. 
        Bir sonraki move() çağrısında kuyruk silinmez, böylece boy uzar.
        """
        self.grow_pending = True

    def check_collision_with_self(self):
        """
        Yılanın başı gövdesine çarpıyor mu kontrol eder.
        O(N) karmaşıklığında listeyi gezer.
        """
        head_x = self.head.x
        head_y = self.head.y
        
        current = self.head.next # Baştan sonraki parçalara bak
        while current is not None:
            if current.x == head_x and current.y == head_y:
                return True
            current = current.next
        return False
        
    def get_coordinates(self):
        """
        Çizim için tüm yılanın koordinatlarını liste olarak döndürür.
        """
        coords = []
        current = self.head
        while current is not None:
            coords.append((current.x, current.y))
            current = current.next
        return coords
