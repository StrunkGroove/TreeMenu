from menu.models import TreeMenu


def fill_database():
    main_menu_items = [
        ("lvl1 1", None),
        ("lvl2 1", "lvl1 1"),
        ("lvl3 1", "lvl2 1"),
        ("lvl3 2", "lvl2 1"),
        ("lvl3 3", "lvl2 1"),
        ("lvl2 2", "lvl1 1"),
        ("lvl2 3", "lvl1 1"),
        ("lvl1 2", None),
        ("lvl1 3", None),
        ("lvl2 4", "lvl1 1"),
        ("lvl3 4", "lvl2 4"),
        ("lvl2 5", "lvl1 1"),
        ("lvl3 5", "lvl2 5"),
        ("lvl1 4", None),
        ("lvl2 6", "lvl1 4"),
        ("lvl3 6", "lvl2 6"),
        ("lvl2 7", "lvl1 4"),
        ("lvl3 7", "lvl2 7"),
    ]

    for name, parent_name in main_menu_items:
        parent = TreeMenu.objects.get(name=parent_name) if parent_name else None
        TreeMenu.objects.create(name=name, table_name='main_menu', parent=parent)

    additional_items = [
        ("one", None),
        ("two", None),
        ("four", "one"),
        ("five", "one"),
        ("six", "one"),
        ("seven", "two"),
        ("eight", "two"),
        ("nine", "two"),
        ("ten", "four"),
        ("eleven", "four"),
        ("twelve", "four"),
    ]

    for name, parent_name in additional_items:
        parent = TreeMenu.objects.get(name=parent_name) if parent_name else None
        TreeMenu.objects.create(name=name, table_name='additional', parent=parent)

fill_database()
print('Fill success!')