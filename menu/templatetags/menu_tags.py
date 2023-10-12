from typing import Dict, Any
from django import template
from menu.models import TreeMenu

register = template.Library()

@register.inclusion_tag('menu/menu_tag.html', takes_context=True)
def draw_menu(context: Dict[str, Any], menu_name: str):
    name = context.get('name')
    
    if name is not None:
        print(name)
        menu_objects = TreeMenu.get_ancestors(name, menu_name)
        menu_objects = sorted(menu_objects, key=lambda x: x.path)
        print(menu_objects)
        menu = {}

        for obj in menu_objects:
            if obj.parent_id is None:
                menu[obj.name] = {'root': obj, 'child': {}}

            else:
                names = obj.path.split('/')
                sub_menu = menu
                for name in names[1:-2]:
                    sub_menu = sub_menu[name]['child']
                sub_menu[names[-2]] = {'root': obj, 'child': {}}
 
        return {"menu": menu}
    
    menu_objects = TreeMenu.objects.filter(parent_id=None, table_name=menu_name)
    menu = {}
    for obj in menu_objects:
        menu[obj.name] = {'root': obj, 'child': []}

    return {"menu": menu}