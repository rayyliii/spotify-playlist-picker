import subprocess
import time

PLAYLIST_URI = "spotify:playlist:1v2QdlbBYDkbWzvQjmAEP2"


def play_playlist() -> None:
	subprocess.Popen(["cmd", "/c", "start", "", PLAYLIST_URI], shell=False)

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
