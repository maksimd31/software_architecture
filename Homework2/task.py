from random import choice
from abc import ABC, abstractmethod


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass

    def open_reward(self):
        self.game_item = self.create_item()
        self.game_item.open()


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class GoldReward(IGameItem):
    def open(self):
        print('Gold')


class GoldGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GoldReward()


class GemReward(IGameItem):
    def open(self):
        print('Gem')


class GemGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return GemReward()


# ДЗ. Добавить новые предметы. Сундуки с новыми предметами.
'ДЗ'

class SilverReward(IGameItem):
    def open(self):
        print('Silver')


class SilverGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return SilverReward()


class PotionReward(IGameItem):
    def open(self):
        print('Potion')


class PotionGenerator(ItemFabric):
    def create_item(self):
        print('Create new bag')
        return PotionReward()


lst = [GoldGenerator(), GemGenerator(), SilverGenerator(), PotionGenerator()]

if __name__ == '__main__':
    # gold_generator = GoldGenerator()
    # gold_generator.open_reward()
    # lst = [GoldGenerator(), GemGenerator()]
    lst = [GoldGenerator(), GemGenerator(), SilverGenerator(), PotionGenerator()]
    for i in range(20):
        choice(lst).open_reward()
