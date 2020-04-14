
Extendflix
=======
---
Löytyy myös osoitteesta:<br>
[Extendflix](https://extendflix.herokuapp.com/)
----
Sisältö:
1. Johdanto
2. Tietokanta
3. Näkymät
4. Templatet

Johdanto
---
Tämä työn on osa kurssin "Ohjelmallinen sisällön hallinta" toteutusta.
Tässä työssä on luotu palvelu, joka yhdistää eri rajapinnoista saatavaa 
tietoa yhdeksi kokoanisuudeksi, josta on nähtävillä Netflixiin viimeisen seitsemän
päivän aikana lisätyt elokuvat,sekä näiden elokuvien arvostelut eri lähteistä.
Elokuvien arvostelut on myös koottu dashboard-tyyppiselle sivulle, josta lisättyjen
elokuvien kokonaisuutta voi tarkastella myös kootussa arvostelunäkymässä.

Koska työssä käytetyt rajapinnat ovat ilmaisia vain rajoitetulla määrällä pyyntöjä
ja päivitettäviten tietojen ei tarvitse olla realiaikaisia, käytetään työssä tietokantaa
tietojen säilömiseen. Tällöin tietokantaan tallennetaan kerran päivässä elokuvien tiedot,
josta niitä tuodaa palveluun.

Tietokanta
---
Tässä projektissa tietokantana toimii Postgresql, joka on on hostattuna Herokun
palvelimella.
Tietokantaan on luotu yksi malli, joka sisältää kaikki tarvittavat tiedot elokuvista.
Tietokannassa on myös malli käyttäjille, joka käyttää Djangon omaa user modelia.
Tietokantaan päivitetään uusimmat tiedot kerran päivässä.

Näkymät
---
Tässä projektissa on yksi appi, jossa näkymiä on yhteensä viisi.
Tässä lista näkymistä, sekä lyhyt kuvaus, jokaisesta näkymästä.

index: <br>
Näkymä renderöi käyttäjälle palvelun kotisivun. Aluksi näkymä tarkistaa, on käyttäjä kirjautunut
sisään. Mikäli käyttäjä ei ole kirjautunut sisään, palautetaan hänet kirjautumissivulle. <br>
Näkymä myös hakee tietokannasta kaikkien sinne tallennettujen elokuvien tiedot ja lähettää ne
kotisivun templatelle.
<br>
data-page: <br>
Näkymä renderöi datasivun, jossa näytetään käyttäjälle koottua arvosteludataa elokuvista.
Näkymä tarkistaa onko käyttäjä kirjautunut palveluun. Mikäli käyttäjä ei ole kirjautunut, 
hänet lähetetään takaisin kirjautumissivulle. Näkymässä tehdään myös tiedon muokkaamista,
jotta dataa voidaan visualisoida sitä seuraavalla templatella. Tässä näkymässä tietoa haetaan
ja muokataan.
<br>
update_movies:<br>
Hakee rajapinnalta uusimmat elokuvat, ja purkaa ne yksittäisiksi elokuviksi, jonka jälkeen haetaan
jokaiselle elokuvalle vielä arvostelutiedot get_ratings -näkymän avulla. Kun arvostelutiedot on 
haettu tallennetaan tiedot jokaisesta elokuvasta tietokantaan.
<br>
get_ratings:<br>
Saa update_movies:lta parametrina elokuvan imdb-id:n, joka perusteella haetaan IMDB, rottentomato ja
metacritic -arvostelut ja palautetaan update_movies funktiolle.
<br>
login:<br>
Palauttaa käyttäjälle kirjautumissivun. Kun kirjautumuslomake palautetaan, tarkistetaan se ja
rekisteröidään käyttäjä kirjautuneeksi.

Templatet
---
Palvelussa käytetään base-templatea, jotta sivujen välille saadaan yhtenäinen ulkoasu. Lisäksi 
base-templaten käyttö helpottaa projektin ylläpitämisessä sillä tiedot tarvitsee päättää vain
yhteen paikkaan.<br>
Palvelussa on käytössä neljä eri templatea, jotka kaikki käyttävät base-templatea pohjanaan.
<br>
login: <br>
Sivu, jossa käyttäjä kirjautuu palveluun. <br>
register: <br>
Sivu, jossa käyttäjä rekisteröityy palveluun. <br>
index: <br>
Sivu, jossa uusimmat elokuvat arvosteluineen on listattuna sivulle. <br>
data_page: <br>
Sivu, jossa arvosteludataa visualisoidaan käyttäjille.



