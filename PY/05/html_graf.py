# html_graf.py

"""
1. vytvoří soubor
2. pomocí for cyklu pro každou hodnotu vytvoříme div
3.  <div style="width: 10px;"></div>
    <div style="width: 20px;"></div>
"""

def create_graf(data: list, filename: str, color: str):
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(f'<style>div{{height:10px;background:{color};margin-bottom:3px;}}</style>')

        for value in data:
            div = f'<div style="width: {value}px;"></div>'
            file.write(div)


create_graf([10, 20, 15, 7, 8], 'my-graf1.html', 'blue')
create_graf([100, 120, 115, 17, 80], 'my-graf2.html', 'red')
