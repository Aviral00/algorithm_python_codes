def job_sequencing(x, y, z):

    a = list(zip(x, y, z))
    m = sorted(a, key=lambda a:a[1])
    b = []
    for i in range(len(m)):
        



