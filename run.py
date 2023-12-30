import pyautogui, time

position =pyautogui.position()
pesan = "AKU YG HABIS DUIT KYINI BANAR MENAGIH"
for a in range(2000000):
  pyautogui.click(position.x,position.y)
  pyautogui.typewrite(pesan)
  print(pesan)
  time.sleep(2)
  pyautogui.typewrite(["enter"])