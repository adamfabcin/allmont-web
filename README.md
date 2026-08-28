# ALL MONT, web

Jednostránkový web pre ALL MONT, spol. s r.o. (Nitra), výroba a montáž plastových
a hliníkových okien a dverí.

## Ako si to pozrieť

Dvakrát kliknite na `SPUSTIT-WEB.command`. Otvorí sa prehliadač na
`http://localhost:8123` a čierne okno so serverom, ktoré musí zostať otvorené.
Internet nie je potrebný, jediné, čo sa ťahá zvonku, je záložné písmo pre
počítače bez Helvetica Neue.

Ručne:

```bash
python3 serve.py 8123
```

Server zámerne zakazuje kešovanie, aby prehliadač po zmene súborov nikdy
neukázal starú verziu stránky.

## Čo je vnútri

```
index.html                 celá stránka, štýly aj skript v jednom súbore
serve.py                   lokálny server bez kešovania
SPUSTIT-WEB.command        spúšťač pre macOS
assets/
  hero-2160.mp4            úvodné video 4K, 3840x2160, 40 MB
  hero-1440.mp4            záloha 2560x1440
  hero-1080.mp4            záloha pre slabé pripojenie
  hero-poster.jpg          prvá snímka, drží miesto kým sa video načíta
  hero-plate.jpg           obrázok namiesto videa na mobile
  hero-ending.jpg          náhľadový obrázok pre sociálne siete
  dodavka-2160.mp4         druhé scrollované video, príchod dodávky, 4K
  dodavka-1440.mp4         záloha 2560x1440
  dodavka-1080.mp4         záloha pre slabé pripojenie
  dodavka-plate.jpg        posledná snímka, namiesto videa na mobile
  allmont-logo-*.svg       logo podľa dizajn manuálu značky
  real-1..3.jpg            ilustračné obrázky v sekcii realizácií
  shot-1.jpg               výrobná hala ALL MONT, skutočná fotka od klienta
```

## Úvodné video

Video je riadené scrollovaním, nie prehrávaním. Preto je zakódované tak, že
**každá snímka je kľúčová**: jeden skok potom dekóduje presne jednu snímku,
okolo 9 ms aj v 4K. Bežné kódovanie s kľúčovou snímkou každých osem znamená
až 72 ms na skok a scrollovanie vlečie.

Recept, ktorým je video vyrobené z majstra v ProRes 422 HQ:

```bash
ffmpeg -i majster.mov -map 0:v:0 -an -sn -dn \
  -vf "fps=25" \
  -c:v libx264 -preset slow -crf 26 \
  -x264-params "keyint=1:min-keyint=1:scenecut=0" \
  -pix_fmt yuv420p -write_tmcd 0 -movflags +faststart \
  hero-2160.mp4
```

Kvalita overená proti majstrovi: SSIM 0,989, v tmavých plochách plných 256
jasových úrovní, teda bez pásovania.

## Piktogramy a oznamovače sekcií

Piktogramy v sortimente sú kreslené na tej istej konštrukcii ako logo: mriežka
96 jednotiek, vonkajší obrys hrúbky 11 s rádiusom R14, vnútorné priečky 6,5
a jeden 45° odlesk vo farbe skla v ľavej hornej tabuli. Preto vyzerajú ako
súrodenci loga. Kto bude kresliť ďalší, nech drží tie isté čísla.

Pred každou sekciou stojí ten istý oznamovač: číslo, vlasová linka a názov
sekcie. Je to jediné miesto, kde názov sekcie stojí, v hlavičke sekcie sa už
neopakuje.

## Druhé video, príchod dodávky

Za úvodným nadpisom beží druhý scrollovaný záber, zakódovaný tým istým receptom
ako intro, každá snímka kľúčová. Pozadie záberu je **biela**, pretože prechod
z prvého videa na druhé ide cez bielu: obraz okna sa vybieli až do úplnej
bielej a z tej sa vynorí dodávka.

```bash
ffmpeg -i dodavka.mov -an -sn -dn \
  -vf "crop=3840:2144:0:8,pad=3840:2160:0:8:color=white,fps=25,format=yuv420p" \
  -c:v libx264 -preset slow -crf 26 \
  -x264-params "keyint=1:min-keyint=1:scenecut=0" \
  -write_tmcd 0 -movflags +faststart dodavka-2160.mp4
```

Čierne pásy 7 px hore aj dole sú nahradené bielou, takže rozmer je presné 16:9
bez orezu a bez deformácie.

## Prečo to nie je ozdobené

Dizajn manuál zakazuje gradienty na plochách, zaoblené rohy aj druhé písmo.
Hĺbku preto nesie pevná mriežka vlasových stĺpcov za stránkou, priesvitné
panely nad ňou, pomalé smerové príchody, nadpisy vysúvané po riadkoch
a obrazy odkrývané stierkou. Nič z toho nie je gradient a nič z toho nemá
zaoblený roh. Kto bude pokračovať, nech to tak nechá.

## Čo ešte potrebuje potvrdenie od firmy

1. **Obrázky v sekcii realizácií sú ilustračné, nie skutočné.** Pred spustením
   na verejnú adresu ich treba vymeniť za fotografie z tých šiestich realizácií,
   ktoré sú v zozname. V sekcii je o tom poctivá poznámka.
2. **Cenník servisu je bez cien.** Zoznam prác je prevzatý z pôvodnej stránky,
   kde bol cenník platný od 15.01.2013. Ceny sú zámerne na vyžiadanie.
3. **Formulár** otvorí návštevníkovi jeho e-mailový program s vyplnenou správou.
   Je to jediné, čo na statickej stránke naozaj funguje. Ak má správu odosielať
   web sám, treba k tomu službu na odosielanie.

## Pred nasadením na verejnú adresu

V `index.html` sú dve značky s poznámkou `DEPLOY STEP`. Doplňte v nich absolútnu
adresu webu, aby náhľad na sociálnych sieťach fungoval:

```html
<meta property="og:url" content="https://REPLACE-AT-DEPLOY/">
<meta property="og:image" content="https://REPLACE-AT-DEPLOY/assets/hero-ending.jpg">
```

## Značka

Farby, písmo a tón vychádzajú z dizajn manuálu značky, verzia 1.0:
azúrová `#1E6FD9` ako akcent, námorná `#0F2233` na text a tmavé plochy,
sklo `#8FC1F2`, hmla `#EEF1F4` na pozadia. Jedno písmo na všetko,
Helvetica Neue, rozdiely nesie hrúbka a prestrih. Pravé uhly, žiadne gradienty
na plochách, žiadne kurzívy.
