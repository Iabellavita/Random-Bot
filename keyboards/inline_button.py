from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choose = InlineKeyboardMarkup(row_width=1,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="🎣 Рандом з виборки слів",
                                          callback_data="words"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="🧩 Рандом з діапазону чисел",
                                          callback_data="digits"
                                      )
                                  ]
                              ])

cancel = InlineKeyboardMarkup(row_width=1,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Назад",
                                          callback_data="cancel"
                                      )
                                  ]
                              ])
