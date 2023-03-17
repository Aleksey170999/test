class Client:
    def __init__(self):
        self.DB = [('Ноутбук', 1500, 'Татьяна', '89002001020'),
                     ('Смартфон', 500, 'Анна', '89202202325'),
                     ('Проектор ', 300, 'Андрей', '89505205656'),
                     ('Принтер', 750, 'Игорь', '89303303236'),
                     ('Планшет', 2300, 'Игорь', '89303303236'),
                     ('Смартфон', 1000, 'Андрей', '89505205656'),
                     ('Ноутбук', 4800, 'Татьяна', '89002001020'),
                     ('Наушники', 780, 'Марина', '89562002350'),
                     ('Сканер', 550, 'Сергей', '89808564559'),
                     ('Планшет!', 1200, 'Анна', '89202202325'),
                     ('Ноутбук', 1100, 'Игорь', '89303303236'),
                     ('Смартфон', 3500, 'Татьяна', '89002001020')]

    def clients_optimized(self, person_name):
        res = {}
        for client in self.DB:
            name = client[2]
            phone = client[3]
            device = client[0]
            price = client[1]

            if name not in res.keys():
                res[name] = {"phone": phone,
                             "devices": [],
                             "prices": []}

            res[name]["devices"].append(device)
            res[name]["prices"].append(price)

        return res[person_name]

    def get_info_by_name(self, name):
        person = self.clients_optimized(name)

        res = f'{name} {person["phone"]}: '
        devices = person['devices']
        prices = person['prices']
        for i in range(len(devices)):
            res += f'{devices[i]} - {prices[i]}; '
        return res[:-2]


test = Client()

print(test.get_info_by_name('Татьяна'))
