#!/usr/bin/env python3
"""
Bibisi Launcher - Launches fake missiles in dots
Renders animated missile launches with ASCII art using dots
"""

import time
import os
import sys

class MissileLauncher:
    def __init__(self):
        self.width = 80
        self.height = 20
        
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_ground(self):
        """Print ground line"""
        print("=" * self.width)
    
    def launch_missile(self, x_start, launch_height=5):
        """Launch a single missile from x_start position"""
        print(f"\n[LAUNCHING MISSILE FROM POSITION {x_start}]")
        
        # Ascent phase
        for height in range(launch_height):
            self.clear_screen()
            print()
            print(" " * self.width)
            
            # Draw missile trail with dots
            for h in range(height + 1):
                line = " " * (x_start) + "." * 5
                if h < height:
                    print(line)
                else:
                    print(line + " <- MISSILE")
            
            # Draw ground
            print()
            print("." * self.width)
            print(f"Height: {height * 10}m | Position: {x_start}")
            time.sleep(0.2)
        
        # Apex
        self.clear_screen()
        print("\n[MISSILE AT APEX]\n")
        apex_line = " " * x_start + "o" + " <- EXPLODING"
        print(apex_line)
        time.sleep(0.3)
        
        # Explosion with dots
        print("\n[DETONATION SEQUENCE]\n")
        for explosion_size in range(1, 6):
            self.clear_screen()
            print()
            explosion = "." * (explosion_size * 2)
            print(" " * (x_start - explosion_size) + explosion)
            print()
            print("." * self.width)
            time.sleep(0.15)
    
    def launch_missile_swarm(self, count=3):
        """Launch multiple missiles in sequence"""
        positions = [10, 40, 70]
        
        print("\n" + "="*self.width)
        print("BIBISI MISSILE LAUNCHER SYSTEM ACTIVATED")
        print("="*self.width)
        time.sleep(1)
        
        for i in range(min(count, len(positions))):
            self.launch_missile(positions[i], launch_height=6)
            print(f"\nMissile {i+1}/{count} detonated successfully!")
            time.sleep(0.5)
        
        # Final status
        self.clear_screen()
        print("\n" + "="*self.width)
        print("ALL MISSILES LAUNCHED AND DETONATED")
        print("BIBISI LAUNCHER STANDING BY")
        print("="*self.width)
    
    def animated_launch_sequence(self):
        """Full animated launch sequence"""
        self.clear_screen()
        
        # Opening sequence
        print("\n" + "." * self.width)
        print("|" + " " * (self.width - 2) + "|")
        print("|" + " " * (self.width - 2) + "|")
        print("|" + " BIBISI LAUNCHER READY ".center(self.width - 2) + "|")
        print("|" + " " * (self.width - 2) + "|")
        print("|" + " " * (self.width - 2) + "|")
        print("." * self.width)
        
        time.sleep(1)
        
        print("\nInitializing missile array...")
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.3)
        print(" READY!\n")
        
        time.sleep(0.5)
        
        # Launch swarm
        self.launch_missile_swarm(count=3)

def main():
    """Main launcher function"""
    launcher = MissileLauncher()
    
    try:
        launcher.animated_launch_sequence()
        
        print("\n\nPress Enter to launch another sequence or Ctrl+C to exit...")
        input()
        main()
        
    except KeyboardInterrupt:
        print("\n\nBibisi Launcher powered down. Missiles secured.")
        sys.exit(0)

if __name__ == "__main__":
    main()
