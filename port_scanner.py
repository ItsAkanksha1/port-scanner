import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import tkinter as tk
from tkinter import messagebox

open_ports = []
scan_in_progress = False

# Function to scan a single port
def scan_port(target, port, executor):
    global scan_in_progress
    if not scan_in_progress:  # If scan is canceled, stop execution
        return
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
    except Exception as e:
        pass
    finally:
        sock.close()

# Function to scan all ports in range
def scan_ports(target, start_port, end_port, filter_ports):
    global scan_in_progress
    open_ports.clear()
    scan_result_text.delete(1.0, tk.END)  # Clear previous scan results

    # GUI Updates: Updating status
    scan_result_text.insert(tk.END, f"Scanning {target}...\n")
    scan_result_text.insert(tk.END, f"Scanning ports {start_port} to {end_port}...\n")
    scan_result_text.insert(tk.END, f"Please wait...\n")
    scan_button.config(state=tk.DISABLED)  # Disable the scan button while scanning

    start_time = datetime.now()
    scan_in_progress = True  # Set scan as in progress

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            # Apply filtering
            if filter_ports and port not in filter_ports:
                continue
            executor.submit(scan_port, target, port, executor)

    end_time = datetime.now()
    scan_result_text.insert(tk.END, f"\nScanning completed in: {end_time - start_time}\n")

    if open_ports:
        for port in open_ports:
            scan_result_text.insert(tk.END, f"[+] Port {port} is open\n")
    else:
        scan_result_text.insert(tk.END, "No open ports found.\n")

    # Save results to file
    with open("scan_results.txt", "w") as file:
        file.write(f"Scan results for {target} (ports {start_port}-{end_port}):\n")
        if open_ports:
            for port in open_ports:
                file.write(f"Port {port} is open\n")
        else:
            file.write("No open ports found.\n")
    messagebox.showinfo("Scan Complete", "Results saved to scan_results.txt")

    # Re-enable scan button
    scan_button.config(state=tk.NORMAL)
    scan_in_progress = False  # Scan finished

# Function to start the scanning when the button is pressed
def start_scan():
    target = target_entry.get()
    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
        if start_port > end_port:
            raise ValueError("Start port cannot be greater than end port.")
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid port range: {e}")
        return

    # Get filter ports
    filter_ports = []
    if filter_ports_entry.get():
        filter_ports = list(map(int, filter_ports_entry.get().split(',')))

    scan_ports(target, start_port, end_port, filter_ports)

# Function to cancel the scan
def cancel_scan():
    global scan_in_progress
    scan_in_progress = False
    scan_button.config(state=tk.NORMAL)
    messagebox.showinfo("Scan Canceled", "The scan has been canceled.")

# Setting up the main GUI window
root = tk.Tk()
root.title("Port Scanner")

# Create and place the components (labels, entry fields, button, and text box)
tk.Label(root, text="Target IP Address:").pack(pady=5)
target_entry = tk.Entry(root, width=30)
target_entry.pack(pady=5)

tk.Label(root, text="Start Port:").pack(pady=5)
start_port_entry = tk.Entry(root, width=30)
start_port_entry.pack(pady=5)

tk.Label(root, text="End Port:").pack(pady=5)
end_port_entry = tk.Entry(root, width=30)
end_port_entry.pack(pady=5)

tk.Label(root, text="Filter Ports (comma-separated, e.g., 80,443):").pack(pady=5)
filter_ports_entry = tk.Entry(root, width=30)
filter_ports_entry.pack(pady=5)

scan_button = tk.Button(root, text="Start Scan", command=start_scan)
scan_button.pack(pady=10)

cancel_button = tk.Button(root, text="Cancel Scan", command=cancel_scan)
cancel_button.pack(pady=5)

scan_result_text = tk.Text(root, height=15, width=50)
scan_result_text.pack(pady=10)

# Start the GUI event loop
root.mainloop()
