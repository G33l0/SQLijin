import time
import os
import requests
import pyfiglet
from datetime import datetime
from googlesearch import search
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.live import Live

# Initialize Rich Console
console = Console()

# --- CONFIGURATION ---
VERSION = "v2.1"
MAKER = "https://t.me/x0x0h33l0"
TARGET_SCOPE = "*.example.com"  # <--- Change this
DORKS_FILE = "dorks.txt"
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:115.0) Gecko/20100101 Firefox/115.0'}
SQL_ERRORS = ["sql syntax", "mysql_fetch", "ora-01756", "sqlite3", "sqlclient", "postgresql query"]

def print_banner():
    # Generate Red Hacker Banner
    banner_text = pyfiglet.figlet_format("SQLijin", font="slant")
    console.print(f"[bold red]{banner_text}[/bold red]")
    
    # Meta Info Panel
    info = f"[bold white]Version:[/bold white] [cyan]{VERSION}[/cyan]\n" \
           f"[bold white]Maker:[/bold white] [blue]{MAKER}[/blue]\n\n" \
           f"[bold yellow]DISCLAIMER:[/bold yellow]\n" \
           f"This tool is for [bold green]EDUCATIONAL AND AUTHORIZED USE ONLY[/bold green].\n" \
           f"The maker is [bold red]NOT responsible[/bold red] for any misuse or damage caused.\n" \
           f"Always ensure you have written permission before testing any target."
    
    console.print(Panel(info, title="[bold red]System Terminal[/bold red]", border_style="red"))

def get_timestamp():
    return datetime.now().strftime("%H:%M:%S")

def check_vulnerability(url):
    try:
        fuzzed_url = url + "'"
        r = requests.get(fuzzed_url, timeout=7, headers=HEADERS, verify=False)
        for error in SQL_ERRORS:
            if error in r.text.lower():
                return True, error
        return False, None
    except:
        return False, None

def scanner():
    print_banner()
    
    if not os.path.exists(DORKS_FILE):
        console.print(f"[{get_timestamp()}] [bold red]ERROR:[/bold red] {DORKS_FILE} not found!")
        return

    with open(DORKS_FILE, 'r') as f:
        dorks = [line.strip() for line in f if line.strip()]

    # Tracking table for the interactive CLI
    results_table = Table(title=f"Discovered Vulnerabilities on {TARGET_SCOPE}", title_style="bold magenta")
    results_table.add_column("Timestamp", style="dim")
    results_table.add_column("Type", style="bold")
    results_table.add_column("Target URL", no_wrap=False)
    results_table.add_column("Detail", style="italic")

    # Interactive Progress Setup
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=40),
        TaskProgressColumn(),
        console=console
    ) as progress:
        
        main_task = progress.add_task("[cyan]Processing Dorks...", total=len(dorks))
        
        for dork in dorks:
            query = f"site:{TARGET_SCOPE} inurl:{dork}"
            progress.update(main_task, description=f"[yellow]Searching: {dork}")
            
            try:
                # Limit results per dork for speed in demo; increase for real use
                for url in search(query, num=5, stop=5, pause=3.0):
                    is_vuln, error_msg = check_vulnerability(url)
                    
                    if is_vuln:
                        console.print(f"[{get_timestamp()}] [bold red]!!! SQLi DETECTED:[/bold red] {url}")
                        results_table.add_row(get_timestamp(), "[red]CRITICAL[/red]", url, f"SQL Leak: {error_msg}")
                    else:
                        console.print(f"[{get_timestamp()}] [bold blue]INFO:[/bold blue] Found surface: {url}")
                
                progress.advance(main_task)
            except Exception as e:
                console.print(f"[{get_timestamp()}] [bold red]THROTTLED:[/bold red] Google cooling down...")
                time.sleep(20)

    # Final Summary Display
    console.print("\n", results_table)
    console.print(f"\n[bold green][*] Scan Complete. Final results displayed above.[/bold green]")

if _name_ == "_main_":
    scanner()