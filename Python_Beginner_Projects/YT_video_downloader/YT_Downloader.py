import os

from pytube import YouTube


def download_audio(link):
    object_file = YouTube(link)
    object_file = object_file.streams.get_audio_only()

    try:
        print("Download Started\n")
        object_file.download()
    except:
        print("Error occur!\n")
    print("Download completed Successfully")


def download_high(link):
    object_file = YouTube(link)
    object_file = object_file.streams.get_highest_resolution()

    try:
        print("Download Started\n")
        object_file.download()
    except:
        print("Error occur!\n")
    print("Download completed Successfully")


def download_low(link):
    object_file = YouTube(link)
    object_file = object_file.streams.get_lowest_resolution()

    try:
        print("Download Started....")
        object_file.download()
    except:
        print("Error occur!\n")

    print("Download completed Successfully")


def confirm():
    x = str(input("Do you want download other files?\nPress yes or no\n"))
    x = x.lower()
    if x == "no" or "n":
        return 0
    elif x == "yes" or "y":
        return 1
    else:
        print("Please enter the valid option\n")
        return confirm()


def execute(file_type):
    match file_type:
        case 1:
            link = input("Please give link for audio file to be downloaded\n")
            download_audio(link)
        case 2:
            link = input("Please give link of video file to be downloaded\n")
            download_high(link)
        case 3:
            link = input("Please give link of video file to be downloaded\n")
            download_low(link)
        case _:
            print("Please choose suitable option")


a = 1
while a != 0:
    os.system("cls")
    print("Welcome to youtube video downloader project!\n")
    file_type = int(input(''' Press the following key for your video type\n
    1.Audio Format
    2.High Quality 
    3.Low Quality\n'''))
    execute(file_type)
    a = confirm()
