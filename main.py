from src.formulas_fisica import generar_pdf


def main():
    ruta_salida = "output/documento.pdf"

    generar_pdf(ruta_salida)

    print(f"PDF generado correctamente: {ruta_salida}")


if __name__ == "__main__":
    main()