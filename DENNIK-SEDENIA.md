# Denník sedenia, 28. augusta 2026

Záznam toho, čo sa v tomto sedení riešilo, prečo a s akým výsledkom. Nie je to
prepis rozhovoru, je to jeho obsah: zadania, merania, slepé uličky a rozhodnutia,
naviazané na commity. Slúži na to, aby sa v budúcnosti nemuselo znova prísť na to,
na čo sa raz prišlo.

Stav a pravidlá sú v `POKRACOVANIE.md`. Tento súbor je história, ten je návod.

---

## Ako sa v tomto sedení pracovalo

Klient zadával po častiach, väčšinou jednou vetou, a hodnotil výsledok očami.
Fungovalo toto:

- **Merať, nie hádať.** Každé rozhodnutie o čitateľnosti a o časovaní padlo
  z čísel. Keď meranie odporovalo zadaniu, povedať to a ponúknuť náhradu.
- **Priznať vlastnú chybu rovno a konkrétne.** Klient na to reagoval dobre,
  aj keď bol podráždený.
- **Keď sa niečo nedarí opraviť na tretí raz, hľadá sa na zlom mieste.**
  Toto je najdrahšia lekcia sedenia, rozpísaná nižšie.
- **Vizuálny problém sa najrýchlejšie rieši vizuálnou predlohou.** Prechod
  medzi videami sa vyriešil až vtedy, keď klient poslal vlastný zostrih.

---

## 1. Piktogramy a oznamovače sekcií · `6fabcb4`

**Zadanie:** krajšie piktogramy v sortimente a systémovejšie prechody medzi
sekciami.

Piktogramy boli kreslené od oka. Prekreslené na konštrukciu loga: mriežka 96,
obrys 11, rádius R14, priečky 6,5, jeden 45° odlesk vo farbe skla. Dva som po
prvom pohľade prekreslil ešte raz: šikmá kľučka pri servise sa čítala ako zlom
a zavadzala si s odleskom, parapetná doska sedela privysoko.

Oddeľovače sekcií boli predtým len na dvoch miestach. Teraz ten istý prvok stojí
na začiatku všetkých ôsmich sekcií a nesie číslo, linku a názov. Štítok
v hlavičke sekcie tým odišiel, inak by tá istá vec stála dvakrát pod sebou.

## 2. Koniec intra stál · `90e574b`

**Zadanie:** „skráť animáciu o pár framov, mám pocit že tam na konci stojí."

Meranie pohybu medzi snímkami ukázalo, že **video nestojí** — posledná sekunda má
100 až 250 percent svojho priemerného pohybu. Stálo scrollovanie: medzi koncom
videa a začiatkom prechodu bolo 616 px, na ktorých sa nedialo nič. Posunutím
`TIME_END` klesla tá medzera na 112 px.

**Poučenie:** zadanie hovorilo „skráť video", príčina bola inde. Bez merania by
sa zahodil živý materiál a pocit by zostal.

## 3. Priemium vrstva · `4df8141`

**Zadanie:** „je to strašne strohé, nech to vyzerá podstatne drahšie, font nemeň."

Manuál zakazuje gradienty, zaoblené rohy aj druhé písmo, takže sa hodnota nedala
kúpiť ozdobou. Postavená je na štyroch veciach: pevná mriežka vlasových stĺpcov
za stránkou (dá priesvitnosti zmysel), pomalšie smerové príchody, nadpisy
vysúvané po riadkoch a obrazy odkrývané stierkou.

Pritom sa našla skrytá chyba: príchody sa spúšťali **dve obrazovky dopredu**,
takže ich nikto nikdy nevidel. Animácia existovala a bola zbytočná.

## 4. Druhé video, príchod dodávky · `5808cba`

**Zadanie:** za úvodný nadpis dať druhé scrollované video s príchodom dodávky,
text posunúť dole.

Zdrojový záber je štúdiový na čistej bielej. Prvá verzia mala bielu vynásobenú
hmlou, aby pozadie záberu bolo farbou stránky. Klient sa spýtal, či sa nemá
pozadie stránky zmeniť na biele — odpoveď bola nie, lebo hmla nesie 60 percent
plôch a celý systém hĺbky na nej stojí. Neskôr sa ukázalo, že pre prechod cez
bielu je predsa len potrebná biela, a násobenie sa vrátilo späť.

## 5. Odovzdanie z intra na dodávku · šesť pokusov

Toto je jadro sedenia a stálo najviac času. **Stojí za prečítanie celé**, lebo
každý pokus zlyhal z iného dôvodu a všetky tie dôvody sú stále aktuálne pasce.

**Pokus 1** `f966c31` — zmenšiť prázdne miesto medzi videami. Pomohlo, ale
klient hlásil tvrdú hranu.

**Pokus 2** `3011ca9` — prekryť obe sekcie a prelínať ich. Pritom sa zistilo, že
pripnutá plocha sa odopne **o jednu obrazovku pred koncom sekcie**, takže
prekryv −95vh nevznikol vôbec a musel byť −195vh.

**Pokus 3** `6489d5d` — priesvitnosť išla z tlmenej hodnoty a pri rýchlom
scrolle zaostávala. Prepnutá na surový postup scrollu.

**Pokus 4** `e33e02d` — `.stage` nemala `z-index`, takže nevytvárala vlastnú
vrstvu a jej deti so `z-index` kreslili nad plochou dodávky. Vyzeralo to ako dve
rôzne chyby naraz: hrana dopredu a „nevracia sa" späť.

**Pokus 5** `d005068` — plocha intra bola `sticky`, čiže sa hýbala. Keď skript
zaostal, jej spodný okraj bolo vidieť. Prepnutá na `fixed`, aby sa nehýbala
nikdy.

**Pokus 6** `de64ff5` — a tu to konečne padlo. Klient popísal, čo vidí: „zospodu
sa vysunie biela lišta". `.hero2` mala biele pozadie a je to obyčajný blok, ktorý
sa scrollovaním posúva hore — a kreslil sa nad pevnou plochou intra. Bielu odvtedy
nesie výlučne pripnutá plocha, ktorá stojí.

**Poučenie, ktoré stojí za zapamätanie:** päťkrát som ladil čísla, hoci príčina
bola zakaždým štrukturálna. Keď oprava nezaberie na tretí raz, netreba hľadať
lepšie číslo, ale iné miesto. A najrýchlejšie to odhalil presný popis toho, čo
klient **vidí**, nie toho, čo si myslí, že je zle.

## 6. Prechod cez bielu podľa predlohy · `69347a2`, `4103ec0`, `d6cc9b5`

Klient nakoniec prechod zostrihal vo videu a poslal ho. Zmerané z jeho zostrihu:
13 snímok bielenia, 1 snímka úplnej bielej (najtmavší bod 251, čiže tam nie je
nič okrem bielej), 12 snímok vynárania dodávky.

Bolo to teda **prelínanie versus prechod cez bielu** — dve úplne odlišné veci.
Celý čas som staval prelínanie. Predloha to rozsekla za jednu minútu merania.

K tomu tri doladenia: bielenie musí ísť zo surového scrollu a začínať už na konci
prvej animácie; video dodávky musí bežať **už pod bielou**, inak sa vynorí na
nultej snímke ako prázdna plocha; a text musí mať vlastného strážcu zápisu.

## 7. Zaseknuté hľadanie v videu · `e1b9fa5`

**Zadanie:** „na animácii dva nefunguje replay, teda aspoň si myslím."

Nemýlil sa. Merané: dopredu snímka 160, späť **156** namiesto 62. Front hľadania
sa vedel natrvalo zaseknúť — príznak „hľadám" sa vypína až keď prehliadač ohlási
dokončenie, a on ho neohlási, keď nový čas padne do tej istej snímky. Odvtedy sa
všetky ďalšie skoky zahadzovali. Doplnená časová poistka 400 ms.

**Poučenie:** rovnaká chyba bola aj v intre, len sa neprejavila tak nápadne.
Keď sa nájde chyba v jednom scrubberi, treba pozrieť aj druhý.

## 8. Drobnosti na záver

- `2c77322` — nápoveda „Scrollujte" biela po celý čas. Meranie ukázalo, že od
  70 percent videa klesne kontrast bielej na 2,1 až 3,1:1, takže bielu drží mäkký
  radiálny závoj s krytím 0,56. Doplnená časť linky žiari.
- `c6f41c1`, `f9e7164` — fotka výrobnej haly. Prvý pokus bol rám 4:3 s bielym
  okrajom, klient chcel fotku na výšku v jej vlastnom pomere. Pritom sa našlo, že
  **atribúty `width` a `height` na `<img>` prebíjajú `aspect-ratio`** a obrázok sa
  kvôli tomu pri odloženom načítaní ani nestiahol.
- `a9a6281` — odstránený pás údajov s certifikátmi za dodávkou.
- `b69c2dd` — `POKRACOVANIE.md` prepísaný načisto.

## 9. Čo zostalo otvorené

Podrobne v `POKRACOVANIE.md`, časti 7 a 8. V skratke:

- **Safari nie je overené.** Overený je Chrome.
- **Mobilná verzia** čaká na odpoveď, či je v zvislom videu vypálené logo.
- **Fotky realizácií** sú stále ilustračné.
- **Verejná adresa** nie je nasadená. Cloudflare Pages nepôjde (limit 25 MB na
  súbor, hero video má 40 MB), Netlify je odporúčaná cesta.

## 10. Poznámka k nástroju

Náhľadový panel v Claude Code tejto stránke pri väčšine rozmerov vracia **prázdne
snímky obrazovky**, hoci stránka je v poriadku. Overené aj na obyčajnej sekcii,
takže to nie je chyba stránky. Veľa vecí sa preto dalo overiť len číslami z DOM.
Kto na to narazí znova, nech na tom nestráca čas a testuje v skutočnom Chrome.
