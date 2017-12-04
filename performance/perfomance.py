import  hashlib
name_of_files = [
    '1.jpg',
    '2.jpg',
    '3.jpg',
    '4.jpg',
    '5.jpg',
    '6.jpg',
    '7.jpg',
    '8.jpg',
    '9.jpg',
    '10.jpg'
]

list_of_md5 = []

for i in name_of_files:
    def hash_to_md5(i):
        hash_md5 = hashlib.md5()
        with open(i, "rb") as f:
            for line in iter(lambda: f.read(4096), b""):
                hash_md5.update(line)
        return list_of_md5.append(hash_md5.hexdigest())



