import numpy as np
import os
import pandas as pd
from matplotlib import pyplot as plt 

print(*[filename.split(".")[0]for filename in os.listdir("./reviews")],sep="\n")
product_id = input("Podaj identyfikator produktu ")

opinions = pd.read_json("reviews/"+product_id+".json")

opinions_count = len(opinions)
pros_count = opinions["pros"].astype(bool).sum()
cons_count = opinions["cons"].astype(bool).sum()
average_score = opinions["stars"].mean().round(2)

recommendations = opinions["recommendation"].value_counts(dropna=False).sort_index().reindex([False, True, None], fill_value=0)
recommendations.plot.pie(
    autopct = "%.1f%%",
    label = "",
    title = "Rekomendacje",
    labels = ["Nie polecam", "Polecam", "Nie mam zdania"],
    colors = ["crimson", "forestgreen", "lightskyblue"]

)
plt.show()

bins= np.arange(0.5,5,0.5)
plt.hist(opinions["stars"],bins=bins+ 0.8,width=0.4)
plt.title('Ocena')
plt.xlabel('Ilość gwiazdek')
plt.ylabel('Ilość')
plt.show()