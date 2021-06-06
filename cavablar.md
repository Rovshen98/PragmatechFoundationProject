Flexbox, Grid Və 12 column texnikaları arasındakı əsas fərqlər:
Flexbox 1 ölçülü sistemdir.
 justify-content, align-items və s. xüsusiyyətləri ilə elementləri səliqəli şəkildə düzmək mümkündür.
12 column sistemi də sətir və sütunlardan ibarətdir.  Bu sistemdə ekran 12 sütuna bölünür
Grid sistemi isə 2 ölçülüdür. Sətir və sütunlardan ibarətdir.12 column sistemindən fərqli olaraq daha mürəkkəb quruluşlu qutuları düzəltmək üçün istifadə olunur.

justify-content: space around və space-between arasındakı fərq:
 məsələn siz display:flex özəlliyi verdiyiniz qutunun içərisində 5 div yaradırsız. əgər siz bu divlərə space-between özəlliyi versəz əsas divin içərisindəki divləri qutuya səpələyəcək.
  amma birinci və sonuncu divləri əsas divə bitişik olacaq.
 əgər siz space-around özəlliyi versəz. yenədə divlər əsas divin içərisində səpələnəcək amma birinci və sonuncu divlərlə əsas divin arasında məsafə olacaq.
 
 em və rem arasındakı fərqlər: em ölçüsü valideyn divə əsasən uyğunlaşır. məsələn div elementinə font-size 20 px vermisiz. və div elementinin içərisində p elementinə isə 3em vrmisiz.
 bu halda p elementini ölçüsü divin 3 qatı olacaq. 
 rem isə əsas olaraq html səhifəsinin ölçüsünə uyğunlaşır.
 % ölçüsü isə əsasən qutulara ölçü vermək üçün istifadə olunur.
