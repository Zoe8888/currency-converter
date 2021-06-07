import requests
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Currency Converter')
root.geometry('500x500')
root.resizable('False', 'False')
root.config(bg='#4ad66d')

api = requests.get("https://v6.exchangerate-api.com/v6/4a704b6911da3fab9b1df53d/latest/USD")
data = api.json()

exchange = data['conversion_rates']
print(exchange)

# conversion = Message(root, text='', bg='#4ad66d')
# conversion.place(relx=0.2, rely=0.2)

amount = Label(root, text='Enter an amount you would like converted: ', bg='#4ad66d')
amount.place(relx=0.2,rely=0.1)

amount_entry = Entry(root, width=25)
amount_entry.place(relx=0.25, rely=0.2)

currency = Label(root, text='Select the currency you wish to convert: ', bg='#4ad66d')
currency.place(relx=0.2, rely=0.3)

answer = Label(root, width=25)
answer.place(relx=0.25, rely=0.9)

conversion = Listbox(root, width=25)
for x in exchange.keys():
    conversion.insert(END, str(x))

conversion.place(relx=0.25, rely=0.4)


def convert():
    entry = float(amount_entry.get())
    result = entry * data['exchange'][conversion.get(ACTIVE)]
    answer.config(text=result)


button = Button(root, text='Convert to US Dollars', command=convert, bg='#4ad66d')
button.place(relx=0.27, rely=0.8)

root.mainloop()