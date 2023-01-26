import requests,os,json
os.system("clear")
zahin="""
   \033[1;33m✧☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
   ☆ \033[1;34mᴡᴇʟᴄᴏᴍᴇ & ᴇɴᴊᴏʏ ᴛʜɪꜱ ᴛᴏᴏʟ \033[1;33m☆ 
   ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
\033[1;35m╔═════════════════════════════════╗
║   \033[1;31m╔════╗╔═══╗╔╗─╔╗╔══╗╔═╗─╔╗    \033[1;35m║
║   \033[1;31m╚══╗═║║╔═╗║║║─║║╚╣─╝║║╚╗║║    \033[1;35m║
║   \033[1;31m──╔╝╔╝║║─║║║╚═╝║─║║─║╔╗╚╝║    \033[1;35m║
║   \033[1;31m─╔╝╔╝─║╚═╝║║╔═╗║─║║─║║╚╗║║    \033[1;35m║
║   \033[1;31m╔╝═╚═╗║╔═╗║║║─║║╔╣─╗║║─║║║    \033[1;35m║
║   \033[1;31m╚════╝╚╝─╚╝╚╝─╚╝╚══╝╚╝─╚═╝    \033[1;35m║
\033[1;35m║        \033[1;36m ☞ZAHIN SAAD☜ \033[1;35m           ║\033[1;35m
\033[1;35m╠═════════════════════════════════╣
\033[1;35m║\033[1;33m  ADMIN    :   ZAHIN SAAD        \033[1;35m║
\033[1;35m║ \033[1;32m TOOLS    :    IP TRACK         \033[1;35m║
\033[1;35m║ \033[1;34m GITHUB   :    Zahin-04         \033[1;35m║
\033[1;35m╚═════════════════════════════════╝

"""
print(zahin)
os.system("xdg-open https://www.facebook.com/profile.php?id=100084166897051")
v=input("\033[1;32mYOUR VICTIM IP : ")
link="http://ip-api.com/json/"+v
IP=requests.get(link).json()
info=("""\033[1;35m
╔═════════════════════════════════╗
║  \033[1;37m ⌘ YOUR VICTIM INFORMATION ⌘ \033[1;37m\033[1;35m  ║\033[1;35m
╚═════════════════════════════════╝
""")
print(info)
os.system("xdg-open https://www.facebook.com/profile.php?id=100084166897051")
print("\033[1;32m\nVICTIM IP ADDRESS ☞ "+IP["query"])
print("\nCOUNTRY NAME ☞ "+IP["country"])
print("\nCOUNTRY CODE ☞ "+IP["countryCode"])
print("\nDIVISION NAME ☞ "+IP["regionName"])
print("\nREGION NAME ☞ "+IP["region"])
print("\nCITY NAME ☞ "+IP["city"])
print("\nZIP CODE ☞ "+IP["zip"])
print("\nLAT NUMBER ☞ "+str(IP["lat"]))
print("\nLON CODE ☞ "+str(IP["lon"]))
print("\nTIME ZONE ☞ "+IP["timezone"])
print("\nNETWORK SERVICE ☞ "+IP["isp"])
print("\nORG ☞ "+IP["org"])
print("\nAS NAME ☞ "+IP["as"])
print("\n")