
# Use

- The script has the following functionalities:

  - Use ***the -r option*** to generate a new valid random MAC in Linux format.
    
  - Use ***the -m option*** to specify the new MAC address you want to apply.
    
  - The script retrieves the current MAC address of the specified interface.
    
  - Change MAC address: The script modifies the MAC address of the chosen interface.
    
  - Clear cache (Linux): After changing the MAC, the script clears the DNS and ARP caches to avoid connectivity issues.

- Clone this repository and install the dependencies with the following command:

        git clone https://github.com/0x5FE/mac_adress_changer.git

- navigate to the folder

        cd mac-changer

- Run the script:

        python mac_changer.py -p linux <interface> [options]
  
- Replace ***<interface>*** with the name of the network interface you want to modify.


  # Possible Errors and Solutions

- ***Unsupported Platform*** If you try to use the script on an operating system other than Linux, you will receive a error. Currently, Windows support is still under development.
- ***Error: ModuleNotFoundError*** No module named 'argparse'
  Solution: Install the argparse package using pip install argparse.
  
- ***Subprocess.CalledProcessError*** Command 'macchanger' failed with exit status 1
  Solution: Check if the macchanger package is installed and accessible on your system. You can try to install the package using your operating system's package manager.

- ***Error: ValueError*** Please specify either -r or -m option
  Solution: You need to specify the -r option to generate a random address or the -m option to manually provide a new address.
  

# Future improvements

- [ ] Implement functionalities to change the MAC address on Windows systems.
- [ ] Create a graphical interface to facilitate the use of the script.
- [ ] Implement cleaning of DNS and ARP caches for Windows systems.
- [ ] Allow the generation of MACs with specific characteristics (e.g. prefix or suffix).
- [ ] Add validation to ensure that the MAC provided is a valid address in the correct format.

# Notice

- This script is intended for educational and research purposes.
  
- Changing the MAC address of your network interface may affect connectivity and violate terms of service for specific networks.
  
- Use this script responsibly and understand the possible impacts before using it.
