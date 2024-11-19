from abc import ABC, abstractmethod
import random


# Абстрактний клас для підводних об'єктів
class Habitat(ABC):
    def __init__(self, name, energy_consumption, capacity):
        self.name = name
        self.energy_consumption = energy_consumption
        self.capacity = capacity

    @abstractmethod
    def functionality(self):
        pass


# Підкласи Habitat
class ResidentialDome(Habitat):
    def __init__(self, name, capacity):
        super().__init__(name, energy_consumption=10, capacity=capacity)

    def functionality(self):
        return f"{self.name} забезпечує житло для {self.capacity} жителів."


class ResearchLab(Habitat):
    def __init__(self, name, research_rate):
        super().__init__(name, energy_consumption=20, capacity=0)
        self.research_rate = research_rate

    def functionality(self):
        return f"{self.name} прискорює дослідження з коефіцієнтом {self.research_rate}."


class FarmingFacility(Habitat):
    def __init__(self, name, food_production_rate):
        super().__init__(name, energy_consumption=15, capacity=0)
        self.food_production_rate = food_production_rate

    def functionality(self):
        return f"{self.name} виробляє їжу зі швидкістю {self.food_production_rate} одиниць."


# Клас MarineSpecies
class MarineSpecies:
    def __init__(self, name, population, role_in_ecosystem):
        self.name = name
        self.population = population
        self.role_in_ecosystem = role_in_ecosystem

    def interact_with_city(self):
        return f"{self.name} впливає на екосистему, виконуючи роль {self.role_in_ecosystem}."


# Клас OceanCurrent
class OceanCurrent:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def affect_city(self):
        return f"Течія {self.name} зі швидкістю {self.strength} впливає на підводне місто."


# Клас Technology
class Technology:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def apply_technology(self):
        return f"Технологія {self.name} дає ефект: {self.effect}."


# Клас ResourceExtractor
class ResourceExtractor:
    def __init__(self, resource_type, extraction_rate):
        self.resource_type = resource_type
        self.extraction_rate = extraction_rate

    def harvest_resource(self):
        return f"Видобуто {self.extraction_rate} одиниць ресурсу {self.resource_type}."


# Основний клас для керування цивілізацією
class UnderwaterCivilization:
    def __init__(self):
        self.habitats = []
        self.species = []
        self.technologies = []
        self.resources = {"energy": 100, "food": 50, "minerals": 0}
        self.ecosystem_health = 100

    def expand_colony(self, habitat):
        self.habitats.append(habitat)
        self.resources["energy"] -= habitat.energy_consumption
        print(f"Побудовано {habitat.name}. Залишок енергії: {self.resources['energy']}.")

    def research_technology(self, technology):
        self.technologies.append(technology)
        print(f"Досліджено технологію {technology.name}: {technology.effect}.")

    def manage_ecosystem(self):
        self.ecosystem_health += random.randint(-10, 10)
        print(f"Екосистема оновлена. Здоров'я екосистеми: {self.ecosystem_health}%.")

    def harvest_resource(self, extractor):
        self.resources["minerals"] += extractor.extraction_rate
        print(extractor.harvest_resource())

    def adapt_to_environment(self, current):
        self.resources["energy"] -= current.strength
        print(f"Пристосовано до течії {current.name}. Залишок енергії: {self.resources['energy']}.")


# Основна програма
def main():
    # Створення цивілізації
    city = UnderwaterCivilization()

    # Додавання об'єктів
    dome = ResidentialDome("Житловий купол Альфа", 50)
    lab = ResearchLab("Лабораторія Глибини", 1.5)
    farm = FarmingFacility("Ферма Нептуна", 30)

    dolphin = MarineSpecies("Дельфін", 200, "Контроль популяції риб")
    current = OceanCurrent("Гольфстрім", 15)

    tech = Technology("Сонячний генератор", "Збільшує енергію на 50 одиниць")
    extractor = ResourceExtractor("Залізна руда", 20)

    # Виконання сценаріїв
    city.expand_colony(dome)
    city.expand_colony(lab)
    city.expand_colony(farm)

    city.research_technology(tech)
    city.harvest_resource(extractor)

    city.manage_ecosystem()
    city.adapt_to_environment(current)

    print(dolphin.interact_with_city())
    print(current.affect_city())
    print(tech.apply_technology())


if __name__ == "__main__":
    main()
