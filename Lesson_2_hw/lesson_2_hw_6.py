goods = []
features = {'название': '', 'цена': '', 'количество': '', 'eд': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'eд': []}
num = 0
feature_ = None
control = None

while True:
    control = input("for continue press 'Enter', for analytics press 'a'")
    num += 1

    if control == 'a':
        for key, value in analytics.items():
            print(f'{key}: {value}')
    for f in features.keys():
        feature_ = input(f'Введите товар "{f}"')
        features[f] = int(feature_) if (f == 'цена' or f == 'количество') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))