class Cashier:
  def __init__(self, items, prices):
      self.items = items
      self.prices = prices

  def calculate_total(self, selected_items):
      total = 0
      for item in selected_items:
          try:
              index = self.items.index(item)
              price = self.prices[index]
              total += price
          except ValueError:
              print(f"{item} tidak ada dalam daftar barang.")
      return total

# Daftar barang dan harga
items = ["apel", "pisang", "jeruk"]
prices = [2500, 1500, 3000]

# Membuat objek kasir
cashier = Cashier(items, prices)

try:
  # Meminta input dari pengguna
  selected_items = input("Masukkan item yang dibeli (pisahkan dengan koma): ").split(",")

  # Menghapus spasi dari setiap item
  selected_items = [item.strip() for item in selected_items]

  # Menghitung total belanja
  total_price = cashier.calculate_total(selected_items)
  print("Total belanja:", total_price)
except KeyboardInterrupt:
  print("\nProgram dihentikan oleh pengguna.")
except Exception as e:
  print(f"Terjadi kesalahan: {e}")
