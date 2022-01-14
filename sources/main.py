import random
import requests


def gen_pwd():
    nb_of_words = random.randrange(3, 5, 1)
    response = requests.get('https://random-word-api.herokuapp.com/word?number=' + str(nb_of_words) + '&swear=0')
    pwd = ""
    for i in response.json():
        pwd += i
        if i != response.json()[nb_of_words - 1]:
            pwd += " "
    return pwd


def complex_pwd(words_list):
    strongest_pwd = ""
    for i in words_list:
        nb = random.randrange(0, 100, 1)
        if i != " ":
            if 0 <= nb <= 14:
                strongest_pwd += str.capitalize(i)
            elif 20 <= nb <= 30:
                j = random.randrange(0, 9, 1)
                strongest_pwd += str(j)
            elif 30 <= nb <= 37:
                k = random.randrange(33, 47, 1)
                strongest_pwd += chr(k)
            else:
                strongest_pwd += i
        else:
            strongest_pwd += i
    return strongest_pwd


if __name__ == '__main__':
    words = gen_pwd()
    pwd = complex_pwd(words)
    print('Your newly generated password is: ' + pwd)
