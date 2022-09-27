import speech_recognition as sr
import pyautogui
import screen_brightness_control as sbc

#? wake up call
wakeUpCall = "سیستم"

#? commands
exit_commands = ['خروج', 'خاموش', 'خارج','تمام','تموم','پایان'] 
prev_commands = ['قبلی','قبلیه']
next_commands = ['بعدی', 'بعدیه']
play_commands = ['پلی', 'پخش']
stop_commands = ['استاپ', 'قطع', 'ببند', 'متوقف']
sound_commands = ['صدا', 'آهنگ', 'اهنگ', 'موسیقی']
sound_mute_commands = ['ببند','میوت']
sound_vol_down = ['کم', 'پایین', ]
sound_vol_up = ['زیاد', 'بالا', ]
bright_commands = ['نور']
bright_up_commands = ['زیاد', 'بالا']
bright_down_commands = ['کم', 'پایین']




def voicRec():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    while True:
        try:
            with mic as source:
                audio = r.listen(source)
                command = r.recognize_google(audio, language='fa-IR').lower()
                if wakeUpCall in command:
                    if any(item in command for item in exit_commands):
                        print('در حال خارج شدن')
                        break
                    elif any(item in command for item in prev_commands):
                        pyautogui.press('prevtrack')
                        print("انجام دادم")
                    elif any(item in command for item in next_commands):
                        pyautogui.press('nexttrack')
                        print("انجام دادم")
                    elif any(item in command for item in play_commands):
                        pyautogui.press('playpause')
                        print("انجام دادم")
                    elif any(item in command for item in stop_commands):
                        pyautogui.press('playpause')
                        print("انجام دادم")
                    elif any(item in command for item in sound_commands):
                        if any(item in command for item in sound_mute_commands):
                            pyautogui.press('volumemute')
                            print("انجام دادم")
                        elif any(item in command for item in sound_vol_down):
                            pyautogui.press('volumedown', pressess=10)
                        elif any(item in command for item in sound_vol_up):
                            pyautogui.press('volumeup', pressess=10)
                    elif any(item in command for item in bright_commands):
                        if any(item in command for item in bright_up_commands):
                            sbc.set_brightness(100)
                            print("انجام دادم")
                        elif any(item in command for item in bright_down_commands):
                            sbc.set_brightness(50)
                            print("انجام دادم")
                    else:
                        print('متوجه نشدم 😁')
        except Exception as e:
            print(e)
            r = sr.Recognizer()
            continue

  
voicRec()