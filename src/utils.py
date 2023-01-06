def chunks(array, n):
    for i in range(0, len(array), n):
        yield array[i:i + n]
