def convert_to_int(string):
  try:
      result = int(string)
      return result
  except ValueError:
      print("Input harus berupa bilangan bulat.")
      return None  # Return None when conversion fails

try:
  umur = input('Masukkan umur kamu: ')  # inputan yang benar adalah angka
  umur5tahunlagi = convert_to_int(umur)
  if umur5tahunlagi is not None:
      umur5tahunlagi += 5
      print(f"Umur kamu 5 tahun lagi adalah {umur5tahunlagi}.")
except KeyboardInterrupt:
  print("\nProgram dihentikan oleh pengguna.")
except Exception as e:
  print(f"Terjadi kesalahan: {e}")
