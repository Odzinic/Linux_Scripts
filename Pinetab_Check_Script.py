# cron template
#* * * * * XAUTHORITY=/home/user/.Xauthority DISPLAY=:0 python /home/user/Documents/Pinetab_Check_Script.py

from lxml import html
import requests
import tkinter as tk
import sys

# URL page for PineTab
pinePage = requests.get("https://pine64.com/product/pinetab-10-1-linux-tablet-with-detached-backlit-keyboard/")

# Extract HTML from PineTab store page
pineHTML = html.fromstring(pinePage.content)

# Parse the stock string from the HTML
stock = pineHTML.xpath('//p[@class="stock out-of-stock"]/text()')

# Check if the stock string is not "Out of stock"
if (stock != ['Out of stock']):
    
    # Create a popup to notify that the PineTab may be in stock
    popup = tk.Tk()
    tk.Label(popup, text="Pinetab may be in stock.").grid(row=1, column=1)
    popup.mainloop()
