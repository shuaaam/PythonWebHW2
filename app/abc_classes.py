from abc import ABC, abstractmethod


class AbstractOut(ABC):

    @abstractmethod
    def output(self):
        pass


class AbcContactBook(AbstractOut):

    def output(self):
        pass

class AbcNotebook(AbstractOut):

    def output(self):
        pass