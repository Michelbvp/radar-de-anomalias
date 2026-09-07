#para testa nível de risco
valor = 900.00
limite_alcada = 10000.00
tem_aprovacao_previa = False

if valor > limite_alcada and not tem_aprovacao_previa:
    print("ANOMALIA: acima da alcada sem aprovacao previa")
else:
    print("Transacao dentro do padrao")

if valor > 100000:
    risco = "ALTO"
elif valor > 10000:
    risco = "MEDIO"
else:
    risco = "BAIXO"

print("Nivel de risco:", risco)