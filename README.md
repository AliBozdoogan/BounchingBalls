# BounchingBalls

TR
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

8 Tane birbirinden farklı python dosyası yükledim ancak içinde yorum satırları olan, asıl sistemin çalıştıkları 3DBall ve Collusion python dosyalarıdır. Diğerlerini sistemin nasıl çalıştığını anlatabilmek adına yükledim.

Canvas kütüphanesini kullanaraktan bir pencere oluşturdum ve içine 5 tane özdeş top yerleştirdim. Topları fizik kurallarına göre hareket ettirdim. Çarpışma anlarında ise momentum kurallarına göre yön değiştirmelerini sağladım(Mantık olarak kodumun doğru olduğunu düşünüyorum ama bir hata aldığım için malesef test edemedim). Mouse ile kontrol etme mekanizması ise şu şekilde tasarladım. Oluşturduğum pencereyi ekranın tam ortasında oluşturdum ve koordinatlar belli olduğu için mouse ile toplatın kesişim kümesini bulabilecek kodu yazdım. İlk başta mouse konumunu aldım ve topların alt kısmı ile kesişiyorsa üst tarafa doğru hareket, sol üst kısmı ile kesişiyorsa sağ tarafa doğru bir hareket son olarak da sağ üst kısmı ile kesişiyorsa sola doğru hareket etmelerini sağlamaya çalıştım.

3 boyutlu uzay boşluğunu ise kendi matriks çarpım fonksiyonumu yazarak oluşturdum. Aslında numpy kütüphanesi matriks çarpımına olanak veriyor ama kullanmamamız istendiği için kendi fonksyionumu oluşturdum. 3 boyutlu mantık biraz farklı 2 boyutludan. 2 boyutludan 3 boyutluya geçmek için projection matriksini kullanarak çarpım yapmanız gerekiyor ve hareket vermek içinde rotation matrikslerini kullanmanız gerekiyor. Phase 2 tam bitmedi ama bir kısmını tamamladığımı düşünüyorum.

Ek olarak mouse ve topların nasıl kesişim kümesini matematiksel olarak nasıl bulduğumu göstermek içinde bir jpeg dosyası yüklüyorum. Arzu ederseniz onuda inceleyebilirsiniz.


Anlatıklarımın hepsini bir video çekerekde elimden geldiğince anlatmaya çalıştım, isterseniz videodanda izleyebilirsiniz.


Link:


https://youtu.be/5kx-8Z5g26U

EN
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

I have installed 8 different python files, but they are 3DBall and Collusion python files with comment lines in which the actual system is running. I uploaded the others to explain how the system works.

I created a window using the Canvas library and placed 5 identical balls in it. I moved the balls according to the laws of physics. In the moments of collision, I made them change direction according to the momentum rules (I think my code is correct as a logic, but unfortunately I couldn't test it because I got an error). I designed the mechanism to control with the mouse as follows. I created the window I created in the middle of the screen, and since the coordinates are clear, I wrote the code to find the intersection set of the sum with the mouse. At first, I took the mouse position and tried to make them move to the top if it intersects with the bottom of the balls, to the right if it intersects with the top left, and finally to the left if it intersects with the top right.

I created the 3-dimensional space by writing my own matrix product function. Actually the numpy library allows matrix multiplication, but since we were asked not to use it, I created my own function. 3D logic is slightly different from 2D. To move from 2D to 3D, you need to multiply using the projection matrix, and you need to use rotation matrices to give movement. Phase 2 isn't quite finished, but I think I've completed some of it.

Additionally, I am uploading a jpeg file to show how I mathematically find the intersection set of mice and balls. If you wish, you can examine it.


I tried to explain all of my narratives as much as I could by making a video, you can watch it on the video if you want.


Link:


https://youtu.be/5kx-8Z5g26U
