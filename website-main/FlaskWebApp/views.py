from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
import random
from openai import OpenAI
from dotenv import load_dotenv
import os
import csv
#from flask_mail import Message
#from . import mail
import io
##the api key is stored in the .env file, this code just in case the api is not found
def configure():
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key is None:
        raise ValueError("API key not found. Please check your .env file and ensure the 'OPENAI_API_KEY' is set.")
    return api_key


api_key = configure()


client = OpenAI(api_key=api_key)


views = Blueprint('views', __name__)

chat_history_list = [] # even index are user message, odd index are bot message
for i in range(8):
    temp = []
    chat_history_list.append(temp)

index_list = [0,1,2,3,4,5,6,7]
first_set = [0,1,2,3]
scenarios = []


#@views.route('/', methods=['GET', 'POST'])
#def login():
#    return render_template("login.html")

#@views.route('/without/<int:participant_id>', methods=['GET', 'POST'])
#def without_chatbot(participant_id):
#    return render_template("without.html", participant_id=participant_id)
@views.route('/', methods=['GET', 'POST'])
def submit():
    #context_choice = request.form.get('contextChoice')
    return render_template("question.html")
    participant_id = request.form.get('participantId')
    

    #if context_choice == 'with':
        
    #    return redirect(url_for('views.scenario_page_with', participant_id=participant_id,scenario_id=random.choice(first_set)))
    #elif context_choice == 'without':
    #    return redirect(url_for('views.scenario_page_without', participant_id=participant_id,scenario_id=random.choice(first_set)))
   
# ####################################################################################
user_chat_history = {}

def chatbot_caregiver(chat_history_list, message):
    messages = [
        {"role": "system","content": "You are a peer-supporter chatbot to support the mental wellbeing of caregivers of Alzheimer's Disease and Related Dementias"},
        #{"role": "system", "content": str(scenario)},
        {"role": "system", "content": str(chat_history_list)},
        {"role": "user", "content": str(message)}
    ]

    response = client.chat.completions.create(model="gpt-4o-mini",
    messages=messages)
    
    bot_response = response.choices[0].message.content
    
    return bot_response

@views.route('/question', methods=['GET', 'POST'])
def question_page():
    participant_id = request.args.get('participant_id')
    if 'user_chat_history' not in session:
        session['user_chat_history'] = {}
        
    user_chat_history = session['user_chat_history']
    
    if request.method == 'POST':
        if request.form.get('action') == 'end_interview':
            #save_data_to_csv_for_own_question(participant_id, user_chat_history.get(participant_id, []))
            session.pop(f'visited_scenarios_{participant_id}', None)
            user_chat_history.pop(participant_id, None)
            session['user_chat_history'] = user_chat_history
            return render_template('thanks.html')
        
        message = request.form.get('message-input')
        if message:
            if participant_id not in user_chat_history:
                user_chat_history[participant_id] = []
                
            user_chat_history[participant_id].append({"Question": message})
            
            bot_response = chatbot_caregiver(user_chat_history[participant_id], message)
            formatted_response = bot_response.replace('\n', '<br>').replace('**', '').replace('###', '')
            user_chat_history[participant_id].append({"Response": formatted_response})
            
            #save_data_to_csv_for_own_question(participant_id, user_chat_history[participant_id])
            session['user_chat_history'] = user_chat_history
            
            return jsonify({"bot_response": formatted_response})
    
    chat_history = user_chat_history.get(participant_id, [])
    return render_template("question.html", participant_id=participant_id, chat_history=chat_history)




#def save_data_to_csv_for_with(participant_id, context_choice, scenario_id, chat_history_list):
    with open('with_data.csv', 'a') as f:
        f.write(f"{participant_id},{context_choice},{scenario_id},{chat_history_list}\n")
#def save_data_to_csv_for_without(participant_id, context_choice, scenario_id, chat_history_list):
    with open('without_data.csv', 'a') as f:
        f.write(f"{participant_id},{context_choice},{scenario_id},{chat_history_list}\n")
#def save_data_to_csv_for_own_question(participant_id, chat_history_list):
    with open('own_question_data.csv', 'a') as f:
        f.write(f"{participant_id},{chat_history_list}\n")


