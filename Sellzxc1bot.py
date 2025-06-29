from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8112352565:AAF4beRypuE2UH7AvwIDemjRGJek9CQiwvo"  # Замените на токен вашего бота

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Отправляем стикер
    await update.message.reply_sticker("CAACAgIAAxkBAAEQOd9oYLSRXUAuumpO4FkVF4cnD6SWVwACoiQAAkIYSEoB_5-7g_3tNDYE")
    
    # Создаем меню
    keyboard = [
        [
            InlineKeyboardButton("📌 Услуги", callback_data='services'),
            InlineKeyboardButton("💻 Создание ботов", callback_data='bots_creation'),
        ],
        [
            InlineKeyboardButton("🌐 Создание сайтов", callback_data='sites_creation'),
            InlineKeyboardButton("📞 Контакты", callback_data='contacts'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🔹 Добро пожаловать!.\n"
        "🔹 Выберите интересующий вас раздел:",
        reply_markup=reply_markup
    )

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'services':
        keyboard = [
            [InlineKeyboardButton("🤖 Боты", callback_data='bots_creation')],
            [InlineKeyboardButton("🌐 Сайты", callback_data='sites_creation')],
            [InlineKeyboardButton("📞 Контакты", callback_data='contacts')],
            [InlineKeyboardButton("🔙 На главную", callback_data='main_menu')]
        ]
        await query.edit_message_text(
            "*🔹Мои услуги:*\n\n"
            "-Разработка Telegram-ботов:\n"
            "- Автоматизация бизнес процессов\n"
            "- Чат-боты для поддержки\n"
            "- Интернет-магазины\n"
            "- Корпоративные сайты\n"
            "- Веб-приложения\n"
            "-управление и настройки сервера\n"
            "-Создание софтов\n"
            "-игры*\n"
            "-приложения *\n\n"
            "Выберите раздел для подробностей:",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == 'bots_creation':
        keyboard = [
            [InlineKeyboardButton("◀️ к услугам", callback_data='services')],
            [InlineKeyboardButton("📞 Контакты", callback_data='contacts')],
            [InlineKeyboardButton("🔙 На главную", callback_data='main_menu')]
        ]
        await query.edit_message_text(
            "🔹Разработка Telegram-ботов\n\n"
            "Я создаю ботов для различных задач:\n"
            "✅ Автоматизация заказов\n"
            "✅ Чат-боты для поддержки\n"
            "✅ Парсинг данных\n"
            "✅ Интеграция с платежами\n"
            "✅ Голосовые и видео-боты\n\n"
            "Стек технологий: Python (aiogram, python-telegram-bot), Node.js, PHP.\n\n"
            "Свяжитесь со мной для заказа: @Sellzxc1",
            reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == 'sites_creation':
        keyboard = [
            [InlineKeyboardButton("◀️ к услугам", callback_data='services')],
            [InlineKeyboardButton("📞 Контакты", callback_data='contacts')],
            [InlineKeyboardButton("🔙 На главную", callback_data='main_menu')]
        ]
        await query.edit_message_text(
            "🔹Создание сайтов\n\n"
            "Я разрабатываю сайты разной сложности:\n"
            "🚀 Лендинги (одностраничники)\n"
            "🛒 Интернет-магазины\n"
            "🏢 Корпоративные сайты\n"
            "📊 Веб-приложения\n\n"
            "Использую: HTML/CSS/JS, React, Django, Flask, WordPress.\n\n"
            "Свяжитесь со мной для заказа: @Sellzxc1",
            reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == 'contacts':
        keyboard = [
            [InlineKeyboardButton("◀️ к услугам", callback_data='services')],
            [InlineKeyboardButton("🔙 На главную", callback_data='main_menu')]
        ]
        await query.edit_message_text(
            "🔹Контакты\n\n"
            "Свяжитесь со мной для обсуждения проекта:\n\n"
            "📩 Email: sellzxc1@bk.ru\n"
            "📱 Telegram: @Sellzxc1\n"
            "🌍 Сайт: Sellzxc1.github.io",
            reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == 'main_menu':
        keyboard = [
            [
                InlineKeyboardButton("📌 Услуги", callback_data='services'),
                InlineKeyboardButton("💻 Создание ботов", callback_data='bots_creation'),
            ],
            [
                InlineKeyboardButton("🌐 Создание сайтов", callback_data='sites_creation'),
                InlineKeyboardButton("📞 Контакты", callback_data='contacts'),
            ]
        ]
        await query.edit_message_text(
            "🔹 Добро пожаловать!\n"
            "Выберите интересующий вас раздел:",
            reply_markup=InlineKeyboardMarkup(keyboard))

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_click))

    application.run_polling()

if __name__ == '__main__':
    main()