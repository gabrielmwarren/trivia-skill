from mycroft import MycroftSkill, intent_file_handler


class Trivia(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('trivia.intent')
    def handle_trivia(self, message):
        self.speak_dialog('trivia')


def create_skill():
    return Trivia()

