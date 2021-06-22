import vk_api
import random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests


def counting(phrase):
    a_letters = ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я', 'ы']
    quantity_slogs = 0  # Переменная с количеством гласных в строке
    phrase = phrase.split()
    for letter_in_a_row in phrase[-1].lower():  # Перебираем все буквы в строке
        for letter in a_letters:  # По очереди сравниваем буквы с гласными
            if letter_in_a_row == letter:
                quantity_slogs += 1  # Если буква гласная увеличиваем счетчик
    return quantity_slogs


def rhyme(sentenc):
    words = open('russian.txt').read().split() + open('new_words.txt').read().split()
    new_words = open('new_words.txt', 'a')
    random.shuffle(words)
    sentence = ''
    for elem in sentenc.split()[-1]:
        if elem.lower() in alp:
            sentence += elem

    if sentence:
        for i in sentence.split():
            if i not in words:
                new_words.write(i + '\n')

        for word in words:
            if (sentence.split()[-1][-1] == word[-1]) and (sentence.split()[-1][-2] == word[-2]) and (counting(sentence) == counting(word)):
                return word
        for word in words:
            if (sentence.split()[-1][-1] == word[-1]) and (sentence.split()[-1][-2] == word[-2]):
                return word
        for word in words:
            if sentence.split()[-1][-2] == word[-2]:
                return word
    else:
        return 'емае, не могу ничё придумать('


def main():
    vk_session = vk_api.VkApi(
        token='e16cf68317bcf5092112a4672cd17b6642e4635eb7ba7b06106c7d661141546f4c42ec4f9fbf8cadbae37')

    longpoll = VkBotLongPoll(vk_session, '205367481')

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            if event.obj.message['text']:
                if event.from_user:
                    vk.messages.send(user_id=event.obj['message']['from_id'],
                                     message=f"{rhyme(event.obj.message['text'])}",
                                     random_id=random.randint(0, 2 ** 64))
                elif event.from_chat:
                    vk.messages.send(chat_id=event.chat_id,
                                     message=f"{rhyme(event.obj.message['text'])}",
                                     random_id=random.randint(0, 2 ** 64))


alp = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


if __name__ == '__main__':
    main()


