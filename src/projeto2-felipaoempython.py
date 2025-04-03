def calcularNivel(vitorias, derrotas):
    return vitorias - derrotas


saldoVitorias = calcularNivel(101, 2)


nivel = ""

if saldoVitorias < 10:
    nivel = "Ferro"
elif saldoVitorias >= 10 and saldoVitorias <= 20:
    nivel = "Bronze"
elif saldoVitorias >= 21 and saldoVitorias <= 50:
    nivel = "Prata"
elif saldoVitorias >= 51 and saldoVitorias <= 80:
    nivel = "Ouro"
elif saldoVitorias >= 81 and saldoVitorias <= 90:
    nivel = "Diamante"
elif saldoVitorias >= 91 and saldoVitorias <= 100:
    nivel = "Lendário"
elif saldoVitorias >= 101:
    nivel = "Imortal"


print(f"O Herói tem de saldo de {saldoVitorias} vitórias e está no nível {nivel}")
