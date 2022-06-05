def get_batch_index(total: int, batch_size: int) -> list:
    """get list of list index
        ex: with batch_size=3, total=8: [[1,2,3], [4,5,6], [7,8]]

    Args:
        total (int): total element
        step (int): batch size
    """

    num = total
    step = batch_size
    rt = []

    if num <= 0 or batch_size <= 0:
        raise Exception('total and batch_size must be greater than zero')

    for x in range(1, num+1, step):
        rt_ = []

        end = min(x+step, num+1)
        for y in range(x, end):
            rt_.append(y)

        rt.append(rt_)

    return rt
