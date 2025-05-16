import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json', 'r') as file:
        data = json.load(file)
        guild = Guild.objects.create(name="Default Guild")
        race = Race.objects.create(name="Human")
        skill = Skill.objects.create(name="Basic Attack", bonus="+5", race=race)


if __name__ == "__main__":
    main()
