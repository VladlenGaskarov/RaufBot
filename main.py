import re
import json

lines = []

with open('message', "r", encoding="utf-8") as message_file:
    message_read = message_file.read()

message_split = message_read.split('\n')

with open('item_price.json', 'r', encoding='utf-8') as of:
    items_prices = json.loads(of.read())

try:
    for i in message_split:
        dream = i
        item = i.split('-')
        if len(item) == 2 and item[0] + item[1][-2:] not in items_prices:
            items_prices[item[0] + item[1][-2:]] = int(re.findall(r'(\d+)', item[1])[0])
            dream = item[0] + '-' + item[0] + item[1][-2:]
        elif len(item) == 2:
            items_prices[item[0] + item[1][-2:]][0] = int(re.findall(r'(\d+)', item[1])[0])
            dream = item[0] + '-' + item[0] + item[1][-2:]
        lines.append(dream)
except Exception as err:
    print('Скорее всего ты не заполнил цены, дурак.', f'Ошибка 14-26: {err}')

with open('item_price.json', 'w', encoding='utf-8') as fh:
    fh.write(json.dumps(items_prices, ensure_ascii=False))

message_final = '\n'.join(lines)
message_final_dee_shop = message_final

try:
    for i in items_prices:
        if not i[-1].isdigit():
            message_final = message_final.replace(i, ' ' + str(items_prices[i][0]+items_prices[i][1]) + i[-2:])
        else:
            message_final = message_final.replace(i, ' ' + str(items_prices[i][0]+items_prices[i][1]))
except Exception as err:
    print('Скорее всего ты не заполнил цены, дурак.', f'Ошибка 33-40: {err}')


with open('Aroma_shop', 'w', encoding='utf-8') as f:
    f.write(message_final)

try:
    for i in items_prices:
        if not i[-1].isdigit():
            message_final_dee_shop = message_final_dee_shop.replace(i, ' ' + str(round(items_prices[i][0]/0.9)+1000) + i[-2:])
        else:
            message_final_dee_shop = message_final_dee_shop.replace(i, ' ' + str(round(items_prices[i][0]/0.9)+1000))
except Exception as err:
    print('Скорее всего ты не заполнил цены, дурак.', f'Ошибка 47-54: {err}')

with open('Dee_shop', 'w', encoding='utf-8') as f:
    f.write(message_final_dee_shop)
