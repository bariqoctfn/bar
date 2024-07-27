class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.__age = age
        self.__address = address

    # Getter untuk age
    def get_age(self):
        return self.__age

    # Setter untuk age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("umur harus lebih dari nol")

    # Getter untuk address
    def get_address(self):
        return self.__address

    # Setter untuk address
    def set_address(self, address):
        self.__address = address

# Membuat objek baru
person1 = Person("John Doe", 30, "manahan no 22")

# Mengakses variabel private menggunakan getter
print("umur:", person1.get_age())
print("alamat:", person1.get_address())

# Mengubah nilai variabel private menggunakan setter
person1.set_age(35)
person1.set_address("manahan nomor 22")

# Mengecek nilai yang telah diubah
print("umur baru:", person1.get_age())
print("Alamat baru:", person1.get_address())
