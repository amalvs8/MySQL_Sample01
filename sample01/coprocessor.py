def covert_data(data):
    column = []
    data = []
    for i in data:
        column.append(i[0])
    cursor_db.execute("SELECT * FROM " + tb + ";")
    for i in cursor_db:
        di = {}
        for j in range(len(i)):
            di[column[j]] = i[j]
        data.append(di)
    return data