def verificar_entradas(parametro_uno, parametro_dos, parametro_tres):

    if parametro_uno < 0:
        return False

    if parametro_dos < 0:
        return False

    if parametro_tres < 0:
        return False

    return True


def ejecutar_operacion_aritmetica(valor_uno, valor_dos, valor_tres):

    parcial_uno = valor_uno + valor_dos
    total = parcial_uno + valor_tres

    return total


def calcular_resultado_integral(primer_valor, segundo_valor, tercer_valor):

    if not verificar_entradas(primer_valor, segundo_valor, tercer_valor):
        return None

    
    resultado = ejecutar_operacion_aritmetica(
        primer_valor,
        segundo_valor,
        tercer_valor
    )

    return resultado




valor_inicial_medicion = 450.5
valor_secundario_medicion = 320.1
valor_terciario_medicion = 150.4

valor_final = calcular_resultado_integral(
    valor_inicial_medicion,
    valor_secundario_medicion,
    valor_terciario_medicion
)

print("Consumo calculado: " + str(valor_final))
