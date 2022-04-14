# BounchingBalls
8 Tane birbirinden farklı python dosyası yükledim ancak içinde yorum satırları olan, asıl sistemin çalıştıkları 3DBall ve Collusion python dosyalarıdır. Diğerlerini sistemin nasıl çalıştığını anlatabilmek adına yükledim.

Canvas kütüphanesini kullanaraktan bir pencere oluşturdum ve içine 5 tane özdeş top yerleştirdim. Topları fizik kurallarına göre hareket ettirdim. Çarpışma anlarında ise momentum kurallarına göre yön değiştirmelerini sağladım(Mantık olarak kodumun doğru olduğunu düşünüyorum ama bir hata aldığım için malesef test edemedim). Mouse ile kontrol etme mekanizması ise şu şekilde tasarladım. Oluşturduğum pencereyi ekranın tam ortasında oluşturdum ve koordinatlar belli olduğu için mouse ile toplatın kesişim kümesini bulabilecek kodu yazdım. İlk başta mouse konumunu aldım ve topların alt kısmı ile kesişiyorsa üst tarafa doğru hareket, sol üst kısmı ile kesişiyorsa sağ tarafa doğru bir hareket son olarak da sağ üst kısmı ile kesişiyorsa sola doğru hareket etmelerini sağlamaya çalıştım.

3 boyutlu uzay boşluğunu ise kendi matriks çarpım fonksiyonumu yazarak oluşturdum. Aslında numpy kütüphanesi matriks çarpımına olanak veriyor ama kullanmamamız istendiği için kendi fonksyionumu oluşturdum. 3 boyutlu mantık biraz farklı 2 boyutludan. 2 boyutludan 3 boyutluya geçmek için projection matriksini kullanarak çarpım yapmanız gerekiyor ve hareket vermek içinde rotation matrikslerini kullanmanız gerekiyor. Phase 2 tam bitmedi ama bir kısmını tamamladığımı düşünüyorum.

Ek olarak mouseun ve topların nasıl kesişim kümesini bulduğumu göstermek içinde bir resim dosyası yüklüyorum. Arzu ederseniz onuda inceleyebilirsiniz.


Anlatıklarımın hepsini bir video çekerekde elimden geldiğince anlatmaya çalıştım, isterseniz videodanda izleyebilirsiniz.


Link:


https://youtu.be/5kx-8Z5g26U
