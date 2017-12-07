def main():
    with open('01.input') as file:
        data = file.readlines()[0].strip()
        # print(first_task(data))
        print(second_part(data));

def first_task(inputData):
    data = list(inputData)
    data += str(data[0])
    val = 0
    prev = None
    for d in data:
        if d == prev:
            val += int(d)
        prev=d
    return val

def second_part(inputData):
    data = list(inputData)
    length = len(data)
    offset = int(length/2)
    val = 0
    for i, d in enumerate(data):
        index = i+offset
        if index >= length:
            index -= length
        match = data[index]
        if d == match:
            val += int(d)
    return val


if __name__ == '__main__':
    main()
