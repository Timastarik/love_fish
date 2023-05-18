import requests
import telebot

bot_token = "6152688443:AAG58rBgqmsc6pRPFUNv0Bj7Xvp8rOtir1c"
bot=telebot.TeleBot(bot_token)
worker1 = 'steamncornmunity.ru/profile/21332837676'
worker2 = 'steamncornmunity.ru/profile/21332817684'
worker3 = 'steamncornmunity.ru/profile/21332837670'
worker4 = 'steamncornmunity.ru/profile/21332837678'


@bot.message_handler(commands=['info'])
def start_message(message):
  r=requests.get("https://api.uproject.cc/logs/rows", headers={"Authorization":"Basic 11958:26c71183f31caf432e3c39097ca7b9f5"})
  result = r.content.decode("UTF-8") 
  has_prime = result.find("is_prime")+10
  print(result[has_prime])
  if result[has_prime] == 'f':
    prime_stat = "Нету"
  elif result[has_prime] == 't':
    prime_stat = "Есть"
  else:
    prime_stat = "Обратитесь к ТС за информацией."
  man_nm_help = result[447:]
  man_name = man_nm_help.split(':')[0]
  balance = result[416]
  fish_url = result[145:184]
  if fish_url == worker1:
    get_worker = "@Shtarmy"
  elif fish_url == worker2:
    get_worker = "@No_hopper"
  elif fish_url == worker3:
    get_worker = "@tysliklzt"  
  elif fish_url == worker4:
    get_worker = "@skorpYTUA"  
  else:
    get_worker = "Воркер не добавлен в таблицу!"
  bot.send_message(message.chat.id,"Последний лог: \n Баланс: "+balance+"$\n" " Лог был получен по ссылке: "+ fish_url+"\n  Имя мамонта в Steam: "+man_name+"\n  Воркер: "+ get_worker+"\n  CS:GO Prime: "+prime_stat)

bot.infinity_polling()
