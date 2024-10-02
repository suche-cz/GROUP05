"""
SOLID - principy pro psaní kvalitního kódu - viz níže
+ kniha: Clean Code - Čistý kód
+ správně pojmenovat názvy
+ programovat na různých urovních abstrakce
    - nemíchat různé úrovně dohromady
    - příklad fabrika: kontrolu kvality děláme jinde než výrobu šroubků
    - příklad restaurace:
        - úroveň zásobování
        - úroveň přípravy (čištění, krájení surovin)
        - úroveň vaření
        - úroveň kompletace a podávání
        - uroveň komunikace se zákazníkem
        - uroveň čištění
        + někdo to celé musí řídit
        (a teď si představte že by toto vše bylo na jednom místě ...)


SOLID PRINCIPY

S - single responsibility principle
- porušení poznáme podle:
    mnoho parametrů
    divná složitá logika

O - open closed principle
- otevřené pro rozšiřování, uzavřené pro modifikaci
- uzravřené pro změnu těla funkce, ale otevřené pro rozšíření dalších typu
- porušení poznáme podle:
    mnoho podmínech podle hodnot stejného typu (pro stejný typ)

L - liskov substitution principle
- OOP - potomek v třídě umí 100% zastoupit svého předka bezeměny
- porušení poznáme podle:
    potomek by změnil rozhraní metod

I - interface segregation principle
- rozdělení tříd do logických celků, aby jsme dědili pouze to co potřebujeme
- porušení poznáme podle:
    objety a třída mají metody nebo atributy, které nedávají smysl

D - Dependency Inversion Principle
- zavislost by měl být na úrovní abstraktního rozhranní
- porušení poznáme podle:
    s objekty se nám sšpatně pracuje, pro jednou činnost musíme použít nějakou složitou logiku

"""

