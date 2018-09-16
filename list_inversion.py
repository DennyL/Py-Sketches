#три способа обращения списка

def invert_array(A:list, N:int):
    """ Обращение массива (поворот массива задом-наперед
        в рамках индексов от 0 до N-1) с использованием встроенного метода
    """
    fragment = A[0:N]
    fragment.reverse()
    return fragment


###########
#   или   #
###########


def invert_array_stepped(A:list, N:int):
    """ Обращение массива (поворот массива задом-наперед
        в рамках индексов от 0 до N-1) без использования метода reverse(), как я сам вижу решение
        через создание и наполнение второго списка
    """
    reversed_list = []
    for i in range(N-1, -1, -1): # инициируем счет вниз по списку от N-1 до 0 включительно
        reversed_list.append(A[i])
    return reversed_list


###########
#   или   #
###########    


def invert_array_mfti(A:list, N:int):
    """ решение, показанное на лекции Хирьянова в МФТИ, позволяет менять список сам в себе.
    """
    for k in range(N//2):
        A[k], A[N-1-k] = A[N-1-k], A[k]
    return A[:N]
        
    


#############
#  TESTING  #
#############

def test1_invert_array():
    """ функция для тестирования invert_array() определенным списком
    """    
    test_list = [1, 2, 3, 4, 5]
    result = invert_array(test_list, 5)
    if result == [5, 4, 3, 2, 1]:
        print("test1 passed")
    else:
        print("test1 failed")


def test2_invert_array():
    """функция для тестирования invert_array() определенным списком"""    
    test_list = [0, 0, 18, 9, -45]
    result = invert_array(test_list, 3)
    if result == [18, 0, 0]:
        print("test2 passed")
    else:
        print("test2 failed")


def test_invert_array_stepped():
    """функция для тестирования invert_array_stepped() определенным списком"""    
    test_list = [0, 0, 18, 9, -45]
    result = invert_array_stepped(test_list, 3)
    if result == [18, 0, 0]:
        print("test_stepped passed")
    else:
        print("test_stepped failed")


def test_invert_array_mfti():
    """функция для тестирования invert_array_mfti() определенным списком"""    
    test_list = [0, 0, 18, 9, -45]
    result = invert_array_mfti(test_list, 3)
    print(result)
    if result == [18, 0, 0]:
        print("test_mfti passed")
    else:
        print("test_mfti failed")



#test1_invert_array()
#test2_invert_array()
#test_invert_array_stepped()
test_invert_array_mfti()
