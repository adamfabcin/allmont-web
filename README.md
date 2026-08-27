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
  allmont-logo-*.svg       logo podľa dizajn manuálu značky
  real-1..3.jpg            ilustračné obrázky v sekcii realizácií
  shot-1.jpg               snímka do sekcie o spoločnosti
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
