def main():
    with open('02.input') as file:
        raw_data = file.readlines()
        data = []
        for line in raw_data:
            data.append([ int(x) for x in line.strip().split('\t') ])
        # print(first_part(data))
        print(second_part(data))

def first_part(inputData):
    data = list(inputData)
    val = 0
    for d in data:
        val += int(max(d) - min(d))
    return val

def second_part(inputData):
    data = list(inputData)
    val = 0
    for d in data:
        d.sort()
        for denominator_index, denominator in enumerate(d):
            for numerator_index in range(denominator_index, len(d)):
                if((d[numerator_index] % denominator == 0) and (d[numerator_index] / denominator != 1)):
                    val += int(d[numerator_index] / denominator)
                    break
    return val


if __name__ == '__main__':
    main()
