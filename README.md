# REST COUNTRIES API 

## API Project

Bu proje, REST Countries API üzerinden ülke bilgilerini çekip analiz etmek amacıyla oluşturulmuştur.

## Veri Analizi

Bu projede kullanılan methods.py dosyası içerisindeki `create_countries_dataframe` fonksiyonu, Rest Countries API'den alınan bilgileri içeren bir DataFrame oluşturur. Oluşturulan DataFrame'deki sütunlar şu bilgileri içermektedir:

- **Country:** Ülkenin adı
- **Capital:** Başkentin adı
- **Population:** Ülkenin nüfusu
- **Area:** Ülkenin yüzölçümü
- **Region:** Ülkenin bölgesi
- **Subregion:** Ülkenin alt bölgesi
- **Languages:** Ülkede konuşulan diller

### Örnek Analizler:

1. **Toplam Nüfus:** DataFrame'deki tüm ülkelerin nüfuslarını toplayabilir ve genel bir nüfus istatistiği oluşturabilirsiniz.

2. **Bölge Bazında Nüfus Analizi:** Bölgelere göre toplam nüfusları karşılaştırabilir ve hangi bölgelerin daha kalabalık olduğunu görselleştirebilirsiniz.

3. **Dil Analizi:** Hangi dillerin en yaygın olduğunu belirleyebilir ve DataFrame üzerinde hangi dillerin öne çıktığını inceleyebilirsiniz.

4. **Yüzölçümü ve Nüfus İlişkisi:** Yüzölçümü ve nüfus arasındaki ilişkiyi inceleyebilir ve büyük yüzölçümüne sahip ülkelerin genellikle büyük nüfuslara sahip olup olmadığını analiz edebilirsiniz.


## Kullanım

Proje içerisinde yer alan methods.py dosyasındaki `get_all_countries` fonksiyonu, belirtilen API üzerinden ülke verilerini çekmek için kullanılır. Gelen veri, `create_countries_dataframe` fonksiyonu ile bir DataFrame'e dönüştürülerek daha fazla analiz için kullanılabilir.

Örnek Kullanım:

```python
import requests
import pandas as pd

# API URL
base_url = "https://restcountries.com/v3.1/all"

# Ülkeleri çek
countries_data = get_all_countries(base_url)

# DataFrame oluştur
df = create_countries_dataframe(countries_data)

# DataFrame'i göster
print(df)
```
