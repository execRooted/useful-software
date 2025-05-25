import getpass
import socket
import platform
import psutil
import datetime
import sys
import time
import os
import subprocess
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, Center
from textual.widgets import Header, Footer, Static, Button
from textual.reactive import reactive

os.system("title ctrl_app - by execRooted")


class DailyTools(Static):
    time = reactive("")
    date = reactive("")
    battery = reactive("Unavailable")
    username = reactive("")
    hostname = reactive("")
    uptime = reactive("")
    timezone = reactive("")
    python_version = reactive("")
    os_info = reactive("")
    ip_addresses = reactive("")
    cpu_info = reactive("")
    memory_info = reactive("")
    disk_info = reactive("")

    def on_mount(self) -> None:
        self.username = getpass.getuser()
        self.hostname = socket.gethostname()
        self.python_version = sys.version.split()[0]  # e.g. '3.10.8'
        self.os_info = f"{platform.system()} {platform.release()} ({platform.machine()})"
        self.cpu_info = self.get_cpu_info()
        self.set_interval(1.0, self.update_info)
        self.update_info()

    def update_info(self) -> None:
        now = datetime.datetime.now()
        self.time = now.strftime("%H:%M:%S")
        self.date = now.strftime("%A, %d %B %Y")

        battery_info = psutil.sensors_battery()
        if battery_info:
            self.battery = f"{battery_info.percent}% {'(Charging)' if battery_info.power_plugged else ''}"
        else:
            self.battery = "Unavailable"

        boot_time = psutil.boot_time()
        uptime_seconds = time.time() - boot_time
        self.uptime = self.format_uptime(uptime_seconds)

        self.timezone = time.tzname[time.daylight]

        self.ip_addresses = self.get_ip_addresses()

        mem = psutil.virtual_memory()
        self.memory_info = f"{mem.used // (1024 ** 2)} MB / {mem.total // (1024 ** 2)} MB ({mem.percent}%)"

        disk = psutil.disk_usage('/')
        self.disk_info = f"{disk.free // (1024 ** 3)} GB free / {disk.total // (1024 ** 3)} GB total"

        self.refresh()

    def get_cpu_info(self) -> str:
        try:
            if platform.system() == "Windows":
                return platform.processor()
            elif platform.system() == "Darwin":
                import subprocess
                cmd = ["sysctl", "-n", "machdep.cpu.brand_string"]
                cpu = subprocess.check_output(cmd).decode().strip()
                return cpu
            else:
                with open("/proc/cpuinfo") as f:
                    for line in f:
                        if "model name" in line:
                            return line.strip().split(":")[1].strip()
        except Exception:
            return "Unknown CPU"
        return "Unknown CPU"

    def get_ip_addresses(self) -> str:
        addrs = psutil.net_if_addrs()
        interfaces = []
        for iface, addr_list in addrs.items():
            for addr in addr_list:
                if addr.family == socket.AF_INET and not addr.address.startswith("127.") and not "vEthernet" in iface:
                    # Show only Hamachi or custom interfaces, not Ethernet or Wi-Fi
                    if "hamachi" in iface.lower():  # Hamachi
                        interfaces.append(f"Hamachi: {addr.address}")
                    elif "tun" in iface.lower():  # VPN, tunneling interfaces
                        interfaces.append(f"VPN: {addr.address}")
                    elif "vpn" in iface.lower():  # Generic VPN interface
                        interfaces.append(f"VPN: {addr.address}")
                    # Add any other custom interface names you want to check here
                    break  # We just need one address per interface

        return ", ".join(interfaces) if interfaces else "No active custom connection"

    def format_uptime(self, seconds: float) -> str:
        days, remainder = divmod(int(seconds), 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, _ = divmod(remainder, 60)
        parts = []
        if days > 0:
            parts.append(f"{days}d")
        if hours > 0 or days > 0:
            parts.append(f"{hours}h")
        parts.append(f"{minutes}m")
        return " ".join(parts)

    def render(self) -> str:
        return (
            f"[bold cyan]:: DAILY TOOLS ::[/bold cyan]\n"
            f"[green]Time[/green]: {self.time}\n"
            f"[green]Date[/green]: {self.date}\n"
            f"[green]Battery[/green]: {self.battery}\n\n"
            f"[yellow]User[/yellow]: {self.username}\n"
            f"[yellow]Host[/yellow]: {self.hostname}\n"
            f"[yellow]Uptime[/yellow]: {self.uptime}\n"
            f"[yellow]Timezone[/yellow]: {self.timezone}\n"
            f"[yellow]Python[/yellow]: {self.python_version}\n"
            f"[yellow]OS[/yellow]: {self.os_info}\n"
            f"[yellow]CPU[/yellow]: {self.cpu_info}\n"
            f"[yellow]Memory[/yellow]: {self.memory_info}\n"
            f"[yellow]Disk[/yellow]: {self.disk_info}\n"
            f"[yellow]Interface IPs[/yellow]: {self.ip_addresses}\n"
        )


class SystemMonitor(Static):
    cpu_usage = reactive(0.0)
    memory_usage = reactive(0.0)
    disk_usage = reactive(0.0)
    disk_total = reactive(0.0)
    disk_used = reactive(0.0)
    boot_time = reactive("")

    def on_mount(self) -> None:
        self.set_interval(1.0, self.update_metrics)

    def update_metrics(self) -> None:
        self.cpu_usage = psutil.cpu_percent(interval=None)
        mem = psutil.virtual_memory()
        self.memory_usage = mem.percent
        disk = psutil.disk_usage('/')
        self.disk_usage = disk.percent
        self.disk_total = disk.total / (1024 ** 3)
        self.disk_used = disk.used / (1024 ** 3)
        self.boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        self.refresh()

    def render(self) -> str:
        return (
            f"[bold cyan]:: SYSTEM MONITORING ::[/bold cyan]\n"
            f"[green]OS[/green]: {platform.system()} {platform.release()}\n"
            f"[green]CPU[/green]: {self.cpu_usage:.1f}%\n"
            f"[green]Memory[/green]: {self.memory_usage:.1f}%\n"
            f"[green]Disk[/green]: {self.disk_usage:.1f}% "
            f"({self.disk_used:.1f} GB / {self.disk_total:.1f} GB)\n"
            f"[green]Boot[/green]: {self.boot_time}\n"
        )


class NetworkMonitor(Static):
    upload_kbps = reactive(0.0)
    download_kbps = reactive(0.0)
    ip_address = reactive("N/A")

    def on_mount(self) -> None:
        self.update_ip_address()
        self._prev = psutil.net_io_counters()
        self.set_interval(1.0, self.update_metrics)

    def update_ip_address(self) -> None:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            self.ip_address = s.getsockname()[0]
            s.close()
        except Exception:
            self.ip_address = "Unavailable"

    def update_metrics(self) -> None:
        now = psutil.net_io_counters()
        delta_sent = now.bytes_sent - self._prev.bytes_sent
        delta_recv = now.bytes_recv - self._prev.bytes_recv
        self.upload_kbps = delta_sent / 1024  # KB/s
        self.download_kbps = delta_recv / 1024
        self._prev = now
        self.refresh()

    def render(self) -> str:
        return (
            f"[bold cyan]:: NETWORK MONITORING ::[/bold cyan]\n"
            f"[green]Network IP[/green]: {self.ip_address}\n"
            f"[green]Upload current[/green]: {self.upload_kbps:.1f} KB/s\n"
            f"[green]Download current[/green]: {self.download_kbps:.1f} KB/s\n"
        )


class ControlPanel(Static):
    def compose(self) -> ComposeResult:
        yield Button("Refresh Metrics", id="refresh", variant="default")
        yield Button("Shutdown System", id="shutdown", variant="error")
        yield Button("Restart System", id="restart", variant="warning")
        yield Button("Reset Network", id="reset_network", variant="warning")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        app = self.app
        system_monitor = app.query_one(SystemMonitor)
        network_monitor = app.query_one(NetworkMonitor)

        self.screen.set_focus(None)  

        match event.button.id:
            case "refresh":
                system_monitor.update_metrics()
                network_monitor.update_metrics()
                network_monitor.update_ip_address()

            case "shutdown":
                app.exit("Shutting down...")
                os.system("shutdown /s /t 1" if sys.platform == "win32" else "shutdown now")

            case "restart":
                app.exit("Restarting...")
                os.system("shutdown /r /t 1" if sys.platform == "win32" else "reboot")

            case "reset_network":
                os.system("cls" if sys.platform == "win32" else "clear")
                if sys.platform == "win32":
                    os.system("ipconfig /release && ipconfig /renew")
                else:
                    os.system("sudo systemctl restart NetworkManager.service")
                os.system("cls" if sys.platform == "win32" else "clear")
                network_monitor.update_metrics()
                network_monitor.update_ip_address()
           

class ctrl_app(App):
    BINDINGS = [("q", "quit", "Exit")]

    CSS = """
    Screen {
        background: #000000;
        color: #00ffcc;
        layout: vertical;
        padding: 1 2;
    }

    Header, Footer {
        background: #001122;
        color: #00ffff;
        text-style: bold;
    }

    Horizontal {
        padding: 1;
        align-horizontal: center;
        align-vertical: middle;
    }

    Static {
        border: round #00ffff;
        padding: 1;
        background: #101010;
        color: #00ffcc;
        width: 100%;
        min-width: 32;
    }

    Button {
        background: #002233;
        color: #00ffff;
        border: round #00ffff;
        margin: 1 0;
        width: 100%;
    }

    Button:hover {
        background: #003344;
    }

    Button:focus {
        background: #002233;
        text-style: none;
    }

    #left-column, #right-column {
        width: 35%;
    }

    #center-column {
        width: 30%;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Center(
            Horizontal(
                Vertical(
                    DailyTools(),
                    id="left-column"
                ),
                Vertical(
                    SystemMonitor(),
                    NetworkMonitor(),
                    id="center-column"
                ),
                Vertical(
                    ControlPanel(),
                    id="right-column"
                )
            )
        )
        yield Footer()


if __name__ == "__main__":
    ctrl_app().run()
