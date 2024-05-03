# sourcery skip: avoid-builtin-shadow
import math

input = 0
output_desire = 0

weight = 0.5

learning_rate = 0.01

interacao = 0

error = math.inf

def activation(calculo_aprendizado):
    return 1 if calculo_aprendizado >= 0 else 0

bias = 1 # viés
weight2 = 0.5
    
while error != 0:
    interacao += 1
    print("####### Interação: ", interacao)

    calculo_aprendizado = (input * weight) + (bias * weight2)
    print(calculo_aprendizado)

    output = activation(calculo_aprendizado)
    print("Entrada", input, "Saída: ", output)

    error = output_desire - output

    if error != 0:
        weight = weight + (learning_rate + error)
        weight2 = weight2 + learning_rate + error
        print("Peso: ", weight)

print("A máquina aprendeu")
    
    