# SELENIUM-SCRAPER

## Hvorfor kan requests/bs4 ikke løse den her version lige så nemt?

*   "requests" modulet henter kun html filen af **URL** adressen.
*   Hjemmesiden "https://quotes.toscrape.com/js/" indholder den rå html ikke quotes.
*   Quotes indsættes dynamisk i **DOM**'en (Document Object Model) af JavaScript efter siden er loadet i browseren
*   requests og BS4 har ikke en JavaScript-engine, der kan eksekvere scriptet.

## Hvorfor er sleep() ikke nok?

*   **sleep(x)** pauser programmet i et fast antal sekunder uanset hvad.
*   Hvis siden loader hurtigere end "x" sekunder vil koden spille tid.
*   Hvis siden loader langsommere crasher scriptet.
*   **WebDriverWait** tjekker DOM'en med korte intervaller og fortsætter øjeblikkeligt.