
import random, sys, time
art1 = """
   ____ _    ____________  __  ___________    ____     ____       _____
  / __ \ |  / / ____/ __ \/ / / / ____/   |  / __ \   / __ \____ / ___/
 / / / / | / / __/ / /_/ / /_/ / __/ / /| | / / / /  / / / / __ \\__ \ 
/ /_/ /| |/ / /___/ _, _/ __  / /___/ ___ |/ /_/ /  / /_/ / /_/ /__/ / 
\____/ |___/_____/_/ |_/_/ /_/_____/_/  |_/_____/  /_____/\____/____/  
"""
art2 = """
   _____     _______ ____  _   _ _____    _    ____    ____       ____  
  / _ \ \   / / ____|  _ \| | | | ____|  / \  |  _ \  |  _ \  ___/ ___| 
 | | | \ \ / /|  _| | |_) | |_| |  _|   / _ \ | | | | | | | |/ _ \___ \ 
 | |_| |\ V / | |___|  _ <|  _  | |___ / ___ \| |_| | | |_| | (_) |__) |
  \___/  \_/  |_____|_| \_\_| |_|_____/_/   \_\____/  |____/ \___/____/ 
"""
art3 = """
  ██████╗ ██╗   ██╗███████╗██████╗ ██╗  ██╗███████╗ █████╗ ██████╗ ██████╗ 
 ██╔═══██╗██║   ██║██╔════╝██╔══██╗██║  ██║██╔════╝██╔══██╗██╔══██╗╚════██╗
 ██║   ██║██║   ██║█████╗  ██████╔╝███████║█████╗  ███████║██║  ██║ █████╔╝
 ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗██╔══██║██╔══╝  ██╔══██║██║  ██║██╔═══╝ 
 ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║██║  ██║███████╗██║  ██║██████╔╝███████╗
  ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝
"""
banners = [art1, art2, art3]
authors = "			By !Woz, MrCuervo & Case."
def Header():
	header = random.choice(banners)
	clear = "\x1b[0m"
	colors = [31, 32, 33, 34, 35, 36]
	color = random.choice(colors)
	for line in header.split("\n"):
		sys.stdout.write("\x1b[1;%dm%s%s\n" % (color, line, clear))
		time.sleep(0.1)
	print("\x1b[1;%dm%s%s\n" % (random.choice(colors),authors, clear))
