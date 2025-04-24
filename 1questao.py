import os


os.system("cls||clear")


def autenticar_funcionario():
    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")
    return matricula, senha


def obter_dados_funcionario():
    salario_base = float(input("Digite o salário base: (R$): "))
    vale_transporte_opcao = input("Deseja receber vale transporte? (s/n):").strip().lower()
    valor_vale_refeicao = float(input("Digite o valor do vale refeição: (R$): "))
    dependentes = 1 
    return salario_base, vale_transporte_opcao, valor_vale_refeicao, dependentes


def calcular_inss(salario):
    if salario <= 1320.00:
        desconto = salario * 0.075
    elif salario <= 2571.29:
        desconto = salario * 0.09
    elif salario <= 3856.94:
        desconto = salario * 0.12
    elif salario <= 7507.49:
        desconto = salario * 0.14
    else:
        desconto = 1051.05 
    return min(desconto, 1051.05)


def calcular_irrf(salario, dependentes):
    deducao_dependentes = dependentes * 189.59
    base_calculo = salario - deducao_dependentes
    if base_calculo <= 2112.00:
        desconto = 0
    elif base_calculo <= 2826.65:
        desconto = base_calculo * 0.075
    elif base_calculo <= 3544.00:
        desconto = base_calculo * 0.15
    elif base_calculo <= 4256.00:
        desconto = base_calculo * 0.225
    else:
        desconto = base_calculo * 0.275
    return desconto


def calcular_vale_transporte(salario, optou_vt):
    return salario * 0.06 if optou_vt == "s" else 0


def calcular_vale_refeicao(valor_vr):
    return valor_vr * 0.20


def calcular_plano_saude(dependentes):
    return dependentes * 150.00


def salario_liquido(salario_base, inss, irrf, vt, vr, plano_saude):
    return salario_base - (inss + irrf + vt + vr + plano_saude)


def exibir_demonstrativo(matricula, salario_base, inss, irrf, vale_transporte, vale_refeicao, plano_saude, salario_liquido):
    print("\n ### DEMONSTRATIVO DE PAGAMENTO ###")
    print(f"Matrícula: {matricula}")
    print(f"Salário Base: {salario_base:.2f}")
    print(f"Desconto INSS: {inss:.2f}")
    print(f"Desconto IRRF: {irrf:.2f}")
    print(f"Vale Transporte: {vale_transporte:.2f}")
    print(f"Vale Refeição: {vale_refeicao:.2f}")
    print(f"Plano de Saúde: {plano_saude:.2f}")
    print(f"Salário Líquido: {salario_liquido:.2f}")


def sistema_folha_pagamento():
    
    matricula, senha = autenticar_funcionario()

   
    salario_base, vt_opcao, valor_vr, dependentes = obter_dados_funcionario()

   
    inss = calcular_inss(salario_base)
    irrf = calcular_irrf(salario_base, dependentes)
    vt = calcular_vale_transporte(salario_base, vt_opcao)
    vr = calcular_vale_refeicao(valor_vr)
    plano_saude = calcular_plano_saude(dependentes)

   
    desconto_total = inss + irrf + vt + vr + plano_saude
    salario_liquido = salario_base - desconto_total

    
    exibir_demonstrativo(matricula, salario_base, inss, irrf, vt, vr, plano_saude, salario_liquido)


sistema_folha_pagamento()
