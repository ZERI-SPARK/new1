
        
        
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/", new=2)
            speak("Enjoy")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/", new=2)

        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com/", new=2)

        elif 'play music' in query:
            music_dir = 'F:\\songs\\Favorite'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Faizan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/", new=2)

        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com/faizangujjar01/", new=2)
            speak("Have a look sir")

        elif 'are you there' in query:
            stMsgs = ['At you service, Sir']
            speak(stMsgs)

        elif 'shutdown the PC' in query:
            choice = input("Please confirm to shutdown the pc (y or n)")
            if choice == 'n':
                exit()
            else:
                os.system("shutdown /s /t 1")

        elif 'exit' in query:
            sys.exit(speak("Ok sir, Take Care."))

             elif 'shutdown the PC' in query:
                choice = input("hey not you ease!!")
            if choice == 'n':
                exit()
            else:
                os.system("shutdown /s /t 1")
                os.system("shutdown /s /t 1")




