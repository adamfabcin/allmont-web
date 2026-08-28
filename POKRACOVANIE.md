# Odovzdanie práce, stav a pravidlá

Tento súbor slúži na to, aby sa v novom sedení dalo pokračovať bez toho, aby sa
znova vymýšľalo, čo už je rozhodnuté. Čítaj ho spolu s `README.md`.

Projekt: jednostránkový web pre **ALL MONT, spol. s r.o.**, Nitra, výroba
a montáž plastových a hliníkových okien a dverí. Pôvodná stránka: allmont.sk.

Repozitár: `github.com/adamfabcin/allmont-web`, vetva `main`, **privátny**.

---

## 0. Kde to práve stojí

Klient to ide **prezentovať svojmu klientovi**, na svojom Macu, lokálne. Stránka
je hotová a funkčná, všetko je commitnuté a pushnuté.

Tri veci, ktoré vie prezentáciu potichu pokaziť a treba na ne upozorniť:

- Zapnuté **Reduce motion** v systéme. Vtedy sa scrollované videá vôbec
  nespustia a ukáže sa statická náhrada. Toto je jediná vec, ktorá to dokáže
  vypnúť bez akéhokoľvek varovania.
- Okno **na výšku alebo užšie ako 1024 px**. To isté, statická náhrada.
- **Safari nie je overené.** Overený je Chrome. Riziko je konkrétne: scrollované
  4K video znamená stovky presných skokov v 40 MB súbore. Kódovanie „každá
  snímka kľúčová" je presne proti tomuto, ale otestované to nebolo. Keby to
  v Safari drhlo, prepnutie na verziu 1440 je jednoriadková zmena v `pickVideo`.

Verejná adresa zatiaľ nie je a nie je nutná. Keby ju chcel, pozri časť 7.

## 1. Ako to spustiť a otestovať

Náhľad: dvakrát kliknúť na `SPUSTIT-WEB.command`, alebo `python3 serve.py 8123`.

Testovanie treba robiť v **skutočnom Chrome**, nie v náhľadovom paneli. Panel
nekreslí, keď nie je v popredí, čím sa zastaví mechanizmus, na ktorom
scrollovanie beží, a stránka vyzerá zamrznutá. Navyše v tomto projekte panel pri
väčšine rozmerov vracia **prázdne snímky obrazovky**, hoci stránka je v poriadku.
Overené to bolo aj na obyčajnej sekcii, takže to nie je chyba stránky. Preto sa
veľa vecí dá overiť len číslami z DOM, nie obrázkom, a treba s tým počítať.

## 2. Čo je hotové a nemá sa meniť

**Úvodné intro je schválené a zamrznuté.** Klient povedal doslova „intro je
super, to necháme tak". Nezasahovať doňho bez výslovnej žiadosti.

Ako intro funguje:

- Zdroj je `hero-2160.mp4`, 3840×2160, 25 snímok, 15,6 s, **každá snímka je
  kľúčová**. To je zámer, nie omyl: jeden skok pri scrollovaní potom dekóduje
  presne jednu snímku, okolo 9 ms aj v 4K. Pri bežnom kódovaní s kľúčovou
  snímkou každých osem to je 72 ms a scrollovanie vlečie.
- Video sa sťahuje celé ako blob, až potom sa zapne scrollovanie. Do vtedy drží
  miesto `hero-poster.jpg`, teda prvá snímka.
- Hero má výšku 1500vh.
- **Päť titulkov** v prvých dvoch tretinách, biele, jeden rovnaký jemný závoj.
  Posledná tretina beží bez textu.
- Nápoveda „Scrollujte" a linka postupu sú dole v strede po celý čas, **biele
  po celý čas**. Predtým sa na svetlých snímkach prepínali na tmavú, lebo
  meranie jasu presne pod nimi hovorí, že od 70 percent videa klesne kontrast
  bielej na 2,1 až 3,1:1. Biela sa drží vlastným systémom čitateľnosti: **mäkký
  radiálny závoj**, ten istý ako za titulkami, krytie 0,56 v strede. To číslo je
  spočítané, nie odhadnuté: aby vyšla norma 4,5:1, musí byť pod písmom jas
  najviac 119. Kto ten závoj odstráni, spraví nápovedu na konci intra
  neviditeľnou.
- Doplnená časť linky postupu **žiari**, žiara rastie spolu s ňou. Linka je plná
  presne vtedy, keď je obrazovka biela, teda keď sa prvá animácia naozaj končí.
  Počíta sa z `VEIL_B`, nie z `TIME_END`.
- Kurzor je zameriavací kríž. Počas intra sa pri scrollovaní skryje a pohyb
  myšou ho vráti. Po intre zostáva.

**Piktogramy sortimentu sú postavené na konštrukcii loga.** Mriežka 96,
vonkajší obrys 11 s rádiusom R14, vnútorné priečky 6,5 a jeden 45° odlesk vo
farbe skla `#8FC1F2` v ľavej hornej tabuli ako podpis. Kreslia sa
v `currentColor`, odlesk nesie trieda `gl`.

**Prechod pred každou sekciou je systémový.** Prvok `.divider` stojí ako prvé
dieťa každej z ôsmich sekcií a nesie číslo `01` až `08`, vlasovú linku
a názov sekcie. Názov nesie oznamovač, preto štítok `.label` v hlavičke sekcie
nie je, inak by tá istá vec stála dvakrát pod sebou.

**Priemium vrstva.** Manuál zakazuje gradienty na plochách, zaoblené rohy aj
druhé písmo, takže hodnotu nesie:

1. **Pevná mriežka vlasových stĺpcov za stránkou.** Priesvitné panely sa pri
   scrollovaní posúvajú voči nej a hĺbka je skutočná. Sú to skutočné 1 px prvky,
   nie gradient. Tmavé bloky a pätička majú tú istú mriežku vo farbe skla.
2. **Príchody, ktoré je vôbec vidieť.** Predtým to bolo preblikanie za 0,32 s
   spúšťané dve obrazovky dopredu, takže ho nikto nikdy neuvidel. Teraz obsah
   prichádza zdola za 0,95 s a spúšťa sa tesne pred vstupom do obrazu. Poistka
   pre rýchle scrollovanie zostáva.
3. **Nadpisy po riadkoch.** Skript zmeria, kde riadky sadli, a až potom nadpis
   poskladá nanovo. Pri zlyhaní zostane obyčajným nadpisom.
4. **Obrazy prichádzajú stierkou** a dosadajú z mierneho priblíženia, s bielymi
   zameriavacími rohmi v jazyku kurzora.

K tomu tichá drobnosť: azúrová hrana, ktorá sa nakreslí. Nad kartou, pod odkazom
v navigácii, pod tlačidlom bez výplne, pod odkazom v pätičke.

## 3. Odovzdanie z intra na dodávku

Toto stálo najviac času a bolo prerobené päťkrát. **Nič z tejto časti nemeniť
naslepo.** Rozsekla to až predloha: klient si prechod zostrihal vo videu a poslal
ho. Z merania jeho zostrihu:

- trinásť snímok sa obraz okna **vybieluje**,
- jednu snímku je celá plocha **úplne biela** (priemerný jas 252, najtmavší bod
  251, čiže tam nie je nič okrem bielej),
- dvanásť snímok sa z tej bielej **vynára dodávka** a hneď prichádza sprava.

Je to teda **prechod cez bielu, nie prelínanie**. Preto je závoj biely a pozadie
záberu dodávky je biele. Video dodávky bolo pôvodne vynásobené hmlou; vrátilo sa
späť presným inverzným prevodom (`colorchannelmixer` 1,071429 / 1,058091 /
1,045082), takže pozadie je opäť čistá 255,255,255.

Rozpis na scroll, celé odovzdanie je jedna obrazovka:

| úsek | závoj | plocha dodávky | snímka dodávky |
|---|---|---|---|
| 0 % | 0,23 | 0 | 0, video sa rozbieha už tu |
| 50 % | **1,00, čistá biela** | 0 | 14 |
| 75 % | 1,00 | 0,45 | 21 |
| 100 % | 1,00 | 1,00 | 29 |

Čísla: `VEIL_A` 0,912, `VEIL_B` 0,9657, `TIME_END` 0,9657, `VAN_VIDEO_A` 0,
`VAN_FADE_A` 0,52, `VAN_FADE_B` 1,0, `.hero2` má `margin-top:-200vh`.

### Sedem vecí, ktoré sa tu pokazili a nesmú sa vrátiť

1. **`.hero2` NESMIE mať vlastnú farbu pozadia.** `.hero` aj `.hero2` sú obe
   `position:relative` so `z-index:auto`, takže sa kreslia v tej istej vrstve
   a rozhoduje poradie v dokumente. `.hero2` je neskôr, takže jej pozadie kreslí
   **nad** pevnou plochou intra. A keďže je to obyčajný blok, ktorý sa
   scrollovaním posúva hore, jej biele pozadie sa cez intro zdvíhalo **ako biela
   lišta zospodu**. Bielu nesie výlučne pripnutá plocha `.stage2`, ktorá stojí.
2. **Plocha intra je `position:fixed`, nie `sticky`,** a prepína ju na to skript
   v `enableScrub`. Pripnutá plocha sa pri scrollovaní hýbe, a keď skript
   o zlomok sekundy zaostane, jej spodný okraj vidno ako **tvrdú hranu**. Pevná
   plocha sa nehýbe nikdy. V štýloch zostáva `sticky`, aby stránka bez
   JavaScriptu neostala pod celoobrazovkovou plochou.
3. **`.stage` musí mať `z-index:0`.** Bez neho nevytvára vlastnú vrstvu a jej
   deti so `z-index` (závoj 20, titulky 14, nápoveda 15, horná lišta 30) kreslia
   nad plochou dodávky.
4. **Plocha intra sa nesmie bledúť priesvitnosťou.** Bielenie robí závoj vnútri
   nej. Keby blednúť začala, presvitalo by cez ňu tmavé pozadie sekcie intra.
5. **Bielenie ide zo surového postupu scrollu, nie z tlmenej hodnoty.** Tlmenie
   patrí len času videa. Kým na ňom visel aj závoj, bielenie zaostávalo
   a prechod pôsobil nadvakrát.
6. **Video dodávky beží už pod bielou.** `VAN_VIDEO_A` (kde sa rozbehne video)
   je 0, ale `VAN_FADE_A` (kde sa začne objavovať plocha) je 0,52. Keď boli obe
   na tom istom čísle, dodávka sa vynorila na nultej snímke, teda ako prázdna
   biela plocha, a pôsobilo to, akoby sa druhá animácia vôbec nezačala.
7. **Text má vlastného strážcu zápisu.** Kým ho mal spoločný s priesvitnosťou
   plochy, prestal sa zapisovať vo chvíli, keď plocha dosiahla jednotku, a text
   sa neobjavil nikdy. Text príde až potom, na postupe sekcie 0,26 až 0,44,
   neposúva sa, len sa vynorí. Príchod zdola aj príchod spolu s dodávkou boli
   skúšané a klient odmietol oboje.

## 4. Pravidlá značky, ktoré platia bez výnimky

Vychádzajú z dizajn manuálu značky, verzia 1.0, ktorý má klient vlastný.
**Manuál má prednosť pred akýmikoľvek zvykmi.**

- **Jedno písmo na všetko:** Helvetica Neue, náhrada Inter Tight. Rozdiely nesie
  len hrúbka, veľkosť a prestrih. Klient to zdôraznil dvakrát.
- **Farby:** azúrová `#1E6FD9` je akcent, nie pozadie. Námorná `#0F2233` na text
  a tmavé plochy. Sklo `#8FC1F2`. Hmla `#EEF1F4` na pozadia. Pomer plôch
  približne 60 hmla, 25 námorná, 12 azúrová.
- **Pozadie stránky sa nemení na biele.** Bola to otázka a odpoveď je nie. Hmla
  nesie 60 percent plôch a celý systém hĺbky na nej stojí: panely sú biele pri
  72 až 88 percentách položené na hmle a mriežka za stránkou je vidieť len vďaka
  tomu rozdielu. Biela je len v odovzdaní na dodávku a v jej sekcii.
- **Žiadne gradienty na plochách, tlačidlách ani texte.** Jediná výnimka je
  závoj pod textom nad videom, čo je systém čitateľnosti, nie ozdoba.
- **Pravé uhly.** Žiadne zaoblené rohy v rozhraní. Jediný rádius v značke je
  R14 na symbole loga, ten patrí len logu a piktogramom postaveným na jeho
  konštrukcii.
- **Žiadne kurzívy.**
- Logo: symbol je okno s krížom a jedným 45° odleskom v ľavej hornej tabuli.
  Nikdy neprekresľovať, používať priložené SVG.

## 5. Technické pasce, ktoré stáli čas

**Hľadanie v videu musí mať časovú poistku.** Kým prebieha jeden skok, ďalší sa
nezadáva, a príznak „hľadám" sa vypína, keď prehliadač ohlási dokončenie. Lenže
on ho neohlási vždy: keď nový čas padne do tej istej snímky, udalosť neprebehne
a príznak zostane zapnutý **navždy**. Video sa tým zasekne v oboch smeroch.
Prejavilo sa to tak, že sa dodávka pri scrollovaní späť nevrátila. Skok, ktorý sa
neohlási do 400 ms, sa preto považuje za stratený. A slučka musí bežať, kým sa
posledný skok naozaj nezadá, nie len kým dobehne tlmená hodnota.

**Atribúty `width` a `height` na `<img>` prebíjajú `aspect-ratio`.** Prehliadač
ich uplatňuje ako pevné rozmery. Šírku prebije `width:100%`, ale výšku neprebije
nič, takže rám dostane pevnú výšku z atribútu. Stalo sa to pri výmene fotky: rám
mal 1200 px namiesto pomeru a obrázok sa kvôli tomu pri odloženom načítaní ani
nestiahol. Všetky obrázky s `aspect-ratio` majú preto aj **`height:auto`**
a atribúty musia sedieť so skutočným pomerom súboru.

**Kolízia názvov v štýloch.** Trieda `done` patrila potvrdzovacej správe pod
formulárom aj systému postupného objavovania, takže štyri bloky po objavení
zhasli. Preto sa animačná trieda menuje `stg-done`.

**Rozostrenie pozadia** je len tam, kde pod prvkom naozaj niečo prechádza, teda
navigácia, spodná lišta a popisky na fotkách. Na plochách nad jednolitým pozadím
je neviditeľné a spôsobovalo nevykreslenie prvkov.

**Rýchle scrollovanie.** Keď stránka spozná rýchle scrollovanie, prelínanie
príchodov úplne vypne, aby nikde nezostalo prázdne miesto.

**Kešovanie.** `serve.py` zámerne zakazuje kešovanie. Adresy obrázkov a videí
nesú `?v=…`, pretože súbory si medzi verziami držali rovnaké názvy.

**Obnovenie stránky** nevracia pozíciu scrollu, intro vždy začína od začiatku.

## 6. Ako sa tu pracuje, čo klient ocenil

- **Merať, nie hádať.** Každé rozhodnutie o čitateľnosti textu nad videom padlo
  z merania jasu presne v mieste textu. Kontrast sa počíta, nie odhaduje.
- **Testovať tou cestou, ktorou ide používateľ.** Jedna chyba sa dlho skrývala
  presne preto, že testy si stavy zapínali ručne a obchádzali vetvu kódu, ktorá
  ju spôsobovala.
- **Hovoriť nahlas o odchýlkach a o vlastných chybách.** Klient na to reaguje
  dobre. Keď meranie povie, že jeho inštrukcia nevyjde, treba to povedať
  a ponúknuť náhradu.
- **Keď sa niečo nedarí opraviť na tretí raz, problém je inde, než sa hľadá.**
  Pri odovzdaní na dodávku sa štyrikrát ladili čísla, hoci príčina bola
  zakaždým štrukturálna. Pomohlo až to, že klient poslal vlastný zostrih.
- **Nevymýšľať fakty o firme.** Texty sekcií sú prevzaté z allmont.sk. Technické
  parametre profilu boli zámerne vyhodené, pretože ich firma nepotvrdila.

## 7. Otvorené veci, ktoré potrebujú firmu

1. **Fotky do sekcie realizácií.** `real-1.jpg` až `real-3.jpg` sú ilustračné,
   vygenerované. V sekcii je o tom poctivá poznámka. Pred spustením naostro ich
   treba vymeniť za skutočné fotky z tých šiestich menovaných realizácií.
   `shot-1.jpg` v sekcii o spoločnosti už **skutočná je**, je to fotka výrobnej
   haly od klienta, na výšku, rám je v jej vlastnom pomere 2:3 bez orezu.
   Variant 4:3 s bielym okrajom po stranách bol skúšaný a klient ho odmietol.
2. **Ceny servisu.** Zoznam prác je z pôvodnej stránky, kde bol cenník platný od
   15.01.2013. Ceny sú zámerne na vyžiadanie.
3. **Formulár** otvára návštevníkovi jeho e-mailový program. Ak má odosielať web
   sám, treba k tomu službu na odosielanie.
4. **Verejná adresa.** Repozitár je privátny a `hero-2160.mp4` má 40 MB.
   Z toho: **Cloudflare Pages nepôjde**, má limit 25 MB na súbor. **GitHub
   Pages** by prešiel, ale na privátnom repozitári vyžaduje platený plán.
   **Netlify** funguje s privátnym repozitárom aj na bezplatnom pláne a veľkosť
   zvládne, to je odporúčaná cesta. Alternatíva na jednorazové ukázanie je
   Cloudflare tunel priamo z Macu, bez účtu a bez nahrávania.
   Pred nasadením doplniť dve značky `REPLACE-AT-DEPLOY` v `index.html`.

## 8. Čo je zadané ako ďalší krok

- **Mobilná verzia.** Klient má pripravené video v zvislom formáte. **Otázka na
  klienta, na ktorej to stojí: bude v tom videu vypálené logo?** Ak áno, treba
  vedieť kde, aby sa naň neposadili titulky ani navigácia. Zatiaľ je na mobile
  namiesto videa statický `hero-plate.jpg`.
- **Zmeny obsahu**, zatiaľ neurčené. Naposledy klient dal preč pás údajov
  s certifikátmi a typmi stavieb, ktorý bol hneď za dodávkou. Certifikáty
  zostali vo vlastnej sekcii 07.

## 9. Kde sú zdroje

`~/Desktop/ALLMONT/` obsahuje `allmont-intro-master-4k.mov` (majster intra,
1,3 GB), `dodavka.mov` (majster dodávky, 323 MB), dizajn manuál v PDF a logá.
Recepty na kódovanie oboch videí sú v `README.md`.
