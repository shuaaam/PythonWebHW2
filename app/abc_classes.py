from abc import ABC, abstractmethod


class AbcRecord(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def add_email(self, new_email):
        pass

    @abstractmethod
    def add_phone(self, new_num):
        pass

    @abstractmethod
    def remove_phone(self, num):
        pass

    @abstractmethod
    def edit_phone(self, num, new_num):
        pass

    @abstractmethod
    def number_in_list(self, num):
        pass

    @abstractmethod
    def get_phone(self, num: str):
        pass

    @abstractmethod
    def get_email(self, email: str):
        pass

    @abstractmethod
    def serealize(self):
        pass

    @abstractmethod
    def deserealize(self, record):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def edit_name(self, new_name: str):
        pass

    @abstractmethod
    def email_in_list(self, mail):
        pass

    @abstractmethod
    def edit_email(self, email, new_email):
        pass


class AbcNote(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_tag(self, new_tag):
        pass

    @abstractmethod
    def change_text(self, new_txt):
        pass

    @abstractmethod
    def delete_tag(self, tag):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def has_tag(self, tag: str):
        pass

    @abstractmethod
    def serealize(self):
        pass

    @abstractmethod
    def deserealize(self, note):
        pass
