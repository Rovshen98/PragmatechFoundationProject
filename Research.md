# 22.06.2021
#### Tranzistor nədir?
Dünya yarandığı gündən  etibarən indiyə qədər ən böyük kəşfin nə olduğunu soruşsalar yəqinki bir çoxumuzun ağlına daş dövründə kəşf edilmiş od, xəritələrin yaranmasına kömək olan kompas və ya bu kimi kəşflər gələcək. Amma dünyanı dəyişdirən ən böyük kəşflərdən biri Tranzistordur. Hal-hazırda dünya əhalisinin 56%-i internetdən stifadə edir. yaponiyada yaşayan bir şəxs Afrikada yaşayan bir şəxslə asanlıqla ünsiyyət qura bilir.<br>
 1946-cı ildə icad edilən kompyuter 150 kv gücündə və 50 ton ağırlığında idi. Və saniyədə 100.000 əməliyyat icra edirdi. Günümüzdə isə hamımızın istifadə etdiyi telefonlar saniyədə 3.2 milyard əməliyyat icra edir. Bu qədər qısa zaman içərisində. 50 tonluq cihazdan 150 qramlıq cihaza keçməyimizi təmin edən qurğu tranzistordur. ilk dəfə radio üzərində yoxlanılıb və səs gücünün artdığı müşahidə edilib. Sonra isə zamanla telefonlarda kompyuterlərdə, roketlərdə vs.- də istifadə olunub.Tranzistor silisium maddəsindən hazırlanır və elektrik siqnallarının gücləndirilməsi, yığılması və dəyişilməsi üçün istifadə edilir.
 
#### Say sistemləri
Kompüterdə verilənlər ikili say sisteminin rəqəmləri ilə təsvir olunur. İnformasiyanın ikili rəqəmlərlə yazılması ikili kodlaşdırma, ikili rəqəmlərin özləri isə bit  adlanır. Bit — informasiyanın ən kiçik ölçü vahidi olub, qiyməti ya “0”, ya da “1” ola bilər.
Natural ədədlərin 10-luq say sistemindən 2-liksay sistemlərinə və əksinə keçid üsulları.
<Br> <br>
İki əsas çevirmə üsulu var:

- Onluq say sistemlərindən digər say sistemlərinə keçid<br>
- Digər say sistemlərindən Onluq say sisteminə keçid. <br>
 <b>Onluq say sistemindən ikilik say sisteminə keçmək üçün</b> ədədi ikiyə
 bölmək və qalığı qeyd etmək lazımdır.
Sonra aldığımız cavabı yenidən ikiyə bölüb qalığı qeyd edirik.

Prosesi axıra kimi davam etdiririk. Sağdan sola ardıcıl qalıqları yazırıq. <Br> <br>
  <b>İkilik say sistemindən onluq say sisteminə keçmək üçün </b> isə:



11001 ikilik ədədininin sağdan başlayaraq üzərinə 0,1, 2, 3, 4 nömrələrini yazırıq.

Sonra isə rəqəmləri 2-nin uyğun qüvvətinə vurub toplayırıq.

#### Mənbə <br>
 - youtube
 - vikipediya
 - yusif.az
 
 # 22.06.2021
 ### Var, Let və Const arasındakı fərqlər:<br>
 - <b>Var</b>- 'variables' sözündən gələn var dataları barındırmaq üçün istifadə olunan konteynerdir. Məsələn:<br>
 var x = 5;
 var y = 6;
 var z = x + y; <br>
 x,y,z burda 'variables'-dir.<Br>
 'Variable'-yə dəyər təyin etmək üçün "=" işarəsindən istifadə olunur:<Br>
  carName = "Volvo";<Br>
 - <b>Let</b>- istifadəsində iki dəfə təyin oluna bilməz.<Br>
 - - Məsələn let istifadəsində siz bunu edə bilməzsiniz:<Br>
      let x = "John Doe";<Br>
       let x = 0;<br>

// SyntaxError: 'x' has already been declared <br>
 (bunu var-da etmək mümkündür)<br>
 - - Blok transkripsiya- let və const blok transkripsiya içərisində yazıla bilir. Let blok transkripsiyadan kənarda dəyər qəbul etmir:<br>
 {<Br>
  let x = 2;<br>
}<br>
// x can NOT be used here<br>
 - <b>Const</b>- elan edildiyi vaxt dəyər təyin olunmalıdır: məs<Br>
    const PI = 3.14159265359;<br>
 ### Console in Javasript<br>
 - console.clear(); - console hissəsini təmizləmək üçündür.<br>
 - console.count(); - əməliyyatı saydırmaq üçün istifadə olunur.<br>
 - console.error(); - error mesajı yazmaq üçün istifadə olunur. <Br>
 - console.warn(); - bu bir xəbərdarlıqdır yazmaq üçün istifadə olunur.<Br>
 - console.log(); - konsola mesaj yazmaq üçün istifadə olunur.<Br>
 - console.table(); - konsola cədvəl yazmaq üçün istifadə olunur.<br>
 ### Data types<br>
 - <b>string</b>- dırnaq işarəsində yazılır. let x = "Volvo";<br>
 - <b>number</b>- rəqəmləri ifadə etmək üçün istifadə olunur.<Br>
 ### Logical Operators<br>
 - &&- və anlamına gəlir<br>
 - ||- və yaxud anlamına gəlir<br>
 - ! - uyğun olmayan anlamına gəlir<br>
 ### JavaScript Arithmetic Operator(Modulus,increment,decrement)<Br>
 - + toplama əməliyyatı üçün istifadə olunur. let x = 100 + 50;<br>
 - - çıxma əməliyyatı üçün istifadə olunur <br>
 - % let x = 5;<br>
     let y = 2;<br>
     let z = x % y;<Br>burda qalıq 1-dir<br>
 - ++ let x = 5;
      x++;
      let z = x; burda x 1 vahid artır və cavab 6-dır. <Br>
 - -- let x = 5;
      x--;
      let z = x; burda x 1 vahid azalır və cavab 4-dür.
 
 
 
 
  
 
