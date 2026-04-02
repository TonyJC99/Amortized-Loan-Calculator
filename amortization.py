# Requires pip
from tabulate import tabulate
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Does not require pip
import csv
import os

# Input Collection
def get_inputs():

    print("=" * 52)
    print("  LOAN AMORTIZATION SYSTEM / SISTEMA DE AMORTIZACIÓN")
    print("=" * 52 + "\n")

    while True:
        try:
            principal = float(input("Loan amount / Monto del préstamo: "))
            if principal > 0:
                break
            print("Must be greater than 0. / Debe ser mayor a 0.")
        except ValueError:
            print("Numeric value required. / Ingrese un valor numérico.")

    while True:
        try:
            annual_rate = float(input("Annual interest rate % / Tasa de interés anual % (ej: 5): "))
            if annual_rate >= 0:
                break
            print("Must be 0 or greater. / Debe ser 0 o mayor.")
        except ValueError:
            print("Numeric value required. / Ingrese un valor numérico.")

    while True:
        try:
            years = int(input("Loan term in years / Plazo en años: "))
            if years > 0:
                break
            print("Must be greater than 0. / Debe ser mayor a 0.")
        except ValueError:
            print("Whole number required. / Ingrese un número entero.")

    return principal, annual_rate, years


# Core Calculation
def calculate_schedule(principal, annual_rate, years):

    monthly_rate = (annual_rate / 100) / 12
    total_months = years * 12

    if annual_rate == 0:
        monthly_payment = principal / total_months
    else:
        monthly_payment = (
            principal
            * (monthly_rate * (1 + monthly_rate) ** total_months)
            / ((1 + monthly_rate) ** total_months - 1)
        )

    schedule = []
    balance = principal

    for month in range(1, total_months + 1):
        interest = balance * monthly_rate
        capital = monthly_payment - interest
        balance -= capital
        if balance < 0:
            balance = 0.0

        schedule.append({
            "month":    month,
            "payment":  monthly_payment,
            "interest": interest,
            "capital":  capital,
            "balance":  balance,
        })

    return schedule, monthly_payment


# Table Display
def display_table(schedule):

    rows = [
        [
            row["month"],
            f"${row['payment']:,.2f}",
            f"${row['interest']:,.2f}",
            f"${row['capital']:,.2f}",
            f"${row['balance']:,.2f}",
        ]
        for row in schedule
    ]

    headers = ["Month / Mes", "Payment / Cuota", "Interest / Interés", "Principal / Capital", "Balance / Saldo"]

    print("\n" + tabulate(rows, headers=headers, tablefmt="simple"))


# Summary Display
def display_summary(principal, annual_rate, years, monthly_payment, schedule):

    total_interest = sum(row["interest"] for row in schedule)
    total_cost = principal + total_interest

    print("\n" + "=" * 52)
    print("  LOAN SUMMARY / RESUMEN DEL PRÉSTAMO")
    print("=" * 52)
    print(f"  {'Principal:':<30} ${principal:,.2f}")
    print(f"  {'Annual Rate / Tasa Anual:':<30}  {annual_rate:.2f}%")
    print(f"  {'Term / Plazo:':<30}  {years} years/años")
    print(f"  {'Monthly Payment / Cuota:':<30} ${monthly_payment:,.2f}")
    print(f"  {'Total Interest / Interés:':<30} ${total_interest:,.2f}")
    print(f"  {'Total Cost / Costo Total:':<30} ${total_cost:,.2f}")
    print("=" * 52 + "\n")


# Chart
def plot_schedule(schedule, principal, annual_rate, years):

    months   = [row["month"]    for row in schedule]
    interest = [row["interest"] for row in schedule]
    capital  = [row["capital"]  for row in schedule]

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.stackplot(months, interest, capital,
                 labels=["Interest / Interés", "Principal / Capital"],
                 colors=["#e74c3c", "#2ecc71"], alpha=0.8)

    ax.set_title(f"Payment Breakdown / Desglose de Pagos\n"
                 f"${principal:,.2f} | {annual_rate}% | {years} years/años",
                 fontsize=13)
    ax.set_xlabel("Month / Mes")
    ax.set_ylabel("Amount / Monto ($)")
    ax.yaxis.set_major_formatter(mticker.StrMethodFormatter("${x:,.0f}"))
    ax.legend(loc="center right")
    ax.set_xlim(1, len(months))

    plt.tight_layout()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    plt.savefig(os.path.join(script_dir, "amortization_chart.png"), dpi=150)
    plt.show()
    print("  Chart saved as / Gráfico guardado como: amortization_chart.png\n")


# Export to CSV
def export_to_csv(schedule):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "amortization_schedule.csv")

    headers = ["month", "payment", "interest", "capital", "balance"]

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(schedule)
        print(f"  Data exported successfully to: {filename}")
    except IOError as e:
        print(f"  Error exporting to CSV: {e}")

if __name__ == "__main__":
    
    # Input
    principal, annual_rate, years = get_inputs()

    # Core Calculation
    schedule, monthly_payment = calculate_schedule(principal, annual_rate, years)

    # Display Information
    display_table(schedule)
    display_summary(principal, annual_rate, years, monthly_payment, schedule)

    # Optional Chart
    choice = input("Show chart? / ¿Mostrar gráfico? (y/n): ").strip().lower()
    if choice == 'y':
        plot_schedule(schedule, principal, annual_rate, years)

    # Optional Export to CSV
    choice = input("Export schedule to CSV? / ¿Exportar a CSV? (y/n): ").strip().lower()
    if choice == 'y':
        export_to_csv(schedule)
    else:
        print("Export skipped. Have a nice day! / Exportacion omitida. Que tenga un buen dia!")