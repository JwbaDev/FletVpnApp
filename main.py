from flet import *
import os
from windscribe import Windscribe


# GET USERNAME FROM YOU ENV
# YOU CREATE ACCOUNT FOR ACTIVE LOGIN
you_username = os.environ.get("username")
you_password = os.environ.get("password")

windscriber = Windscribe(you_username,you_password)


def main(page:Page):

	page.vertical_alignment="center"

	def connecttovpn(e):
		# SHOW SNACKBAR 
		page.snack_bar = SnackBar(
			Text("connecting.....",size=30,
				weight="bold"
			),
			bgcolor="purple"
			)
		page.snack_bar.open = True
		page.update()


		# AND CONNECT TO WINDSCRIBE VPN
		while True:
			# rand=True IS FOR YOU RANDOM COUNTRY
			windscriber.connect(rand=True)
			input("IF YOU ENTER THIS .THEN RANDOM COUNTRY AGAIN .")
			time.sleep(1)




	page.add(
		Column([
		Text("Vpn Connector",size=30,weight="bold"),
		IconButton(icon="wifi",
			icon_size=50,
			icon_color="white",
			bgcolor="blue",
			on_click=connecttovpn

			)

		],alignment="center")

		)
flet.app(target=main)


# AND NOW CHECK MY COUNTRY BEFORE TEST THIS APP

# NOW TEST APP 