arquivo = open("wine.data","r", encoding = "utf8")
arq = arquivo.readlines()

itens = []
classificacao = []

#ts = teste size, quantidade da base que será usada como teste
ts = 0.3

for linha in arq:
    t = linha.split(",")
    clas = int(t[0])
    t[13] = t[13].rstrip('\n')
    t.remove(t[13])
    t.remove(t[0])
    for j in range(len(t)):
        t[j] = float(t[j])

    itens.append(t)
    #retirando \n do final da classificacao
    classificacao.append(clas)

arquivo.close()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(itens, classificacao, test_size=.3)

from sklearn.neighbors import KNeighborsClassifier

neigh = KNeighborsClassifier(n_neighbors=1)

#Treinando
neigh.fit(X_train, y_train)

total = len(X_test)
acertos = 0
erros = 0

ref = ["A","B","C"]
refR = ["classe1","classe2","classe3"]
# = [A,B,C] = [classe1,classe2,classe3]
classe1 = [0,0,0]
classe2 = [0,0,0]
classe3 = [0,0,0]
matrizC = [classe1,classe2,classe3]

predicts = neigh.predict(X_test)
for k in range(len(X_test)):
    pred = predicts[k]
    real = y_test[k]
    print("Teste",k+1,"->","Predicao:",pred,"//""Classe Real:",real)

    if real == "1":
        if pred == real:
            acertos += 1
            classe1[0] += 1
        elif pred == "2":
            erros += 1
            classe1[1] += 1
        else:
            erros += 1
            classe1[2] += 1
    elif real == "2":
        if pred == real:
            acertos += 1
            classe2[1] += 1
        elif pred == "1":
            erros += 1
            classe2[0] += 1
        else:
            erros += 1
            classe2[2] += 1
    else:
        if pred == real:
            acertos += 1
            classe3[2] += 1
        elif pred == "1":
            erros += 1
            classe3[0] += 1
        else:
            erros += 1
            classe3[1] += 1

print("--------------------------------------")
print(" ",ref[0],"",ref[1],"",ref[2]," <-- Predicted Class")
c = 0
for lines in matrizC:
    print(lines,end=" || ")
    print(ref[c],"=",refR[c])
    c+=1

#classe1
tp = classe1[0]
fp = classe2[0] + classe3[0]
fn = classe1[1] + classe1[2]
tn = total - tp - fp - fn

#classe2
tp = classe2[1]
fp = classe1[1] + classe3[1]
fn = classe2[0] + classe2[2]
tn = total - tp - fp - fn

#classe3
tp = classe3[2]
fp = classe1[2] + classe2[2]
fn = classe3[0] + classe3[1]
tn = total - tp - fp - fn

taxa = (acertos/total)*100

if total == acertos + erros:
    print("Quantidade de acertos:",acertos)
    print("Quantidade de erros:",erros)
    print(f"Taxa de acertos: {taxa:.2f}%")
    print("Total:", total)
else:
    print("ERRO")
