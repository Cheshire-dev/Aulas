salario_min = float(input())
salario_funcionario = float(input())

if (salario_funcionario < salario_min*3):
    salario_funcionario *= 1.5
if (salario_funcionario >= salario_min*3 and salario_funcionario <= salario_min*10):
    salario_funcionario *= 1.20
else:
    salario_funcionario *= 1.15

print(f"{salario_funcionario:.2f}")