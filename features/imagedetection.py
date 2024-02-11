from bardapi import BardCookies
import datetime
cookie_dict ={
    "__Secure-1PSID":"bAgW7BuWT7gxLLfMiekjVvWI5aBGLh0w1kqHIfgC8OSQ6mLqUKfkPmls5HpYayQE9I6Hpw.",
    "__Secure-1PSIDTS":"sidts-CjEB3e41hYWyd__LNcxGb6KP_Udnl6j2ynNrs1j01Qx0GocL9gRAIwXtsbZVkyFh2fSZEAA",
    "__Secure-1PSIDCC":"APoG2W_ig2GXoMJcq3p5Qf5smov9iMsB8Sqgquzd7T-NeVR8GS_r3Itd1-H-ITLj_60peX0tsg"
}
bard = BardCookies(cookie_dict=cookie_dict)

def split_and_save_paragraphs(data, filename):
    paragraphs = data.split('\n\n')
    with open(filename, 'w') as file:
        file.write(data)
    data = paragraphs[:2]
    separator = ', '
    joined_string = separator.join(data)
    return joined_string


while True:
    imagename = str(input("Enter The Image Name : "))
    image = open(imagename,'rb').read()
    bard = BardCookies(cookie_dict=cookie_dict)
    results = bard.ask_about_image('what is in the image?',image=image)['content']
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H%M%S")
    filenamedate = str(formatted_time) + str(".txt")
    filenamedate = "brain\\DataBase\\" + filenamedate
    print(split_and_save_paragraphs(results, filename=filenamedate))