import telebot
from datetime import datetime
from dotenv import load_dotenv
import os
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from DB_logic import DB_manager
from ai_service import generate_response
load_dotenv()
manager = DB_manager(os.getenv("DB_NAME"))
bot = telebot.TeleBot(os.getenv("TG_API"))
user_questions_num = {}
answers = {}
user_last_message_id ={}
questions = [" What do you enjoy doing the most?",
             "What makes you bored the most?",
             "Which format of work in your opinion fits you the most",
             "How do you prefer working, in a team or independently",
             "Whats more important for you?",
             "What skills do you already have or want to develop?"]

def generate_start_keyboard():
    start_keyboard = InlineKeyboardMarkup()
    b1 = InlineKeyboardButton(text="Describe myself⭐", callback_data="start_describe")
    b2 = InlineKeyboardButton(text="Quiz🧐", callback_data='start_quiz')
    start_keyboard.add(b1, b2)
    return start_keyboard

def generate_question_keyboard(question_number):
    questions = InlineKeyboardMarkup(row_width=1)
    if question_number == 1:
        b1 = InlineKeyboardButton(text="Analyze📈", callback_data="question_1_analyze")
        b2 = InlineKeyboardButton(text="Creating something artistic🖼️", callback_data="question_1_creating_artistic_things")
        b3 = InlineKeyboardButton(text="working and creating new technologies🤖", callback_data="question_1_creating_and_working_with_tech")
        b4 = InlineKeyboardButton(text="communicating with other people🗣️", callback_data="question_1_communicating_with_people")
        b5 = InlineKeyboardButton(text="Solving logical problems➗", callback_data="question_1_solving_problems")
        questions.add(b1,b2,b3,b4,b5)
        return questions
    elif question_number == 2:
        b1 = InlineKeyboardButton(text="Long coding🖥️", callback_data="question_2_long_coding")
        b2 = InlineKeyboardButton(text="Monotonous routine work🏢", callback_data="question_2_routine_work")
        b3 = InlineKeyboardButton(text="Talking to clients💬", callback_data="question_2_talking_to_clients")
        b4 = InlineKeyboardButton(text="Artistic work🎭", callback_data="question_2_anti_artistic_work")
        b5 = InlineKeyboardButton(text="None above makes me bored🫠", callback_data="question_2_nothing")
        questions.add(b1,b2,b3,b4,b5)
        return questions
    elif question_number == 3:
        b1 = InlineKeyboardButton(text="Artistic🎨", callback_data="question_3_artistic")
        b2 = InlineKeyboardButton(text="Analytic📊", callback_data="question_3_analytic")
        b3 = InlineKeyboardButton(text="Technical🖥️", callback_data="question_3_technical")
        b4 = InlineKeyboardButton(text="Communicative🗨️", callback_data="question_3_communicative")
        b5 = InlineKeyboardButton(text="I dont know🧐", callback_data="question_3_nothing")
        questions.add(b1,b2,b3,b4,b5)
        return questions
    elif question_number == 4:
        b1 = InlineKeyboardButton(text="Alone👨‍💻", callback_data="question_4_alone")
        b2 = InlineKeyboardButton(text="In a team👩‍💻👨‍💻", callback_data="question_4_in_a_team")
        b3 = InlineKeyboardButton(text="No difference🤷‍♂️", callback_data="question_4_no_difference")
        questions.add(b1,b2,b3)
        return questions
    elif question_number == 5:
        b1 = InlineKeyboardButton(text="High salary💵", callback_data="question_5_high_salary")
        b2 = InlineKeyboardButton(text="Quiet work🏢", callback_data="question_5_quiet_work")
        b3 = InlineKeyboardButton(text="Interesting tasks📊", callback_data="question_5_interesting_tasks")
        b4 = InlineKeyboardButton(text="Opportunity for growth🪴", callback_data="question_5_opportunity_for_growth")
        b5 = InlineKeyboardButton(text="Flexible graphic🎇", callback_data="question_5_flexible_graphic")
        questions.add(b1,b2,b3,b4,b5)
        return questions
    elif question_number == 6:
        b1 = InlineKeyboardButton(text="A little programming👨‍💻", callback_data="question_6_little_programming")
        b2 = InlineKeyboardButton(text="Design🎨", callback_data="question_6_design")
        b3 = InlineKeyboardButton(text="Analytic/tables📊", callback_data="question_6_analytic")
        b4 = InlineKeyboardButton(text="Marketing/SMM💹", callback_data="question_6_marketing")
        b5 = InlineKeyboardButton(text="Nothing🤷‍♂️", callback_data="question_6_nothing")
        questions.add(b1,b2,b3,b4,b5)
        return questions
@bot.message_handler(commands=['start','menu'])
def send_welcome(message):
    text="""\
    Hi there🙂, I am a bot that helps you find a profession in IT based on your description like, whats your hobby, your favorite subjects and generally about you, if you dont 
    feel like writing a description about yourself, i can ask you some questions and thanks to do answers i can recommend you a job😊, just click one of the buttons under this message⬇️!\
    """
    bot.send_message(message.chat.id, text, reply_markup=generate_start_keyboard())

def quiz(message,num_questions):
    #bot.send_message(message.chat.id, "Alright! Let's start up the quiz.")
    time.sleep(1)
    if num_questions == 1:
        msg = bot.send_message(message.chat.id, questions[0], reply_markup=generate_question_keyboard(1))
        #num_questions +=1
        user_last_message_id[message.chat.id] = msg.id
    elif num_questions == 2:
        bot.edit_message_text(questions[1],message.chat.id,user_last_message_id[message.chat.id],reply_markup=generate_question_keyboard(2))
        #num_questions +=1
    elif num_questions == 3:
        bot.edit_message_text(questions[2],message.chat.id,user_last_message_id[message.chat.id],reply_markup=generate_question_keyboard(3))
        #num_questions +=1
    elif num_questions == 4:
        bot.edit_message_text(questions[3],message.chat.id,user_last_message_id[message.chat.id],reply_markup=generate_question_keyboard(4))
        #num_questions +=1
    elif num_questions == 5:
        bot.edit_message_text(questions[4],message.chat.id,user_last_message_id[message.chat.id],reply_markup=generate_question_keyboard(5))
        #num_questions +=1
    elif num_questions == 6:
        bot.edit_message_text(questions[5],message.chat.id,user_last_message_id[message.chat.id],reply_markup=generate_question_keyboard(6))
        #num_questions +=1
    else:
        bot.edit_message_text("That's all the questions I have for now! Thank you for participating in the quiz.",message.chat.id,user_last_message_id[message.chat.id])

def describe(message):
    bot.send_message(message.chat.id, "Thanks! Processing a suggestion profession for you🎇...")
    description = message.text
    user_id = message.chat.id
    today = datetime.now().strftime("%d-%m-%Y")
    ai_summary = generate_response(f'Based on the following description of a user, recommend an IT profession that would suit them best, dont make the answer too long, use some emojis, dont make the answer too hard to understand:{description}')
    bot.send_message(user_id,ai_summary)
    manager.add_info_desc(user_id, description, ai_summary, today)

@bot.callback_query_handler(func=lambda call: call.data.startswith('start_'))
def handle_start_keyboard(call):
    button_text = call.data.split('_')[1]
    if button_text == "describe":
        bot.send_message(call.message.chat.id, "Please describe yourself, your hobbies🏓, favorite subjects🦾, and anything else that might help me recommend a profession for you😊")
        bot.register_next_step_handler(call.message, describe)
    elif button_text == "quiz":
        user_questions_num[call.message.chat.id] = 1
        bot.send_message(call.message.chat.id, 'Great🙂! I will ask you a few questions that will help me recommend a profession for you.')
        quiz(call.message,1)


@bot.callback_query_handler(func=lambda call: call.data.startswith('question_'))
def handle_questions(call):
    user_id = call.message.chat.id 
    if user_id not in answers:
        answers[user_id] = {}
    step = user_questions_num.get(user_id, 1)
    questions_text = questions[step - 1]
    #print(f"User {user_id} is on step {step}:{call.data}")
    button_text = "_".join(call.data.split('_')[1:])
    answers[user_id][questions_text] = button_text
    next_step = step + 1
    user_questions_num[user_id] = next_step
    today = datetime.now()
    if next_step <= len(questions):
        quiz(call.message, next_step)
    else:
        bot.edit_message_text("Thanks! Processing a suggestion profession for you..🎇",call.message.chat.id,user_last_message_id[user_id])
        ai_summary = generate_response(f'Here are the quiz answers of a user. Analyze them and recommend an IT profession, dont make the answer too long, use some emojis and dont make the response too hard to understand.:{answers[user_id]}')
        bot.send_message(user_id,ai_summary)
        manager.add_info_quiz(user_id, str(answers[user_id]), ai_summary, today.strftime("%d-%m-%Y"))
        #bot.send_message(user_id, f'Final answers:{answers[user_id]}') 
    
if __name__ == '__main__':
    manager.make_tables()
    bot.infinity_polling() 