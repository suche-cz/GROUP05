# samostatna_prace.py

"""
zadání:
1) vytvořte funkci come_home
- která vždy vyprintuje: "jsem doma"
- a zavolá vstupní činnost - callback funkce

2) vytvoříme 2 funkce, které mouh sloužit jako callback funkce
    a) go_sleep - vyprintuje "Jdu spát"
    b) go_run - vyprintuje "Jdu běhat"
"""

def come_home(callback):
    print("jsem doma")
    return callback()
    
def go_run():
    print("Jdu běhat")
    return 10

def go_sleep():
    print("Jdu spát")
    return 20

come_home(go_run)
come_home(go_sleep)
