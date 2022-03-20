# s216356

## Analiza struktury opinii w serwisie ceneo.pl

|Składowa|Selektor|Zmienna|
|--------|--------|-------|
|opinia|div.js_product-review|review|
|identyfikator opinii|\[data_entry-id\]review+id|
|autor|.user-post__author-name|author|
|rekomendacja|span.user-post__author-recomendation > em|recomendation|
|liczba gwiazdek|span.score-marker score-marker--s|stars|
|treść|div.user-post__text|content|
|data wystawienia|span.user-post__published > time:nth-child(1) \[datetime\]|publish_date|
|data zakupu|span.user-post__published > time:nth-child(2) \[datetime\]|purchase_date|
|dla ilu przydatna|button.vote-yes >span |usefull|
|dla ilu nieprzydatna|button.vote-no >span|useless|
|lista zalet|div.review-feature_tittle--positives ~ review feature_item||
|lista wad|div.review-feature_tittle--negatives ~ review feature_item||
||||