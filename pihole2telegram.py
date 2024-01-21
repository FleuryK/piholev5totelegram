import config
from telegram.ext import *
from telegram import *
from parse import *
import time
from keyboard import *

print('Bot démarré ...')

bold = '*'

async def start(update, context):
	await context.bot.send_message(chat_id=update.message.chat.id, text="Bonjour, je suis un bot pour Pi-Hole.")
	time.sleep(1)

	user = str(update.message.from_user.id)
	if user not in config.TELEGRAM_USER_ID:
		time.sleep(1)
		userid = update.message.from_user.id
		await context.bot.send_message(chat_id=update.message.chat.id, text="Votre ID utilisateur n'est pas dans la liste des admins 😢\nVotre ID utilisateur est " + str(userid))
	else:
		await context.bot.send_sticker(chat_id=update.message.chat.id, sticker='CAADAgADBQADqWzzCr24QnCkXz6YAg')
		time.sleep(2)
		await context.bot.send_message(chat_id=update.message.chat.id, text="Vous pouvez utiliser /help pour afficher l'aide.")

async def help(update, context):
	await context.bot.send_message(chat_id=update.message.chat.id, text="/id : Afficher votre ID utilisateur\n/pihole : Afficher le menu")

async def myid(update, context):
	userid = update.message.from_user.id
	await context.bot.send_message(chat_id=update.message.chat.id, text=userid)

async def pihole(update, context):
	user = str(update.message.from_user.id)
	if user in config.TELEGRAM_USER_ID:
		await context.bot.send_message(chat_id=update.message.chat.id, text=genstats(), reply_markup=reply_markup, parse_mode='Markdown')

async def button(update, context):
	query = update.callback_query
	if query.data == '1':
		await context.bot.editMessageText(text=genstats(),
										  chat_id=query.message.chat.id,
										  message_id=query.message.message_id,
										  reply_markup=reply_markup,
										  parse_mode='Markdown')

	if query.data == '2':
		await context.bot.editMessageText(text='Veuillez choisir :',
										  reply_markup=reply_markup2,
										  chat_id=query.message.chat.id,
										  message_id=query.message.message_id)

	if query.data == '4':
		await context.bot.editMessageText(text=top_it('topClients'),
										  chat_id=query.message.chat.id,
										  message_id=query.message.message_id,
										  reply_markup=reply_markup2,
										  parse_mode='Markdown')

	if query.data == '5':
		await context.bot.editMessageText(text=top_it('topItems', 1),
										  chat_id=query.message.chat.id,
										  message_id=query.message.message_id,
										  reply_markup=reply_markup2,
										  parse_mode='Markdown')

	if query.data == '6':
		await context.bot.editMessageText(text=top_it('topItems', 2),
										  chat_id=query.message.chat.id,
										  message_id=query.message.message_id,
										  reply_markup=reply_markup2,
										  parse_mode='Markdown')

	if query.data == '3':
		await context.bot.editMessageText(text='Veuillez choisir :',
										  reply_markup=reply_markup3,
										  chat_id=query.message.chat.id,
										  message_id=query.message.message_id)

	if query.data == '7':
		await context.bot.editMessageText(text=check_status('status'),
										  chat_id=query.message.chat.id,
										  message_id=query.message.message_id,
										  reply_markup=reply_markup3,
										  parse_mode='Markdown')

	if query.data == '8':
		await context.bot.editMessageText(text=check_status('enable'),
										  chat_id=query.message.chat.id,
										  message_id=query.message.message_id,
										  reply_markup=reply_markup3,
										  parse_mode='Markdown')

	if query.data == '9':
		await context.bot.editMessageText(text=check_status('disable'),
										  chat_id=query.message.chat.id,
										  message_id=query.message.message_id,
										  reply_markup=reply_markup3,
										  parse_mode='Markdown')

	if query.data == '10':
		await context.bot.editMessageText(text = genstats(),
										  chat_id = query.message.chat.id,
										  message_id = query.message.message_id,
										  reply_markup = reply_markup,
										  parse_mode = 'Markdown')

if __name__ == '__main__':
	application = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()

	# Commandes
	application.add_handler(CommandHandler('start', start))
	application.add_handler(CommandHandler('help', help))
	application.add_handler(CommandHandler('id', myid))
	application.add_handler(CommandHandler('pihole', pihole))
	application.add_handler(CallbackQueryHandler(button))

	# Execution du bot
	application.run_polling(1.0)