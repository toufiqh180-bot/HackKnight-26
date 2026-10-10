import time
import webbrowser

RICKROLL_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&autoplay=1"


def reveal_mystery():
    print("Decrypting hidden signal...")
    time.sleep(1)
    print("ur ab to get.")
    time.sleep(1)
    print("RICK ROLLED MF...")
    time.sleep(1)

    for _ in range(100):
        webbrowser.open_new_tab(RICKROLL_URL)

    print("Mystery solved.")


if __name__ == "__main__":
    reveal_mystery()
