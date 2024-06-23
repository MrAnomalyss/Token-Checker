import pystyle
from pystyle import Write, Colors
import requests
import raducord
from raducord import Logger
import ctypes
import time
import asyncio


tittle ="""
    \t\t\t████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
    \t\t\t╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
    \t\t\t   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║
    \t\t\t   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║
    \t\t\t   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║
    \t\t\t   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
    \t\t\t============================================                                          
    """
Write.Print(tittle, Colors.blue_to_red, interval=0.000)
def main():
    with open('tokens.txt', 'r') as file:
        tokens = file.readlines()

    tokens = [token.strip() for token in tokens]

    valid_tokens = 0  
    fail_tokens = 0
    
    


    for token in tokens:
        headers = {"Authorization": token}
        response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
        
            

        
        if response.status_code == 200:
            valid_tokens += 1
            Logger.success(f'Success,Token valid,{valid_tokens}')
            with open('results.txt', 'a') as f:
                    f.write(token + "\n")
        else:
            fail_tokens += 1
            Logger.failed(f'Error,Token invalid,{fail_tokens}')
            ctypes.windll.kernel32.SetConsoleTitleW(f'𝓥𝓪𝓵𝓲𝓭 𝓣𝓸𝓴𝓮𝓷𝓼:{valid_tokens}   𝓕𝓪𝓲𝓵 𝓣𝓸𝓴𝓮𝓷𝓼:{fail_tokens}   𝓭𝓲𝓼𝓬𝓸𝓻𝓭.𝓰𝓰/𝓡𝓨4𝓶𝓐𝓔𝔁𝓻𝓳𝓿')
        

    

if __name__ == '__main__':
    
    main()
    enter = input('Press Enter to Exit...')