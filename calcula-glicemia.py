glicemia_resultado_x = 99
glicemia_resultado_y = 126


print("Insira o valor da sua glicemia")


input_do_usuario = int(input())


def resultado_diabetes():

    if input_do_usuario <= glicemia_resultado_x:
        print("Sua glicemia está dentro do limite.")

    else:
        print("Sua glicemia está na faixa de diabetes.")

resultado_diabetes()