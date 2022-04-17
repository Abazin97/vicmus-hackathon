


class Exhibit:
    '''
    Класс экспозиции, содержащий текстовую и звуковую информацию на русском и 
    английском языке, а также её фото
    '''
    path = r'\media'
    
    
    def __init__(self, name, ru_txt, en_txt, ru_sound, en_sound, photo):
        '''
        name: str
        ru_txt: str
        en_txt: str
        ru_sound: str (path to file)
        en_sound: str (path to file)
        photo: list (list of paths to files)
        '''
        self.name = name
        self.ru_txt = ru_txt
        self.en_txt = en_txt
        self.ru_sound = ru_sound
        self.en_sound = en_sound
        self.photo = photo
    
    
    def send_info(self, bot, chat_id, with_sound=False, eng=False):
        pass



phr = {
    'greet': {
        'ru': 'Здравствуйте!',
        'en': ''},
}
