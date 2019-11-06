import string
m=raw_input("enter month of birth ")
d=input("enter date of birth ")
a=string.lower(m)
if (a=="march" and d>=21 and d<=31) or (a=="april" and d<=19 and d>=1):
 print("Aries")
elif (a=="april" and d>=20 and d<=30) or (a=="may" and d<=20 and d>=1):
 print("Taurus")
elif (a=="may" and d>=21 and d<=31) or (a=="june" and d<=21 and d>=1):
 print("Gemini")
elif (a=="june" and d>=22 and d<=30) or (a=="july" and d<=22 and d>=1):
 print("Cancer")
elif (a=="july" and d>=23 and d<=31) or (a=="august" and d<=22 and d>=1):
 print("Leo")
elif (a=="august" and d>=23 and d<=31) or (a=="september" and d<=22 and d>=1):
 print("Virgo")
elif (a=="september" and d>=23 and d<=30) or (a=="october" and d<=23 and d>=1):
 print("Libra")
elif (a=="october" and d>=24 and d<=31) or (a=="november" and d<=21 and d>=1):
 print("Scorpio")
elif (a=="november" and d>=22 and d<=30) or (a=="december" and d<=21 and d>=1):
 print("Sagittarius")
elif (a=="december" and d>=22 and d<=31) or (a=="january" and d<=21 and d>=1):
 print("Capricorn")
elif (a=="january" and d>=20 and d<=31) or (a=="february" and d<=18 and d>=1):
 print("Aquarius")
elif (a=="february" and d>=19 and d<=29) or (a=="march" and d<=20 and d>=1):
 if a=="february" and d==29 :
  print("Is it a leap year ==> Y or N")
  yn=raw_input()
  yn=string.upper(yn)
  if(yn=="Y"):
   print("Pisces")
  else:
   print("Invalid Input")
 else:
  print("Pisces")
else:
 print("Invalid Input")

