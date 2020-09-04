from pprint import pprint

from wialon import Wialon, WialonError, flags

wialon = Wialon()
login = None
token = 'cc06cce5395ef07d3e3407ae05e79a9808EC7AC81B47A18DA69B534A43958D265B22FB46'

try:
    login = wialon.token_login(token=token)
except WialonError as e:
    print("Error while login")

wialon.sid = login['eid']


def api_wialon_dwnObj(name):

    custom_flag = flags.ITEM_DATAFLAG_BASE

    spec = {
        'itemsType': 'avl_unit',
        'propName': 'sys_name',
        'propValueMask': '*'+name+'*',
        'sortType': 'sys_name'
    }
    interval = {"from": 0, "to": 0}

    units = wialon.core_search_items(spec=spec, force=1, flags=custom_flag, **interval)
    return units['items'][0]['id']


def api_wialon_reg_fuel(id_obj, date_u, volume):

    wialon.unit_registry_fuel_filling_event({
                                            "date": date_u,
                                            "volume": volume,
                                            "cost": 0.0,
                                            "location": 'АЗС',
                                            "deviation": 30,
                                            "x": '0',
                                            "y": '0',
                                            "description": 'C Газпрома',
                                            "itemId": id_obj
                                            })


if __name__ == '__main__':
    name = '283'
    id_ob = api_wialon_dwnObj(name)
    api_wialon_reg_fuel(id_ob, 1596626280, 20)
