from argparse import ArgumentParser
from subprocess import run
from json import loads



import subprocess
import sys

def run_command(command):
    """Run a shell command and return the output."""
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return result.decode().strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e.output.decode()}")
        return None

def win_prop(option):
    """Replicate the win_prop function to get window properties."""
    BSPC_WIN_INFO=run(["bspc query -T -n focused"], text=True, capture_output=True, shell=True)
    WIN_GEO=dict(loads(BSPC_WIN_INFO.stdout)).get("rectangle")
    x, y, width, height=(WIN_GEO["x"], WIN_GEO["y"], WIN_GEO["width"], WIN_GEO["height"])
    return (x, y, width, height)

def handle_verbose(*args):
    """Handle verbose output."""
    print(" ".join(args))

def handle_mode():
    """Handle the mode option."""
    if run_command("bspc query -N -n focused.floating > /dev/null") is not None:
        run_command("bspc node -t tiled")
    else:
        run_command("bspc node -t floating")

def handle_focus(node):
    """Handle the focus option."""
    run_command(f"bspc node -f {node}")

def handle_move(direction, value):
    """Handle the move option."""
    if run_command("bspc query -N -n focused.floating > /dev/null") is not None:
        # Adjust movement for floating window
        if direction == "east":
            run_command(f"bspc node -v {value} 0")
        elif direction == "south":
            run_command(f"bspc node -v 0 {value}")
        elif direction == "north":
            run_command(f"bspc node -v 0 -{value}")
        elif direction == "west":
            run_command(f"bspc node -v -{value} 0")
    else:
        # Logic for tiled windows
        width = win_prop("-width")
        height = win_prop("-height")
        if width is not None and height is not None:
            if width <= height:
                # Adjust based on the width/height ratio
                if direction == "north":
                    if win_prop("-x") < 15:
                        run_command("bspc node @parent --rotate 90")
                    else:
                        run_command("bspc node @parent --rotate 270")
                elif direction == "south":
                    run_command("bspc node @parent --rotate 90")
                else:
                    run_command(f"bspc node -s {direction}")
            else:
                # Adjust for wide windows
                if direction == "east":
                    if win_prop("-y") < 45:
                        run_command("bspc node @parent --rotate 90")
                    else:
                        run_command("bspc node @parent --rotate 270")
                elif direction == "west":
                    if win_prop("-y") < 45:
                        run_command("bspc node @parent --rotate 270")
                    else:
                        run_command("bspc node @parent --rotate 90")
                else:
                    run_command(f"bspc node -s {direction}")

def handle_resize(direction, value):
    """Handle resizing."""
    if direction == "left":
        run_command(f"bspc node -z {direction} -{value} 0 || bspc node -z right -{value} 0")
    elif direction == "bottom":
        run_command(f"bspc node -z {direction} 0 {value} || bspc node -z top 0 {value}")
    elif direction == "top":
        run_command(f"bspc node -z {direction} 0 -{value} || bspc node -z bottom 0 -{value}")
    elif direction == "right":
        run_command(f"bspc node -z {direction} {value} 0 || bspc node -z left {value}")

def show_usage():
    """Print usage information."""
    print("No operation given!!")
    print("Usage: python toggle_window.py")
    print("  mode: toggle from tiled to floating window with one call")
    print("  move [east, north, south, west] [int]: moves the window in the given direction and interval when floating")
    print("  resize [left, right, bottom, top] [int]: resizes the window based on the given direction and interval")
    print("  focus [east, north, south, west]: focuses the window without disturbing the movement.")

def main():
    """Main function to handle command-line options."""
    if len(sys.argv) < 2:
        show_usage()
        return

    option = sys.argv[1]

    if option == "-verbose":
        handle_verbose(*sys.argv[1:])
    elif option == "--mode":
        handle_mode()
    elif option == "--focus" and len(sys.argv) > 2:
        handle_focus(sys.argv[2])
    elif option == "--move" and len(sys.argv) > 3:
        handle_move(sys.argv[2], sys.argv[3])
    elif option == "--resize" and len(sys.argv) > 3:
        handle_resize(sys.argv[2], sys.argv[3])
    else:
        show_usage()

if __name__ == "__main__":
    main()

