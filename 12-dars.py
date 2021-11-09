# =============================================================================
# akam={'ismi':'Sardor','yoshi':32,'manzili':'Moskva'}
# print(f"Akaming ismi {akam['ismi']}, yoshi {akam['yoshi']}, yashash joyi {akam['manzili']}")
# =============================================================================


# =============================================================================
# amin={'taom':'osh'}
# xuzayfa={'taom':'tovuq'}
# xayrulla={'taom':"go'sht"}
# sarvar={'taom':'tuxum'}
# botir={'taom':'baliq'}
# 
# print(f"Xuzayfaning sevimli taomi {xuzayfa['taom']}")
# print(f"Aminning sevimli taomi {amin['taom']}")
# print(f"Botirning sevimli taomi {botir['taom']}")
# =============================================================================


# =============================================================================
# izoh={'integer':'bu oddiy son',
#       'else':"yoki ma'nosini anglatadi",
#       'string':'kod yozilgan qator',
#       'if':'agar',
#       'for':'takrorlanish',
#       'title':'stringni bosh harf bilan chiqaradi',
#       'upper':'hammasini katta harfda chiqaradi'
#       }
# soz=input("Kalit so'z kiriting: ")
# 
# if soz in izoh:
#     print(izoh[soz])
# else:
#     print("Bunday so\'z mavjud emas!")
# ============================================================================



izoh={'integer':'bu oddiy son',
      'else':"yoki ma'nosini anglatadi",
      'string':'kod yozilgan qator',
      'if':'agar',
      'for':'takrorlanish',
      'title':'stringni bosh harf bilan chiqaradi',
      'upper':'hammasini katta harfda chiqaradi'
      }
soz=input("Kalit so'z kiriting: ")

if soz in izoh:
    print(f"{soz.title()} so\'zi {izoh[soz]} deb tarjima qilinadi")
else:
    print("Bunday so\'z mavjud emas!")


