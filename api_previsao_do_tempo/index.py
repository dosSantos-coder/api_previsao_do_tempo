#Primeiro se deve Instalar a biblioteca requests do pip no terminal digite "pip intall requests"
#Assim você poderá utilizar os comandos import dentro do código
#Recomendo vocês fazerem as suas no site 'https://openweathermap.org/' é de graça mas está tudo em inglês.

#Aqui eu chamo a biblioteca do pip chamada requests
import requests

#Essa é minha chave de API que está dentro da variável CHAVE_DA_API
CHAVE_DA_API ="74f272095d5084e45d74f4688a513498"

#Aqui será a variável que irá receber o nome da cidade na qual será retornado a previsão do tempo
cidade = input('Digite o nome da cidade em letras minúsculas e sem acentos: ')

#Esse é o Link da API que está dentro da variável link, é daqui que irá sair as informações do tempo requisitadas pelo usuário.
#Dentro do link reparem que eu coloquei as duas variaveis dentro do link. A primeira será para fazer a busca na cidade a segunda é a chave que ir nos retornar a busca.
#O 'f' antes do link é o que me permite adicionar as minhas variaveis dentro do link.
#Ao final do link eu adicionei &lang=ptbr para que as informações da API sejam nos dadas em portugues.
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={CHAVE_DA_API}&lang=pt_br"

#Dentro da variável 'requisicao' será trazido as informações do tempo contidos na API
#A função .get tras as informações contidas no link 
requisicao = requests.get(link)

#Um dicionario dos dados que obtemos lá na API aqui eu trago a variavel 'requisicao' que contem a API do tempo 
#A função .json() trás para o python os arquivos json contidos na API
#É a partir dessa variál que iremos traduzir os dados da API para o portugues e para o facil entendimento.
#Já que, todos os dados estão em inglês e a temperatura está em graus Kelvin
requisicao_dici = requisicao.json()

#O 'weather' é um vetor e o elemento 'description' é o que descreve os valores as informações do tempo exemplo: 'Ensolarado' ou 'Chuvoso'
#No vetor 'weather' o elemento 'description' é o primeiro sendo assim possui o valor de 0 representado no código como [0]
descricao = requisicao_dici['weather'][0]['description']

#Essa variável aqui converte os graus Kelvin para graus Celsius para que assim dé uma infromação mais acessivel.
#Segundo o Google -273.15 é o valor certo para fazer a converão.
conversao_p_celsius = 273.15

#Aqui a variável temperatura vai armazenar o valor especifico da temperatura do código trazendo é claro valores obtidos na API
#Aqui na temperatura é feito um calculo para trazer o valor de Celsius.
temperatura = requisicao_dici['main']['temp'] - conversao_p_celsius

#Esse print nos permite visualizar as informações contidas nas variáveis acima.
#As informações que eu quero trazer com ese print são a descrição do tempo e a temperatura.
print('O tempo na sua cidade está : ',descricao,'\nE está fazendo : ', f"{temperatura}°C nessa região.")