# Odovzdanie práce, stav a pravidlá

Tento súbor slúži na to, aby sa v novom sedení dalo pokračovať bez toho, aby sa
znova vymýšľalo, čo už je rozhodnuté. Čítaj ho spolu s `README.md`.

Projekt: jednostránkový web pre **ALL MONT, spol. s r.o.**, Nitra, výroba
a montáž plastových a hliníkových okien a dverí. Pôvodná stránka: allmont.sk.

---

## 1. Čo je hotové a nemá sa meniť

**Úvodné intro je schválené a zamrznuté.** Klient povedal doslova „intro je
super, to necháme tak". Nezasahovať doňho bez výslovnej žiadosti.

Ako intro funguje:

- Zdroj je `hero-2160.mp4`, 3840×2160, 25 snímok, 15,6 s, **každá snímka je
  kľúčová**. To je zámer, nie omyl: jeden skok pri scrollovaní potom dekóduje
  presne jednu snímku, okolo 9 ms aj v 4K. Pri bežnom kódovaní s kľúčovou
  snímkou každých osem to je 72 ms a scrollovanie vlečie.
- Video sa sťahuje celé ako blob, až potom sa zapne scrollovanie. Do vtedy drží
  miesto `hero-poster.jpg`, teda prvá snímka.
- Hero má výšku 1500vh. Čas videa ide so scrollom rovnomerne po `TIME_END`
  (0,90), potom drží poslednú snímku.
- **Päť titulkov** v prvých dvoch tretinách, biele, jeden rovnaký jemný závoj.
  Posledná tretina beží bez textu.
- Na konci sa obraz rozplynie do farby stránky a **nadpis sa vynára priamo
  v tom prechode** (blok `.end`), aby za introm nezostala prázdna obrazovka.
- Nápoveda „Scrollujte" a linka postupu sú dole v strede po celý čas.
- Kurzor je zameriavací kríž. Počas intra sa pri scrollovaní skryje a pohyb
  myšou ho vráti. Po intre zostáva.

## 2. Pravidlá značky, ktoré platia bez výnimky

Vychádzajú z dizajn manuálu značky, verzia 1.0, ktorý má klient vlastný.
**Manuál má prednosť pred akýmikoľvek zvykmi.**

- **Jedno písmo na všetko:** Helvetica Neue, náhrada Inter Tight. Rozdiely nesie
  len hrúbka, veľkosť a prestrih. Klient to zdôraznil dvakrát. Žiadne druhé
  písmo, ani na čísla, ani na štítky.
- **Farby:** azúrová `#1E6FD9` je akcent, nie pozadie. Námorná `#0F2233` na text
  a tmavé plochy. Sklo `#8FC1F2`. Hmla `#EEF1F4` na pozadia. Pomer plôch
  približne 60 hmla, 25 námorná, 12 azúrová.
- **Žiadne gradienty na plochách, tlačidlách ani texte.** Jediná výnimka je
  závoj pod textom nad videom, čo je systém čitateľnosti, nie ozdoba.
- **Pravé uhly.** Žiadne zaoblené rohy v rozhraní. Jediný rádius v značke je
  R14 na symbole loga, ten patrí len logu a piktogramom postaveným na jeho
  konštrukcii.
- **Žiadne kurzívy.**
- Logo: symbol je okno s krížom a jedným 45° odleskom v ľavej hornej tabuli.
  Nikdy neprekresľovať, používať priložené SVG.

## 3. Ako sa tu pracuje, čo klient ocenil

- **Merať, nie hádať.** Každé rozhodnutie o čitateľnosti textu nad videom padlo
  z merania jasu presne v mieste textu, nie od oka. Kontrast sa počíta, nie
  odhaduje. Krivka pohybu videa určila, kde sedia titulky.
- **Testovať tou cestou, ktorou ide používateľ.** Jedna chyba sa dlho skrývala
  presne preto, že testy si stavy zapínali ručne a obchádzali tak vetvu kódu,
  ktorá ju spôsobovala. Testy musia nechať pracovať skutočný kód.
- **Hovoriť nahlas o odchýlkach a o vlastných chybách.** Klient na to reagoval
  dobre. Keď meranie povie, že jeho inštrukcia nevyjde, treba to povedať
  a ponúknuť náhradu.
- **Nevymýšľať fakty o firme.** Texty sekcií sú prevzaté z allmont.sk. Technické
  parametre profilu boli zámerne vyhodené, pretože ich firma nepotvrdila.

## 4. Otvorené veci, ktoré potrebujú firmu

1. **Fotky do sekcie realizácií.** `real-1.jpg` až `real-3.jpg` sú ilustračné,
   vygenerované. V sekcii je o tom poctivá poznámka. Pred spustením naostro ich
   treba vymeniť za skutočné fotky z tých šiestich menovaných realizácií.
2. **Ceny servisu.** Zoznam prác je z pôvodnej stránky, kde bol cenník platný od
   15.01.2013. Ceny sú zámerne na vyžiadanie.
3. **Formulár** otvára návštevníkovi jeho e-mailový program. Ak má odosielať web
   sám, treba k tomu službu na odosielanie.
4. **Verejná adresa.** Pages na privátnom repozitári vyžaduje platený plán.
   Možnosti: repozitár na verejný, GitHub Pro, alebo Cloudflare Pages
   či Netlify, ktoré fungujú aj s privátnym repozitárom.
   Pred nasadením doplniť dve značky označené `DEPLOY STEP` v `index.html`.

## 5. Čo bolo zadané ako ďalší krok

- **Krajšie piktogramy** v sekcii sortimentu. Súčasné sú nakreslené od oka.
  Správne riešenie: postaviť ich na konštrukcii loga, teda mriežka 96 jednotiek,
  vonkajší obrys 11 jednotiek, vnútorné priečky 6,5, rádius R14, a jeden 45°
  odlesk vo farbe skla ako podpis. Vtedy budú vyzerať ako súrodenci loga.
- **Krajšie prechody medzi sekciami.** Teraz sú oddeľovače len na troch miestach
  a nesystematicky. Cieľom je jeden opakovaný prvok pred každou sekciou, ktorý
  nesie číslo, názov a vlasovú linku, aby prechod bol oznámený a nie náhodný.
- **Mobilná verzia.** Klient má pripravené video v zvislom formáte. Treba sa
  spýtať, či v ňom bude vypálené logo.
- **Zmeny obsahu**, zatiaľ neurčené.

## 6. Technické veci, ktoré sa už raz vyriešili, netreba nanovo

- **Kolízia názvov v štýloch.** Trieda `done` patrila potvrdzovacej správe pod
  formulárom aj systému postupného objavovania, takže štyri bloky na stránke
  po objavení zhasli. Preto sa animačná trieda menuje `stg-done`.
- **Rozostrenie pozadia** je len tam, kde pod prvkom naozaj niečo prechádza,
  teda navigácia, spodná lišta a popisky na fotkách. Na plochách nad jednolitým
  pozadím je nevidiéteľné a spôsobovalo nevykreslenie prvkov.
- **Rýchle scrollovanie.** Obsah sa pripravuje dve obrazovky dopredu a keď
  stránka spozná rýchle scrollovanie, prelínanie úplne vypne, aby nikde
  nezostalo prázdne miesto.
- **Kešovanie.** `serve.py` zámerne zakazuje kešovanie. Adresy obrázkov a videí
  nesú `?v=3`, pretože súbory si medzi verziami držali rovnaké názvy a prehliadač
  ukazoval staré snímky.
- **Obnovenie stránky** nevracia pozíciu scrollu, intro vždy začína od začiatku.

## 7. Ako to spustiť a otestovať

Náhľad: dvakrát kliknúť na `SPUSTIT-WEB.command`, alebo `python3 serve.py 8123`.

Testovanie sa robilo v skutočnom Chrome cez protokol DevTools, nie v náhľadovom
paneli. Panel nekreslí, keď nie je v popredí, čím sa zastaví mechanizmus, na
ktorom scrollovanie beží, a stránka vyzerá zamrznutá.
