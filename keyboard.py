from telegram import *


keyboard = [[InlineKeyboardButton("📊 Stats général 📊", callback_data='1')],
			[InlineKeyboardButton("📋 Top items 📋", callback_data='2')],
			[InlineKeyboardButton("⚙ Gestion ⚙", callback_data='3')]]

keyboard2 = [[InlineKeyboardButton("Top clients", callback_data='4')],
			 [InlineKeyboardButton("Top requêtes", callback_data='5'),
			  InlineKeyboardButton("Top pubs", callback_data='6')],
			 [InlineKeyboardButton("Menu principal", callback_data='10')]]

keyboard3 = [[InlineKeyboardButton("Statut du Pi-Hole", callback_data='7')],
			 [InlineKeyboardButton("Activer  ✅", callback_data='8'),
			  InlineKeyboardButton("Désactiver  ❌", callback_data='9')],
			 [InlineKeyboardButton("Menu principal", callback_data='10')]]


reply_markup = InlineKeyboardMarkup(keyboard)
reply_markup2 = InlineKeyboardMarkup(keyboard2)
reply_markup3 = InlineKeyboardMarkup(keyboard3)