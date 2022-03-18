lista_sklepow = {
    "warzywniak": ["marchew", "seler", "rukola"] ,
    "piekarnia": ["chleb", "paczek", "bulki"]
}

print("lista zakupow:")
for a,d in lista_sklepow.items():
  print(f"Ide do", a, "kupuje tu nastepujace rzeczy", d)

x = len(lista_sklepow["warzywniak"])+len(lista_sklepow["piekarnia"])
print(f"W sumie kupuje", x, "produktow")