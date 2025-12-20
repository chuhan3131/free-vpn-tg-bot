from aiogram.fsm.state import State, StatesGroup


class CaptchaState(StatesGroup):
    waiting_captcha = State()