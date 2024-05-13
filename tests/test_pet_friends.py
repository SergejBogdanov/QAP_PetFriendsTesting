from api import PetFriends
from settings import valid_email, valid_password
import os


pf = PetFriends()


def test_add_new_pet_without_foto_with_valid_data(name='Mila',
                                                  animal_type='Shepherd',
                                                  age=3):
    """Проверяем что можно добавить питомца без фото с корректными данными."""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_without_foto_with_incorrect_age(name='Mila',
                                                     animal_type='Shepherd',
                                                     age=-2):
    """Проверяем что нельзя добавить питомца без фото с некорректными данными (возраст)."""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Отправляем запрос с некорректным возрастом и сохраняем полученный ответ с кодом статуса в status
    status, _ = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 400


def test_add_new_pet_without_foto_with_incorrect_auth_key(name='Mila',
                                                          animal_type='Shepherd',
                                                          age=3):
    """Проверяем что нельзя добавить питомца без фото с некорректным auth_key."""

    # Отправляем запрос с некорректными api ключём и сохраняем полученный ответ с кодом статуса в status
    status, _ = pf.add_new_pet_without_photo({"key": "12345"}, name, animal_type, age)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403


def test_get_api_key_for_valid_user():
    """ Проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(valid_email, valid_password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_get_api_key_with_incorrect_email():
    """ Проверяем что запрос api ключа с некорректныи email возвращает статус 403"""

    # Отправляем запрос с некорректными email и сохраняем полученный ответ с кодом статуса в status
    status, _ = pf.get_api_key('123@45.ru', valid_password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403


def test_get_api_key_with_incorrect_password():
    """ Проверяем что запрос api ключа с некорректныи паролем возвращает статус 403"""

    # Отправляем запрос с некорректными паролем и сохраняем полученный ответ с кодом статуса в status
    status, _ = pf.get_api_key(valid_email, '12345')

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403


def test_get_all_pets_with_valid_key(my_pets_filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
        Доступное значение параметра my_pets_filter - 'my_pets' либо '' """

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_list_of_pets(auth_key, my_pets_filter)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert len(result['pets']) > 0


def test_get_all_pets_with_incorrect_auth_key(my_pets_filter=''):
    """ Проверяем что запрос всех питомцев с некорректным auth_key возвращает статус 403."""

    # Отправляем запрос с некорректными api ключём и сохраняем полученный ответ с кодом статуса в status
    status, _ = pf.get_list_of_pets({"key": "12345"}, my_pets_filter)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403


def test_add_new_pet_with_valid_data(name='Mila',
                                     animal_type='Shepherd',
                                     age=3,
                                     pet_photo='images/Mila.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_incorrect_photo_format(name='Mila',
                                                 animal_type='Shepherd',
                                                 age=3,
                                                 pet_photo='images/filename.txt'):
    """Проверяем что нельзя добавить питомца с некорректными данными (фото не в разрешённом формате)."""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, _ = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 400


def test_add_new_pet_with_incorrect_age(name='Mila',
                                        animal_type='Shepherd',
                                        age=-2,
                                        pet_photo='images/Mila.jpg'):
    """Проверяем что нельзя добавить питомца с некорректными данными (возраст)."""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, _ = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 400


def test_add_new_pet_with_incorrect_auth_key(name='Mila',
                                             animal_type='Shepherd',
                                             age=3,
                                             pet_photo='images/Mila.jpg'):
    """Проверяем что нельзя добавить питомца с некорректным auth_key."""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status, _ = pf.add_new_pet({"key": "12345"}, name, animal_type, age, pet_photo)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403


def test_add_photo_of_pet_with_valid_data(my_pets_filter="my_pets",
                                          pet_photo='images/Mila.jpg'):
    """Проверяем что можно добавить фото с корректными данными."""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, my_pets_filter)

    # Если список не пустой, то пробуем добавить фото
    if len(my_pets['pets']) > 0:
        # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

        # Сверяем полученные данные с нашими ожиданиями
        assert status == 200
        assert len(result['pet_photo']) > 0
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_add_photo_of_pet_with_incorrect_photo_format(my_pets_filter="my_pets",
                                                      pet_photo='images/filename.txt'):
    """Проверяем что нельзя добавить фото не в разрешённом формате."""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, my_pets_filter)

    # Если список не пустой, то пробуем добавить фото
    if len(my_pets['pets']) > 0:
        # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
        status, _ = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

        # Сверяем полученные данные с нашими ожиданиями
        assert status == 400
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_add_photo_of_pet_with_incorrect_auth_key(my_pets_filter="my_pets",
                                                  pet_photo='images/Mila.jpg'):
    """Проверяем что нельзя добавить фото с некорректным auth_key"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, my_pets_filter)

    # Если список не пустой, то пробуем добавить фото
    if len(my_pets['pets']) > 0:
        # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
        status, _ = pf.add_photo_of_pet({"key": "12345"}, my_pets['pets'][0]['id'], pet_photo)

        # Сверяем полученные данные с нашими ожиданиями
        assert status == 403
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_delete_pet_with_valid_data(my_pets_filter="my_pets",
                                    name='Mila',
                                    animal_type='Shepherd',
                                    age=3,
                                    pet_photo='images/Mila.jpg'):
    """Проверяем возможность удаления питомца"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, my_pets_filter)

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
        _, my_pets = pf.get_list_of_pets(auth_key, my_pets_filter)

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, my_pets_filter)

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_delete_pet_with_incorrect_auth_key(my_pets_filter="my_pets",
                                            name='Mila',
                                            animal_type='Shepherd',
                                            age=3,
                                            pet_photo='images/Mila.jpg'):
    """Проверяем невозможность удаления питомца с некорректным auth_key"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, my_pets_filter)

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
        _, my_pets = pf.get_list_of_pets(auth_key, my_pets_filter)

    # Берём id первого питомца из списка и отправляем запрос на удаление с некорректным auth_key
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet({"key": "12345"}, pet_id)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403


def test_update_pet_info_with_valid_data(my_pets_filter="my_pets",
                                         name='Mila',
                                         animal_type='Shepherd',
                                         age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, my_pets_filter)

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'],
                                            name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_update_pet_info_with_incorrect_age(my_pets_filter="my_pets",
                                            name='Mila',
                                            animal_type='Shepherd',
                                            age=-2):
    """Проверяем невозможность обновления информации о питомце с некорректными данными (возраст)"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, my_pets_filter)

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, _ = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'],
                                       name, animal_type, age)

        # Сверяем полученные данные с нашими ожиданиями
        assert status == 400
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_update_pet_info_with_incorrect_auth_key(my_pets_filter="my_pets",
                                                 name='Mila',
                                                 animal_type='Shepherd',
                                                 age=5):
    """Проверяем невозможность обновления информации о питомце с некорректным auth_key"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, my_pets_filter)

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст с некорректным auth_key
    if len(my_pets['pets']) > 0:
        status, _ = pf.update_pet_info({"key": "12345"}, my_pets['pets'][0]['id'],
                                       name, animal_type, age)

        # Сверяем полученные данные с нашими ожиданиями
        assert status == 403
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")
