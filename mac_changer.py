import argparse
import subprocess
import random
import string
import re

def get_random_mac_address():
  uppercased_hexdigits = ''.join(set(string.hexdigits.upper()))
  mac = ""
  for i in range(6):
    for j in range(2):
      if i == 0:
        mac += random.choice("02468ACE")
      else:
        mac += random.choice(uppercased_hexdigits)
    mac += ":"
  return mac.strip(":")

def get_current_mac_address(platform, iface):
  """Get current MAC address based on platform."""
  if platform == "linux":
    output = subprocess.check_output(["ip", "addr", "show", iface]).decode()
    # Adapt regular expression for Linux output format
    return re.search(r"link/ether (.+?) ", output).group(1).strip()
  elif platform == "windows":
    # Implement Windows-specific MAC retrieval using PowerShell or WMI
    raise NotImplementedError("Windows support not yet implemented")
  else:
    raise ValueError(f"Unsupported platform: {platform}")

def change_mac_address(platform, iface, new_mac_address):
  """Change MAC address based on platform."""
  if platform == "linux":
    # Use macchanger if available
    try:
      subprocess.check_call(["macchanger", "-a", new_mac_address, iface])
    except subprocess.CalledProcessError:
      # Handle macchanger failure, try alternatives
      raise NotImplementedError("macchanger usage not implemented")
  elif platform == "windows":
    # Implement Windows-specific MAC change (may require admin privileges)
    raise NotImplementedError("Windows support not yet implemented")
  else:
    raise ValueError(f"Unsupported platform: {platform}")

def clear_cache(platform):
  if platform == "linux":
    # Limpar cache DNS
    subprocess.check_call(["sudo", "service", "dnsmasq", "restart"])
    # Limpar cache ARP
    subprocess.check_call(["sudo", "arp", "-d"])
  elif platform == "windows":
    # Implementar a limpeza de cache para Windows
    raise NotImplementedError("Windows support not yet implemented")
  else:
    raise ValueError(f"Unsupported platform: {platform}")

def main():
  parser = argparse.ArgumentParser(description="Python Mac Changer")
  parser.add_argument("-p", "--platform", choices=["linux", "windows"], required=True, help="Target platform")
  parser.add_argument("interface", help="The network interface name")
  parser.add_argument("-r", "--random", action="store_true", help="Whether to generate a random MAC address")
  parser.add_argument("-m", "--mac", help="The new MAC you want to change to")
  args = parser.parse_args()

  # Detect platform and handle accordingly
  platform = args.platform
  iface = args.interface

  if args.random:
    new_mac_address = get_random_mac_address()
  elif args.mac:
    new_mac_address = args.mac
  else:
    raise ValueError("Please specify either -r or -m option")

  # Retrieve current MAC address
  old_mac_address = get_current_mac_address(platform, iface)
  print(f"[*] Old MAC address: {old_mac_address}")

  # Change MAC address
  try:
    change_mac_address(platform, iface, new_mac_address)
  except NotImplementedError as e:
    print(f"Error: {e}")
    return

  clear_cache(platform)

  # Verify change
  new_mac_address = get_current_mac_address(platform, iface)
  print(f"[+] New MAC address: {new_mac_address}")

if __name__ == "__main__":
  main()
