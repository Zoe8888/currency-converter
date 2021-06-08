import requests
from tkinter import *

root = Tk()
root.title('Currency Converter')
root.geometry('400x400')
root.resizable('False', 'False')
root.config(bg='#4ad66d')


amount = Label(root, text='Enter an amount you would like converted: ', bg='#4ad66d')
amount.place(relx=0.16, rely=0.1)

amount_entry = Entry(root, width=25, bg='#e4e4e0')
amount_entry.place(relx=0.25, rely=0.2)

currency = Label(root, text='Enter the currency code you wish to convert: ', bg='#4ad66d')
currency.place(relx=0.16, rely=0.3)

currency_entry = Entry(root, width=25, bg='#e4e4e0')
currency_entry.place(relx=0.25, rely=0.4)


def convert():
    api = "https://v6.exchangerate-api.com/v6/4a704b6911da3fab9b1df53d/latest/" + currency_entry.get()
    data = requests.get(api).json()
    result = int(amount_entry.get()) * data['conversion_rates']['USD']
    print(result)
    answer.config(text=result)


button = Button(root, text='Convert to US Dollars', command=convert, bg='#4ad66d')
button.place(relx=0.29, rely=0.55)

answer = Label(root, width=25)
answer.place(relx=0.25, rely=0.7)

root.mainloop()