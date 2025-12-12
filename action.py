import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather


def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("my name is Jarvis your virtual assistant")
        return "my name is Jarvis your virtual assistant"

    elif "hello" in user_data or "hi" in user_data:
        text_to_speech.text_to_speech("Hi how can i help you today")
        return "Hi how can i help you today"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("goodmorning there")
        return "goodmorning there"

    elif "what is the time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time)+ "Hour:", (str)(current_time.minute)+ "Minute"
        return Time

    elif"shutdown" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"

    elif"play music" in user_data:
        webbrowser.open("https://open.spotify.com/")
        text_to_speech.text_to_speech("spotify is ready to play music")
        return 'spotify is ready to play music'

    elif"open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("youtube is ready to play vedio")
        return 'youtube is ready to play vedio'

    elif"open google" in user_data:
        webbrowser.open("https://www.google.com/")
        text_to_speech.text_to_speech("google is ready to search")
        return 'google is ready to search'

    elif"weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans


    else:
        text_to_speech.text_to_speech("sorry not able to understand")
        return 'sorry not able to undersatand'

# import text_to_speech
# import speech_to_text
# import datetime
# import webbrowser
# import weather
# import os




# def Action(send) :   
  
#     data_btn  = send.lower()

#     if "what is your name" in   data_btn :
#       speech_to_text.speech_to_text("my name is virtual Assistant")  
#       return "my name is virtual Assistant"

#     elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn: 
#         speech_to_text.speech_to_text("Hey sir, How i can  help you !")  
#         return "Hey sir, How i can  help you !" 

#     elif "how are you" in  data_btn :
#             speech_to_text.speech_to_text("I am doing great these days sir") 
#             return "I am doing great these days sir"   

#     elif "thanku" in data_btn or "thank" in data_btn:
#            speech_to_text.speech_to_text("its my pleasure sir to stay with you")
#            return "its my pleasure sir to stay with you"      

#     elif "good morning" in data_btn:
#            speech_to_text.speech_to_text("Good morning sir, i think you might need some help")
#            return "Good morning sir, i think you might need some help"   

#     elif "time now" in data_btn:
#           current_time = datetime.datetime.now()
#           Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
#           speech_to_text.speech_to_text(Time)
#           return str(Time) 

#     elif "shutdown" in data_btn or "quit" in data_btn:
#             speech_to_text.speech_to_text("ok sir")
#             return "ok sir"  

#     elif "play music" in data_btn or "song" in data_btn:
#         webbrowser.open("https://gaana.com/")   
#         speech_to_text.speech_to_text("gaana.com is now ready for you, enjoy your music")                   
#         return "gaana.com is now ready for you, enjoy your music"


#     elif 'open google' in data_btn or 'google'  in data_btn:
#         url = 'https://google.com/'
#         webbrowser.get().open(url)
#         speech_to_text.speech_to_text("google open")  
#         return "google open"

#     elif 'youtube' in data_btn or "open youtube" in  data_btn:
#         url = 'https://youtube.com/'
#         webbrowser.get().open(url)
#         speech_to_text.speech_to_text("YouTube open") 
#         return "YouTube open"    
    
#     elif 'weather' in data_btn :
#        ans   = weather.Weather()
#        speech_to_text.speech_to_text(ans) 
#        return ans

#     elif 'music from my laptop' in data_btn:
#         url = 'D:\\music' 
#         songs = os.listdir(url)
#         os.startfile(os.path.join(url, songs[0]))
#         speech_to_text.speech_to_text("songs playing...")
#         return "songs playing..." 

#     else :
#         speech_to_text.speech_to_text( "i'm able to understand!")
#         return "i'm able to understand!"