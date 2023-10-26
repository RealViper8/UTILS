try:
    import os
    os.system("")
except:
    print("Error switching to os terminal !")
    exit(1)

try:
    from database.db import database
    import wget
    from Engine import engine
except:
    print("Error custom imports couldnt get imported !")
    exit(1)

class colours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[37'
    MAGENTA = '\033[35'
    YELLOW = '\033[33'
    GREY = '\033[90'
    BRIGHT_YELLOW = '\033[93'

try:
    import platform
    import sys
    import atexit
    from configparser import ConfigParser
    import requests
    from flask import Flask, render_template
except ModuleNotFoundError as A:
    print(colours.WARNING+str(A)+colours.ENDC)
    exit(1)

try:
    import time
    import threading
    from tqdm.auto import tqdm, trange
    import http.server
    import socketserver
except ModuleNotFoundError as A:
    print(colours.FAIL+str(A)+colours.ENDC)
    exit(1)

count = 0
for i in platform.python_version():
    if count == 0:
        ver = str(i)
        count += 1
    elif count == 2:
        ver_2 = str(i)
        count += 1
    elif count == 3:
        ver_2 += str(i)
        count += 1
    else:
        count += 1

config = ConfigParser()

def on_exit():
    print()
    print(colours.WARNING+"Exiting..."+colours.ENDC)
    try:
        os.rmdir("assets\\temp")
        print(colours.OKGREEN+"Clearing temp"+colours.ENDC)
    except:
        print("   "+colours.OKCYAN+"-> Closing & 0"+colours.ENDC)
    exit(0)

proxies = {
    # US Washington
    'US' : {'https': 'https://52.138.8.192:3128'},
    # Austria 
    'EU' : {'https' : 'https://82.218.176.25:32650'},
    # Vietnam Hanoi
    'VIETNAM' : {'https' : 'https://103.56.157.44:3128'},
    # Anonym 1
    'ANO1' : {'https' : 'https://103.187.117.163:8080'},
    # Anonym 2
    'ANO2' : {'https' : 'https://177.200.239.46:999'}
}

if os.path.exists("config.toml"):
    config.read("config.toml")
    if config["settings.options"]["clear_temp"] == True:
        atexit.register(on_exit)

def host_web():
    app = Flask(__name__)
    
    @app.route("/")
    def home():
        return render_template("home.html")    
    @app.route("/help")
    def help():
        return render_template("help.html")
    @app.route("/credits")
    def credits():
        return render_template("credits.html")
    @app.route("/contact")
    def contact():
        return render_template("contact.html")
    app.run()

class App:
    def run(self):
        if not os.path.exists("config.toml"):
            config.add_section("settings.menu")
            config.set("settings.menu","gui","False")
            config.set("settings.menu","database","True")
            config.set("settings.menu","account","False")
            config.add_section("settings.options")
            config.set("settings.options","save","True")
            config.set("settings.options","clear_temp","True")
            with open("config.toml","w") as f:
                config.write(f)
        return
        
    def load_start(self):
        for i in trange(100,ncols=50):
            if i == 0: threading.Thread(target=self.run).start(); done = True
            if done == True:
                time.sleep(0.03)

    def database_mode(self):
        count = 0
        while True:
            try:
                if count == 0:
                    os.system("clear" if os.name == "posix" else "cls")
                    print(colours.WARNING+"\n### Database ###"+colours.OKCYAN+" custom terminal with custom database commands\n"+colours.ENDC)
                    count += 1
                I = input(colours.OKGREEN+"Database:"+colours.OKBLUE+os.getcwd()+colours.ENDC+"$"+" ")
                if I == "help":
                    print()
                    print("help                             Shows this menu")
                    print("terminal                         Go back to terminal mode")
                    print("db <TableName>()                 Create database with empty table")
                    print("del                              Delete database")
                    print("c-d                              Change database")
                    print("exit                             Exits with code 0")
                    print()
                elif I == "terminal" or I == "terminal-mode" or I == "Terminal" or I == "cmd":
                    self.terminal()
                elif I == "exit" or I == "exit".capitalize():
                    on_exit()
                elif I == "" or I.isspace():
                    print()
                else:
                    print()
                    os.system(I)
                    print()
            except KeyboardInterrupt:
                print()
                on_exit()
            except Exception as E:
                print("Error: "+str(E))

    def terminal(self):        
        if config["settings.menu"]["gui"] == "False":
            count = 0
            while True:
                if count == 0:
                    os.system("timeout 2 > nul")
                    os.system("clear" if os.name == "posix" else "cls")
                    print(colours.WARNING+"\n### UTILS ###"+colours.OKCYAN+" custom terminal with custom commands and options\n"+colours.ENDC)
                    count += 1
                if config.has_option("settings.options","pt_text"):
                    config.read("config.toml")
                    cf = config.get("settings.options","pt_text")
                    I = input(colours.OKGREEN+f"{cf}:"+colours.OKBLUE+os.getcwd()+colours.ENDC+"$"+" ")
                else:
                    I = input(colours.OKGREEN+"Terminal:"+colours.OKBLUE+os.getcwd()+colours.ENDC+"$"+" ")
                if I == "help":
                    print()
                    print("help                 Shows this help menu")
                    print("gcw <WLAN-SSID>      Get current password from saved wifi")
                    print("show-profiles        Show all saved network profiles")
                    print("dw <URL>             Download File using url")
                    print("pt <Text>            Change the 'Terminal' text")
                    print("engine               Start a 3d Engine and view .obj Files")
                    print("iwshow               Shows what websites can see (ip address ...)")
                    print("web-host             Host a web server on port 5000")
                    print("proxy                Use and change proxy when browsing with utils")
                    print("host-l <PORT>        Create a tcp server on localhost !")
                    print("host-w               Create a tcp server online !")
                    print("encoder              Launch the golang base64 encoder/decoder")
                    print("exit                 Exits with code 0")
                    if config["settings.menu"]["database"] == "True":
                        print("database             Change to the database mode")
                    print()
                elif I == "encoder":
                    os.system("start encoder.exe")
                    print("\n"+colours.OKCYAN+"Launched the Encoder/Decoder"+colours.ENDC+"\n")
                elif I == "web-host":
                    app = Flask(__name__)
                    
                    @app.route("/")
                    def home():
                        return render_template("home.html")    
                    @app.route("/help")
                    def help():
                        return render_template("help.html")
                    @app.route("/credits")
                    def credits():
                        return render_template("credits.html")
                    @app.route("/contact")
                    def contact():
                        return render_template("contact.html")
                    app.run()
                elif I == "host-w" or I == "host-w".capitalize():
                    if os.path.exists("ngrok.exe"):
                        if not os.path.exists(os.getenv("LOCALAPPDATA")+"\\ngrok\\ngrok.yml"):
                            print("How to get the ngrok token : https://ngrok.com/docs/agent/#authtokens")
                            I = input("Auth-Token -> ")
                            
                            if I == "" or I.isspace():
                                print("The token cannot be empty !")
                                os.system("pause")
                                continue
                            os.system(f"ngrok config add-authtoken {I}")
                        port = input("Port -> ")
                        
                        try:
                            port = int(port)
                        except:
                            print(colours.WARNING+"Port should be integer or real number with 4 digits !"+colours.ENDC)
                        handler = http.server.SimpleHTTPRequestHandler
                        httpd = socketserver.TCPServer(("", port), handler)
                        print(f"{colours.OKCYAN}Serving on port {port} global using ngrok{colours.ENDC}")
                        print(f"{colours.OKGREEN}Website : http://localhost:{port}{colours.GREY}")
                        os.system("start ngrok.exe tcp "+str(port))
                        try:
                            threading.Thread(target=httpd.serve_forever).start()
                            os.system("pause > nul")
                            print(colours.ENDC)
                            os.system("taskkill /f /im ngrok.exe")
                            print()
                            continue
                        except KeyboardInterrupt:
                            os.system("taskkill /f /im ngrok")
                            print("Stopping !")
                            continue
                    else:
                        print("Error: Make sure you have ngrok.exe in this directory \"{}\"".format(os.getcwd()))
                elif "host-w" in I:
                    I = I.split(" ")
                    try:
                        I[1]
                    except:
                        print("Error: command takes one argument 0 given")
                        continue
                    if os.path.exists("ngrok.exe"):
                        if not os.path.exists(os.getenv("LOCALAPPDATA")+"\\ngrok\\ngrok.yml"):
                            print("How to get the ngrok token : https://ngrok.com/docs/agent/#authtokens")
                            I = input("Auth-Token -> ")
                            
                            if I == "" or I.isspace():
                                print("The token cannot be empty !")
                                os.system("pause")
                                continue
                            os.system(f"ngrok config add-authtoken {I}")
                        port = I[1]
                        
                        try:
                            port = int(port)
                        except:
                            print(colours.WARNING+"Port should be integer or real number with 4 digits !"+colours.ENDC)
                        handler = http.server.SimpleHTTPRequestHandler
                        httpd = socketserver.TCPServer(("", port), handler)
                        print(f"{colours.OKCYAN}Serving on port {port} global using ngrok{colours.ENDC}")
                        print(f"{colours.OKGREEN}Website : http://localhost:{port}{colours.GREY}")
                        os.system("start ngrok.exe tcp "+str(port))
                        try:
                            threading.Thread(target=httpd.serve_forever).start()
                            os.system("pause > nul")
                            print(colours.ENDC)
                            os.system("taskkill /f /im ngrok.exe")
                            print()
                            continue
                        except KeyboardInterrupt:
                            os.system("taskkill /f /im ngrok")
                            print("Stopping !")
                            continue
                    else:
                        print("Error: Make sure you have ngrok.exe in this directory \"{}\"".format(os.getcwd()))
                elif I == "host-l" or I == "host-l".capitalize():
                    print()
                    I = input(colours.OKBLUE+"Wich port to host? (8080 default) -> "+colours.ENDC)
                    if I == "" or I.isspace():
                        I = 8080
                    if I != 0 and int(I) > 0 and len(str(I)) > 2:
                        print('\n'+colours.BOLD+"Starting Server !"+colours.ENDC+'\n')
                        os.system("title TCP Server")
                        handler = http.server.SimpleHTTPRequestHandler

                        if I != "" or not I.isspace():
                            port = int(I)
                        else: port = 8080

                        httpd = socketserver.TCPServer(("", port), handler)

                        print(f"{colours.OKCYAN}Serving on port {port}{colours.ENDC}")
                        print(f"{colours.OKGREEN}Website : http://localhost:{port}{colours.GREY}")

                        try:
                            threading.Thread(target=httpd.serve_forever).start()
                            os.system("pause > nul")
                        except KeyboardInterrupt:
                            print("Stopping !")
                elif "host-l" in I:
                    I = I.split(" ")
                    try:
                        try:
                            int(I[1])
                        except:
                            print("\n"+colours.FAIL+"Error: argument should be real example 8080"+colours.ENDC+"\n")
                            continue
                        if I[1] == "" or I[1].isspace():
                            port = 8080
                        else:
                            port = I[1]
                        print("Starting Server !")
                        handler = http.server.SimpleHTTPRequestHandler
                        if I != "" or not I.isspace():
                            port = int(I[1])
                        else: port = 8080

                        httpd = socketserver.TCPServer(("", port), handler)
                        print(f"{colours.OKCYAN}Serving on port {port}{colours.ENDC}")
                        print(f"{colours.OKGREEN}Website : http://localhost:{port}{colours.GREY}")

                        try:
                            threading.Thread(target=httpd.serve_forever).start()
                        except KeyboardInterrupt:
                            print("Stopping !")
                    except:
                        print(f"Error: command \"{I[0]}\" takes one argument 0 given")
                elif I == "proxy" or I == "proxy".capitalize():
                    print("\n"+colours.HEADER+"Wich proxy would you want ?"+colours.ENDC+"\n")
                    print(colours.MAGENTA+"LList : "+colours.ENDC)
                    for i in proxies: print(colours.OKBLUE+"    "+i+colours.ENDC)
                    print(colours.OKCYAN+"\nANO1 : Anonym\nANO2 : Anonym 2\nGET : Get current using proxy\nNone : Use no proxy\n"+colours.ENDC)
                    proxy = input(colours.OKGREEN+"Proxy Name -> "+colours.ENDC)
                    if proxy == "GET" or proxy == "get":
                        config.read("config.toml")
                        if not config.has_option("settings.options","proxy"):
                            config.set("settings.options","proxy","None")
                            with open("config.toml","w") as f:
                                config.write(f)
                        if config.get("settings.options","proxy") != "None": print("\n"+colours.OKGREEN+"Current Proxy : "+config.get("settings.options","proxy")+colours.ENDC+"\n"); continue
                        else:
                            print("\n"+colours.OKCYAN+"No proxy is being used"+colours.ENDC+"\n")
                            continue
                    if proxy == "US" or proxy == "EU" or proxy == "VIETNAM" or proxy == "V" or proxy == "ANO1" or proxy == "ANO2" or proxy == "None":
                        print("\n"+colours.OKGREEN+"Saving %s to config.toml\n" % proxy+colours.ENDC)
                        if not config.has_section("settings.options"): config.add_section("settings.options")
                        config.set("settings.options","proxy",proxy)
                        with open("config.toml","w") as f:
                            config.write(f)
                    else:
                        print("\n"+colours.WARNING+"Please write one from this list !\n"+colours.ENDC)
                elif "proxy" in I:
                    I = I.split(" ")
                    try:
                        proxy = I[1]
                        if proxy == "list" or proxy == "list".capitalize():
                            print("\n"+colours.MAGENTA+"LList : "+colours.ENDC)
                            for i in proxies: print(colours.OKBLUE+"    "+i+colours.ENDC)
                            print(colours.OKCYAN+"\nANO1 : Anonym\nANO2 : Anonym 2\nGET : Get current using proxy\nNone : Use no proxy\n"+colours.ENDC)
                            continue
                        if proxy == "GET" or proxy == "get":
                            config.read("config.toml")
                            if config.get("settings.options","proxy") != "None": print("\n"+colours.OKBLUE+"Current Proxy : "+config.get("settings.options","proxy")+colours.ENDC+"\n"); continue
                            else:
                                print("\n"+colours.OKBLUE+"No proxy is being used"+colours.ENDC+"\n")
                                continue
                        if proxy == "US" or proxy == "EU" or proxy == "VIETNAM" or proxy == "V" or proxy == "ANO1" or proxy == "ANO2" or proxy == "None" or proxy == "none".capitalize():
                            print("\n"+colours.OKGREEN+"Saving %s to config.toml\n" % proxy+colours.ENDC)
                            if not config.has_section("settings.options"): config.add_section("settings.options")
                            config.set("settings.options","proxy",proxy)
                            with open("config.toml","w") as f:
                                config.write(f)
                    except:
                        print("Error: command takes arguments 0 given")
                elif I == "iwshow" or I == "iwconfig" or I == "iwshow".capitalize():
                    print()
                    if config.has_option("settings.options","proxy"):
                        if config.get("settings.options","proxy") != "None":
                            print(colours.HEADER+"You are using the proxy : "+config.get("settings.options","proxy")+"\n"+colours.WARNING+"Note: Using Proxies the connection isnt stable and can be interrupted !"+colours.ENDC)
                            try:
                                response = requests.get("https://ipinfo.io/json",proxies=proxies[config.get("settings.options","proxy")])
                            except requests.exceptions.ConnectTimeout:
                                print(colours.FAIL+"Error: Connection is timed out please try not using a proxy"+colours.ENDC+"\n")
                                continue
                            except Exception as E:
                                print(colours.FAIL+"Error: "+E+colours.ENDC)
                                continue
                        else:
                            response = requests.get("https://ipinfo.io/json")
                    else:
                        response = requests.get("https://ipinfo.io/json")
                    print(colours.WARNING+"These informations can websites see:"+colours.ENDC+"\n")
                    print(response.text+"\n")
                elif I == "engine" or I == "engine".capitalize():
                    engine.start_engine()
                elif "engine" in I:
                    I = I.split(" ")
                    try:
                        if os.path.exists(I[1]):
                            engine.start_engine(I[1])
                        else:
                            print()
                            print(colours.FAIL+"Engine Error: No path found '"fr"{I[1]}"+"'"+colours.ENDC)
                            print()
                    except: print(colours.WARNING+"Engine Error: command takes one argument but 0 given"+colours.ENDC)
                elif I == "database":
                    self.database_mode()
                elif "dw" in I:
                    I = I.split(" ")
                    try:
                        I[1]
                        Name = input("Name for the file? : ")
                        wget.download(url=I[1],out=Name)
                        print()
                    except: print("\n"+colours.FAIL+"Error: command takes one argument 0 given"+colours.ENDC)
                    print()
                elif "gcw" in I:
                    print()
                    I = I.split(" ")
                    try: os.system("netsh wlan show profile %s key=clear" % I[1])
                    except: print(colours.FAIL+"Error: command takes one argument 0 given"+colours.ENDC)
                    print()
                elif I == "" or I.isspace():
                    print()
                elif I == "ls" or I == "list":
                    print()
                    os.system("dir")
                    print()
                elif I == "clear":
                    os.system("clear" if os.name == "posix" else "cls")
                elif "pt" in I:
                    I = I.split(" ")
                    try:
                        if not I[1] == "default" or not I[1] == "df" and not I[1].isspace() and not I[1] == "":
                            config.set("settings.options","pt_text",I[1])
                            with open("config.toml","w") as f:
                                config.write(f)
                        elif I[1] == "default" or I[1] == "df" or I[1] == "" or I[1].isspace():
                            config.set("settings.options","pt_text","Terminal")
                            with open("config.toml","w") as f:
                                config.write(f)
                    except: print(colours.FAIL+"Error: command takes one argument 0 given"+colours.ENDC)
                elif I == "show-profiles":
                    os.system("netsh wlan show profile")
                elif I == "exit":
                    on_exit()
                else:
                    print()
                    os.system(I)
                    print()
        elif config["settings.menu"]["gui"] == "True":
            print("gui")

    def load_cmd(self):
        for i in trange(100,ncols=50):
            if i == 0: threading.Thread(target=self.terminal).start(); done = True
            if done == True:
                time.sleep(0)

if __name__ == "__main__":
    os.system("title UTILS")
    sys.argv.pop(0)
    print()
    txt = "Argument : " if len(sys.argv) < 2 else "Arguments : "
    print(txt+str(sys.argv) if len(sys.argv) > 0 else colours.HEADER+"No Arguments"+colours.ENDC)
    print()
    if len(sys.argv) > 0:
        if sys.argv[0] == "help" or sys.argv[0] == "Help" or sys.argv[0] == "help".capitalize() or sys.argv[0] == "--help":
            print(colours.HEADER+"Usage of utils with arguments:"+colours.ENDC)
            print(colours.WARNING+" Options:"+colours.ENDC)
            
            print(colours.OKGREEN+"     help                Shows this")
            print("     database            Goes direct into database mode")
            print("     gcw <WLAN SSID>     Shows if saved the wifi password")
            print("     show-profiles       Show all saved wifi")
            print("     engine              Starts the 3D engine")
            print("     wsl                 launches wsl if you have it")
            print("     host-l              Host directly a TCP server")
            print("     host-w              Host a server that anyone can acces !")
            print("     web-host            Host a website localy and edit it !")
            print(colours.ENDC)
        elif sys.argv[0] == "web-host" or sys.argv[0] == "web-host" or sys.argv[0] == "web-host".capitalize() or sys.argv[0] == "--web-host" or sys.argv[0] == "--TCP-Web-Server" or sys.argv[0] == "--TCP-Server-Web" or sys.argv[0] == "--TCP-webserver" or sys.argv[0] == "--TCP-Webserver":
            host_web()
        elif sys.argv[0] == "host-w" or sys.argv[0] == "Host-w" or sys.argv[0] == "host-w".capitalize() or sys.argv[0] == "--host-w" or sys.argv[0] == "--TCP-Server-w":
            if os.path.exists("ngrok.exe"):
                if not os.path.exists(os.getenv("LOCALAPPDATA")+"\\ngrok\\ngrok.yml"):
                    print("How to get the ngrok token : https://ngrok.com/docs/agent/#authtokens")
                    I = input("Auth-Token -> ")
                    if I == "" or I.isspace():
                        print("The token cannot be empty !")
                        os.system("pause")
                        exit(1)
                    os.system(f"ngrok config add-authtoken {I}")
                port = input("Port -> ")
                try:
                    port = int(port)
                except:
                    print(colours.FAIL+"Error: port should be numeric with 4 digits or more"+colours.ENDC)
                handler = http.server.SimpleHTTPRequestHandler
                httpd = socketserver.TCPServer(("", port), handler)
                print(f"Serving on port {port}")
                print(f"Website : http://localhost:{port}")

                try:
                    threading.Thread(target=httpd.serve_forever).start()
                    
                except KeyboardInterrupt:
                    
                    print("Stopping !")
                os.system(f"start ngrok tcp {port}")
            else:
                print(f"Error: Please install ngrok file in this directory \"{str(os.getcwd())}\" !")
        elif sys.argv[0] == "host-l" or sys.argv[0] == "Host-l" or sys.argv[0] == "host-l".capitalize() or sys.argv[0] == "--host-l" or sys.argv[0] == "--TCP-Server":
            try:
                sys.argv[1]
            except:
                sys.argv.append(str(8080))
            try:
                if sys.argv[1] != "" and not sys.argv[1].isspace():
                    print("Starting Server !")
                    handler = http.server.SimpleHTTPRequestHandler
                    if sys.argv[1] != "" and not sys.argv[1].isspace():
                        port = int(sys.argv[1])
                    else: port = 8080

                    httpd = socketserver.TCPServer(("", port), handler)
                    print(f"Serving on port {port}")
                    print(f"Website : http://localhost:{port}")
                    try:
                        httpd.serve_forever()
                    except KeyboardInterrupt:
                        
                        print("Stopping !")
            except:
                print(f"Error: command \"{sys.argv[0]}\" takes one argument 0 given !")
                os.system("pause > nul")
        elif sys.argv[0] == "wsl" or sys.argv[0] == "Wsl" or sys.argv[0] == "wsl".capitalize() or sys.argv[0] == "--wsl" or sys.argv[0] == "--launch":
            print(os.system("wsl"))
        elif sys.argv[0] == "engine" or sys.argv[0] == "Engine" or sys.argv[0] == "engine".capitalize() or sys.argv[0] == "--engine":
            try:
                engine.start_engine(sys.argv[1])
            except:
                engine.start_engine()
        elif sys.argv[0] == "database" or sys.argv[0] == "Database" or sys.argv[0] == "database".capitalize() or sys.argv[0] == "--database":
            App().database_mode()
        elif sys.argv[0] == "gcw" or sys.argv[0] == "--gcw" or sys.argv[0] == "gcw".capitalize() and len(sys.argv) >= 1:
            print()
            try: os.system("netsh wlan show profile %s key=clear" % sys.argv[1])
            except: print(colours.FAIL+"Error: command takes one argument 0 given"+colours.ENDC)
            print()
        elif sys.argv[0] == "show-profiles" or sys.argv[0] == "Show-profiles" or sys.argv[0] == "show-profiles".capitalize() or sys.argv[0] == "--show-profiles" or sys.argv[0] == "show-profile":
            print()
            os.system("netsh wlan show profile")
        exit(0)
    print(colours.OKCYAN+"\n### UTILS ###\n"+colours.ENDC)
    print(colours.OKBLUE+"Python Version: "+ver+"."+ver_2+colours.ENDC+"\n")

    print(colours.OKGREEN+"Launching."+colours.ENDC if float(ver+"."+ver_2) > 3.10 else colours.FAIL+"Please use python version 3.10 or later"+colours.ENDC)

    if not float(ver+"."+ver_2) < 3.11:
        RESUME = True
    else:
        RESUME = False

    if RESUME == True:
        if os.path.exists("config.toml"): 
            config.read("config.toml")
            print("\n"+colours.OKCYAN+"Preparing Terminal"+colours.ENDC)
            App().load_cmd()
        if not os.path.exists("config.toml"): App().load_start(); App().terminal()
