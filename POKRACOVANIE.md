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
  (0,98), rozplývanie do farby stránky beží od `VEIL_A` 0,92 po `VEIL_B` 1,0.
  Prekrývajú sa zámerne: posledných zhruba dvadsať snímok okna sa prehrá už
  pod rozplývaním, čo je to isté, ako keby boli odstrihnuté, len sa nič
  nezahodilo. Rozplývanie končí presne na 1,0, teda presne tam, kde sekcia
  končí a nastupuje dodávka, takže **za introm nezostane ani kúsok prázdnej
  obrazovky**.

  Ako sa k tomu došlo: pôvodne bolo `TIME_END` 0,90 a `VEIL_A` 0,955, medzi
  koncom videa a začiatkom prechodu teda bolo 616 px scrollu, na ktorých sa
  nedialo nič. Meranie pohybu medzi snímkami pritom ukázalo, že samotné video
  až do konca beží, posledná sekunda má 100 až 250 percent svojho priemerného
  pohybu. Stálo teda scrollovanie, nie obraz. Nápoveda „Scrollujte" (0,920 až
  0,975) aj nástup navigácie (0,955) sú naviazané na rozplývanie, nie na koniec
  videa, a treba ich posúvať spolu s ním.
- **Päť titulkov** v prvých dvoch tretinách, biele, jeden rovnaký jemný závoj.
  Posledná tretina beží bez textu.
- Na konci sa obraz rozplynie do farby stránky a **nadpis sa vynára priamo
  v tom prechode** (blok `.end`), aby za introm nezostala prázdna obrazovka.
- Nápoveda „Scrollujte" a linka postupu sú dole v strede po celý čas.
- Kurzor je zameriavací kríž. Počas intra sa pri scrollovaní skryje a pohyb
  myšou ho vráti. Po intre zostáva.

**Piktogramy sortimentu sú postavené na konštrukcii loga.** Nekreslia sa už od
oka. Každý stojí v mriežke 96, vonkajší obrys má hrúbku 11 a rádius R14, vnútorné
priečky 6,5 a jeden 45° odlesk vo farbe skla `#8FC1F2` v ľavej hornej tabuli ako
podpis. Sú to teda súrodenci loga, nie cudzie ikony. Kreslia sa v `currentColor`,
odlesk nesie trieda `gl`. Šesť motívov: okno s nadsvetlíkom, tri úzke tabule,
krídlo so šípkou, dvere s bočným svetlom a kľučkou, okno s parapetnou doskou,
okno s kľučkou.

**Prechod pred každou sekciou je systémový.** Ten istý prvok `.divider` stojí ako
prvé dieťa každej z ôsmich sekcií a nesie číslo `01` až `08`, vlasovú linku
s pomaly bežiacim azúrovým ťahom a názov sekcie. Názov nesie oznamovač, preto sa
štítok `.label` z hlavičky sekcie zrušil, inak by tá istá vec stála na stránke
dvakrát pod sebou. Na tmavých sekciách sa linka aj text prepnú, sekcia si drží
vlastné odsadenie a oznamovač zdedí len šírku sadzobného zrkadla. Odsadenia
sekcií sú preto späť na jednom rytme, bez ručných výnimiek.

**Druhá priemium vrstva.** Zadanie znelo, nech to vyzerá podstatne drahšie.
Manuál pritom zakazuje gradienty na plochách, zaoblené rohy aj druhé písmo,
takže hodnotu nebolo možné kúpiť ozdobou. Nesú ju štyri veci:

1. **Pevná mriežka za stránkou.** Priesvitné plochy boli doteraz priesvitné do
   prázdna, pod nimi bola jednoliata farba, takže sklo nebolo vidieť. Teraz je
   za nimi pevná mriežka vlasových stĺpcov, panely sa pri scrollovaní posúvajú
   voči nej a hĺbka je skutočná. Sú to skutočné 1 px prvky, nie gradient.
   Tmavé bloky a pätička majú tú istú mriežku vo farbe skla.
2. **Príchody, ktoré je vôbec vidieť.** Predtým to bolo preblikanie za 0,32 s,
   ktoré sa spúšťalo dve obrazovky dopredu, takže ho nikto nikdy neuvidel.
   Teraz obsah prichádza zdola za 0,95 s a spúšťa sa tesne pred vstupom do
   obrazu. Poistka pre rýchle scrollovanie zostáva: keď človek cukne o viac
   ako obrazovku, okno sa roztiahne späť na dve obrazovky a prelínanie sa
   vypne, takže nikde nezostane diera.
3. **Nadpisy po riadkoch.** Každý riadok je vlastné okienko a text sa doň
   zasunie zdola. Skript najprv zabalí slová, odmeria, kde riadky sadli, a až
   potom nadpis poskladá nanovo. Robí sa to znova pri zmene šírky okna a keď
   čokoľvek zlyhá, nadpis zostane obyčajným nadpisom.
4. **Obrazy prichádzajú stierkou** zhora nadol a dosadajú z mierneho
   priblíženia, s bielymi zameriavacími rohmi, ktoré sú ten istý jazyk ako
   kurzor. Rohy sú biele s tichým tieňom, pretože azúrová sa na svetlej fotke
   stratí a na tmavej kričí.

K tomu tichá drobnosť po celej stránke: hrana, ktorá sa nakreslí. Azúrová linka
nad kartou, pod odkazom v navigácii, pod tlačidlom bez výplne, pod odkazom
v pätičke, a vlasová linka oznamovača sa pri príchode roztiahne od ľavého okraja.

**Druhé scrollované video, príchod dodávky.** Za nadpisom „Dodávka a montáž"
beží druhý scrollovaný záber. Intro zostalo nedotknuté, toto je samostatná
sekcia s vlastnou pripnutou plochou, vlastným postupom a vlastným sťahovaním.

Kľúčové rozhodnutie je farba. Zdrojový záber je štúdiový, na úplne čistej bielej
255,255,255, overené meraním. Pri kódovaní je preto biela vynásobená hmlou
`#EEF1F4`, takže **pozadie záberu je farba stránky**. Z toho plynú tri veci naraz:

- Intro sa na konci rozplynie do farby stránky a prvá snímka tohto videa je
  presne tá istá farba. Prechod medzi dvoma pripnutými plochami preto nie je
  vidieť, hoci je to obyčajný scroll.
- Nie je tu obrázok, ktorý drží miesto, ani krúžok načítania. Kým sa súbor
  sťahuje, drží miesto samotné pozadie stránky, takže nie je čo nahrádzať.
- Záber môže byť zobrazený cez `object-fit:contain` a pásy, ktoré pri tom
  vzniknú, nie je vidieť. `cover` sem nepatrí, stojan so sklom siaha až po
  pravý okraj obrazu a na užšej obrazovke by ho orezalo.

**Pozadie stránky sa preto nemení na biele.** Bola to otázka a odpoveď je nie.
Hmla nesie podľa manuálu 60 percent plôch a celý systém hĺbky na nej stojí:
panely sú biele pri 72 až 88 percentách položené na hmle a mriežka za stránkou
je vidieť len vďaka tomu rozdielu. Na bielom pozadí by panely aj mriežka zmizli.
Zosúladil sa teda záber so stránkou, nie stránka so záberom.

Záber je presné 16:9 a využíva sa celý. Čierne pásy 7 px hore aj dole boli
nahradené bielou, ktorá sa pri kódovaní stala hmlou, takže rozmer je 3840×2160
bez orezu a bez deformácie. Text sedí dole. Stojí nad obrazom, preto je pod ním
závoj, ten istý systém čitateľnosti ako v intre, len obrátený: tam tmavý na
tmavom zábere, tu z hmly na svetlom. Krytie 0,86 je merané, nie odhadnuté:
najtmavší bod pod textom cez všetkých 167 snímok má bez závoja kontrast 1,0:1,
so závojom 10,4:1. Úplné krytie by dalo 14,1:1, ale zjedlo by kolesá dodávky.

**Obe plochy sa prekrývajú, prechod je prelínanie, nie scroll.** Toto je
najdôležitejšia časť a bola postavená na dva razy nesprávne, tak pozor:

- `.hero2` má `margin-top:-195vh`. Nie -95vh. Pripnutá plocha intra sa totiž
  odopne už **jednu obrazovku pred koncom** svojej sekcie, nie na jej konci.
  Prekryv teda musí byť o tú obrazovku väčší, inak nevznikne vôbec. 100vh je
  to dobehnutie, 95vh je samotné prelínanie.
- Na prekryve sú obe pripnuté plochy naraz. Plocha dodávky má `z-index:1`,
  takže kreslí navrchu, a jej priesvitnosť riadi skript zo svojho postupu.
  Pozadie sekcie `.hero2` sa pritom kreslí **pod** plochu intra, takže cez
  polopriesvitnú dodávku vidno dohrávajúce intro. To je zámer.
- Rozplynutie intra do hmly je **rýchlejšie** ako prelínanie (0,925 až 0,965
  oproti prekryvu, ktorý beží až do konca). Musí to tak byť, inak by sa pod
  polopriesvitnou plochou dodávky ukazoval duch poslednej snímky okna.
- **`.stage` musí mať `z-index:0`. Toto je najdôležitejší riadok celého
  odovzdania.** Bez neho `.stage` nevytvára vlastnú vrstvu, takže jej deti so
  `z-index`, teda závoj 20, titulky 14, nápoveda 15 a horná lišta 30, nekreslia
  vnútri intra, ale v spoločnej vrstve stránky, a tým pádom **nad** plochou
  dodávky, ktorá má `z-index:1`. Prelínanie pritom pracovalo správne, len ho
  intro prekrývalo zhora. Prejavovalo sa to dvoma vecami naraz, ktoré vyzerali
  ako dve rôzne chyby: tvrdý zlom na hrane pripnutej plochy pri scrollovaní
  dopredu, a pri scrollovaní späť dojem, že sa animácia už nevracia, pretože
  krycí závoj intra prekryl dodávku aj sám seba.
- **Plocha intra sa rozplýva priesvitnosťou, nie maskou.** Skúšaná bola aj
  maska s prechodom na spodnom okraji, ale maska má z podstaty okraj a práve
  ten okraj bol tá seknutá hrana. Priesvitnosť žiadnu geometriu nemá, takže sa
  nemá kde nič seknúť: okno sa po celej ploche naraz vytratí do farby stránky,
  zatiaľ čo dodávka pribúda. Je to čisté prelínanie, `intro 1 → 0` a
  `dodávka 0 → 1` na tom istom úseku.
- **Prekryv je 200vh, teda dve celé obrazovky.** Pri 95vh bolo prelínanie
  technicky správne, ale dodávka za ten čas stihla vystrčiť len nos a plocha
  pôsobila prázdno. Cez dve obrazovky sa okno rozplýva a dodávka prichádza
  súčasne, takže nie je chvíľa, keď by na obrazovke nebolo nič.
- Plocha intra je počas celého prelínania **pripnutá** (`stTop` je 0) a je
  úplne priesvitná ešte predtým, než by sa vôbec pohla. To je overené
  skenovaním celého úseku, nie odhadom.
- **Priesvitnosť prelínania ide zo surového postupu scrollu, nie z tlmenej
  hodnoty.** Tlmenie patrí k času videa, aby skoky nedrhli. Pri prelínaní
  zaostávalo, takže pri rýchlejšom scrolle plocha nestihla docelovať skôr,
  než sa pripnutá plocha intra odopla, a bolo vidieť **tvrdú hranu**: obraz
  okna odchádzal hore a pod ním svietila holá hmla. Toto bola hlásená chyba.
- Prelínanie končí na **72 percentách** prekryvu, nie na sto. Zvyšok je
  rezerva, aby bolo hotové s istotou skôr, než sa intro pohne. Pri 1440×860 to
  vychádza tak, že prelínanie dobehne na 11 811 px a intro sa odopne až na
  12 040 px.
- Keď je plocha dodávky krycia, plocha intra sa prepne na `visibility:hidden`.
  Poistka proti tej istej hrane a zároveň úspora pri skladaní obrazu.
- Dodávka sa pohne v tej istej chvíli, ako sa začne prelínať (`VAN_LEAD` 0).
  Nečaká na nič. Príchod sprava tým neprichádza o nič, len sa jeho začiatok
  deje už pod rozplývajúcim sa oknom, nie až po ňom.
- Záber dodávky má `object-fit:contain` a `object-position:50% 40%`. Contain,
  nie cover: stojan so sklom siaha až po pravý okraj obrazu a cover by ho na
  inom pomere strán odrezal. Takto sa záber vždy zmestí celý, na väčšej
  obrazovke vyrastie, a pásy, ktoré pritom vzniknú, nie je vidieť, majú tú istú
  farbu ako pozadie záberu aj ako stránka. Ťažisko nad stredom drží dodávku
  nad textom.
- `VAN_SKIP` bol zrušený, žiadne snímky sa nepreskakujú. Príchod je celý.

Sekcia má 720vh, `VAN_END` je 0,94, teda tá istá filozofia ako pri intre: video
dobehne tesne pred koncom a nezostane stáť. Výška je zvolená tak, aby spád vyšiel
na 3,3vh na snímku, teda takmer rovnako ako intro (3,85vh na snímku).

`TIME_END` intra je 0,93, teda presne tam, kde sa prekryv začína. Nie je to len
kvôli medzere: keby video okna bežalo ďalej, dekódovali by sa počas prelínania
dve 4K videá naraz a scroll by sekol. Preto je aj filter, ktorý zahodí požiadavku
na ten istý čas, aby držaná snímka nespúšťala hľadanie znova a znova. Filtrovať
sa to musí pri vstupe, nie vo fronte, inak front zahodí čakajúcu požiadavku. Kvalita overená proti majstrovi,
SSIM 0,994. Veľkosti: 9,6 MB v 4K, 5,4 MB a 3,7 MB ako záloha.

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

Prvé dve veci sú hotové, popísané sú v časti 1. Ostáva:

- **Mobilná verzia.** Klient má pripravené video v zvislom formáte. **Otázka na
  klienta, na ktorej to stojí: bude v tom videu vypálené logo?** Ak áno, treba
  vedieť kde, aby sa naň neposadili titulky ani navigácia. Zatiaľ je na mobile
  namiesto videa statický `hero-plate.jpg`.
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
