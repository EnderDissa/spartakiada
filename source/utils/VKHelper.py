from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api


class VKHelper:
    def __init__(self, vk_session):
        self.vk = vk_session.get_api()
        self.vk_session = vk_session

    def lsend(self, id, text):
        print("sended to " + str(id))
        self.vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})

    def lsend_withA(self, id, text, attachment):
        print("sended to " + str(id))
        self.vk_session.method('messages.send',
                               {'user_id': id, 'message': text, 'attachment': attachment, 'random_id': 0})

    def send(self, id, text):
        print("sended to " + str(id))
        self.vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})

    def sender(self, sender_type):
        pass

    def send_message(self, peer_id, message, keyboard=None, attachment=None):
        payload = {
            "peer_id": peer_id,
            "message": message,
            "random_id": 0
        }
        if keyboard:
            payload["keyboard"] = keyboard
        if attachment:
            payload["attachment"] = attachment

        try:
            self.vk.messages.send(**payload)
        except vk_api.exceptions.ApiError as e:
            raise Exception(f"Ошибка отправки сообщения: {e}")

    def create_keyboard(self, buttons):
        keyboard = VkKeyboard(inline=True)
        for button in buttons:
            if button.get("newline"): keyboard.add_line()
            keyboard.add_callback_button(
                label=button["label"],
                payload=button["payload"],
                color=getattr(VkKeyboardColor, button["color"].upper())
            )
        return keyboard.get_keyboard() if buttons else None

    def create_standart_keyboard(self, buttons):
        keyboard = VkKeyboard(inline=False)
        for button in buttons:
            if button.get("newline"): keyboard.add_line()
            keyboard.add_button(
                label=button["label"],
                payload=button["payload"],
                color=getattr(VkKeyboardColor, button["color"].upper())
            )

        return keyboard.get_keyboard()

    def create_link_keyboard(self, buttons):
        keyboard = VkKeyboard(inline=True)
        for button in buttons:
            if button.get("newline"): keyboard.add_line()
            keyboard.add_openlink_button(
                label=button["label"],
                payload=button["payload"],
                link=button["link"]
            )

        return keyboard.get_keyboard()