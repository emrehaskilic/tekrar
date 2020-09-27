# dicyionary() key value formatında dataları lstelemek içink ullanırlı kson formatında data tutar
#webApi java scirpt angular jsnative mongo gbi birçok platformu desteklemektedir

personeller = [

    {
        "id":1,
        "indexno":0,
        "firstname": "murat",
        "lastname":"vuranok",
        "mail":"murat.vuranok@bilgeadam.com",
        "Phone": "+9055554443322",
        "phones": [
           {
               "no":12312312,
               "title":"work",
               "description":""

           },
           {
               "no":12312312,
               "title":"school",
               "description":""

           },
           {
              "no":12312312,
               "title":"home",
               "description":""

           },
           {
               "id":2,
        "indexno":1,
        "firstname": "mehmet",
        "lastname":"civelek",
        "mail":"mehmet.civelek@bilgeadam.com",
        "Phone": "+9055554443322"



           }

        ]
         }
]

print(personeller[0])

print(personeller[0]["phones"])

# dictionary içerisinde yer alan bir kaydı güncellemek isterseniz

i = 0  # hangi eleman güncellenecek
key = "firstname"
value = "şahin"

oldRecord = personeller[i][key]

personeller[i][key] = value

newRecord = personeller[i][key]
print(oldRecord)
print(newRecord)
print(personeller)

firstname = input("isim:")
lastname = input("soyisim:")
phone = input("telefon no:")

id = len(personeller)
indexno = len(personeller) -1

personeller.append(
    {
        "id":id,
        "indexno":indexno,
        "firstname":firstname,
        "lastname": lastname,
        "mail": f"{firstname}.{lastname}@bilgeadam.com.",
        "phone": phone
 }

)

print(personeller[:])