#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import re
import csv
def process_text(input_text, is_activism):
    # Verwende reguläre Ausdrücke, um den Text in Abschnitte zu unterteilen
    sections = re.split(r'\w+\sProfilbild\n', input_text)

    # Entferne leere Abschnitte
    sections = [section.strip() for section in sections if section.strip()]

    # Entferne Zeilenumbrüche aus jedem Abschnitt und alles, was dahinter kommt
    cleaned_sections = [re.sub(r'\n.*', '', section) for section in sections]

    # Prüfe, ob die CSV-Datei bereits existiert
    file_exists = os.path.isfile('files/shell.csv')

    # Öffne die CSV-Datei zum Schreiben oder Anhängen
    with open('files/shell.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Wenn die Datei neu erstellt wird, schreibe die Header-Zeile
        if not file_exists:
            writer.writerow(['ID', 'Text', 'Is_Activism'])

        # Bestimme die ID des letzten Eintrags in der vorhandenen CSV
        id_counter = 1
        if file_exists:
            with open('files/shell.csv', mode='r', newline='', encoding='utf-8') as read_file:
                reader = csv.reader(read_file)
                # Prüfe, ob die ID-Zeile bereits existiert, und überspringe sie
                header = next(reader, None)
                if header and header[0] == 'ID':
                    id_counter = max(int(row[0]) for row in reader) + 1

        for section in cleaned_sections:
            # Prüfe, ob die Zeile "Gefällt" enthält
            if is_activism == "true":
                is_activism = True
            else:
                is_activism = False

            # Schreibe die Daten in die CSV-Datei
            writer.writerow([id_counter, section, is_activism])

            # Inkrementiere die ID
            id_counter += 1



text = '''🏭 🛠️ We’ve diverted resources to make isopropyl alcohol at the Shell Pernis refinery in the Netherlands, and donated 2.5 million litres to the Dutch health-care sector. Work continues at the manufacturing plant, with new safety procedures in place. Apart from making fuels that keep people moving, Shell Pernis also makes raw materials for cleaning solvents, disinfectants and other essential products needed to fight the #coronavirus. For more on our response to #COVID19, see link in bio.
172 Wo.
massimiliano_0013s Profilbild
SHELL СКОРО МИСТЕР ПУТИН ВАС ВЫГОНИТ ИЗ АФРИКИ, ЧТО ВЫ ДУМАЕТЕ ПО ЭТОМУ ПОВОДУ?
9 Wo.Antworten
valves_coosais Profilbild
GOOD.
9 Wo.Antworten
yoyoklaagzak38s Profilbild
Eyy ik was op shell Pernis mooie centrale mijn oom was daar een hoge piet in
12 Wo.Antworten
bernardklaus_s Profilbild
Pls, I need a job in shell company, thank you
14 Wo.Antworten
solbergkristines Profilbild
😢😍😮🔥Can You Shell 😍
23 Wo.Antworten
bennettanderson617s Profilbild
I need a job if you care write back
30 Wo.Antworten
jionee_kilifis Profilbild
Cool Vibez Cool Team
31 Wo.Antworten
ethangirard27s Profilbild
👏👏
34 Wo.Gefällt 2 MalAntworten
bylaurasotos Profilbild
Stop contaminate our planet, stop killing people, shell is a criminal company. #boycotshell
42 Wo.Gefällt 3 MalAntworten
that_sweet_leafs Profilbild
How do you sleep at night knowing you’re the main cause of destroying our planet
42 Wo.Gefällt 1 MalAntworten
that_sweet_leafs Profilbild
What do you tell your children when they ask why the world is ending?
42 Wo.Gefällt 1 MalAntworten
that_sweet_leafs Profilbild
Making record profits in fuel while the rest of the world can’t afford to live
42 Wo.Gefällt 1 MalAntworten
mer_amg__chriss Profilbild
Why is fuel so expensive if you the same amount of fuel is being consumed since before the pandemic?
56 Wo.Gefällt 1 MalAntworten
mauro42os Profilbild
😡😡😡😡😡😡
61 Wo.Antworten
soeprijadiabis Profilbild
😊
62 Wo.Antworten
quelyne_ryans Profilbild
Shell 😍
66 Wo.Gefällt 1 MalAntworten
actuallykakyoins Profilbild
L
70 Wo.Antworten
afzalbmw.calvinkleins Profilbild
ATOMIC BOMB PAKISTAN 🇵🇰 PRESIDENT VLADIMIR PUTIN FIVE TRILLION DOLLARS 💵 ATOM BOMB 💣 ATOM MOBILE INTERNET MOHAMMED HUSSEIN ATOMS ⚛️ MANUFACTURING GIGA FACTORIES METAL TESLA GERMANY FIFTY THOUSAND DOLLARS 💵 FIVE HUNDRED TRILLION DOLLARS 💵 CHINA MOBILE GOVERNMENT CENTRAL AFRICA AUSTRALIA CITY 🌃 PETROCHEMICAL FIVE HUNDRED TRILLION EUROS 💶 LONDON VICTORIA VERSAILLES FRANCE 🇫🇷 CENTURIES VIRGIN GALAXY 🌌 SAMSUNG MOBILE GALAXY 🌌 CENTRAL WEATHER CHANNEL REVENUE FIFTY BILLION FACTORIES VEHICLES 🚗 VOLKSWAGEN CITY 🌃 MANUFACTURING FACTORIES DIESEL MOTOR FUEL DIVESTMENT FUEL ⛽️ ATOMIC ENERGY ELECTRICITY FACTORIES ZUCKERBERG FACEBOOK METAL GOVERNMENT SPONSORED INTERNATIONAL TRADE REVENUE FACTORIES FIFTEEN BILLION DOLLARS 💵 WARREN BUFFETT MANUFACTURING FACTORIES VOLVO FORD DELTA INDUSTRIAL FACTORIES FIFTEEN BILLION DOLLARS 💵 USA 🇺🇸💎💎💳💳📻📻📻📺📺🎛🎛🎛🧭🧭⏱⏱⏰⏰⏰🧯🧯🧯☎️☎️☎️📟📟📺📺📻📻📻📻📻📺💿💿💿📀📀📀💻💻💻💻🖥🖥🖥⌚️⌚️DIRECTOR ANGELINA JOLIE ANGOLA ATOM FIFTY BILLIONAIRES WORLDWIDE REVENUE FIFTY TRILLION DOLLARS 💵 🇦🇴 ⛽️ 🇦🇺 🇨🇳 🇩🇪 💣
77 Wo.Gefällt 1 MalAntworten
mydesign.biz.uas Profilbild
While Russians are shelling hospitals and kindergartens in Ukraine, @Shell is cynically buying Russian oil and fuels further slaughter of Ukrainian civilians. We don't need your money Shell, we need you to #StopBuyingRussianOil
78 Wo.Antworten
molyn.liliias Profilbild
Stop war in Ukraine 🇺🇦
78 Wo.Antworten
liudmyla_0593s Profilbild
While Russians are shelling hospitals and kindergartens in Ukraine, Shell is cynically buying Russian oil and fuels further slaughter of Ukrainian civilians. We don't need your money Shell, we need you to
78 Wo.Antworten
maryn.kas Profilbild
@Shell is sponsoring extermination of Ukrainian civilians. #StopBuyingRussianOil
78 Wo.Antworten
lukashevychromans Profilbild
While Russians are destroying hospitals and kindergartens in Ukraine, @Shell is cynically buying Russian oil and fuels further slaughter of Ukrainian civilians. We don't need your money Shell, we need you to #StopBuyingRussianOil
78 Wo.Antworten
shev__lenas Profilbild
In 12 days, 38 children were killed, 840 – wounded in Ukraine by Russian military. @Shell is buying Russian oil and sponsors the killing of Ukrainian kids. No special aid funds will return us our children. Shell should #StopBuyingRussianOil
78 Wo.Antworten
lilitimors Profilbild
In 12 days, 38 children were killed, 840 – wounded in Ukraine by Russian military. @Shell is buying Russian oil and sponsors the killing of Ukrainian kids. No special aid funds will return us our children. Shell should #StopBuyingRussianOil
78 Wo.Gefällt 1 MalAntworten
elcio__cs Profilbild
🤬 Stop buying crude oild from Russia
78 Wo.Gefällt 1 MalAntworten
tetiana_ilchenko_s Profilbild
Shell is buying Russian🇷🇺 oil and sponsors the killing of Ukrainian🇺🇦 kids.😔 No special aid funds will return us our children. Shell should #StopBuyingRussianOil🙏‼️
78 Wo.Antworten
tetiana_ilchenko_s Profilbild
Stop War in Ukraine 🇺🇦‼️
78 Wo.Antworten
ye_fimenkos Profilbild
stop buying oil from Russia, stop financing the war in Ukraine, Russia uses the lowest means of war, children and civilians of Ukraine are dying!! stop the war’
78 Wo.Antworten
jannipgrams Profilbild
Shame
78 Wo.Gefällt 1 MalAntworten
m1chelss Profilbild
🇺🇦
78 Wo.Antworten
angie.graesslers Profilbild
War supporter!!!
78 Wo.Gefällt 1 MalAntworten
repetutorkhms Profilbild
People are suffering while you are making money #nowarinukraine🇺🇦
78 Wo.Gefällt 3 MalAntworten
bogdan_rns Profilbild
Murderers of 🇺🇦 people
78 Wo.Gefällt 1 MalAntworten
tanyamotrenkos Profilbild
Stop killing people in Ukraine!
78 Wo.Gefällt 1 MalAntworten
hairartistruslans Profilbild
Murderes of Ukraine
78 Wo.Gefällt 1 MalAntworten
freshpoison2s Profilbild
disappointment
78 Wo.Antworten
boiarovigors Profilbild
Shell is the sponsor of Russian blood terrorism
78 Wo.Gefällt 3 MalAntworten
lubricantsbelts Profilbild
🔥
80 Wo.Antworten
kostianvolkov100s Profilbild
Hello 03.02.2022, I stopped at a Shell gas station at 39 Sumskaya Street, Kursk, Russia, where 150 rubles more gasoline mistakenly got into my tank, which the police were called to and an explanation was given, while we were giving explanations, the head of this gas station Anatoly scratched my car!!!! At the request of the police, we were shown a video and we saw how Anatoly was doing it, after learning that we were shown the video, Anatoly forbade us to show it and said that they would request it officially.and the fact that it may not be saved before the request....One thing is not clear how such deranged people work under such well-known nonsense as Shell... and who will repair my car? In our city , everyone is surprised by this situation and cannot believe that reputation is not important to you
82 Wo.Antworten
trueginis Profilbild
@senad.ab @nzh9.7
85 Wo.Gefällt 1 MalAntworten
sig_privprivs Profilbild
this comment section, gives me hope. thank you everyone.
87 Wo.Gefällt 1 MalAntworten
isabelagl.igls Profilbild
Out of the oceans! #saveourwildcoast
89 Wo.Gefällt 3 MalAntworten
chindimps_s Profilbild
Trash
90 Wo.Gefällt 4 MalAntworten
danielacfragosos Profilbild
🤬🤬🤬🤬🤬
90 Wo.Antworten
ameliamfouches Profilbild
Leave South Africa’s coastline alone!!!! Stop the #seismicsurvey!!! #tohellwithshell #gotohellshell
90 Wo.Gefällt 4 MalAntworten
_stephfitnie_s Profilbild
KILLING MARINE LIFE
90 Wo.Gefällt 1 MalAntworten
mr.alius Profilbild
🇳🇬 💔
90 Wo.Antworten
cosmicsnakequeens Profilbild
🤮🤮🤮🤮🤮🤮🤮
90 Wo.Gefällt 2 MalAntworten
trystanfates Profilbild
Green washing! You’re taking our future from us!
91 Wo.Gefällt 2 MalAntworten
capetownballoons Profilbild
#tohellwithshell #savethewildcoast #fuckoffshell
91 Wo.Gefällt 1 MalAntworten
edvinhdesigns Profilbild
Stop met het vervuilen van de aarde!!
91 Wo.Antworten
meg_calders Profilbild
#tohellwithshell 🇿🇦 LEAVE OUR WILD COAST ALONE!
91 Wo.Gefällt 3 MalAntworten
sir_ziercher_the18ths Profilbild
Devils
91 Wo.Gefällt 2 MalAntworten
caity_sincs Profilbild
#tohellwithshell #savethewildcoast
91 Wo.Gefällt 1 MalAntworten
vaezi_mehrans Profilbild
Dear
Hope you are fine.
It's pleasure that visit and follow our holding page ( Ompayaco) and like posts. Thank you so much for your cooperation🙏🌷
https://instagram.com/ompayaco?utm_medium=copy_link
Best regards
M.vaez
CEO at Ompaya holding
91 Wo.Antworten
scwuffless Profilbild
#TOHELLWITHSHELL 🇿🇦
91 Wo.Gefällt 1 MalAntworten
alexkarev96s Profilbild
Killers oceans
91 Wo.Gefällt 1 MalAntworten
lalaurenlals Profilbild
Leave south africa alone! We don't want you here destroying our marine life/ ecosystem. Rot op
92 Wo.Gefällt 3 MalAntworten
lalaurenlals Profilbild
#TOHELLWITHSHELL #TOHELLWITHSHELL #TOHELLWITHSHELL #TOHELLWITHSHELL #TOHELLWITHSHELL #TOHELLWITHSHELL
92 Wo.Gefällt 4 MalAntworten
lalaurenlals Profilbild
#TOHELLWITHSHELL
92 Wo.Gefällt 4 MalAntworten
lalaurenlals Profilbild
#TOHELLWITHSHELL
92 Wo.Gefällt 5 MalAntworten
olly_shreddersons Profilbild
Voetsek... Sincerely 🇿🇦
92 Wo.Gefällt 3 MalAntworten
x___danielle__xs Profilbild
#tohellwithshell
92 Wo.Gefällt 2 MalAntworten
runsurfyogagirl_031s Profilbild
All while destroying our oceans 🤬
93 Wo.Gefällt 5 MalAntworten
kazimauberts Profilbild
disgusting organizations
94 Wo.Gefällt 4 MalAntworten
jon_lovesyou_s Profilbild
Thinking BIG ❤️
96 Wo.Antworten
mzzashantis Profilbild
I wonder how much you are donating to cater for the spillage your company is causing in the NIger Delta , livestock are dying , nothing is growing . Take responsibility for the damages nooooowww😢😢😢😢.'''


process_text(text, "true")




