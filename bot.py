import telebot
from dotenv import load_dotenv
import os
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from DB_logic import DB_manager
from ai_service import generate_response
load_dotenv()
bot = telebot.TeleBot(os.getenv("TG_API"))
user_questions_num = {}

def generate_start_keyboard():
    start_keyboard = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton(text="Describe myself", callback_data="start_describe")
    b2 = InlineKeyboardButton(text="little quiz", callback_data='start_quiz')
    start_keyboard.add(b1, b2)
    return start_keyboard

def generate_question_keyboard(question_number):
    questions = InlineKeyboardMarkup(row_width=1)
    if question_number == 1:
        b1 = InlineKeyboardButton(text="Analyze", callback_data="question_1_analyze")
        b2 = InlineKeyboardButton(text="Creating something artistic", callback_data="question_1_artistic")
        b3 = InlineKeyboardButton(text="working and creating new technologies", callback_data="question_1_tech")
        b4 = InlineKeyboardButton(text="communicating with other people", callback_data="question_1_communicate")
        b5 = InlineKeyboardButton(text="Solving logical problems", callback_data="question_1_solve")
        questions.add(b1,b2,b3,b4,b5)
        return questions
    elif question_number == 2:
        b1 = InlineKeyboardButton(text="Long coding", callback_data="question_2_long_coding")
        b2 = InlineKeyboardButton(text="Monotonous routine work", callback_data="question_2_routine")
        b3 = InlineKeyboardButton(text="Talking to clients", callback_data="question_2_talking")
        b4 = InlineKeyboardButton(text="Artistic work", callback_data="question_2_anti_artistic")
        b5 = InlineKeyboardButton(text="None above makes me bored", callback_data="question_2_nothing")
        questions.add(b1,b2,b3,b4,b5)
        return questions
@bot.message_handler(commands=['start'])
def send_welcome(message):
    text="""\
    Hi there, I am a bot that helps you find a profession in IT based on your description like, whats your hobby, your favorite subjects and generally about you, if you dont 
    feel like writing a description about yourself, i can ask you some questions and thanks to do answers i can recommend you a job, just click one of the buttons under this message!\
    """
    bot.send_message(message.chat.id, text, reply_markup=generate_start_keyboard())

def quiz(message,num_questions):
    bot.send_message(message.chat.id, "Alright! Let's start up the quiz.")
    time.sleep(1)
    if num_questions == 1:
        bot.send_message(message.chat.id, "Question 1: What do you enjoy doing the most?", reply_markup=generate_question_keyboard(1))
        #num_questions +=1
    elif num_questions == 2:
        bot.send_message(message.chat.id, "What makes you bored the most?", reply_markup=generate_question_keyboard(2))
        #num_questions +=1
    elif num_questions == 3:
        bot.send_message(message.chat.id, "Which format of work do you prefer?", reply_markup=generate_question_keyboard(3))
        #num_questions +=1
    elif num_questions == 4:
        bot.send_message(message.chat.id, "How do you prefer working, in a team or independently?", reply_markup=generate_question_keyboard(4))
        #num_questions +=1
    elif num_questions == 5:
        bot.send_message(message.chat.id, "Whats more important for you?:", reply_markup=generate_question_keyboard(5))
        #num_questions +=1
    elif num_questions == 6:
        bot.send_message(message.chat.id, "What skills do you have now?", reply_markup=generate_question_keyboard(6))
        #num_questions +=1
    else:
        bot.send_message(message.chat.id, "That's all the questions I have for now! Thank you for participating in the quiz.")


@bot.callback_query_handler(func=lambda call: call.data.startswith('start_'))
def handle_start_keyboard(call):
    button_text = call.data.split('_')[1]
    if button_text == "describe":
        bot.send_message(call.message.chat.id, "Please describe yourself, your hobbies, favorite subjects, and anything else that might help me recommend a profession for you")
    elif button_text == "quiz":
        user_questions_num[call.message.chat.id] = 1#
        bot.send_message(call.message.chat.id, 'Great! I will ask you a few questions that will help me recommend a profession for you.')
        quiz(call.message,1)#
@bot.callback_query_handler(func=lambda call: call.data.startswith('question_'))

def handle_questions(call):
    user_id = call.message.chat.id #finish the buttons and add logic!!!
    step = user_questions_num.get(user_id, 1)
    print(f"User {user_id} is on step {step}:{call.data}")
    next_step = step + 1
    user_questions_num[user_id] = next_step
    quiz(call.message, next_step)
    button_text = call.data.split('_')[1]
bot.infinity_polling()