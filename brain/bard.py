from bardapi import BardCookies
import datetime
cookie_dict ={
    "__Secure-1PSID":"bAixHRlvqQh5xUo44iqNR6DNDY3641jh1KS92_bu5UfUyDMKS9oYNQIkp6MUPL9OqEAPKQ.",
    "__Secure-1PSIDTS":"sidts-CjIB3e41hSVRcLlPjfcWwvAR_Q_cw2NJagFE7EnOKAiaUWBPWxcySS3AfQJIbF6Xfgjq8RAA",
    "__Secure-1PSIDCC":"APoG2W-U5l4AR-1d0y-hn7dtIwDjuuxbk6uz2PwH1Le-39nJrJfzoRatceOX3p7UJMBr3QA"
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
    Question = input("Enter The Query : ")
    RealQuestion = str(Question)
    results = bard.get_answer(RealQuestion)['content']
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H%M%S")
    filenamedate = str(formatted_time) + str(".txt")
    filenamedate = "brain\\DataBase\\" + filenamedate
    print(split_and_save_paragraphs(results, filename=filenamedate))