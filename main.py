import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import numpy as np
import seaborn as sns
from tkinter import *

def Crawling():
    total_amount = []
    month_amount = []

    search_text = e0.get()

    driver = webdriver.Chrome()
    driver.get("https://www.dabangapp.com/?gclid=CjwKCAiAkp6tBhB5EiwANTCx1GzQbOjXHN86HCzCzE7YIG3xXyx-nobz1lzAf-A8i5G0YjKwkziQ3xoCUPoQAvD_BwE")

    time.sleep(2)

    search_box = driver.find_element(By.CLASS_NAME, "styled__Input-sc-126ee4m-4.dSHDYM")
    search_box.send_keys(search_text)
    time.sleep(1)
    if search_text[-1] == "역":
        search_first = driver.find_element(By.CLASS_NAME, "styled__SubwayBtn-jva10k-3.kvwbsU")
        search_first.click()
        time.sleep(2)
    elif search_text[-3:] == "대학교":
        search_first = driver.find_element(By.CLASS_NAME, "styled__UnivBtn-jva10k-6.kmQrKm")
        search_first.click()
        time.sleep(2)
    elif search_text[-1] == "동":
        search_first = driver.find_element(By.CLASS_NAME, "styled__RegionBtn-jva10k-2.ivEBMm")
        search_first.click()
        time.sleep(2)

    amount_button = driver.find_element(By.CLASS_NAME, "styled__Filter-utpkdn-0.hctGmK")
    amount_button.click()
    time.sleep(0.5)
    all_amount = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div[1]/div/label[2]/input')
    buy_amount = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div/div[1]/div/label[3]/input')
    all_amount.click()
    time.sleep(0.2)
    buy_amount.click()
    time.sleep(0.2)
    amount_button.click()
    time.sleep(1)

    e1.delete(0, "end")
    e1.insert(0, driver.current_url)

    amount_list = driver.find_elements(By.CLASS_NAME, "styled__Price-sc-1fwit0q-8.HFtIW")

    for i in range(len(amount_list)):
        total_amount.append(list(map(int, amount_list[i].text[3:].replace("억", "").split("/")))[0])
        month_amount.append(list(map(int, amount_list[i].text[3:].replace("억", "").split("/")))[1])
        if total_amount[-1] > 1000 or month_amount[-1] > 100:
            del total_amount[-1]
            del month_amount[-1]

    avg_month = sum(month_amount)//len(month_amount)
    avg_total = sum(total_amount)//len(total_amount)
    plt.scatter(total_amount, month_amount)
    plt.scatter(avg_total, avg_month, label=f"Deposit Average: {avg_total} | Monthly Average: {avg_month}", marker="*", color="red")
    plt.xlabel("Deposit", labelpad=15, fontdict={'family': 'serif', 'color': 'b', 'weight': 'bold', 'size': 14}, loc="right")
    plt.ylabel("Monthly", labelpad=15, fontdict={'family': 'serif', 'color': 'r', 'weight': 'bold', 'size': 14}, loc="top")
    plt.grid(True, alpha=0.5, linestyle="--")
    plt.xticks(np.arange(100, 1100, 100))
    plt.yticks(np.arange(20, 110, 10))
    plt.legend(loc=(0, 1.0))
    plt.show()

def OpenUrl():
    driver = webdriver.Chrome()
    driver.get(e1.get())
    while True:
        continue



window = Tk()
window.geometry("600x300+100+100")
window.resizable(False, False)
window.title("Room Crawler")

l0 = Label(window, text="검색지역", font=("굴림", 40))
l0.pack(side="top")
l1 = Label(window, text="주의", font=("굴림", 20), fg='red')
l1.pack()
l2 = Label(window, text="검색어는 단어 전체를 입력해야 실행됩니다.", font=("굴림", 13), fg='red')
l2.pack()
l3 = Label(window, text="예) OO대학교, OO역, OO동", font=("굴림", 15), fg='red')
l3.pack()

e0 = Entry(window, fg="black", bd=5)
e0.pack()
e1 = Entry(window, fg="cyan", bg="black")
e1.bind("<Key>", lambda a: "break")
e1.pack()

b0 = Button(window, text="주소 바로가기", font=("굴림", 10), command=OpenUrl)
b0.pack()
b1 = Button(window, text="시작", font=("굴림", 40), command=Crawling)
b1.pack()

window.mainloop()
