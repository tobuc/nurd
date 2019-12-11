IDE olarak pycharm kullandım ve python 3.6 kullandım.

Flask redis mysql kullandım.

veritabanında productreview tablosunda ProductID foreign key olmalı fakat tanımlanmamış onu düzelttim.
ReviewDate columnı default değerini current_timestamp yaptım.
Rating columnı null olamayacağı için 0 gönderdim.
veritabanının düzeltilmiş halini klasöre koydum insert edilebilir veya
ALTER TABLE `productreview` ADD CONSTRAINT `fk` FOREIGN KEY (`ProductID`) REFERENCES `product`(`ProductID`) ON DELETE CASCADE ON UPDATE CASCADE;
sql komutu çalıştırılabilir.

virtualenv sinde "rq worker" komutunu çalıştırmak gerekiyor.

iki tane queue kullandım. biri bad_work_check için diğeri notification için.

queue 'lar bad_work_check.txt ve notification_history.txt adlarında iki tane log dosyası oluşturuyor.

db_config.py 'de database bağlantı ayarları yapılmalı.

sql injection için parametrize değer alıyor.

Authentication için JWT kullanabilirdim fakat pdf'te authentication istenmediği için yazmadım.




