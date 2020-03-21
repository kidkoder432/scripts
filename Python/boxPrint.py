def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("'symbol' needs to be of length 1")
    if width + height <= 4:
        raise Exception("'width' and 'height' must be greater than 2")
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + ' ' * (width - 2) + symbol)

    print(symbol * width)

boxPrint('#', 22, 10)
