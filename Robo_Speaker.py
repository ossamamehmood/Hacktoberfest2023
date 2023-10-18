import os
if __name__ == '__main__':
    print("Welcome to RoboSpeaker First Project \n")
    while True:
        x = str(input("Enter what do you want me to pronounce!"))
        cmd = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}')"
        if x == "q":
            break
        os.system(cmd)