🧠 Automação de Cadastro de Produtos com Python
Este projeto automatiza o processo de cadastro de produtos em uma plataforma web utilizando Python e a biblioteca pyautogui. Os dados são lidos de um arquivo CSV e inseridos automaticamente no sistema.

🚀 Funcionalidades
Abertura automática do navegador.
Acesso à plataforma de cadastro.
Login automatizado.
Leitura de base de dados (produtos.csv).
Cadastro de produtos de forma iterativa.

📁 Pré-requisitos
Antes de executar o projeto, certifique-se de ter o Python instalado e, em seguida, instale as bibliotecas necessárias com os seguintes comandos:

bash
Copiar
Editar
pip install pyautogui
pip install pandas
# A biblioteca 'time' já é incluída por padrão no Python
🛠️ Como usar
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/Jhonwgomes/Python.git
Coloque o arquivo produtos.csv na mesma pasta do script.

Execute o script Python:

bash
Copiar
Editar
python nome_do_script.py
⚠️ Importante: Não use o computador durante a execução do script, pois o pyautogui controla o teclado e o mouse.

📌 Observações
O script depende das coordenadas da tela para clicar nos elementos. Se necessário, ajuste os valores de x e y de acordo com a resolução do seu monitor e posição dos elementos.

O tempo de espera (time.sleep()) pode ser ajustado dependendo da velocidade do seu sistema e da internet.

🤝 Contribuição
Contribuições são bem-vindas! Sinta-se livre para abrir issues e pull requests.

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
