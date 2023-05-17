import requests
import time
import telebot
import threading

bot_token = "6152688443:AAG58rBgqmsc6pRPFUNv0Bj7Xvp8rOtir1c"
bot=telebot.TeleBot(bot_token)
r=requests.get("https://api.uproject.cc/logs/rows", headers={"Authorization":"Basic 11958:26c71183f31caf432e3c39097ca7b9f5"})
result = r.content.decode("UTF-8")    

@bot.message_handler(commands=['info'])
def start_message(message):
  man_nm_help = result[447:]
  man_name = man_nm_help.split(':')[0]
  balance = result[416]
  fish_url = result[145:181]
  bot.send_message(message.chat.id,"Пооследний лог: \n Баланс: "+balance+"$\n" "Лог был получен по ссылке: "+ fish_url+"\nИмя мамонта в Steam: "+man_name)
bot.infinity_polling()