import os

if __name__ == "__main__":
    print("Welcome to RoboSpeaker 1.1. Created by Shraddha")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q":
            os.system("pause")
            break
        command = f'powershell -Command "Add-Type –AssemblyName System.Speech; ' \
                  f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
        os.system(command)
