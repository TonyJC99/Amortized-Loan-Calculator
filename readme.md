## What does the program do? / Que es lo que hace el programa?
- The program takes the basic data of an amortized loan, such as the principle, interest rate, and how long it's meant to be paid for, and breaks it down for the user.
- El programa toma los datos basicos de un prestamo amortizado, como el principal, la tasa de interes, y el plazo de tiempo en la cual debe ser pagado, y lo desglosa para el usuario.

## Why did I make it? / Porque lo cree? 
- I have a Bachelor's Degree in Banking and Finance, and I want to become a data analyst dealing with financial data. To do this, I have to show my prowess when it comes to creating scripts in Python, and creating code to show a user a breakdown of their amortized loan is a good way to do it.
- Tengo una licenciatura en banca y finanzas, y quiero ser un analista de datos relacionado con datos financieros. Para hacer esto, necesito demostrar mi capacidad en crear codigo en Python, para demostrar a un usuario un desglose de su deuda amortizada.

## Features / Características
- Bilingual output (English/Spanish) / Salida bilingüe (Inglés/Español)
- Input validation for all fields / Validación de entrada para todos los campos
- Formatted amortization table / Tabla de amortización formateada
- Loan summary with totals / Resumen del préstamo con totales
- Payment breakdown chart (saved as PNG) / Gráfico de desglose de pagos (guardado como PNG)

## Requirements / Requisitos
- Python 3.8 or higher / Python 3.8 o superior
- tabulate
- matplotlib

## How to Run / Cómo Ejecutar
1. Install dependencies / Instalar dependencias:
   pip install tabulate matplotlib
2. Run the script / Ejecutar el script:
   python amortization.py
3. Enter loan amount, interest rate, and term when prompted.
   Ingrese el monto, tasa de interés, y plazo cuando se le solicite.

Sample output:
![Amortization Chart](amortization_chart.png)