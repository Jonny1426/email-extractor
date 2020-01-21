import re
import requests 

try:
    r = requests.get('')
   
    if r.status_code == requests.codes.ok:
        print('Site acessado com sucesso')
        print('-'*15)

        padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', r.text)
        
        if padrao:
            print('Quantidade de emails encontrados:', len(padrao))
            print(padrao)

            arquivo = open('email.txt', 'a')

            for email in padrao:
                arquivo.write(email+'\n')
            arquivo.close()

        else:
            print('padrao não encontrado')

    else:
        print('Erro ao tentar acessar o site. Código de resposta:', r.status_code)

except Exception as e:
    print('Erro: ', e)
