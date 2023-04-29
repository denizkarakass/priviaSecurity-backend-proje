# PRİVİA SECURİTY BACKEND PROJESİ
Bu proje, Django web çerçevesi kullanılarak geliştirilmiş bir web uygulamasıdır. Bu dosya, proje hakkında temel bilgileri içermektedir.    

###  Sanal Çalışma Ortamın Hazırlanması     
``` git clone https://github.com/KullaniciAdi/proje-adi.git ``` Proje dosyalarınızı bilgisayarınıza klonlayın.          
``` python -m venv env  ``` Sanal ortam oluşturun.         
``` env\Scripts\activate  ``` Sanal ortamı aktifleştirin.       
```  pip install Django ``` Django kurulum.    
```  dijango-admin startproject priviasecurity  ``` Projeyi başlat.       
```  cd priviasecurity_con ``` Dizine gitme.       
```  python manage.py runserver ``` Projeyi yerel makinenizde çalıştırın.         
http://127.0.0.1:8000/ adresinde proje ana sayfasına erişebilirsiniz.

### Dosya Yapısı MVT ( Model View Template )
![ MVT Yapısı ](./images/mvt.jpg)  
proje-adi/
├── uygulama-adi/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── models.py
│   └── urls.py
├── proje-adi/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md

uygulama-adi: priviasecurity-backend-task.   
migrations: Django'nun veritabanı model değişikliklerini izlemek için kullanılan dosyalar.    
templates: HTML dosyaları için kullanılan şablonlar.     
static: CSS, JS, resimler gibi statik dosyalar için kullanılan klasör.       
views.py: Django uygulamasındaki kontrollerin bulunduğu dosya.         
models.py: Django uygulamasındaki veritabanı modellerinin tanımlandığı dosya.          
urls.py: Django uygulamasındaki URL yönlendirmelerinin bulunduğu dosya.          
settings.py: Django projesinin genel ayarlarının yapılandırıldığı dosya.         
db.sqlite3: Projenin SQLite veritabanı dosyası.        
manage.py: Django projesinin yönetim arayüzü.         
requirements.txt: Projede kullanılan tüm kütüphanelerin sürümlerinin bulunduğu dosya.             
