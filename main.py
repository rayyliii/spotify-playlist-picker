import subprocess
import time


PLAYLISTS = {
    "1": {
        "name": "Hardstyle",
        "uri": "spotify:playlist:1v2QdlbBYDkbWzvQjmAEP2"
    },
      "2": {
        "name": "Hyperpop",
        "uri": "spotify:playlist:23I1HOHKYklVpkFlJTvlR2"
    },
    "3": {
        "name": "Chill",
        "uri": "spotify:playlist:4QMUf03FuxfX5L8vP2uHvR"
    },
    "4": {
        "name": "Sage",
        "uri": "spotify:playlist:3jfQ52z0k6AyXCujgQsmK1"
    }
}



def play_playlist() -> None:

    print("Which playlist do you want to play?\n")

    for number, playlist in PLAYLISTS.items():
        print(f"{number}. {playlist['name']}")

    choice = input("\nEnter number: ")

    if choice not in PLAYLISTS:
        print("Invalid choice.")
        return

    playlist_uri = PLAYLISTS[choice]["uri"]

    print(f"Opening {PLAYLISTS[choice]['name']}...")

    subprocess.Popen(
        ["cmd", "/c", "start", "", playlist_uri],
        shell=False
    )

    time.sleep(4)
    send_keys = (
        "$shell = New-Object -ComObject WScript.Shell; "
        "[void]$shell.AppActivate('Spotify'); "
        "1..5 | ForEach-Object { $shell.SendKeys('{TAB}') }; "
        "$shell.SendKeys('{ENTER}'); "
    )
    subprocess.run(["powershell", "-NoProfile", "-Command", send_keys], check=True)


if __name__ == "__main__":
    play_playlist()
