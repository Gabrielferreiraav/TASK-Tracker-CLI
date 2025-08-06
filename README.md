# TASK-Tracker-CLI
Um simples gerenciador de tarefas por linha de comando (CLI) construído em Python. Este projeto permite adicionar, listar, atualizar e deletar tarefas diretamente do terminal, com os dados persistidos em um arquivo JSON.

# Funcionalidades
Adicionar Tarefa: Crie uma nova tarefa com um título.

Listar Tarefas: Visualize todas as tarefas, incluindo seus IDs únicos e status.

Atualizar Tarefa: Modifique o título de uma tarefa existente usando seu ID.

Remover Tarefa: Exclua uma tarefa permanentemente usando seu ID.

Persistência de Dados: As tarefas são salvas em um arquivo tasks.json no mesmo diretório do script, garantindo que suas tarefas não sejam perdidas ao fechar o terminal.

# Como Usar
Pré-requisitos
Certifique-se de ter o Python 3 instalado em sua máquina.

Executando o Projeto
Clone o Repositório:

git clone https://github.com/Gabrielferreiraav/TASK-Tracker-CLI.git
cd TASK-Tracker-CLI

Use os Comandos:

Adicionar uma nova tarefa:

python task_tracker.py add "Estudar Python para back-end"

Listar todas as tarefas:

python task_tracker.py list
(A saída mostrará o ID único de cada tarefa, que você precisará para os próximos comandos.)

Atualizar uma tarefa:

python task_tracker.py update <ID_DA_TAREFA> "Novo título da tarefa"

Remover uma tarefa:

python task_tracker.py delete <ID_DA_TAREFA>

# Tecnologias Utilizadas
Python 3: A linguagem de programação principal.

json: Módulo nativo para persistência de dados.

os: Módulo nativo para interagir com o sistema de arquivos.

argparse: Módulo nativo para construir a interface de linha de comando.

uuid: Módulo nativo para geração de identificadores únicos.
