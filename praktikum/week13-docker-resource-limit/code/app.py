import os
import time
import sys

def game():
    print(f"\nProgram Game Survival Resource (PID: {os.getpid()})")
    print(f"Setiap Level naik 50MB RAM ")

    print("\nMemuat Texture Game ( Memory Test)")
    ram_use = []

    survival = bytearray(50 * 1024 * 1024) # 50 MB RAM

    try:
        for level in range(1,11):
            print(f"Loading Level {level}... | Total RAM : {level * 50} MB")
            ram_use.append(survival[:])

            time.sleep(1)

        print(f"\nSelamat! Anda mencapai Level {level}")
        print("RAM 500MB Berhasil dimuat")

    except MemoryError:
        print("\n Game Crashed ( Force Close )")
        print("Penyebab : Out Of Memory")
        print("Docker mematikan paksa game.")

        sys.exit(1)

    print("\nRendering Grafik ( CPU Test )")
    print("CPU dipaksa kerja 100%\n")

    start_time = time.time()
    while time.time() - start_time < 5:
        _ = [x**2 for x in range(5000)]
    
    print("   -> Rendering Selesai.\n")

if __name__ == "__main__":
    game()