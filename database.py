import main

def down_req():
    def write_data(data):
        folder = open("data.txt", "w")
        folder.write(data)
        folder.close()
    

    def read_data():
        folder = open("data.txt").read(1)
        return folder
    
    data = ''
    if main.os.path.exists("data.txt"):
        data = read_data()

    else:
        folder = write_data('0')

    if data == '1':
        return 1
    else:
        main.os.system("pip install tk; pip install pygame; pip install sql")
        write_data('1')